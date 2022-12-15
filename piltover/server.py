import asyncio
import secrets

from uuid import uuid4
from io import BytesIO

from loguru import logger
from piltover.enums import Transport
from piltover.exceptions import Disconnection
from piltover.connection import Connection
from piltover.types.primitive import Message
from piltover.types import Keys
from piltover.utils import read_int, generate_large_prime, gen_keys, get_public_key_fingerprint
from piltover.tl import TL
from piltover.tl.types import Int128


class Server:
    HOST = "127.0.0.1"
    PORT = 4430

    def __init__(self, host: str = None, port: int = None, server_keys: Keys = None):
        self.host = host if host is not None else self.HOST
        self.port = port if port is not None else self.PORT

        self.server_keys: Keys = server_keys
        if self.server_keys is None:
            self.server_keys = gen_keys()
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

            server_nonce = read_int(secrets.token_bytes(128 // 8))
            print(f"{server_nonce=}")
            # TODO: remember nonce and server_nonce in the session for security purposes

            # resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector long = ResPQ;
            # TODO: replace bytes(20) with actual data:
            # auth_key_id (8), message_id (8) and message_length (4)
            await self.conn.send(
                bytes(20) + TL.encode(
                    {
                        "_": "resPQ",
                        "nonce": req_pq.nonce,
                        "server_nonce": server_nonce,
                        "pq": str(pq),
                        "server_public_key_fingerprints": [self.server.fingerprint],
                    }
                )
            )
        else:
            assert False, "TODO: authorized messages check"

    async def recv(self) -> TL:
        return await self.read_msg()

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
