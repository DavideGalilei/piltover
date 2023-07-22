import json
import inspect

from io import BytesIO
from typing import cast, Union, Any
from types import GenericAlias
from collections import defaultdict

from loguru import logger

from piltover.tl.types import (
    Basic,
    TLType,
    Int,
    FlagsOf,
    Bit,
    read_builtin,
    write_builtin,
    typecheck,
)
from piltover.exceptions import InvalidConstructor
from piltover.utils import nameof

try:
    from piltover.tl.generated import MAP, NAME_MAP
except ImportError:
    logger.error(
        "Couldn't import TL map. Please run this command and try again `python3 tools/gen_tl.py update`"
    )
    exit(1)

from icecream import ic


class TL(TLType):
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

            if issubclass(check_type, GenericAlias) or issubclass(
                check_type, (bool, int, float, str, bytes)
            ):
                decoded = read_builtin(TL, typ, data)
            elif issubclass(check_type, Basic):
                if isinstance(typ, Int):
                    decoded = typ.deserialize(data)
                elif isinstance(typ, FlagsOf):
                    decoded = typ.deserialize(TL, result, data)
                else:
                    assert False, "Unreachable"
            elif issubclass(check_type, TLType):
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

        if isinstance(obj, TLType):
            obj = obj.get_dict()

        name = obj["_"]
        tltype = NAME_MAP[name]

        write_builtin(TL, int, tltype["cid"], to=result)

        reference_flags: defaultdict[str, int] = defaultdict(int)
        to_skip: set[str] = set()
        for field, typ in tltype.get("params", {}).items():
            if isinstance(typ, FlagsOf):
                if typ.typ is Bit:
                    typ.serialize(TL, field, obj, obj)

                    if obj.get(field, False):
                        reference_flags[typ.param] |= 1 << typ.pos
                    else:
                        reference_flags[typ.param] &= ~(1 << typ.pos)

                    if field not in obj:
                        to_skip.add(field)
                else:
                    if obj.get(field, None) is not None:
                        reference_flags[typ.param] |= 1 << typ.pos
                    else:
                        to_skip.add(field)
                        reference_flags[typ.param] &= ~(1 << typ.pos)

        for field, typ in tltype.get("params", {}).items():
            if field in to_skip:
                continue
            elif field in reference_flags:
                obj[field] = reference_flags[field]
                # ic("FLAGS", value)

            value = obj[field]

            checked = False
            check_type = typ
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                if not typecheck(typ, value):
                    raise TypeError(
                        f"Wrong parameter type for {field!r}: got {nameof(value)} but expected {nameof(typ)}"
                    )
                checked = True
                check_type = type(typ)

            if not checked and not typecheck(check_type, value):
                raise TypeError(
                    f"Wrong parameter type for {field!r}: got {nameof(value)} but expected {nameof(typ)}"
                )

            if field.startswith("_"):
                continue
            elif field not in obj:
                raise ValueError(f"Missing parameter {field!r} of type {nameof(typ)}")

            if issubclass(
                check_type, (bool, int, float, str, bytes, list, GenericAlias)
            ):
                write_builtin(TL, typ, value, to=result)
            elif issubclass(check_type, Basic):
                if isinstance(typ, Int):
                    result.write(typ.serialize(value))
                elif isinstance(typ, FlagsOf):
                    result.write(typ.serialize(TL, field, obj, value))
                else:
                    assert False, "Unreachable"
            elif issubclass(check_type, TLType):
                result.write(TL.encode(value))
            else:
                raise ValueError(
                    f"Invalid type: expected {field}: {nameof(typ)}, got {nameof(value)}"
                )

        return result.getvalue()

    @staticmethod
    def from_dict(obj: dict) -> "TL":
        objname = obj["_"]
        tltype = NAME_MAP[objname]

        result = type(objname, (TL,), {})()
        result._ = objname
        result._cid = tltype["cid"]

        reference_flags: defaultdict[str, int] = defaultdict(int)
        to_skip: set[str] = set()
        for field, typ in tltype.get("params", {}).items():
            if isinstance(typ, FlagsOf):
                if obj.get(field, None) is not None:
                    reference_flags[typ.param] |= 1 << typ.pos
                else:
                    to_skip.add(field)
                    reference_flags[typ.param] &= ~(1 << typ.pos)

        for field, typ in tltype.get("params", {}).items():
            if field.startswith("_") or field in to_skip:
                continue
            elif field in reference_flags:
                setattr(result, field, reference_flags[field])
                continue
            elif field not in obj:
                raise ValueError(f"Missing parameter {field!r} of type {nameof(typ)}")

            value = obj[field]

            """
            checked = False
            check_type = typ
            if isinstance(check_type, GenericAlias) or not inspect.isclass(check_type):
                if not typecheck(check_type, value):
                    raise TypeError(f"Wrong parameter type for {field!r}: got {nameof(value)} but expected {nameof(typ)}")
                checked = True
                check_type = type(typ)

            if not checked and not typecheck(check_type, value):
                raise TypeError(f"Wrong parameter type for {field!r}: got {nameof(value)} but expected {nameof(typ)}")
            """

            setattr(result, field, value)

        return result

    def get_dict(self) -> dict:
        attrs = {"_": nameof(self)}
        attrs |= {
            param: value
            for param, value in self.__dict__.items()
            if not callable(value) and not param.startswith("_")
        }
        return attrs

    def _get_recursive_dict(self) -> dict:
        result = {
            "_": self._,
        }

        for param, value in self.__dict__.items():
            if not callable(value) and not param.startswith("_"):
                if isinstance(value, TL):
                    result |= {param: value._get_recursive_dict()}
                elif isinstance(value, list):
                    tmp = []
                    for item in value:
                        if isinstance(item, TL):
                            tmp.append(item._get_recursive_dict())
                        else:
                            tmp.append(item)
                    result |= {param: tmp}
                else:
                    result |= {param: value}
        return result

    def __str__(self) -> str:
        attrs = self._get_recursive_dict()
        return json.dumps(attrs, indent=4, default=str)

    def __repr__(self) -> str:
        return f"""{nameof(self)}({
            ", ".join(
                f"{param}={value!r}"
                for param, value
                in self.__dict__.items()
                if not callable(value) and not param.startswith("_")
            )
        })"""

    def __getattr__(self, __name: str):
        return self.__getattribute__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)
