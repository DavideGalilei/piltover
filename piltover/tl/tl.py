from io import BytesIO
from typing import cast

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
        assert len(args) != 1, "Wrong type specified"
        ret: typ = args[0]

        assert read_int(data.read(4)) == VECTOR_CID, "Vector with wrong constructor id"
        length = read_int(data.read(4))

        result = []
        for i in range(length):
            result.append(read_builtin(ret, data))
        return result
    else:
        raise TypeError("Invalid type, couldn't deserialize")


class TL:
    @staticmethod
    def decode(data: BytesIO) -> "TL":
        cid = int.from_bytes(data.read(4), byteorder="little", signed=False)

        reference = MAP[cid]
        objname = reference["_"]
        result = type(objname, (TL,), {})()

        for name, typ in reference["params"].items():
            if issubclass(typ, Basic):
                decoded = typ.deserialize(data)
            elif isinstance(typ, (int, str, bytes, list)):
                decoded = read_builtin(typ, data)
            else:
                raise ValueError(f"Invalid type: {objname}({name}: {typ})")

            setattr(result, name, decoded)

        return cast(TL, result)

    def __str__(self) -> str:
        return f"""{type(self).__name__}({
            ", ".join(
                f"{param}={value}"
                for param, value
                in self.__dict__.items()
                if not callable(value) and not param.startswith("_")
            )
        })"""

    __repr__ = __str__
