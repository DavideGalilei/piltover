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
    Int64,
    TLType,
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
}

NAME_MAP: dict[int, dict] = {
    ref["_"]: {
        "cid": cid,
        **ref,
    }
    for cid, ref in MAP.items()
}

__all__ = ["MAP", "NAME_MAP", "LAYER"]
