import os
import time
import asyncio
import secrets
import hashlib

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
from piltover.tl import TL


class Server:
    HOST = "127.0.0.1"
    PORT = 4430

    def __init__(self, host: str | None = None, port: int | None = None, server_keys: Keys | None = None):
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

        # https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info
        extra = writer.get_extra_info("peername")
        header = await reader.read(1)

        transport = None
        if header == b"\xef":
            # TCP Abridged
            transport = Transport.Abridged
        elif header == b"\xee":
            # TCP Intermediate
            # 0xeeeeeeee
            assert (
                await reader.read(3) == b"\xee\xee\xee"
            ), "Invalid TCP Intermediate header"
            transport = Transport.Intermediate
        elif header == b"\xdd":
            # Padded Intermediate
            # 0xdddddddd
            assert (
                await reader.read(3) == b"\xdd\xdd\xdd"
            ), "Invalid TCP Intermediate header"
            assert False, "TODO: Padded Intermediate"
        else:
            # TCP Full, obfuscation
            assert False, "TCP Full, transport obfuscation not supported"

        assert (
            transport is not None
        ), f"Transport is None, aborting... (header: {header})"
        logger.info(f"Connected client with {transport} {extra}")

        await self.welcome(reader=reader, writer=writer, transport=transport)

    async def welcome(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        transport: Transport,
    ):
        uuid = uuid4().hex
        client = Client(
            transport=transport,
            server=self,
            reader=reader,
            writer=writer,
            peerinfo=writer.get_extra_info("peerinfo"),
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
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        peerinfo: tuple,
    ):
        self.server: Server = server
        self.uuid: str = uuid
        self.peerinfo: tuple = peerinfo

        self.conn: Connection = Connection.new(
            transport=transport,
            reader=reader,
            writer=writer,
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

            req_pq = TL.decode(data)

            p = generate_large_prime(32)
            q = generate_large_prime(32)

            if p > q:
                p, q = q, p

            assert p != -1, "p is -1"
            assert q != -1, "q is -1"
            assert p != q

            pq = p * q
            # print(f"server {p=}")
            # print(f"server {q=}")
            # print(f"server {pq=}")

            server_nonce = int.from_bytes(
                secrets.token_bytes(128 // 8), byteorder="big", signed=True
            )

            # TODO: remember nonce and server_nonce in the session for security purposes

            # resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector long = ResPQ;
            # TODO: replace bytes(20) with actual data:
            # auth_key_id (8), message_id (8) and message_length (4)

            # TODO: ERROR: server_nonce isn't equal to pyrogram's deserialized value...
            await self.conn.send(
                bytes(20)
                + TL.encode(
                    {
                        "_": "resPQ",
                        "nonce": req_pq.nonce,
                        "server_nonce": server_nonce,
                        "pq": pq.to_bytes(128 // 8, "big", signed=True),
                        "server_public_key_fingerprints": [self.server.fingerprint],
                    }
                )
            )

            req_dh_params = await self.auth_recv()

            assert req_dh_params._ == "req_DH_params"
            client_p = int.from_bytes(req_dh_params.p, "big", signed=False)
            client_q = int.from_bytes(req_dh_params.q, "big", signed=False)

            assert client_p == p, "client_p is different than server_p"
            assert client_q == q, "client_q is different than server_q"

            # print(f"{client_p=} {client_q=}")

            encrypted_data = req_dh_params.encrypted_data

            private = self.server.private_key.private_numbers()
            public = self.server.public_key.public_numbers()

            key_aes_encrypted = (
                pow(
                    int.from_bytes(encrypted_data, "big", signed=False),
                    private.d,
                    public.n,
                )
                .to_bytes(256, "big", signed=False)
                .lstrip(b"\0")
            )

            # idk TODO: restart generation with dh_fail instead
            # assert key_aes_encrypted >= public.n, "key_aes_encrypted greater than RSA modulus, aborting..."

            # https://github.com/teamgram/teamgram-server/blob/820e5b122285b7ce76ffa81e8e4ac48e211ce423/app/interface/gateway/internal/server/handshake.go#L338

            # print(key_aes_encrypted)
            # ic(key_aes_encrypted.hex())
            p_q_inner_data = TL.decode(BytesIO(key_aes_encrypted[20:]))
            assert (
                hashlib.sha1(TL.encode(p_q_inner_data)).digest()
                == key_aes_encrypted[:20]
            ), "sha1 of data doesn't match"

            new_nonce: bytes = p_q_inner_data.new_nonce.to_bytes(
                256 // 8, "little", signed=False
            )

            # new_nonce_hash = hashlib.sha1(new_nonce).digest()[:128 // 8]
            logger.info("Generating safe prime...")
            dh_prime, g = gen_safe_prime(2048)

            # ic(dh_prime, g)
            logger.info("Prime successfully generated")

            a = int.from_bytes(secrets.token_bytes(256), "big")
            g_a = pow(g, a, dh_prime).to_bytes(256, "big")

            answer = TL.encode(
                {
                    "_": "server_DH_inner_data",
                    "nonce": p_q_inner_data.nonce,
                    "server_nonce": server_nonce,
                    "g": g,
                    "dh_prime": dh_prime.to_bytes(2048 // 8, "big", signed=False),
                    "g_a": g_a,
                    "server_time": int(time.time()),
                }
            )
            server_nonce_bytes = server_nonce.to_bytes(128 // 8, "little", signed=True)

            answer_with_hash = hashlib.sha1(answer).digest() + answer
            answer_with_hash += secrets.token_bytes(-len(answer_with_hash) % 16)
            tmp_aes_key = (
                hashlib.sha1(new_nonce + server_nonce_bytes).digest()
                + hashlib.sha1(server_nonce_bytes + new_nonce).digest()[:12]
            )
            tmp_aes_iv = (
                hashlib.sha1(server_nonce_bytes + new_nonce).digest()[12:]
                + hashlib.sha1(new_nonce + new_nonce).digest()
                + new_nonce[:4]
            )
            encrypted_answer = tgcrypto.ige256_encrypt(
                answer_with_hash, tmp_aes_key, tmp_aes_iv
            )

            await self.conn.send(
                bytes(20)
                + TL.encode(
                    {
                        "_": "server_DH_params_ok",
                        "nonce": p_q_inner_data.nonce,
                        "server_nonce": p_q_inner_data.server_nonce,
                        "encrypted_answer": encrypted_answer,
                    }
                )
            )

            set_client_DH_params = await self.auth_recv()

            decrypted_params = tgcrypto.ige256_decrypt(
                set_client_DH_params.encrypted_data, tmp_aes_key, tmp_aes_iv
            )
            client_DH_inner_data = TL.decode(BytesIO(decrypted_params[20:]))
            assert (
                hashlib.sha1(TL.encode(client_DH_inner_data)).digest()
                == decrypted_params[:20]
            ), "sha1 hash mismatch for client_DH_inner_data"

            auth_key = (
                pow(
                    int.from_bytes(client_DH_inner_data.g_b, "big", signed=False),
                    a,
                    dh_prime,
                )
            ).to_bytes(256, "big", signed=False)

            auth_key_hash = hashlib.sha1(auth_key).digest()[64 // 8 :]
            auth_key_aux_hash = hashlib.sha1(auth_key).digest()[: 64 // 8]

            ic(server_nonce_bytes, auth_key, auth_key_hash)

            await self.conn.send(
                bytes(20)
                + TL.encode(
                    {
                        "_": "dh_gen_ok",
                        "nonce": client_DH_inner_data.nonce,
                        "server_nonce": server_nonce,
                        "new_nonce_hash1": int.from_bytes(
                            hashlib.sha1(
                                new_nonce + bytes([1]) + auth_key_aux_hash
                            ).digest()[: 128 // 8],
                            "big",
                            signed=False,
                        ),
                    }
                )
            )

            auth_key_id = read_int(hashlib.sha1(auth_key).digest()[-8:])
            await self.server.register_auth_key(
                auth_key_id=auth_key_id, auth_key=auth_key
            )
            logger.info(
                "Auth key generation successfully completed! Disconnecting client..."
            )
            raise Disconnection()
        # else:
        #     assert False, "TODO: authorized messages check"

        self.auth_key = await self.server.get_auth_key(auth_key_id=auth_key_id)

        if self.auth_key is None:
            logger.warning("Invalid auth key id provided, disconnecting...")
            raise Disconnection()

        self.session_id = auth_key_id
        msg = await self.decrypt(data=data)
        ic(self.session_id)

        await self.propagate(Request.from_msg(self, msg))

    async def auth_recv(self) -> TL:
        msg = await self.read_auth_msg()
        result = TL.decode(BytesIO(msg.data))
        # result._session_id = msg.session_id
        return result

    async def send(self, obj: TL, originating_request: Optional["Request"] = None):
        if originating_request is not None:
            if obj._ not in ["ping"]:
                obj = TL.from_dict(
                    {
                        "_": "rpc_result",
                        "req_msg_id": originating_request.msg_id,
                        "result": obj,
                    }
                )
        await self.conn.send(await self.encrypt(obj, originating_request=originating_request))

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

    async def encrypt(self, obj: TL, originating_request: Optional["Request"] = None) -> bytes:
        if self.session_id is None:
            assert False, "FATAL: self.session_id is None"
        elif self.auth_key is None:
            assert False, "FATAL: self.auth_key is None"
        elif self.auth_key_id is None:
            assert False, "FATAL: self.auth_key_id is None"

        serialized = TL.encode(obj)

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

        data = (
            Int64.serialize(self.server.salt)
            + Int64.serialize(self.session_id)
            + Int64.serialize(msg_id)
            + seq_no.to_bytes(4, "little", signed=False) # b"\0" * 4 # self.seq_no()
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
        data = BytesIO(tgcrypto.ige256_decrypt(data.read(), aes_key, aes_iv))
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
                # import traceback
                # traceback.print_exc()
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

    async def answer(self, data: dict):
        obj = TL.from_dict(data)
        await self.client.send(obj, self)

    @staticmethod
    def from_msg(client: Client, msg: Message) -> "Request":
        return Request(
            client=client,
            obj=TL.decode(BytesIO(msg.data)),
            msg_id=msg.msg_id,
            seq_no=msg.seq_no,
        )
