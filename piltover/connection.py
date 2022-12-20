import asyncio

from abc import ABC, abstractmethod

from loguru import logger

from piltover.enums import Transport
from piltover.exceptions import Disconnection


def check(data: bytes) -> bytes:
    if not data:
        # data = b""
        logger.error("Empty data received")
        raise Disconnection()
    return data


class Connection(ABC):
    @staticmethod
    def new(
        transport: Transport,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> "Connection":
        MODES = {
            Transport.Intermediate: TCPIntermediate
        }

        trans = MODES.get(transport)
        return trans(reader=reader, writer=writer)

    @abstractmethod
    def __init__(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        ...

    @abstractmethod
    async def send(self, data: bytes):
        ...

    @abstractmethod
    async def recv(self) -> bytes:
        ...
    
    @abstractmethod
    async def close(self):
        ...


class TCPAbridged(Connection):
    def __init__(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        self.reader = reader
        self.writer = writer

    async def send(self, data: bytes):
        # Round up length
        length = (len(data) + 3) // 4
        
        if length >= 0x7f:  # 127
            self.writer.write(b"\x7f")
        
        self.writer.write(length.to_bytes(1, byteorder="little", signed=False))
        await self.writer.drain()


    async def recv(self) -> bytes:
        header = check(await self.reader.read(1))

        length: int = int.from_bytes(header, byteorder="little", signed=False)
        
        assert length != 0, "Received packet length=0"
        if length >= 0x7f:  # 127
            head = check(await self.reader.read(1))
            assert head == b"\x7f", f"Invalid header for TCP Abdridged (should be 0x7f, got {head:x!r})"
            length = int.from_bytes(check(await self.reader.read(3)), byteorder="little", signed=False)
        
        length *= 4
        return check(await self.reader.read(length))

    async def close(self):
        await self.writer.close()
        await self.writer.wait_closed()


class TCPIntermediate(Connection):
    def __init__(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        self.reader = reader
        self.writer = writer

    async def send(self, data: bytes):
        length = len(data)
        self.writer.write(length.to_bytes(4, "little", signed=False))
        self.writer.write(data)
        await self.writer.drain()

    async def recv(self) -> bytes:
        length = int.from_bytes(check(await self.reader.read(4)), byteorder="little", signed=False)

        assert length != 0, "Received null length"
        # TODO: length check, allow for maximum buffer size (e.g. 1MB)
        # raise TooMuch

        payload = check(await self.reader.read(length))
        return payload

    async def close(self):
        await self.writer.close()
        await self.writer.wait_closed()
