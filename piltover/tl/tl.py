import json

from io import BytesIO
from typing import cast, Union
from types import GenericAlias

from piltover.tl.types import Basic, Int64, Int128
from piltover.utils import read_int


VECTOR_CID = 0x1cb5c415


MAP = {
    0xbe7e8ef1: {
        "_": "req_pq_multi",
        "params": {
            "nonce": Int128,
        },
        "ret": "ResPQ",
    },
    0x60469778: {
        "_": "req_pq",
        "params": {
            "nonce": Int128,
        },
        "ret": "ResPQ",
    },
    0x05162463: {
        "_": "resPQ",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "pq": str,
            "server_public_key_fingerprints": list[Int64],
        },
        "is": "ResPQ",
    },
}

NAME_MAP = {
    ref["_"]: {
        "cid": cid,
        **ref,
    }
    for cid, ref
    in MAP.items()
}

# resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector<long> = ResPQ;


def read_bytes(data: BytesIO) -> bytes:
    # https://core.telegram.org/mtproto/serialize#base-types

    length = int.from_bytes(data.read(1), "little")

    if length <= 253:
        result = data.read(length)
        data.read(-(length + 1) % 4)
    else:
        length = int.from_bytes(data.read(3), "little")
        result = data.read(length)
        data.read(-length % 4)
    
    return result


def read_string(data: BytesIO) -> str:
    return read_bytes(data).decode(errors="ignore")


def read_builtin(typ: type, data: BytesIO):
    if isinstance(typ, int):
        return read_int(data.read(4))
    elif isinstance(typ, str):
        return read_string(data)
    elif isinstance(typ, bytes):
        return read_bytes(data)
    elif isinstance(typ, list):
        args = typ.__args__
        assert len(args) == 1, "Wrong type specified"
        ret: type = args[0]

        assert read_int(data.read(4)) == VECTOR_CID, "Vector with wrong constructor id"
        if issubclass(ret, TL):
            cid = read_int(data.read(4))

        length = read_int(data.read(4))

        result = []
        if issubclass(ret, TL):
            for _ in range(length):
                result.append(TL.decode(data))
        else:
            for _ in range(length):
                result.append(read_builtin(ret, data))
        return result
    else:
        raise TypeError("Invalid type, couldn't deserialize")


def write_builtin(typ: type, value, to: BytesIO):
    if not typecheck(typ, value):
        raise TypeError("Invalid type")
    elif isinstance(typ, GenericAlias) and issubclass(typ.mro()[0], (list,)):
        if issubclass(typ.mro()[0], list):
            args = typ.__args__
            assert len(args) == 1, "Wrong type specified"
            ret: type = args[0]

            write_builtin(int, VECTOR_CID, to=to)
            write_builtin(int, len(value), to=to)

            if issubclass(ret, Basic):
                for element in value:
                    to.write(ret.serialize(element))
            elif issubclass(ret, TL):
                write_builtin(int, value._cid, to=to)

                for element in value:
                    to.write(element.serialize())
            else:
                for element in value:
                    write_builtin(ret, element, to=to)
        else:
            assert False, "Unreachable"
    elif issubclass(typ, int):
        to.write(int.to_bytes(value, 4, byteorder="little", signed=False))
    elif issubclass(typ, str):
        write_builtin(bytes, value.encode(), to=to)
    elif issubclass(typ, bytes):
        length = len(value)

        if length <= 253:
            to.write(
                bytes([length])
                + value
                + bytes(-(length + 1) % 4)
            )
        else:
            to.write(
                bytes([254])
                + length.to_bytes(3, "little")
                + value
                + bytes(-length % 4)
            )
    else:
        raise TypeError("Invalid type, couldn't serialize")


def typecheck(typ: type, value) -> bool:
    if isinstance(typ, GenericAlias):
        if issubclass(typ.mro()[0], list):
            if not isinstance(value, list):
                return False

            args = typ.__args__
            assert len(args) == 1, "Wrong type specified"
            ret: type = args[0]

            if len(value) == 0:
                return True
            return typecheck(ret, value[0])
    elif issubclass(typ, (int, str, bytes)):
        return isinstance(value, (int, str, bytes))
    elif issubclass(typ, Basic):
        if typ in {Int64, Int128} and isinstance(value, int):
            return True
    elif issubclass(typ, TL):
        return isinstance(value, (dict, TL))
    return False


class TL:
    @staticmethod
    def decode(data: BytesIO) -> "TL":
        cid = int.from_bytes(data.read(4), byteorder="little", signed=False)

        reference = MAP[cid]
        objname = reference["_"]
        result = type(objname, (TL,), {})()

        for name, typ in reference["params"].items():
            if isinstance(typ, GenericAlias) or isinstance(typ, (int, str, bytes)):
                decoded = read_builtin(typ, data)
            if issubclass(typ, Basic):
                decoded = typ.deserialize(data)
            elif isinstance(typ, TL):
                decoded = TL.decode(data)
            else:
                raise ValueError(f"Invalid type: {objname}({name}: {typ})")

            setattr(result, name, decoded)

        result._cid = cid
        return cast(TL, result)

    @staticmethod
    def encode(obj: Union[dict, "TL"]) -> bytes:
        result = BytesIO()

        if isinstance(obj, TL):
            obj = obj.get_dict()
        
        name = obj["_"]
        tltype = NAME_MAP[name]

        write_builtin(int, tltype["cid"], to=result)

        for field, typ in tltype["params"].items():
            value = obj[field]

            if field.startswith("_"):
                continue
            elif field not in obj:
                raise ValueError(f"Missing parameter {field!r} of type {type(typ).__name__}")
            elif not typecheck(typ, value):
                raise TypeError(f"Wrong parameter type for {field!r}: got {type(value).__name__} but expected {typ.__name__}")

            if isinstance(typ, GenericAlias) or issubclass(typ, (int, str, bytes)):
                write_builtin(typ, value, to=result)
            elif issubclass(typ, Basic):
                result.write(typ.serialize(value))
            elif issubclass(typ, TL):
                result.write(TL.encode(value))
            else:
                raise ValueError(f"Invalid type: expected {field}: {typ.__name__}, got {type(value).__name__}")

        result.seek(0)
        data = result.read()
        print(data)
        return data

    def get_dict(self) -> dict:
        attrs = {"_": type(self).__name__}
        attrs |= {
            param: value
            for param, value
            in self.__dict__.items()
            if not callable(value) and not param.startswith("_")
        }
        return attrs

    def __str__(self) -> str:
        attrs = self.get_dict()
        return json.dumps(attrs, indent=4)

    def __repr__(self) -> str:
        return f"""{type(self).__name__}({
            ", ".join(
                f"{param}={value}"
                for param, value
                in self.__dict__.items()
                if not callable(value) and not param.startswith("_")
            )
        })"""
