import struct
import inspect

from io import BytesIO
from abc import ABC, abstractmethod
from types import GenericAlias
from dataclasses import dataclass

from loguru import logger

from piltover.utils import read_int, nameof, read_bytes, write_bytes
from icecream import ic


VECTOR_CID = 0x1CB5C415
BOOL_FALSE = 0xBC799737
BOOL_TRUE = 0x997275B5
MSG_CONTAINER_CID = 0x73F1F8DC
RPC_RESULT_CID = 0xF35C6D01


class TLType:
    ...


@dataclass(init=True, repr=True, frozen=True, kw_only=True)
class CoreMessage:
    msg_id: int
    seq_no: int
    obj: TLType


def read_string(data: BytesIO) -> str:
    return read_bytes(data).decode(errors="ignore")


def read_builtin(TL, typ: type, data: BytesIO):
    if issubclass(typ, bool):
        cid = read_int(data.read(4))
        assert cid in [BOOL_FALSE, BOOL_TRUE], "Invalid bool value provided"
        return cid == BOOL_TRUE
    elif issubclass(typ, int):
        return read_int(data.read(4))
    elif issubclass(typ, float):
        return struct.unpack("d", data.read(8))[0]
    elif issubclass(typ, str):
        return read_string(data)
    elif issubclass(typ, bytes):
        return read_bytes(data)
    elif isinstance(typ, GenericAlias):
        if issubclass(typ.mro()[0], list):
            args = typ.__args__
            assert len(args) >= 1, "Wrong type specified"
            ret = args[0]
            
            is_raw = len(args) > 1 and args[1] == "RAW"
            if not is_raw:
                cid = data.read(4)
                # ic(cid.hex())
                assert read_int(cid) == VECTOR_CID, "Vector with wrong constructor id"
            # if isinstance(ret, str) or issubclass(ret, TLType):
            #     cid = read_int(data.read(4))
            #     print(cid, hex(cid))

            length = read_int(data.read(4))
            # ic(length)

            result = []
            if is_raw and issubclass(ret, bytes):
                # logger.warning("If this didn't work, remember that you didn't check RAW is_raw types read for msg_container yet...")

                for _ in range(length):
                    msg_id = read_int(data.read(8))
                    seq_no = read_int(data.read(4))
                    length = read_int(data.read(4))
                    # ic(msg_id, seq_no, length)

                    result.append(
                        CoreMessage(
                            msg_id=msg_id,
                            seq_no=seq_no,
                            obj=TL.decode(data),
                        )
                    )
            elif isinstance(ret, str) or (inspect.isclass(ret) and issubclass(ret, TLType)):
                for _ in range(length):
                    result.append(TL.decode(data))
            elif isinstance(ret, Basic):
                if isinstance(ret, Int):
                    for _ in range(length):
                        result.append(ret.deserialize(data))
                else:
                    assert False, "TODO, flags read in vector?"
            else:
                for _ in range(length):
                    result.append(read_builtin(TL, ret, data))
            return result
        else:
            assert False, "Unreachable"
    else:
        raise TypeError(f"Invalid type, couldn't deserialize: {nameof(typ)}")


def write_builtin(TL, typ: type, value, to: BytesIO):
    if not typecheck(typ, value):
        raise TypeError("Invalid type")
    elif isinstance(typ, GenericAlias) and issubclass(typ.mro()[0], (list,)):
        if issubclass(typ.mro()[0], list):
            args = typ.__args__
            assert len(args) >= 1, "Wrong type specified"
            ret = args[0]

            is_raw = len(args) > 1 and args[1] == "RAW"
            if not is_raw:
                write_builtin(TL, int, VECTOR_CID, to=to)
            write_builtin(TL, int, len(value), to=to)

            if len(value) == 0:
                return

            check_type = ret
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                check_type = type(ret)

            if issubclass(check_type, Basic):
                if issubclass(check_type, Int):
                    for element in value:
                        to.write(ret.serialize(element))
                # elif isinstance(typ, FlagsOf):
                #     for element in value:
                #         to.write(ret.serialize(element))
                else:
                    assert False, "Unreachable"
            elif issubclass(check_type, TLType) or isinstance(value[0], TLType):
                # write_builtin(TL, int, value[0]._cid, to=to)

                for element in value:
                    to.write(TL.encode(element))
            elif issubclass(check_type, bytes) and is_raw:
                for element in value:
                    to.write(element)
            else:
                for element in value:
                    write_builtin(TL, ret, element, to=to)
        else:
            assert False, "Unreachable"
    elif issubclass(typ, bool):
        to.write(Int32.serialize(BOOL_TRUE if value else BOOL_FALSE))
    elif issubclass(typ, int):
        to.write(int.to_bytes(value, 4, byteorder="little", signed=False))
    elif isinstance(typ, float):
        to.write(struct.pack("d", value))
    elif issubclass(typ, str):
        write_builtin(TL, bytes, value.encode(), to=to)
    elif issubclass(typ, bytes):
        write_bytes(value, to=to)
    else:
        raise TypeError("Invalid type, couldn't serialize")


