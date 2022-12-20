import inspect

from hashlib import sha256
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


def kdf(auth_key: bytes, msg_key: bytes, outgoing: bool) -> tuple:
    # taken from pyrogram, mtproto.py
    # https://core.telegram.org/mtproto/description#defining-aes-key-and-initialization-vector
    x = 0 if outgoing else 8

    sha256_a = sha256(msg_key + auth_key[x: x + 36]).digest()
    sha256_b = sha256(auth_key[x + 40:x + 76] + msg_key).digest()  # 76 = 40 + 36

    aes_key = sha256_a[:8] + sha256_b[8:24] + sha256_a[24:32]
    aes_iv = sha256_b[:8] + sha256_a[8:24] + sha256_b[24:32]

    return aes_key, aes_iv
