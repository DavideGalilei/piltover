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


class Int(Basic):
    SIZE = 32
    signed = True

    def __init__(self, signed: bool = True):
        self.signed = signed

    @classmethod
    def deserialize(cls, data: BytesIO, signed: bool = None) -> int:
        return read_int(data.read(cls.SIZE), signed=signed if signed is not None else cls.signed)

    @classmethod
    def serialize(cls, n: int, signed: bool = True) -> bytes:
        return n.to_bytes(cls.SIZE, byteorder="little", signed=signed if signed is not None else cls.signed)


class Int64(Int):
    SIZE = 64 // 8


class Int128(Int):
    SIZE = 128 // 8


class Int256(Int):
    SIZE = 256 // 8
