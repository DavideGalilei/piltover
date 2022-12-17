import time
import asyncio
import secrets
import hashlib

import tgcrypto

from uuid import uuid4
from io import BytesIO

from loguru import logger
from icecream import ic

from piltover.enums import Transport
from piltover.exceptions import Disconnection
from piltover.connection import Connection
from piltover.types.primitive import Message
from piltover.types import Keys
from piltover.utils import read_int, generate_large_prime, gen_keys, get_public_key_fingerprint, restore_private_key, restore_public_key
from piltover.tl import TL


class Server:
    HOST = "127.0.0.1"
    PORT = 4430

    def __init__(self, host: str = None, port: int = None, server_keys: Keys = None):
        self.host = host if host is not None else self.HOST
        self.port = port if port is not None else self.PORT

        self.server_keys: Keys = server_keys
        if self.server_keys is None:
            self.server_keys = gen_keys()

        self.public_key = restore_public_key(self.server_keys.public_key)
        self.private_key = restore_private_key(self.server_keys.private_key)

        self.fingerprint: int = get_public_key_fingerprint(self.server_keys.public_key)

        self.clients: dict[str, Client] = {}
        self.clients_lock = asyncio.Lock()

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
            assert await reader.read(3) == b"\xee\xee\xee", "Invalid TCP Intermediate header"
            transport = Transport.Intermediate
        elif header == b"\xdd":
            # Padded Intermediate
            # 0xdddddddd
            assert await reader.read(3) == b"\xdd\xdd\xdd", "Invalid TCP Intermediate header"
            assert False, "TODO: Padded Intermediate"
        else:
            # TCP Full, obfuscation
            assert False, "TCP Full, transport obfuscation not supported"

        assert transport is not None, f"Transport is None, aborting... (header: {header})"
        logger.info(f"Connected client with {transport} {extra}")

        await self.welcome(reader=reader, writer=writer, transport=transport)

    async def welcome(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, transport: Transport):
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


