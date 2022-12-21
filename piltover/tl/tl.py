import json
import inspect

from io import BytesIO
from typing import cast, Union, Any
from types import GenericAlias
from collections import defaultdict

from piltover.tl.types import Basic, TLType, Int, Int64, Int128, Int256, FlagsOf, read_builtin, write_builtin, typecheck
from piltover.exceptions import InvalidConstructor
from piltover.utils import nameof


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
    0x7abe77ec: {
        "_": "ping",
        "params": {
            "ping_id": Int64,
        },
        "ret": "Pong",
    },
    0x347773c5: {
        "_": "pong",
        "params": {
            "msg_id": Int64,
            "ping_id": Int64,
        },
        "is": "Pong",
    },
    0xda9b0d0d: {
        "_": "invokeWithLayer",
        "params": {
            "layer": int,
            "query": TLType,
        },
        "ret": TLType,
    },
    0xc1cd5ea9: {
        "_": "initConnection",
        "params": {
            "flags": int,
            "api_id": int,
            "device_model": str,
            "system_version": str,
            "app_version": str,
            "system_lang_code": str,
            "lang_pack": str,
            "lang_code": str,
            "proxy": FlagsOf("flags", 0, "InputClientProxy"),
            "params": FlagsOf("flags", 1, "JSONValue"),
            "query": TLType,
        },
        "ret": TLType,
    },
    0xc4f9186b: {
        "_": "help.getConfig",
        "ret": "Config",
    },
    0x232566ac: {
        "_": "config",
        "params": {
            "flags": int,
            "phonecalls_enabled": FlagsOf("flags", 1, bool),
            "default_p2p_contacts": FlagsOf("flags", 3, bool),
            "preload_featured_stickers": FlagsOf("flags", 4, bool),
            "ignore_phone_entities": FlagsOf("flags", 5, bool),
            "revoke_pm_inbox": FlagsOf("flags", 6, bool),
            "blocked_mode": FlagsOf("flags", 8, bool),
            "pfs_enabled": FlagsOf("flags", 13, bool),
            "force_try_ipv6": FlagsOf("flags", 14, bool),
            "date": int,
            "expires": int,
            "test_mode": bool,
            "this_dc": int,
            "dc_options": list["DcOption"],
            "dc_txt_domain_name": str,
            "chat_size_max": int,
            "megagroup_size_max": int,
            "forwarded_count_max": int,
            "online_update_period_ms": int,
            "offline_blur_timeout_ms": int,
            "offline_idle_timeout_ms": int,
            "online_cloud_timeout_ms": int,
            "notify_cloud_delay_ms": int,
            "notify_default_delay_ms": int,
            "push_chat_period_ms": int,
            "push_chat_limit": int,
            "saved_gifs_limit": int,
            "edit_time_limit": int,
            "revoke_time_limit": int,
            "revoke_pm_time_limit": int,
            "rating_e_decay": int,
            "stickers_recent_limit": int,
            "stickers_faved_limit": int,
            "channels_read_media_period": int,
            "tmp_sessions": FlagsOf("flags", 0, int),
            "pinned_dialogs_count_max": int,
            "pinned_infolder_count_max": int,
            "call_receive_timeout_ms": int,
            "call_ring_timeout_ms": int,
            "call_connect_timeout_ms": int,
            "call_packet_timeout_ms": int,
            "me_url_prefix": str,
            "autoupdate_url_prefix": FlagsOf("flags", 7, str),
            "gif_search_username": FlagsOf("flags", 9, str),
            "venue_search_username": FlagsOf("flags", 10, str),
            "img_search_username": FlagsOf("flags", 11, str),
            "static_maps_provider": FlagsOf("flags", 12, str),
            "caption_length_max": int,
            "message_length_max": int,
            "webfile_dc_id": int,
            "suggested_lang_code": FlagsOf("flags", 2, str),
            "lang_pack_version": FlagsOf("flags", 2, int),
            "base_lang_pack_version": FlagsOf("flags", 2, int),
            "reactions_default": FlagsOf("flags", 15, "Reaction"),
        },
        "ret": "Config",
    },
    0xf35c6d01: {
        "_": "rpc_result",
        "params": {
            "req_msg_id": Int64,
            "result": TLType,
        },
        "is": "RpcResult",
    },
    0x73f1f8dc: {
        "_": "msg_container",
        "params": {
            "messages": list[bytes, "RAW"],
        },
        "is": "MessageContainer",
    },
}

NAME_MAP: dict[int, dict] = {
    ref["_"]: {
        "cid": cid,
        **ref,
    }
    for cid, ref
    in MAP.items()
}

# resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector<long> = ResPQ;


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

            if issubclass(check_type, GenericAlias) or issubclass(check_type, (bool, int, str, bytes)):
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
        for field, typ in tltype["params"].items():
            if isinstance(typ, FlagsOf):
                if obj.get(field, None) is not None:
                    reference_flags[typ.param] |= typ.pos
                else:
                    to_skip.add(field)
                    reference_flags[typ.param] |= 0

        for field, typ in tltype["params"].items():
            if field in to_skip:
                continue

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

            if issubclass(check_type, (bool, int, str, bytes, list, GenericAlias)):
                write_builtin(TL, typ, value, to=result)
            elif issubclass(check_type, Basic):
                # print(name, field, typ)
                if isinstance(typ, Int):
                    result.write(typ.serialize(value))
                elif isinstance(typ, FlagsOf):
                    result.write(typ.serialize(TL, value))
                else:
                    assert False, "Unreachable"
            elif issubclass(check_type, TLType):
                result.write(TL.encode(value))
            else:
                raise ValueError(f"Invalid type: expected {field}: {nameof(typ)}, got {nameof(value)}")

        result.seek(0)
        data = result.read()
        return data

    @staticmethod
    def from_dict(obj: dict) -> "TL":
        objname = obj["_"]
        tltype = NAME_MAP[objname]

        result = type(objname, (TL,), {})()
        result._ = objname

        reference_flags: defaultdict[str, int] = defaultdict(int)
        to_skip: set[str] = set()
        for field, typ in tltype["params"].items():
            if isinstance(typ, FlagsOf):
                if obj.get(field, None) is not None:
                    reference_flags[typ.param] |= typ.pos
                else:
                    to_skip.add(field)
                    reference_flags[typ.param] |= 0

        for field, typ in tltype["params"].items():
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

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)
