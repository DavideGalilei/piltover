from io import BytesIO
from abc import ABC, abstractmethod

from piltover.utils import read_int


class Basic(ABC):
    @classmethod
    @abstractmethod
    def deserialize(cls, data: BytesIO):
        ...

    @classmethod
    @abstractmethod
    def serialize(cls):
        ...


class Int64(Basic):
    SIZE = 64 // 8

    @classmethod
    def deserialize(cls, data: BytesIO) -> int:
        return read_int(data.read(cls.SIZE))

    @classmethod
    def serialize(cls, n: int) -> bytes:
        return n.to_bytes(cls.SIZE, byteorder="little", signed=False)


class Int128(Basic):
    SIZE = 128 // 8

    @classmethod
    def deserialize(cls, data: BytesIO) -> int:
        return read_int(data.read(cls.SIZE))

    @classmethod
    def serialize(cls, n: int) -> bytes:
        return n.to_bytes(cls.SIZE, byteorder="little", signed=False)
