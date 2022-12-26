import os
import time
import asyncio
import secrets
import hashlib
from types import SimpleNamespace

import tgcrypto

from uuid import uuid4
from io import BytesIO
from typing import Callable, Awaitable, Any, Optional
from collections import defaultdict
from dataclasses import dataclass

from loguru import logger
from icecream import ic

from piltover.enums import Transport
from piltover.exceptions import Disconnection
from piltover.connection import Connection
from piltover.types.primitive import Message
from piltover.types import Keys
from piltover.tl.types import Int32, Int64
from piltover.utils import (
    read_int,
    generate_large_prime,
    gen_safe_prime,
    gen_keys,
    get_public_key_fingerprint,
    restore_private_key,
    restore_public_key,
    kdf,
)
from piltover.utils.rsa_utils import rsa_decrypt, rsa_pad_inverse
from piltover.utils.buffered_stream import BufferedStream
from piltover.tl import TL


class Server:
    HOST = "0.0.0.0"
    PORT = 4430

    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        server_keys: Keys | None = None,
    ):
        self.host = host if host is not None else self.HOST
        self.port = port if port is not None else self.PORT

        self.server_keys = server_keys
        if self.server_keys is None:
            self.server_keys = gen_keys()

        self.public_key = restore_public_key(self.server_keys.public_key)
        self.private_key = restore_private_key(self.server_keys.private_key)

        self.fingerprint: int = get_public_key_fingerprint(self.server_keys.public_key)

        self.clients: dict[str, Client] = {}
        self.clients_lock = asyncio.Lock()
        self.auth_keys: dict[int, bytes] = {}
        self.handlers: defaultdict[
            str, list[Callable[[Client, Request], Awaitable[Any]]]
        ] = defaultdict(list)
        self.salt: int = 0

    @logger.catch
    async def handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        # Check the transport: https://core.telegram.org/mtproto/mtproto-transports

        stream = BufferedStream(reader=reader, writer=writer)

        # https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info
        extra = writer.get_extra_info("peername")
        header = await stream.peek(1)

        transport = None
        if header == b"\xef":
            await stream.read(1)  # discard
            # TCP Abridged
            transport = Transport.Abridged
        elif header == b"\xee":
            await stream.read(1)  # discard
            # TCP Intermediate
            # 0xeeeeeeee
            assert (
                await stream.read(3) == b"\xee\xee\xee"
            ), "Invalid TCP Intermediate header"
            transport = Transport.Intermediate
        elif header == b"\xdd":
            await stream.read(1)  # discard
            # Padded Intermediate
            # 0xdddddddd
            assert (
                await stream.read(3) == b"\xdd\xdd\xdd"
            ), "Invalid TCP Intermediate header"
            transport = Transport.PaddedIntermediate
        # else:
        #     # TCP Full, obfuscation
        #     assert False, "TCP Full, transport obfuscation not supported"
        else:
            # TODO: obfuscation?
            # The seq_no in TCPFull always starts with 0, so we can recognize
            # the transport and distinguish it from obfuscated ones (starting with 64 random bytes)
            # by checking whether the seq_no bytes are zeroed
            soon = await stream.peek(8)
            if soon[-4:] == b"\0\0\0\0":
                transport = Transport.Full
            else:
                # Obfuscated Transports
                transport = Transport.Obfuscated

        assert (
            transport is not None
        ), f"Transport is None, aborting... (header: {header})"
        logger.info(f"Connected client with {transport} {extra}")

        await self.welcome(stream=stream, transport=transport)

    async def welcome(
        self,
        stream: BufferedStream,
        transport: Transport,
    ):
        uuid = uuid4().hex
        client = Client(
            transport=transport,
            server=self,
            stream=stream,
            peerinfo=stream.get_extra_info("peerinfo"),
            uuid=uuid,
        )
        task = asyncio.create_task(client.worker())
        # task.add_done_callback(lambda: self.clean(task))
        async with self.clients_lock:
            self.clients[uuid] = client

    async def serve(self):
        server = await asyncio.start_server(self.handle, self.HOST, self.PORT)
        async with server:
            await server.serve_forever()

    async def register_auth_key(self, auth_key_id: int, auth_key: bytes):
        self.auth_keys[auth_key_id] = auth_key

    async def get_auth_key(self, auth_key_id: int) -> bytes | None:
        return self.auth_keys.get(auth_key_id, None)

    def on_message(self, typ: str):
        def decorator(func: Callable[[Client, Request], Awaitable[Any]]):
            logger.debug("Added handler for function {typ!r}", typ=typ)

            async def wrapper(client: Client, request: Request, *args, **kwargs):
                return await func(client, request, *args, **kwargs)

            self.handlers[typ].append(wrapper)

            return wrapper

        return decorator


