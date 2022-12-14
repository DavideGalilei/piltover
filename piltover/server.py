import asyncio

from uuid import uuid4
from io import BytesIO

from loguru import logger
from piltover.enums import Transport
from piltover.exceptions import Disconnection
from piltover.connection import Connection
from piltover.types.primitive import Message
from piltover.utils import read_int
from piltover.tl import TL


class Server:
    HOST = "127.0.0.1"
    PORT = 4430

    def __init__(self, host: str = None, port: int = None):
        self.host = host if host is not None else self.HOST
        self.port = port if port is not None else self.PORT

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
            print(TL.decode(BytesIO(msg.data)).__str__())
        else:
            assert False, "TODO: authorized messages check"

    @logger.catch
    async def worker(self):
        try:
            try:
                await self.authorize()

                while True:
                    try:
                        payload = await self.conn.recv()
                        print(payload.hex())
                    except AssertionError:
                        logger.exception("Unexpected failed assertion", backtrace=True)
            except Disconnection:
                logger.info("Client disconnected")
        finally:
            # Cleanup tasks: client disconnected, or an error occurred
            async with self.server.clients_lock:
                self.server.clients.pop(self.uuid, None)