class Client:
    def __init__(
        self,
        server: Server,
        uuid: str,
        transport: Transport,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        peerinfo: tuple = None,
    ):
        self.server: Server = server
        self.uuid: str = uuid
        self.peerinfo: tuple = peerinfo

        self.conn: Connection = Connection.new(
            transport=transport,
            reader=reader,
            writer=writer,
        )

    async def read_msg(self) -> Message:
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
        msg = await self.read_msg()
        print(msg)

        if msg.session_id == 0:
            print(msg.data.hex())
            req_pq = TL.decode(BytesIO(msg.data))
            print(req_pq)

            p = generate_large_prime(32)
            q = generate_large_prime(32)

            if p > q:
                p, q = q, p

            assert p != -1, "p is -1"
            assert q != -1, "q is -1"
            assert p != q

            pq = p * q
            print(f"server {p=}")
            print(f"server {q=}")
            print(f"server {pq=}")

            server_nonce = int.from_bytes(secrets.token_bytes(128 // 8), byteorder="big", signed=True)
            print(f"{server_nonce=}")
            # TODO: remember nonce and server_nonce in the session for security purposes

            # resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector long = ResPQ;
            # TODO: replace bytes(20) with actual data:
            # auth_key_id (8), message_id (8) and message_length (4)

            # TODO: ERROR: server_nonce isn't equal to pyrogram's deserialized value...
            await self.conn.send(
                bytes(20) + TL.encode(
                    {
                        "_": "resPQ",
                        "nonce": req_pq.nonce,
                        "server_nonce": server_nonce,
                        "pq": pq.to_bytes(128 // 8, "big", signed=True),
                        "server_public_key_fingerprints": [self.server.fingerprint],
                    }
                )
            )

            req_dh_params = await self.recv()
            print(f"{req_dh_params=}")
            assert req_dh_params._ == "req_DH_params"
            client_p = int.from_bytes(req_dh_params.p, "big", signed=False)
            client_q = int.from_bytes(req_dh_params.q, "big", signed=False)
            
            assert client_p == p, "client_p is different than server_p"
            assert client_q == q, "client_q is different than server_q"
            
            print(f"{client_p=} {client_q=}")

            encrypted_data = req_dh_params.encrypted_data

            private = self.server.private_key.private_numbers()
            public = self.server.public_key.public_numbers()

            key_aes_encrypted = pow(
                int.from_bytes(encrypted_data, "big", signed=False),
                private.d,
                public.n,
            ).to_bytes(256, "big", signed=False).lstrip(b"\0")

            # idk TODO: restart generation with dh_fail instead
            # assert key_aes_encrypted >= public.n, "key_aes_encrypted greater than RSA modulus, aborting..."
            

            # https://github.com/teamgram/teamgram-server/blob/820e5b122285b7ce76ffa81e8e4ac48e211ce423/app/interface/gateway/internal/server/handshake.go#L338

            # print(key_aes_encrypted)
            # ic(key_aes_encrypted.hex())
            p_q_inner_data = TL.decode(BytesIO(key_aes_encrypted[20:]))
            assert hashlib.sha1(TL.encode(p_q_inner_data)).digest() == key_aes_encrypted[:20], "sha1 of data doesn't match"

            print(p_q_inner_data)

            new_nonce: bytes = p_q_inner_data.new_nonce.to_bytes(128, "big", signed=False)

            new_nonce_hash = hashlib.sha1(new_nonce).digest()[:128 // 8]
            dh_prime = generate_large_prime(2048, safe=True)
            assert dh_prime != -1, "Couldn't generate dh_prime"
            print(dh_prime)

            if p % 8 == 7:
                g = 2
            elif p % 3 == 2:
                g = 3
            elif p % 5 in [1, 4]:
                g = 5
            elif p % 24 in [19, 23]:
                g = 6
            elif p % 7 in [3, 5, 6]:
                g = 7
            else:
                g = 4
            
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
            answer_with_hash = hashlib.sha1(answer).digest() + answer
            answer_with_hash += secrets.token_bytes(-len(answer_with_hash) % 16)
            tmp_aes_key = (
                hashlib.sha1(new_nonce + server_nonce).digest()
                + hashlib.sha1(server_nonce + new_nonce).digest()[:12]
            )
            tmp_aes_iv = (
                hashlib.sha1(server_nonce + new_nonce).digest()[12:12+8]
                + hashlib.sha1(new_nonce + new_nonce)
                + new_nonce[:4]
            )
            encrypted_answer = tgcrypto.ige256_encrypt(answer_with_hash, tmp_aes_key, tmp_aes_iv)

            await self.conn.send(
                bytes(8) + TL.encode(
                    {
                        "_": "server_DH_params_ok",
                        "nonce": p_q_inner_data.nonce,
                        "server_nonce": p_q_inner_data.server_nonce,
                        "encrypted_answer": encrypted_answer,
                    }
                )
            )
            ic(await self.recv())
            # TODO: https://core.telegram.org/mtproto/samples-auth_key#request-to-start-diffie-hellman-key-exchange
            # TODO: https://core.telegram.org/mtproto/auth_key#presenting-proof-of-work-server-authentication
        else:
            assert False, "TODO: authorized messages check"

    async def recv(self) -> TL:
        return TL.decode(BytesIO((await self.read_msg()).data))

    @logger.catch
    async def worker(self):
        try:
            try:
                await self.authorize()

                while True:
                    try:
                        payload = await self.recv()
                        print(payload)
                    except AssertionError:
                        logger.exception("Unexpected failed assertion", backtrace=True)
            except Disconnection:
                logger.info("Client disconnected")
        finally:
            # Cleanup tasks: client disconnected, or an error occurred
            async with self.server.clients_lock:
                self.server.clients.pop(self.uuid, None)