def typecheck(typ, value) -> bool:
    if isinstance(typ, FlagsOf):
        return typecheck(typ.typ, value)
    elif isinstance(typ, str) and isinstance(value, TLType):
        # print(typ, value._, repr(value), typ == value._)
        # TODO: user of User (using obj["is"])
        return True
    elif isinstance(typ, GenericAlias) or not inspect.isclass(typ):
        if isinstance(typ, GenericAlias):
            if issubclass(typ.mro()[0], list):
                if not isinstance(value, list):
                    return False

                args = typ.__args__
                assert len(args) >= 1, "Wrong type specified"
                ret = args[0]

                if len(value) == 0:
                    return True

                if isinstance(ret, str) and isinstance(value[0], (TLType, dict)):
                    return True
                return typecheck(ret, value[0])
            else:
                assert False, "Unreachable"
        elif isinstance(typ, Basic):
            if issubclass(type(typ), Int) and isinstance(value, int):
                return True
    else:
        if issubclass(typ, (bool, int, float, str, bytes)):
            return isinstance(value, typ)
        elif issubclass(typ, Basic):
            if issubclass(typ, Int) and isinstance(value, int):
                return True
            elif issubclass(typ, Bit) and isinstance(value, bool):
                return True
        elif issubclass(typ, TLType):
            return isinstance(value, (dict, TLType))
    return False


class Basic(ABC):
    @abstractmethod
    def deserialize(cls, TL, data: BytesIO):
        ...

    @abstractmethod
    def serialize(cls, TL):
        ...


class Int(Basic):
    def __init__(self, name: str, size: int, signed: bool = False):
        self.size = size
        self.signed = signed
        self.__name__ = name

    def deserialize(self, data: BytesIO, signed: bool | None = None) -> int:
        return read_int(data.read(self.size), signed=signed if signed is not None else self.signed)

    def serialize(self, n: int, signed: bool | None = None) -> bytes:
        return n.to_bytes(self.size, byteorder="little", signed=signed if signed is not None else self.signed)

    def __str__(self) -> str:
        return f"{nameof(self)}(signed={self.signed})"
    
    def __repr__(self) -> str:
        return nameof(self)

    def __call__(self, signed: bool = False) -> "Int":
        return Int(self.__name__, self.size, signed=signed)


Int32 = Int("Int32", size=32 // 8)
Int64 = Int("Int64", size=64 // 8)
Int128 = Int("Int128", size=128 // 8)
Int256 = Int("Int256", size=256 // 8)


class FlagsOf(Basic):
    def __init__(self, param: str, pos: int, typ) -> None:
        self.param = param
        self.pos = pos
        self.typ = typ

    def deserialize(self, TL, result: TLType, data: BytesIO):
        if self.typ is Bit:
            return bool(getattr(result, self.param) & (1 << self.pos))
        elif getattr(result, self.param) & (1 << self.pos):
            if isinstance(self.typ, str):
                return TL.decode(data)

            check_type = self.typ
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                check_type = type(self.typ)

            if issubclass(check_type, GenericAlias) or issubclass(check_type, (bool, int, float, str, bytes)):
                decoded = read_builtin(TL, self.typ, data)
            elif issubclass(check_type, Basic):
                decoded = self.typ.deserialize(data)
            elif issubclass(check_type, TLType):
                decoded = TL.decode(data)
            else:
                raise ValueError("Invalid type")

            return decoded
        return None

    def serialize(self, TL, field: str, orig: dict, obj) -> bytes:
        if self.typ is Bit:
            if orig.get(field, False):
                orig[self.param] |= (1 << self.pos)
            else:
                orig[self.param] &= ~(1 << self.pos)
            return b""
        elif orig[self.param] & (1 << self.pos):
            if isinstance(self.typ, str):
                return TL.encode(obj)

            check_type = self.typ
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                check_type = type(self.typ)

            if issubclass(check_type, (bool, int, float, str, bytes, list, GenericAlias)):
                tmp = BytesIO()
                write_builtin(TL, self.typ, obj, to=tmp)
                return tmp.getvalue()
            elif issubclass(check_type, Basic):
                # print(name, field, typ)
                if isinstance(self.typ, Int):
                    return self.typ.serialize(obj)
                elif isinstance(self.typ, FlagsOf):
                    return self.typ.serialize(TL, obj)
                else:
                    assert False, "Unreachable"
            elif issubclass(check_type, TLType):
                return TL.encode(obj)
            else:
                raise ValueError("Invalid type")
        return b""

    def __str__(self) -> str:
        return f"{nameof(self)}({self.param}, {self.pos}, {nameof(self.typ)})"


class Bit(Basic):
    ...
