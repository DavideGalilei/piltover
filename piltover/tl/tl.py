import json
import inspect

from io import BytesIO
from typing import cast, Union
from types import GenericAlias

from piltover.tl.types import Basic, Int, Int64, Int128, Int256
from piltover.utils import read_int, nameof
from piltover.exceptions import InvalidConstructor


VECTOR_CID = 0x1cb5c415


MAP = {
    0xbe7e8ef1: {
        "_": "req_pq_multi",
        "params": {
            "nonce": Int128(signed=True),
        },
        "ret": "ResPQ",
    },
    0x60469778: {
        "_": "req_pq",
        "params": {
            "nonce": Int128(signed=True),
        },
        "ret": "ResPQ",
    },
    0x05162463: {
        "_": "resPQ",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "pq": bytes,
            "server_public_key_fingerprints": list[Int64(signed=False)],
        },
        "is": "ResPQ",
    },
    0xd712e4be: {
        "_": "req_DH_params",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "p": bytes,
            "q": bytes,
            "public_key_fingerprint": Int64,
            "encrypted_data": bytes,
        },
        "ret": "Server_DH_Params"
    },
    0x83c95aec: {
        "_": "p_q_inner_data",
        "params": {
            "pq": bytes,
            "p": bytes,
            "q": bytes,
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "new_nonce": Int256(signed=False),
        },
        "is": "P_Q_inner_data",
    },
    0xa9f55f95: {
        "_": "p_q_inner_data_dc",
        "params": {
            "pq": str,
            "p": str,
            "q": str,
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "new_nonce": Int256(signed=False),
            "dc": int,
        },
        "is": "P_Q_inner_data",
    },
    0xd0e8075c: {
        "_": "server_DH_params_ok",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "encrypted_answer": bytes,
        },
        "is": "Server_DH_Params",
    },
    0xb5890dba: {
        "_": "server_DH_inner_data",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "g": int,
            "dh_prime": bytes,
            "g_a": bytes,
            "server_time": int,
        },
        "is": "Server_DH_inner_data",
    },
    0xf5045f1f: {
        "_": "set_client_DH_params",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "encrypted_data": bytes,
        },
        "ret": "Set_client_DH_params_answer",
    },
    0x6643b654: {
        "_": "client_DH_inner_data",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "retry_id": Int64(signed=True),
            "g_b": bytes,
        },
        "is": "Client_DH_Inner_Data",
    },
    0x3bcbf734: {
        "_": "dh_gen_ok",
        "params": {
            "nonce": Int128(signed=True),
            "server_nonce": Int128(signed=True),
            "new_nonce_hash1": Int128(signed=False),
        },
        "is": "Set_client_DH_params_answer",
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
    if issubclass(typ, int):
        return read_int(data.read(4))
    elif issubclass(typ, str):
        return read_string(data)
    elif issubclass(typ, bytes):
        return read_bytes(data)
    elif isinstance(typ, GenericAlias):
        if issubclass(typ.mro()[0], list):
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
            assert False, "Unreachable"
    else:
        raise TypeError(f"Invalid type, couldn't deserialize: {nameof(typ)}")


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

            check_type = ret
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                check_type = type(ret)

            if issubclass(check_type, Basic):
                for element in value:
                    to.write(ret.serialize(element))
            elif issubclass(check_type, TL):
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
    if isinstance(typ, GenericAlias) or not inspect.isclass(typ):
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
            else:
                assert False, "Unreachable"
        elif isinstance(typ, Basic):
            if issubclass(type(typ), Int) and isinstance(value, int):
                return True
    else:
        if issubclass(typ, (int, str, bytes)):
            return isinstance(value, typ)
        elif issubclass(typ, Basic):
            if issubclass(typ, Int) and isinstance(value, int):
                return True
        elif issubclass(typ, TL):
            return isinstance(value, (dict, TL))
    return False


class TL:
    @staticmethod
    def decode(data: BytesIO) -> "TL":
        cid = int.from_bytes(data.read(4), byteorder="little", signed=False)

        if cid not in MAP:
            raise InvalidConstructor(cid=cid)
        reference = MAP[cid]
        objname = reference["_"]
        result = type(objname, (TL,), {})()

        for name, typ in reference.get("params", {}).items():
            check_type = typ
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                check_type = type(typ)

            if issubclass(check_type, GenericAlias) or issubclass(check_type, (int, str, bytes)):
                decoded = read_builtin(typ, data)
            elif issubclass(check_type, Basic):
                decoded = typ.deserialize(data)
            elif issubclass(check_type, TL):
                decoded = TL.decode(data)
            else:
                raise ValueError(f"Invalid type: {objname}({name}: {nameof(typ)})")

            setattr(result, name, decoded)

        result._cid = cid
        result._ = objname
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

            checked = False
            check_type = typ
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                if not typecheck(check_type, value):
                    raise TypeError(f"Wrong parameter type for {field!r}: got {nameof(value)} but expected {nameof(typ)}")
                checked = True
                check_type = type(typ)

            if not checked and not typecheck(check_type, value):
                raise TypeError(f"Wrong parameter type for {field!r}: got {nameof(value)} but expected {nameof(typ)}")

            if field.startswith("_"):
                continue
            elif field not in obj:
                raise ValueError(f"Missing parameter {field!r} of type {nameof(typ)}")

            if issubclass(check_type, (int, str, bytes, list, GenericAlias)):
                write_builtin(typ, value, to=result)
            elif issubclass(check_type, Basic):
                # print(name, field, typ)
                result.write(typ.serialize(value))
            elif issubclass(check_type, TL):
                result.write(TL.encode(value))
            else:
                raise ValueError(f"Invalid type: expected {field}: {nameof(typ)}, got {nameof(value)}")

        result.seek(0)
        data = result.read()
        return data

    def get_dict(self) -> dict:
        attrs = {"_": nameof(self)}
        attrs |= {
            param: value
            for param, value
            in self.__dict__.items()
            if not callable(value) and not param.startswith("_")
        }
        return attrs

    def __str__(self) -> str:
        attrs = self.get_dict()
        return json.dumps(attrs, indent=4, default=str)

    def __repr__(self) -> str:
        return f"""{nameof(self)}({
            ", ".join(
                f"{param}={value}"
                for param, value
                in self.__dict__.items()
                if not callable(value) and not param.startswith("_")
            )
        })"""

    def __getattr__(self, __name: str):
        return self.__getattribute__(__name)
