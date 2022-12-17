import inspect

from types import GenericAlias


def read_int(data: bytes, signed: bool = False) -> int:
    return int.from_bytes(data, byteorder="little", signed=signed)


def nameof(class_or_value) -> str:
    if hasattr(class_or_value, "__name__"):
        return class_or_value.__name__
    elif isinstance(class_or_value, GenericAlias):
        return str(class_or_value)
    elif inspect.isclass(class_or_value):
        return class_or_value.__name__
    return type(class_or_value).__name__
