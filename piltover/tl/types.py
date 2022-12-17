from io import BytesIO
from abc import ABC, abstractmethod

from piltover.utils import read_int, nameof


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
    def __init__(self, name: str, size: int, signed: bool = True):
        self.size = size
        self.signed = signed
        self.__name__ = name

    def deserialize(self, data: BytesIO, signed: bool = None) -> int:
        return read_int(data.read(self.size), signed=signed if signed is not None else self.signed)

    def serialize(self, n: int, signed: bool = None) -> bytes:
        return n.to_bytes(self.size, byteorder="little", signed=signed if signed is not None else self.signed)

    def __str__(self) -> str:
        return f"{nameof(self)}(signed={self.signed})"

    def __call__(self, signed: bool = True) -> "Int":
        return Int(self.__name__, self.size, signed=signed)


Int64 = Int("Int64", size=64 // 8)
Int128 = Int("Int128", size=128 // 8)
Int256 = Int("Int256", size=256 // 8)
