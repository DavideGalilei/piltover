import json
import inspect

from io import BytesIO
from typing import cast, Union, Any
from types import GenericAlias
from collections import defaultdict

from piltover.tl.types import Basic, TLType, Int, Int64, Int128, Int256, FlagsOf, Bit, read_builtin, write_builtin, typecheck, VECTOR_CID
from piltover.exceptions import InvalidConstructor
from piltover.utils import nameof

from icecream import ic


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
            "server_public_key_fingerprints": list[Int64(signed=True)],
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
            "pq": bytes,
            "p": bytes,
            "q": bytes,
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
    0xbf9459b7: {
        "_": "invokeWithoutUpdates",
        "params": {
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
            "phonecalls_enabled": FlagsOf("flags", 1, Bit),
            "default_p2p_contacts": FlagsOf("flags", 3, Bit),
            "preload_featured_stickers": FlagsOf("flags", 4, Bit),
            "ignore_phone_entities": FlagsOf("flags", 5, Bit),
            "revoke_pm_inbox": FlagsOf("flags", 6, Bit),
            "blocked_mode": FlagsOf("flags", 8, Bit),
            "pfs_enabled": FlagsOf("flags", 13, Bit),
            "force_try_ipv6": FlagsOf("flags", 14, Bit),
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
    0x5e002502: {
        "_": "auth.sentCode",
        "params": {
            "flags": int,
            "type": TLType,
            "phone_code_hash": str,
            "next_type": FlagsOf("flags", 1, "auth.CodeType"),
            "timeout": FlagsOf("flags", 2, int),
        },
        "is": "auth.SentCode",
    },
    0xa677244f: {
        "_": "auth.sendCode",
        "params": {
            "phone_number": str,
            "api_id": int,
            "api_hash": str,
            "settings": TLType,
        },
        "ret": "auth.SentCode",
    },
    0xc000bba2: {
        "_": "auth.sentCodeTypeSms",
        "params": {
            "length": int,
        },
        "is": "auth.SentCodeType",
    },
    0x8a6469c2: {
        "_": "codeSettings",
        "params": {
            "flags": int,
            "allow_flashcall": FlagsOf("flags", 0, Bit),
            "current_number": FlagsOf("flags", 1, Bit),
            "allow_app_hash": FlagsOf("flags", 4, Bit),
            "allow_missed_call": FlagsOf("flags", 5, Bit),
            "logout_tokens": FlagsOf("flags", 6, list[bytes]),
        },
        "is": "CodeSettings",
    },
    0xf3427b8c: {
        "_": "ping_delay_disconnect",
        "params": {
            "ping_id": Int64,
            "disconnect_delay": int,
        },
        "ret": "Pong",
    },
    0x8d52a951: {
        "_": "auth.signIn",
        "params": {
            "flags": int,
            "phone_number": str,
            "phone_code_hash": str,
            "phone_code": FlagsOf("flags", 0, str),
            "email_verification": FlagsOf("flags", 1, "EmailVerification"),
        },
        "ret": "auth.Authorization",
    },
    0x33fb7bb8: {
        "_": "auth.authorization",
        "params": {
            "flags": int,
            "setup_password_required": FlagsOf("flags", 1, Bit),
            "otherwise_relogin_days": FlagsOf("flags", 1, int),
            "tmp_sessions": FlagsOf("flags", 0, int),
            "user": TLType, # User
        },
        "is": "auth.Authorization",
    },
    0x8f97c628: {
        "_": "user",
        "params": {
            "flags": int,
            "self": FlagsOf("flags", 10, Bit),
            "contact": FlagsOf("flags", 11, Bit),
            "mutual_contact": FlagsOf("flags", 12, Bit),
            "deleted": FlagsOf("flags", 13, Bit),
            "bot": FlagsOf("flags", 14, Bit),
            "bot_chat_history": FlagsOf("flags", 15, Bit),
            "bot_nochats": FlagsOf("flags", 16, Bit),
            "verified": FlagsOf("flags", 17, Bit),
            "restricted": FlagsOf("flags", 18, Bit),
            "min": FlagsOf("flags", 20, Bit),
            "bot_inline_geo": FlagsOf("flags", 21, Bit),
            "support": FlagsOf("flags", 23, Bit),
            "scam": FlagsOf("flags", 24, Bit),
            "apply_min_photo": FlagsOf("flags", 25, Bit),
            "fake": FlagsOf("flags", 26, Bit),
            "bot_attach_menu": FlagsOf("flags", 27, Bit),
            "premium": FlagsOf("flags", 28, Bit),
            "attach_menu_enabled": FlagsOf("flags", 29, Bit),
            "flags2": int,
            "id": Int64,
            "access_hash": FlagsOf("flags", 0, Int64),
            "first_name": FlagsOf("flags", 1, str),
            "last_name": FlagsOf("flags", 2, str),
            "username": FlagsOf("flags", 3, str),
            "phone": FlagsOf("flags", 4, str),
            "photo": FlagsOf("flags", 5, "UserProfilePhoto"),
            "status": FlagsOf("flags", 6, "UserStatus"),
            "bot_info_version": FlagsOf("flags", 14, int),
            "restriction_reason": FlagsOf("flags", 18, list["RestrictionReason"]),
            "bot_inline_placeholder": FlagsOf("flags", 19, str),
            "lang_code": FlagsOf("flags", 22, str),
            "emoji_status": FlagsOf("flags", 30, "EmojiStatus"),
            "usernames": FlagsOf("flags2", 0, list["Username"]),
        },
        "is": "User",
    },
    0xedd4882a: {
        "_": "updates.getState",
        "ret": "updates.State",
    },
    0xa56c2a3e: {
        "_": "updates.state",
        "params": {
            "pts": int,
            "qts": int,
            "date": int,
            "seq": int,
            "unread_count": int,
        },
        "is": "updates.State",
    },
    0xb60f5918: {
        "_": "users.getFullUser",
        "params": {
            "id": TLType,
        },
        "is": "users.UserFull",
    },
    0x3b6d152e: {
        "_": "users.userFull",
        "params": {
            "full_user": TLType,
            "chats": list["Chat"],
            "users": list["User"],
        },
        "is": "users.UserFull",
    },
    0xf7c1b13f: {
        "_": "inputUserSelf",
        "is": "InputUser",
    },
    0xc4b1fc3f: {
        "_": "userFull",
        "params": {
            "flags": int,
            "blocked": FlagsOf("flags", 0, Bit),
            "phone_calls_available": FlagsOf("flags", 4, Bit),
            "phone_calls_private": FlagsOf("flags", 5, Bit),
            "can_pin_message": FlagsOf("flags", 7, Bit),
            "has_scheduled": FlagsOf("flags", 12, Bit),
            "video_calls_available": FlagsOf("flags", 13, Bit),
            "voice_messages_forbidden": FlagsOf("flags", 20, Bit),
            "id": Int64,
            "about": FlagsOf("flags", 1, str),
            "settings": TLType,
            "profile_photo": FlagsOf("flags", 2, "Photo"),
            "notify_settings": TLType,
            "bot_info": FlagsOf("flags", 3, "BotInfo"),
            "pinned_msg_id": FlagsOf("flags", 6, int),
            "common_chats_count": int,
            "folder_id": FlagsOf("flags", 11, int),
            "ttl_period": FlagsOf("flags", 14, int),
            "theme_emoticon": FlagsOf("flags", 15, str),
            "private_forward_name": FlagsOf("flags", 16, str),
            "bot_group_admin_rights": FlagsOf("flags", 17, "ChatAdminRights"),
            "bot_broadcast_admin_rights": FlagsOf("flags", 18, "ChatAdminRights"),
            "premium_gifts": FlagsOf("flags", 19, list["PremiumGiftOption"]),
        },
        "is": "UserFull",
    },
    0xa518110d: {
        "_": "peerSettings",
        "params": {
            "flags": int,
            "report_spam": FlagsOf("flags", 0, Bit),
            "add_contact": FlagsOf("flags", 1, Bit),
            "block_contact": FlagsOf("flags", 2, Bit),
            "share_contact": FlagsOf("flags", 3, Bit),
            "need_contacts_exception": FlagsOf("flags", 4, Bit),
            "report_geo": FlagsOf("flags", 5, Bit),
            "autoarchived": FlagsOf("flags", 7, Bit),
            "invite_members": FlagsOf("flags", 8, Bit),
            "request_chat_broadcast": FlagsOf("flags", 10, Bit),
            "geo_distance": FlagsOf("flags", 6, int),
            "request_chat_title": FlagsOf("flags", 9, str),
            "request_chat_date": FlagsOf("flags", 9, int),
        },
        "is": "PeerSettings",
    },
    0xa83b0426: {
        "_": "peerNotifySettings",
        "params": {
            "flags": int,
            "show_previews": FlagsOf("flags", 0, bool),
            "silent": FlagsOf("flags", 1, bool),
            "mute_until": FlagsOf("flags", 2, int),
            "ios_sound": FlagsOf("flags", 3, "NotificationSound"),
            "android_sound": FlagsOf("flags", 4, "NotificationSound"),
            "other_sound": FlagsOf("flags", 5, "NotificationSound"),
        },
        "is": "PeerNotifySettings",
    },
    0x10101010: {
        "_": "test",
        "params": {
            "users": list["User"],
        },
        "is": "Test",
    },
    0x0d91a548: {
        "_": "users.getUsers",
        "params": {
            "id": list["InputUser"],
        },
        "ret": list["User"],
    },
    0xd3bc4b7a: {
        "_": "userEmpty",
        "params": {
            "id": Int64(signed=False)
        },
        "is": "User",
    },
    VECTOR_CID: {
        "_": "vector",
        "params": {
            "data": list[TLType, "RAW"],
        },
        "is": "Vector",
    },
    0x62d6b459: {
        "_": "msgs_ack",
        "params": {
            "msg_ids": list[Int64(signed=False)],
        },
        "is": "MsgsAck",
    },
    # auth.authorizationSignUpRequired#44747e9a flags:# terms_of_service:flags.0?help.TermsOfService = auth.Authorization;
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
                if typ.typ is Bit:
                    typ.serialize(TL, field, obj, obj)

                    if obj.get(field, False):
                        reference_flags[typ.param] |= (1 << typ.pos)
                    else:
                        reference_flags[typ.param] &= ~(1 << typ.pos)

                    if field not in obj:
                        to_skip.add(field)
                else:
                    if obj.get(field, None) is not None:
                        reference_flags[typ.param] |= (1 << typ.pos)
                    else:
                        to_skip.add(field)
                        reference_flags[typ.param] &= ~(1 << typ.pos)

        for field, typ in tltype["params"].items():
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
                    result.write(typ.serialize(TL, field, obj, value))
                else:
                    assert False, "Unreachable"
            elif issubclass(check_type, TLType):
                result.write(TL.encode(value))
            else:
                raise ValueError(f"Invalid type: expected {field}: {nameof(typ)}, got {nameof(value)}")

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
        for field, typ in tltype["params"].items():
            if isinstance(typ, FlagsOf):
                if obj.get(field, None) is not None:
                    reference_flags[typ.param] |= (1 << typ.pos)
                else:
                    to_skip.add(field)
                    reference_flags[typ.param] &= ~(1 << typ.pos)

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
