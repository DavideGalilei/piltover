import os
import time
import asyncio
import secrets
import hashlib

import tgcrypto

from types import SimpleNamespace
from io import BytesIO
from typing import Callable, Awaitable, Optional, cast
from collections import defaultdict

from loguru import logger
from icecream import ic

from piltover.enums import Transport
from piltover.exceptions import Disconnection, InvalidConstructor
from piltover.connection import Connection
from piltover.types import Keys
from piltover.tl.types import (
    Int32,
    Int64,
    CoreMessage,
    EncryptedMessage,
    DecryptedMessage,
    UnencryptedMessage,
)
from piltover.utils import (
    read_int,
    generate_large_prime,
    gen_safe_prime,
    gen_keys,
    get_public_key_fingerprint,
    restore_private_key,
    restore_public_key,
    kdf,
    background,
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
        self.auth_keys: dict[int, tuple[bytes, SimpleNamespace]] = {}
        self.handlers: defaultdict[
            # TODO incorporate the session_id, perhaps into a contextvar
            str,
            list[Callable[[Client, CoreMessage, int], Awaitable[TL | dict | None]]],
        ] = defaultdict(list)
        self.salt: int = 0

    @logger.catch
    async def handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        try:
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
        except Disconnection:
            logger.error(
                "Client disconnected before even trying to generate an auth key :("
            )

    async def welcome(
        self,
        stream: BufferedStream,
        transport: Transport,
    ):
        client = Client(
            transport=transport,
            server=self,
            stream=stream,
            peerinfo=stream.get_extra_info("peerinfo"),
        )
        task = background(client.worker())
        # task.add_done_callback(lambda: self.clean(task))

    async def serve(self):
        server = await asyncio.start_server(self.handle, self.HOST, self.PORT)
        async with server:
            await server.serve_forever()

    async def register_auth_key(
        self, auth_key_id: int, auth_key: bytes, shared: SimpleNamespace
    ):
        self.auth_keys[auth_key_id] = (auth_key, shared)

    async def get_auth_key(
        self, auth_key_id: int
    ) -> tuple[bytes, SimpleNamespace] | None:
        return self.auth_keys.get(auth_key_id, None)

    def on_message(self, typ: str):
        def decorator(
            func: Callable[[Client, CoreMessage, int], Awaitable[TL | dict | None]]
        ):
            logger.debug("Added handler for function {typ!r}", typ=typ)

            self.handlers[typ].append(func)
            return func

        return decorator


class Client:
    def __init__(
        self,
        server: Server,
        transport: Transport,
        stream: BufferedStream,
        peerinfo: tuple,
    ):
        self.server: Server = server
        self.peerinfo: tuple = peerinfo

        self.conn: Connection = Connection.new(
            transport=transport,
            stream=stream,
        )

        self.auth_data = None

        self._msg_id_last_time = 0
        self._msg_id_offset = 0
        # TODO should be session-specific
        self._incoming_content_related_msgs = 0
        self._outgoing_content_related_msgs = 0

    async def read_message(self) -> EncryptedMessage | UnencryptedMessage:
        data = BytesIO(await self.conn.recv())
        auth_key_id = read_int(data.read(8))
        if auth_key_id == 0:
            message_id = read_int(data.read(8))
            message_data_length = read_int(data.read(4))
            message_data = data.read(message_data_length)
            return UnencryptedMessage(message_id, message_data)
        msg_key = data.read(16)
        encrypted_data = data.read()
        return EncryptedMessage(auth_key_id, msg_key, encrypted_data)

    async def send(
        self,
        objects: TL | list[tuple[TL, CoreMessage]],
        session_id: int,
        originating_request: Optional[CoreMessage] = None,
    ):
        await self.conn.send(
            await self.encrypt(
                objects,
                session_id,
                originating_request=originating_request.message_id
                if originating_request is not None
                else None,
            )
        )

    async def handle_unencrypted_message(self, obj: TL):
        match obj._:
            case "req_pq_multi" | "req_pq":
                req_pq_multi = obj
                p = generate_large_prime(31)
                q = generate_large_prime(31)

                if p > q:
                    p, q = q, p

                self.auth_data = SimpleNamespace()
                self.auth_data.p, self.auth_data.q = p, q

                assert p != -1, "p is -1"
                assert q != -1, "q is -1"
                assert p != q

                pq = self.auth_data.p * self.auth_data.q
                ic(p, q, pq)

                # print(f"server {p=}")
                # print(f"server {q=}")
                # print(f"server {pq=}")

                self.auth_data.server_nonce = int.from_bytes(
                    secrets.token_bytes(128 // 8), byteorder="big", signed=False
                )

                res_pq = TL.encode(
                    {
                        "_": "resPQ",
                        "nonce": req_pq_multi.nonce,
                        "server_nonce": self.auth_data.server_nonce,
                        "pq": pq.to_bytes(64 // 8, "big", signed=False),
                        "server_public_key_fingerprints": [self.server.fingerprint],
                    }
                )

                await self.conn.send(
                    bytes(8)
                    + Int64.serialize(self.msg_id(in_reply=True))
                    + Int32.serialize(len(res_pq))
                    + res_pq
                )
            case "req_DH_params":
                assert self.auth_data

                req_dh_params = obj

                assert (
                    len(req_dh_params.p) == 4
                ), f"client_p size must be 4 bytes, not {len(req_dh_params.p)}"
                assert (
                    len(req_dh_params.q) == 4
                ), f"client_q size must be 4 bytes, not {len(req_dh_params.q)}"
                client_p = int.from_bytes(req_dh_params.p, "big", signed=False)
                client_q = int.from_bytes(req_dh_params.q, "big", signed=False)
                assert (
                    client_p == self.auth_data.p
                ), "client_p is different than server_p"
                assert (
                    client_q == self.auth_data.q
                ), "client_q is different than server_q"

                assert self.auth_data.server_nonce == req_dh_params.server_nonce
                # TODO: check server_nonce in other places too

                # print(f"{client_p=} {client_q=}")

                encrypted_data = req_dh_params.encrypted_data
                assert len(encrypted_data) == 256, "Invalid encrypted data"

                old = False  # Whether to use old pre-RSA_PAD encryption? No. TODO

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

                assert p_q_inner_data._ in [
                    "p_q_inner_data",
                    "p_q_inner_data_dc",
                    "p_q_inner_data_temp_dc",
                ], f"Expected p_q_inner_data_*, got instead {p_q_inner_data._}"

                new_nonce: bytes = p_q_inner_data.new_nonce.to_bytes(
                    256 // 8, "little", signed=False
                )
                self.auth_data.new_nonce = new_nonce

                # new_nonce_hash = hashlib.sha1(new_nonce).digest()[:128 // 8]
                logger.info("Generating safe prime...")
                self.auth_data.dh_prime, g = gen_safe_prime(2048)

                # ic(dh_prime, g)
                logger.info("Prime successfully generated")

                self.auth_data.a = int.from_bytes(secrets.token_bytes(256), "big")
                g_a = pow(g, self.auth_data.a, self.auth_data.dh_prime).to_bytes(
                    256, "big"
                )

                # https://core.telegram.org/mtproto/auth_key#dh-key-exchange-complete
                # IMPORTANT: Apart from the conditions on the Diffie-Hellman
                # prime dh_prime and generator g, both sides are to check
                # that g, g_a and g_b are greater than 1 and less than dh_prime - 1.
                # We recommend checking that g_a and g_b are between 2^{2048-64} and dh_prime - 2^{2048-64} as well.
                # TODO

                answer = TL.encode(
                    {
                        "_": "server_DH_inner_data",
                        "nonce": p_q_inner_data.nonce,
                        "server_nonce": self.auth_data.server_nonce,
                        "g": g,
                        "dh_prime": self.auth_data.dh_prime.to_bytes(
                            2048 // 8, "big", signed=False
                        ),
                        "g_a": g_a,
                        "server_time": int(time.time()),
                    }
                )
                self.auth_data.server_nonce_bytes = (
                    server_nonce_bytes
                ) = self.auth_data.server_nonce.to_bytes(
                    128 // 8, "little", signed=False
                )

                answer_with_hash = hashlib.sha1(answer).digest() + answer
                answer_with_hash += secrets.token_bytes(-len(answer_with_hash) % 16)
                self.auth_data.tmp_aes_key = (
                    hashlib.sha1(new_nonce + server_nonce_bytes).digest()
                    + hashlib.sha1(server_nonce_bytes + new_nonce).digest()[:12]
                )
                self.auth_data.tmp_aes_iv = (
                    hashlib.sha1(server_nonce_bytes + new_nonce).digest()[12:]
                    + hashlib.sha1(new_nonce + new_nonce).digest()
                    + new_nonce[:4]
                )
                encrypted_answer = tgcrypto.ige256_encrypt(
                    answer_with_hash,
                    self.auth_data.tmp_aes_key,
                    self.auth_data.tmp_aes_iv,
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
                    + Int64.serialize(self.msg_id(in_reply=True))
                    + Int32.serialize(len(server_dh_params_ok))
                    + server_dh_params_ok
                )
            case "set_client_DH_params":
                assert self.auth_data
                assert hasattr(self.auth_data, "tmp_aes_key")
                set_client_DH_params = obj
                decrypted_params = tgcrypto.ige256_decrypt(
                    set_client_DH_params.encrypted_data,
                    self.auth_data.tmp_aes_key,
                    self.auth_data.tmp_aes_iv,
                )
                client_DH_inner_data = TL.decode(BytesIO(decrypted_params[20:]))
                assert (
                    hashlib.sha1(TL.encode(client_DH_inner_data)).digest()
                    == decrypted_params[:20]
                ), "sha1 hash mismatch for client_DH_inner_data"

                self.auth_data.auth_key = auth_key = (
                    pow(
                        int.from_bytes(client_DH_inner_data.g_b, "big", signed=False),
                        self.auth_data.a,
                        self.auth_data.dh_prime,
                    )
                ).to_bytes(256, "big", signed=False)

                auth_key_digest = hashlib.sha1(auth_key).digest()
                auth_key_hash = auth_key_digest[-8:]
                auth_key_aux_hash = auth_key_digest[:8]

                # ic(shared.server_nonce_bytes, auth_key, auth_key_hash)
                # print("AUTH KEY:", auth_key.hex())
                # print("SHA1(auth_key) =", hashlib.sha1(auth_key).hexdigest())
                # ic(shared.new_nonce.hex())
                # ic(auth_key_aux_hash.hex())

                dh_gen_ok = TL.encode(
                    {
                        "_": "dh_gen_ok",
                        "nonce": client_DH_inner_data.nonce,
                        "server_nonce": self.auth_data.server_nonce,
                        "new_nonce_hash1": int.from_bytes(
                            hashlib.sha1(
                                self.auth_data.new_nonce
                                + bytes([1])
                                + auth_key_aux_hash
                            ).digest()[-16:],
                            "little",
                            signed=False,
                        ),
                    }
                )

                await self.conn.send(
                    bytes(8)
                    + Int64.serialize(self.msg_id(in_reply=True))
                    + Int32.serialize(len(dh_gen_ok))
                    + dh_gen_ok
                )

                self.auth_data.auth_key_id = read_int(auth_key_hash)
                await self.server.register_auth_key(
                    auth_key_id=self.auth_data.auth_key_id,
                    auth_key=self.auth_data.auth_key,
                    shared=self.auth_data,  # TODO remove shared
                )
                logger.info("Auth key generation successfully completed!")
                # self.auth_key = self.auth_data.auth_key
                # self.auth_key_id = auth_key_id

                # Maybe we should keep it
                # self.auth_data = None
            case "msgs_ack":
                logger.debug("Received ack for messages {msg_ids}", msg_ids=obj.msg_ids)
            case _:
                logger.error("Received unexpected unencrypted message {obj}", obj=obj)
                raise RuntimeError(
                    "Received unexpected unencrypted message"
                )  # TODO right error

    async def handle_encrypted_message(
        self, core_message: CoreMessage, session_id: int
    ):
        self.update_incoming_content_related_msgs(
            cast(TL, core_message.obj), session_id, core_message.seq_no
        )
        await self.propagate(
            core_message, session_id
        )  # TODO this should always be just_return and we call self.send manually here

    async def recv(self):
        message = await self.read_message()
        if isinstance(message, EncryptedMessage):
            # TODO: kick clients sending encrypted messages with invalid auth_key/(auth_key_id?)
            # Steps: run tdesktop, restart the server, receive a message:
            # AttributeError: 'types.SimpleNamespace' object has no attribute 'auth_key'
            decrypted = await self.decrypt(message)
            try:
                core_message = decrypted.to_core_message(TL)
            except InvalidConstructor as e:
                await self.reply_invalid_constructor(e, decrypted)
                return
            logger.debug(core_message)
            await self.handle_encrypted_message(core_message, decrypted.session_id)
        elif isinstance(message, UnencryptedMessage):
            # TODO validate message_id (useless since it's not encrypted but ¯\_(ツ)_/¯)
            # TODO handle invalid constructors
            decoded = TL.decode(BytesIO(message.message_data))
            logger.debug(decoded)
            await self.handle_unencrypted_message(decoded)

    # TODO fix indentation
    # TODO this method has a terrible signature
    # TODO don't mix list and non-list parameters
    # TODO this method doesn't do what it says it does - it should ONLY encrypt
    async def encrypt(
        self,
        objects: TL | list[tuple[TL, CoreMessage]],
        session_id: int,
        originating_request: Optional[int] = None,
    ) -> bytes:
        if self.auth_data.auth_key is None:
            assert False, "FATAL: self.auth_key is None"
        elif self.auth_data.auth_key_id is None:
            assert False, "FATAL: self.auth_key_id is None"

        ic("SENDING", objects)

        if isinstance(objects, TL):
            final_obj = objects
            serialized = TL.encode(objects)

            if originating_request is None:
                msg_id = self.msg_id(in_reply=False)
            else:
                # TODO check
                is_content_related = self.is_content_related(objects)
                if is_content_related:
                    msg_id = self.msg_id(in_reply=True)
                else:
                    msg_id = originating_request + 1
            seq_no = self.get_outgoing_seq_no(objects, session_id)
        else:
            container = {
                "_": "msg_container",
                "messages": [],
            }
            for obj, core_message in objects:
                serialized = TL.encode(obj)

                # TODO what if there is no core_message (rename it to originating_request too)
                if self.is_content_related(obj):
                    msg_id = self.msg_id(in_reply=True)
                else:
                    # suspicious
                    msg_id = core_message.message_id + 1
                seq_no = self.get_outgoing_seq_no(obj, session_id)

                container["messages"].append(
                    (
                        Int64.serialize(msg_id)
                        + Int32.serialize(seq_no)
                        + Int32.serialize(len(serialized))
                        + serialized
                    )
                )
            final_obj = TL.from_dict(container)
            serialized = TL.encode(final_obj)

        # ic(self.session_id, self.auth_key_id)
        data = (
            Int64.serialize(self.server.salt)
            + Int64.serialize(session_id)
            + Int64.serialize(self.msg_id(in_reply=True))
            + self.get_outgoing_seq_no(final_obj, session_id).to_bytes(
                4, "little", signed=False
            )
            + len(serialized).to_bytes(4, "little", signed=False)
            + serialized
        )

        padding = os.urandom(-(len(data) + 12) % 16 + 12)

        # 96 = 88 + 8 (8 = incoming message (server message); 0 = outgoing (client message))
        msg_key_large = hashlib.sha256(
            self.auth_data.auth_key[96 : 96 + 32] + data + padding
        ).digest()
        msg_key = msg_key_large[8:24]
        # ic(self.auth_key[96:96 + 32])
        aes_key, aes_iv = kdf(self.auth_data.auth_key, msg_key, False)

        result = (
            Int64.serialize(self.auth_data.auth_key_id)
            + msg_key
            + tgcrypto.ige256_encrypt(data + padding, aes_key, aes_iv)
        )
        ic(len(result))
        return result

    async def decrypt(self, message: EncryptedMessage) -> DecryptedMessage:
        if self.auth_data is None:
            got = await self.server.get_auth_key(message.auth_key_id)
            if got is None:
                # TODO error -404
                assert False, "FATAL: self.auth_key is None"
            # self.auth_data.auth_key = auth_key[0]
            auth_key, auth_data = got
            self.auth_data = auth_data

        aes_key, aes_iv = kdf(self.auth_data.auth_key, message.msg_key, True)

        decypted = BytesIO(
            tgcrypto.ige256_decrypt(message.encrypted_data, aes_key, aes_iv)
        )
        salt = decypted.read(8)  # Salt
        session_id = read_int(decypted.read(8))
        message_id = read_int(decypted.read(8))
        seq_no = read_int(decypted.read(4))
        message_data_length = read_int(decypted.read(4))
        return DecryptedMessage(
            salt,
            session_id,
            message_id,
            seq_no,
            decypted.read(message_data_length),
            decypted.read(),
        )

    async def reply_invalid_constructor(
        self, e: InvalidConstructor, decrypted: DecryptedMessage
    ):
        formatted = f"{e.cid:x}".zfill(8).upper()
        logger.error(
            "Invalid constructor: {formatted} (message_id={message_id})",
            formatted=formatted,
            message_id=decrypted.message_id,
        )

        await self.conn.send(
            await self.encrypt(
                TL.from_dict(
                    {
                        "_": "rpc_result",
                        "req_msg_id": decrypted.message_id,
                        "result": TL.from_dict(
                            {
                                "_": "rpc_error",
                                "error_code": 400,
                                "error_message": f"INPUT_CONSTRUCTOR_INVALID_{formatted}",
                            }
                        ),
                    }
                ),
                session_id=decrypted.session_id,
                originating_request=decrypted.message_id,
            )
        )

    async def ping_worker(self):
        while True:
            await asyncio.sleep(10)
            logger.debug("Sending ping...")

            await self.send(
                TL.from_dict(
                    {
                        "_": "ping",
                        "ping_id": int.from_bytes(os.urandom(4), "big"),
                    }
                )
            )

    @logger.catch
    async def worker(self):
        ping = None
        try:
            self.conn = await self.conn.init()
            # ping = asyncio.create_task(self.ping_worker())

            while True:
                try:
                    await self.recv()
                except AssertionError:
                    logger.exception("Unexpected failed assertion", backtrace=True)
                # TODO: except invalid constructor id, raise INPUT_CONSTRUCTOR_INVALID_5EEF0214 (e.g.)
                # except InvalidConstructor as e:
                #     await self.reply_invalid_constructor(e, msg)
                except Disconnection:
                    raise
                except Exception as e:
                    logger.exception("Unexpected error", backtrace=True)
        except Disconnection:
            logger.info("Client disconnected")

            # import traceback
            # traceback.print_exc()
        finally:
            # Cleanup tasks: client disconnected, or an error occurred
            if ping is not None:
                ping.cancel()

    @staticmethod
    def is_content_related(obj: TL) -> bool:
        return obj._ in ["ping", "pong", "http_wait", "msgs_ack", "msg_container"]

    def msg_id(self, in_reply: bool) -> int:
        # credits to pyrogram
        # about msg_id:
        # https://core.telegram.org/mtproto/description#message-identifier-msg-id
        # Client message identifiers are divisible by 4, server message
        # identifiers modulo 4 yield 1 if the message is a response to
        # a client message, and 3 otherwise.

        now = int(time.time())
        self._msg_id_offset = (
            (self._msg_id_offset + 4) if now == self._msg_id_last_time else 0
        )
        msg_id = (now * 2**32) + self._msg_id_offset + (1 if in_reply else 3)
        self._msg_id_last_time = now

        assert msg_id % 4 in [1, 3], f"Invalid server msg_id: {msg_id}"
        return msg_id

    def update_incoming_content_related_msgs(
        self, obj: TL, session_id: int, seq_no: int
    ):
        # TODO split by session ID
        expected = self._incoming_content_related_msgs * 2
        if self.is_content_related(obj):
            self._incoming_content_related_msgs += 1
            expected += 1
        # TODO(security) validate according to https://core.telegram.org/mtproto/service_messages_about_messages#notice-of-ignored-error-message

    def get_outgoing_seq_no(self, obj: TL, session_id: int) -> int:
        # TODO split by session id
        ret = self._outgoing_content_related_msgs * 2
        if self.is_content_related(obj):
            self._outgoing_content_related_msgs += 1
            ret += 1
        return ret

    async def propagate(
        self, request: CoreMessage, session_id: int, just_return: bool = False
    ):
        if request.obj._ == "msg_container":
            results = []
            for msg in request.obj.messages:
                msg: CoreMessage
                handlers = self.server.handlers.get(msg.obj._, [])

                result = None
                for rpc in handlers:
                    result = await rpc(self, msg, session_id)
                    if result is None:
                        continue
                    elif isinstance(result, dict):
                        result = TL.from_dict(result)
                    break

                if result is None:
                    logger.warning("No handler found for obj:\n{obj}", obj=msg.obj)
                    result = TL.from_dict(
                        {
                            "_": "rpc_error",
                            "error_code": 501,
                            "error_message": "Not implemented",
                        }
                    )
                if result is False:
                    continue

                if result._ not in ("ping", "pong", "rpc_result"):
                    result = TL.from_dict(
                        {
                            "_": "rpc_result",
                            "req_msg_id": msg.message_id,
                            "result": result,
                        }
                    )
                results.append((result, msg))

            if not results:
                # invokeWith_*
                logger.warning("Empty msg_container, returning...")
                return

            assert results, "TODO: rpc_error"
            # if just_return:
            #     return results
            await self.send(results, session_id)
        else:
            handlers = self.server.handlers.get(request.obj._, [])

            result = None
            for rpc in handlers:
                result = await rpc(self, request, session_id)

                if result is None:
                    continue
                elif isinstance(result, dict):
                    result = TL.from_dict(result)
                break

            if result is None:
                logger.warning("No handler found for obj:\n{obj}", obj=request.obj)
                result = TL.from_dict(
                    {
                        "_": "rpc_error",
                        "error_code": 501,
                        "error_message": "Not implemented",
                    }
                )
            if result is False:
                return

            if result._ not in ("ping", "pong", "rpc_result"):
                result = TL.from_dict(
                    {
                        "_": "rpc_result",
                        "req_msg_id": request.message_id,
                        "result": result,
                    }
                )

            if just_return:
                return result

            await self.send(
                result,
                session_id,
                originating_request=request,
            )
