"""
import warnings

from importlib import import_module

MAP = {}

for module in ["api_tl", "map"]:
    try:
        module = import_module(module, "piltover.tl.generated")
        MAP |= module.MAP
    except ImportError:
        warnings.warn(f"Couldn't import {module}.py")


if not MAP:
    warnings.warn("Empty MAP")
    raise ImportError("Empty MAP")
"""

from piltover.tl.types import (
    VECTOR_CID,
    BOOL_TRUE,
    BOOL_FALSE,
    MSG_CONTAINER_CID,
    RPC_RESULT_CID,
    RPC_ERROR_CID,
    Int32,
    Int64,
    TLType,
    FlagsOf,
    Bit,
)

from .api_tl import MAP as API_MAP, LAYER
from .mtproto_tl import MAP as MTPROTO_MAP


MAP = API_MAP | MTPROTO_MAP

# hardcoded types
MAP |= {
    VECTOR_CID: {
        "_": "vector",
        "params": {
            "data": list[TLType, "RAW"],
        },
        "is": "Vector",
    },
    BOOL_TRUE: {
        "_": "boolTrue",
        "is": "Bool",
    },
    BOOL_FALSE: {
        "_": "boolFalse",
        "is": "Bool",
    },
    MSG_CONTAINER_CID: {
        "_": "msg_container",
        "params": {
            "messages": list[bytes, "RAW"],
        },
        "is": "MessageContainer",
    },
    RPC_RESULT_CID: {
        "_": "rpc_result",
        "params": {
            "req_msg_id": Int64,
            "result": TLType,
        },
        "is": "RpcResult",
    },
    RPC_ERROR_CID: {
        "_": "rpc_error",
        "params": {
            "error_code": Int32,
            "error_message": str,
        },
        "is": "RpcError",
    },
}

# TODO: multiple layers support
# special cased constructors
MAP |= {
    0x2619a90e: {
        "_": "messages.getStickerSet_71",
        "params": {
            "stickerset": TLType,
        },
        "ret": "messages.StickerSet",
    },
    0xb60a24a6: {
        "_": "messages.stickerSet_71",
        "params": {
            "set": TLType,  # StickerSet_71
            "packs": list["StickerPack"],
            "documents": list["Document_71"],
        },
        "is": "messages.StickerSet_71",
    },
    0xcd303b41: {
        "_": "stickerSet_71",
        "params": {
            "flags": Int32,
            "installed": FlagsOf("flags", 0, Bit),
            "archived": FlagsOf("flags", 1, Bit),
            "official": FlagsOf("flags", 2, Bit),
            "masks": FlagsOf("flags", 3, Bit),
            "id": Int64,
            "access_hash": Int64,
            "title": str,
            "short_name": str,
            "count": int,
            "hash": int,
        },
        "is": "StickerSet_71",
    },
    0x800fd57d: {
        "_": "langpack.getLanguages_72",
        "ret": list["LangPackLanguage_72"],
    },
    0x117698f1: {
        "_": "langPackLanguage_72",
        "params": {
            "name": str,
            "native_name": str,
            "lang_code": str,
        },
        "is": "LangPackLanguage_72",
    },
}

NAME_MAP: dict[int, dict] = {
    ref["_"]: {
        "cid": cid,
        **ref,
    }
    for cid, ref in MAP.items()
}

__all__ = ["MAP", "NAME_MAP", "LAYER"]