class Client:
    def __init__(
        self,
        server: Server,
        uuid: str,
        transport: Transport,
        stream: BufferedStream,
        peerinfo: tuple,
    ):
        self.server: Server = server
        self.uuid: str = uuid
        self.peerinfo: tuple = peerinfo

        self.conn: Connection = Connection.new(
            transport=transport,
            stream=stream,
        )
        self.session_id: int | None = None
        self.auth_key: bytes | None = None
        self.auth_key_id: int | None = None

    async def read_auth_msg(self) -> Message:
        data = BytesIO(await self.conn.recv())
        session_id = read_int(data.read(8))
        msg_id = read_int(data.read(8))
        length = read_int(data.read(4))

        # TODO: session_id cache auth check
        # TODO: msg_id check
        # TODO: length check

        payload = data.read(length)
        return Message(session_id=session_id, data=payload, msg_id=msg_id)

    async def authorize(self):
        data = BytesIO(await self.conn.recv())
        auth_key_id = read_int(data.read(8))
        self.auth_key_id = auth_key_id

        if auth_key_id == 0:
            msg_id = read_int(data.read(8))
            length = read_int(data.read(4))

            req_pq_multi = TL.decode(data)

            assert req_pq_multi._ in ("req_pq_multi", "req_pq"), "Invalid request"
            shared = SimpleNamespace()

            def get_msg_id() -> int:
                return msg_id + 1  # 2 + (not msg_id % 2)

            # Whether to use or not the new RSA_PAD algorithm
            # TODO: handle different server public key
            old = False

            async def handle(obj: TL) -> bool:
                match obj._:
                    case "req_pq_multi" | "req_pq":
                        req_pq_multi = obj
                        p = generate_large_prime(31)
                        q = generate_large_prime(31)

                        if p > q:
                            p, q = q, p

                        shared.p, shared.q = p, q

                        assert p != -1, "p is -1"
                        assert q != -1, "q is -1"
                        assert p != q

                        pq = shared.p * shared.q

                        # print(f"server {p=}")
                        # print(f"server {q=}")
                        # print(f"server {pq=}")

                        shared.server_nonce = int.from_bytes(
                            secrets.token_bytes(128 // 8), byteorder="big", signed=True
                        )

                        res_pq = TL.encode(
                            {
                                "_": "resPQ",
                                "nonce": req_pq_multi.nonce,
                                "server_nonce": shared.server_nonce,
                                "pq": pq.to_bytes(64 // 8, "big", signed=False),
                                "server_public_key_fingerprints": [
                                    self.server.fingerprint
                                ],
                            }
                        )

                        await self.conn.send(
                            bytes(8)
                            + Int64.serialize(get_msg_id())
                            + Int32.serialize(len(res_pq))
                            + res_pq
                        )
                    case "req_DH_params":
                        # req_dh_params, msg_id = await self.auth_recv()
                        req_dh_params = obj
                        client_p = int.from_bytes(req_dh_params.p, "big", signed=False)
                        client_q = int.from_bytes(req_dh_params.q, "big", signed=False)

                        assert (
                            client_p == shared.p
                        ), "client_p is different than server_p"
                        assert (
                            client_q == shared.q
                        ), "client_q is different than server_q"

                        # print(f"{client_p=} {client_q=}")

                        encrypted_data = req_dh_params.encrypted_data
                        assert len(encrypted_data) == 256, "Invalid encrypted data"

                        if old:
                            key_aes_encrypted = rsa_decrypt(
                                encrypted_data,
                                public_key=self.server.public_key,
                                private_key=self.server.private_key,
                            ).lstrip(b"\0")
                        else:
                            key_aes_encrypted = rsa_pad_inverse(
                                encrypted_data,
                                public_key=self.server.public_key,
                                private_key=self.server.private_key,
                            ).lstrip(b"\0")

                        # idk TODO: restart generation with dh_fail instead
                        # assert key_aes_encrypted >= public.n, "key_aes_encrypted greater than RSA modulus, aborting..."

                        # print(key_aes_encrypted)
                        # ic(key_aes_encrypted.hex())

                        if old:
                            p_q_inner_data = TL.decode(BytesIO(key_aes_encrypted[20:]))

                            assert (
                                hashlib.sha1(TL.encode(p_q_inner_data)).digest()
                                == key_aes_encrypted[:20]
                            ), "sha1 of data doesn't match"
                        else:
                            p_q_inner_data = TL.decode(BytesIO(key_aes_encrypted))
                            ic(p_q_inner_data)

                        new_nonce: bytes = p_q_inner_data.new_nonce.to_bytes(
                            256 // 8, "little", signed=False
                        )
                        shared.new_nonce = new_nonce

                        # new_nonce_hash = hashlib.sha1(new_nonce).digest()[:128 // 8]
                        logger.info("Generating safe prime...")
                        shared.dh_prime, g = gen_safe_prime(2048)

                        # ic(dh_prime, g)
                        logger.info("Prime successfully generated")

                        shared.a = int.from_bytes(secrets.token_bytes(256), "big")
                        g_a = pow(g, shared.a, shared.dh_prime).to_bytes(256, "big")

                        answer = TL.encode(
                            {
                                "_": "server_DH_inner_data",
                                "nonce": p_q_inner_data.nonce,
                                "server_nonce": shared.server_nonce,
                                "g": g,
                                "dh_prime": shared.dh_prime.to_bytes(
                                    2048 // 8, "big", signed=False
                                ),
                                "g_a": g_a,
                                "server_time": int(time.time()),
                            }
                        )
                        shared.server_nonce_bytes = (
                            server_nonce_bytes
                        ) = shared.server_nonce.to_bytes(
                            128 // 8, "little", signed=True
                        )

                        answer_with_hash = hashlib.sha1(answer).digest() + answer
                        answer_with_hash += secrets.token_bytes(
                            -len(answer_with_hash) % 16
                        )
                        shared.tmp_aes_key = (
                            hashlib.sha1(new_nonce + server_nonce_bytes).digest()
                            + hashlib.sha1(server_nonce_bytes + new_nonce).digest()[:12]
                        )
                        shared.tmp_aes_iv = (
                            hashlib.sha1(server_nonce_bytes + new_nonce).digest()[12:]
                            + hashlib.sha1(new_nonce + new_nonce).digest()
                            + new_nonce[:4]
                        )
                        encrypted_answer = tgcrypto.ige256_encrypt(
                            answer_with_hash,
                            shared.tmp_aes_key,
                            shared.tmp_aes_iv,
                        )

                        server_dh_params_ok = TL.encode(
                            {
                                "_": "server_DH_params_ok",
                                "nonce": p_q_inner_data.nonce,
                                "server_nonce": p_q_inner_data.server_nonce,
                                "encrypted_answer": encrypted_answer,
                            }
                        )

                        await self.conn.send(
                            bytes(8)
                            + Int64.serialize(get_msg_id())
                            + Int32.serialize(len(server_dh_params_ok))
                            + server_dh_params_ok
                        )
                    case "set_client_DH_params":
                        set_client_DH_params = obj
                        decrypted_params = tgcrypto.ige256_decrypt(
                            set_client_DH_params.encrypted_data,
                            shared.tmp_aes_key,
                            shared.tmp_aes_iv,
                        )
                        client_DH_inner_data = TL.decode(BytesIO(decrypted_params[20:]))
                        assert (
                            hashlib.sha1(TL.encode(client_DH_inner_data)).digest()
                            == decrypted_params[:20]
                        ), "sha1 hash mismatch for client_DH_inner_data"

                        shared.auth_key = auth_key = (
                            pow(
                                int.from_bytes(
                                    client_DH_inner_data.g_b, "big", signed=False
                                ),
                                shared.a,
                                shared.dh_prime,
                            )
                        ).to_bytes(256, "big", signed=False)

                        auth_key_hash = hashlib.sha1(auth_key).digest()[-64 // 8 :]
                        auth_key_aux_hash = hashlib.sha1(auth_key).digest()[: 64 // 8]

                        # ic(shared.server_nonce_bytes, auth_key, auth_key_hash)
                        print("AUTH KEY:", auth_key.hex())
                        print("SHA1(auth_key) =", hashlib.sha1(auth_key).hexdigest())
                        ic(shared.new_nonce.hex())
                        ic(auth_key_aux_hash.hex())

                        dh_gen_ok = TL.encode(
                            {
                                "_": "dh_gen_ok",
                                "nonce": client_DH_inner_data.nonce,
                                "server_nonce": shared.server_nonce,
                                "new_nonce_hash1": ic(int.from_bytes(
                                    hashlib.sha1(
                                        shared.new_nonce
                                        + bytes([1])
                                        + auth_key_aux_hash
                                    ).digest()[-16:],
                                    "little",
                                    signed=False,
                                )),
                            }
                        )

                        await self.conn.send(
                            bytes(8)
                            + Int64.serialize(get_msg_id())
                            + Int32.serialize(len(dh_gen_ok))
                            + dh_gen_ok
                        )
                        return True
                    case _:
                        assert False, "Unreachable"
                return False

            await handle(ic(req_pq_multi))

            while True:
                obj, msg_id = await self.auth_recv()
                ic(obj)
                if await handle(obj):
                    break

            auth_key_id = read_int(hashlib.sha1(shared.auth_key).digest()[-8:])
            await self.server.register_auth_key(
                auth_key_id=auth_key_id,
                auth_key=shared.auth_key,
            )
            logger.info("Auth key generation successfully completed!")

            self.auth_key = shared.auth_key
            self.auth_key_id = auth_key_id
            # TODO: server salt
            # self.server_salt = shared.new_nonce[0:8] ^ shared.server_nonce[0:8]

            # raise Disconnection()
            # await self.conn.send(Int32.serialize(-404, signed=True))
        # else:
        #     assert False, "TODO: authorized messages check"
        else:
            self.auth_key = await self.server.get_auth_key(auth_key_id=auth_key_id)

            if self.auth_key is None:
                logger.warning("Invalid auth key id provided, disconnecting...")
                raise Disconnection()

            self.session_id = auth_key_id
            msg = await self.decrypt(data=data)
            ic(self.session_id)

            await self.propagate(Request.from_msg(self, msg))

    async def auth_recv(self) -> tuple[TL, int]:
        msg = await self.read_auth_msg()
        result = TL.decode(BytesIO(msg.data))
        # result._session_id = msg.session_id
        return result, msg.msg_id

    async def send(
        self, objects: list[TL], originating_request: Optional["Request"] = None
    ):
        if originating_request is not None:
            for i in range(len(objects)):
                if objects[i]._ not in ["ping"]:
                    objects[i] = TL.from_dict(
                        {
                            "_": "rpc_result",
                            "req_msg_id": originating_request.msg_id,
                            "result": objects[i],
                        }
                    )

        await self.conn.send(
            await self.encrypt(objects, originating_request=originating_request)
        )

    async def recv(self) -> "Request":
        data = BytesIO(await self.conn.recv())
        session_id = read_int(data.read(8))
        # TODO: errors... am I supposed to fix them?
        # assert session_id == self.session_id, "Wrong session id"

        decrypted = await self.decrypt(data=data)

        return Request(
            client=self,
            obj=TL.decode(BytesIO(decrypted.data)),
            msg_id=decrypted.msg_id,
            seq_no=decrypted.seq_no,
        )

    async def encrypt(
        self, objects: TL | list[TL], originating_request: Optional["Request"] = None
    ) -> bytes:
        if self.session_id is None:
            assert False, "FATAL: self.session_id is None"
        elif self.auth_key is None:
            assert False, "FATAL: self.auth_key is None"
        elif self.auth_key_id is None:
            assert False, "FATAL: self.auth_key_id is None"

        if isinstance(objects, TL):
            return await self.encrypt(
                [objects], originating_request=originating_request
            )

        serialized = TL.encode(objects[0])
        # TODO: handle multiple messages in a single container

        # about msg_id:
        # https://core.telegram.org/mtproto/description#message-identifier-msg-id
        # Client message identifiers are divisible by 4, server message
        # identifiers modulo 4 yield 1 if the message is a response to
        # a client message, and 3 otherwise.
        if originating_request is not None:
            # is_content_related = originating_request.obj._ in ["ping"]
            orig_msg_id = originating_request.msg_id
            msg_id = orig_msg_id + (not orig_msg_id % 2)  # + (not is_content_related)
            # msg_id += 4 * (orig_msg_id % 4 == msg_id % 4)
            # ic(msg_id)
            assert msg_id % 2 != 0
            seq_no = originating_request.seq_no + 1

            if originating_request.obj._ not in ["ping"]:
                serialized = TL.encode(
                    {
                        "_": "msg_container",
                        "messages": [
                            (
                                Int64.serialize(msg_id)
                                + Int32.serialize(seq_no)
                                + Int32.serialize(len(serialized))
                                + serialized
                            )
                        ],
                    }
                )
                # ic("container::", serialized)
        else:
            assert False, "TODO"
            # TODO: self.last_received_msg_id + 1 (for seq_no too)
            # idk, check docs
            seq_no = 1
            msg_id = 1

        ic(self.session_id, self.auth_key_id)
        data = (
            Int64.serialize(self.server.salt)
            + Int64.serialize(self.session_id)
            + Int64.serialize(msg_id)
            + seq_no.to_bytes(4, "little", signed=False)  # b"\0" * 4 # self.seq_no()
            + len(serialized).to_bytes(4, "little", signed=False)
            + serialized
        )
        # TODO: check seq_no generation maybe?

        padding = os.urandom(-(len(data) + 12) % 16 + 12)

        # 96 = 88 + 8 (8 = incoming message (server message); 0 = outgoing (client message))
        msg_key_large = hashlib.sha256(
            self.auth_key[96 : 96 + 32] + data + padding
        ).digest()
        msg_key = msg_key_large[8:24]
        # ic(self.auth_key[96:96 + 32])
        aes_key, aes_iv = kdf(self.auth_key, msg_key, False)

        return (
            Int64.serialize(self.auth_key_id)
            + msg_key
            + tgcrypto.ige256_encrypt(data + padding, aes_key, aes_iv)
        )

    async def decrypt(self, data: BytesIO) -> Message:
        # session_id = read_int(data.read(8))

        # if self.session_id is None:
        #     assert False, "FATAL: self.session_id is None"
        if self.auth_key is None:
            assert False, "FATAL: self.auth_key is None"

        msg_key = data.read(16)

        aes_key, aes_iv = kdf(self.auth_key, msg_key, True)

        got = data.read()
        data = BytesIO(tgcrypto.ige256_decrypt(got, aes_key, aes_iv))
        salt = data.read(8)  # Salt
        self.session_id = read_int(data.read(8))

        msg_id = read_int(data.read(8))
        seq_no = read_int(data.read(4))
        length = read_int(data.read(4))
        return Message(
            session_id=self.session_id,
            msg_id=msg_id,
            seq_no=seq_no,
            data=data.read(length),
        )

    @logger.catch
    async def worker(self):
        try:
            try:
                self.conn = await self.conn.init()
                await self.authorize()

                while True:
                    try:
                        request = await self.recv()
                        ic(request)
                        await self.propagate(request)
                    except AssertionError:
                        logger.exception("Unexpected failed assertion", backtrace=True)
            except Disconnection:
                logger.info("Client disconnected")
                # raise
                # import traceback
                # traceback.print_exc()
            # TODO: except invalid constructor id, raise INPUT_CONSTRUCTOR_INVALID_5EEF0214 (e.g.)
        finally:
            # Cleanup tasks: client disconnected, or an error occurred
            async with self.server.clients_lock:
                self.server.clients.pop(self.uuid, None)

    async def propagate(self, request: "Request"):
        for rpc in self.server.handlers.get(request.obj._, []):
            await rpc(self, request)


@dataclass(init=True, repr=True)
class Request:
    client: Client
    obj: TL
    msg_id: int
    seq_no: int

    async def answer(self, data: dict | list | TL):
        if isinstance(data, dict):
            obj = [TL.from_dict(data)]
        elif isinstance(data, list):
            obj = [
                TL.from_dict(element) for element in data if not isinstance(element, TL)
            ]
        else:
            obj = [data]
        await self.client.send(obj, self)

    @staticmethod
    def from_msg(client: Client, msg: Message) -> "Request":
        return Request(
            client=client,
            obj=TL.decode(BytesIO(msg.data)),
            msg_id=msg.msg_id,
            seq_no=msg.seq_no,
        )
