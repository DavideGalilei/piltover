import asyncio
import uvloop

from pathlib import Path

from loguru import logger
from piltover.server import Server, Client, Request
from piltover.utils import gen_keys, get_public_key_fingerprint
from piltover.types import Keys
from piltover.tl import TL


root = Path(__file__).parent.resolve(strict=True)
data = root / "data"
data.mkdir(parents=True, exist_ok=True)

secrets = data / "secrets"
secrets.mkdir(parents=True, exist_ok=True)

privkey = secrets / "privkey.asc"
pubkey = secrets / "pubkey.asc"


if True:
    # Hot code reloading
    import jurigged

    def log(s: jurigged.live.WatchOperation):
        if hasattr(s, "filename") and "unknown" not in s.filename:
            file = Path(s.filename)
            print("Reloaded", file.relative_to(root))

    jurigged.watch("piltover/*.py", logger=log)


async def main():
    if not (pubkey.exists() and privkey.exists()):
        with privkey.open("w+") as priv, pubkey.open("w+") as pub:
            keys: Keys = gen_keys()
            priv.write(keys.private_key)
            pub.write(keys.public_key)

    private_key = privkey.read_text()
    public_key = pubkey.read_text()

    fp = get_public_key_fingerprint(public_key)
    logger.info(
        "Pubkey fingerprint: {fp:x} ({no_sign})",
        fp=fp, no_sign=fp.to_bytes(8, "big", signed=True).hex()
    )

    pilt = Server(
        server_keys=Keys(
            private_key=private_key,
            public_key=public_key,
        )
    )

    @pilt.on_message("ping")
    async def pong(client: Client, request: Request):
        print(request.obj, request.msg_id)

        logger.success("Sent ping ping_id={ping_id}", ping_id=request.obj.ping_id)

        return {
            "_": "pong",
            "msg_id": request.msg_id,
            "ping_id": request.obj.ping_id,
        }


    @pilt.on_message("ping_delay_disconnect")
    async def ping_delay_disconnect(client: Client, request: Request):
        return {
            "_": "pong",
            "msg_id": request.msg_id,
            "ping_id": request.obj.ping_id,
        }


    @pilt.on_message("invokeWithLayer")
    async def invoke_with_layer(client: Client, request: Request):
        return await client.propagate(
            Request(
                client=client,
                obj=request.obj.query,
                msg_id=request.msg_id,
                seq_no=request.seq_no,
            ),
            just_return=True,
        )

    @pilt.on_message("invokeWithoutUpdates")
    async def invoke_without_updates(client: Client, request: Request):
        return await client.propagate(
            Request(
                client=client,
                obj=request.obj.query,
                msg_id=request.msg_id,
                seq_no=request.seq_no,
            ),
            just_return=True,
        )

    @pilt.on_message("initConnection")
    async def init_connection(client: Client, request: Request):
        # hmm yes yes, I trust you client
        # the api id is always correct, it has always been!

        print("initConnection with Api ID:", request.obj.api_id)

        return await client.propagate(
            Request(
                client=client,
                obj=request.obj.query,
                msg_id=request.msg_id,
                seq_no=request.seq_no,
            ),
            just_return=True,
        )

    @pilt.on_message("help.getConfig")
    async def get_config(client: Client, request: Request):
        import time

        return {
            "_": "config",
            "date": int(time.time()),
            "expires": int(time.time() + 60 * 10),
            "test_mode": False,
            "this_dc": 2,
            "dc_options": [],
            "dc_txt_domain_name": "",
            "chat_size_max": 200,
            "megagroup_size_max": 200000,
            "forwarded_count_max": 100,
            "online_update_period_ms": 30_000,
            "offline_blur_timeout_ms": 30_000,
            "offline_idle_timeout_ms": 30_000,
            "online_cloud_timeout_ms": 30_000,
            "notify_cloud_delay_ms": 60_000,
            "notify_default_delay_ms": 10_000,
            "push_chat_period_ms": 1_000,
            "push_chat_limit": 1,
            "saved_gifs_limit": 100,
            "edit_time_limit": 48 * 60 * 60,
            "revoke_time_limit": int(2**31 - 1),
            "revoke_pm_time_limit": int(2**31 - 1),
            "rating_e_decay": 2,
            "stickers_recent_limit": 15,
            "stickers_faved_limit": 5,
            "channels_read_media_period": 24 * 60 * 60,
            "pinned_dialogs_count_max": 5,
            "pinned_infolder_count_max": 200,
            "call_receive_timeout_ms": 20_000,
            "call_ring_timeout_ms": 20_000,
            "call_connect_timeout_ms": 20_000,
            "call_packet_timeout_ms": 5_000,
            "me_url_prefix": "https://🐳.me/",
            "caption_length_max": 2048,
            "message_length_max": 4096,
            "webfile_dc_id": 2,
        }

    @pilt.on_message("auth.sendCode")
    async def send_code(client: Client, request: Request):
        from binascii import crc32

        code = 69696
        code = str(code).encode()

        return {
            "_": "auth.sentCode",
            "type": TL.from_dict(
                {
                    "_": "auth.sentCodeTypeSms",
                    "length": len(code),
                }
            ),
            "phone_code_hash": f"{crc32(code):x}".zfill(8),
            # "next_type": FlagsOf("flags", 1, "auth.CodeType"),
            "timeout": 30,
        }

    user = {
        "_": "user",
        "self": True,
        "contact": True,
        "mutual_contact": False,
        "deleted": False,
        "bot": False,
        "verified": True,
        "restricted": False,
        "min": False,
        "support": False,
        "scam": False,
        "apply_min_photo": False,
        "fake": False,
        "bot_attach_menu": False,
        "premium": False,
        "attach_menu_enabled": False,
        "id": 123456,
        "access_hash": 0,
        "first_name": "Testing",
        "last_name": ":)",
        "username": "test",
        "phone": "123456",
        # "status": FlagsOf("flags", 6, "UserStatus"),
        "lang_code": "en",
    }

    @pilt.on_message("auth.signIn")
    async def sign_in(client: Client, request: Request):
        from binascii import crc32

        code = 69696
        code = str(code).encode()

        return {
            "_": "auth.authorization",
            "setup_password_required": False,
            "user": TL.from_dict(user),
        }

    @pilt.on_message("updates.getState")
    async def get_state(client: Client, request: Request):
        import time

        return {
            "_": "updates.state",
            "pts": 0,
            "qts": 0,
            "date": int(time.time()),
            "seq": 0,
            "unread_count": 0,
        }

    @pilt.on_message("users.getFullUser")
    async def get_full_user(client: Client, request: Request):
        if request.obj.id._ == "inputUserSelf":
            return {
                "_": "users.userFull",
                "full_user": TL.from_dict(
                    {
                        "_": "userFull",
                        "blocked": False,
                        "phone_calls_available": False,
                        "phone_calls_private": False,
                        "can_pin_message": True,
                        "has_scheduled": False,
                        "video_calls_available": False,
                        "voice_messages_forbidden": True,
                        "id": user["id"],
                        "about": "hi, this is a test bio",
                        "settings": TL.from_dict(
                            {
                                "_": "peerSettings",
                            }
                        ),
                        "profile_photo": None,
                        "notify_settings": TL.from_dict(
                            {
                                "_": "peerNotifySettings",
                                "show_previews": True,
                                "silent": False,
                            }
                        ),
                        "common_chats_count": 0,
                    }
                ),
                "chats": [],
                "users": [TL.from_dict(user)],
            }
        logger.warning("id: inputUser is not inputUserSelf: not implemented")

    @pilt.on_message("users.getUsers")
    async def get_users(client: Client, request: Request):
        result: list[TL] = []

        for id in request.obj.id:
            if id._ == "inputUserSelf":
                result.append(TL.from_dict(user))
            else:
                # TODO: other input users
                result.append(TL.from_dict({"_": "userEmpty"}))

        return {
            "_": "vector",
            "data": result,
        }

    @pilt.on_message("auth.bindTempAuthKey")
    async def bind_temp_auth_key(client: Client, request: Request):
        return {
            "_": "boolTrue",
        }

    @pilt.on_message("help.getNearestDc")
    async def get_nearest_dc(client: Client, request: Request):
        return {
            "_": "nearestDc",
            "country": "Y-Land",
            "this_dc": 2,
            "nearest_dc": 2,
        }

    @pilt.on_message("help.getAppConfig")
    async def get_app_config(client: Client, request: Request):
        return {
            "_": "jsonObject",
            "value": [],
        }

    @pilt.on_message("help.getCountriesList")
    async def get_countries_list(client: Client, request: Request):
        return {
            "_": "help.countriesList",
            "countries": [
                TL.from_dict(
                    {
                        "_": "help.country",
                        "hidden": False,
                        "iso2": "yl",
                        "default_name": "Y-Land",
                        "name": "Y-Land",
                        "country_codes": [
                            TL.from_dict(
                                {
                                    "_": "help.countryCode",
                                    "country_code": "yl",
                                    "prefixes": ["42"],
                                    "patterns": ["XXXXX"],
                                }
                            )
                        ],
                    }
                ),
            ],
            "hash": 0,
        }

    @pilt.on_message("auth.exportLoginToken")
    async def export_login_token(client: Client, request: Request):
        return {
            "_": "auth.loginToken",
            "expires": 1000,
            "token": b"levlam",
        }

    @pilt.on_message("msgs_ack")
    async def msgs_ack(client: Client, request: Request):
        ...

    """
    @pilt.on_message("msgs_state_req")
    async def msgs_state_req(client: Client, request: Request):
        ...
    """

    @pilt.on_message("messages.getDialogFilters")
    async def get_dialog_filters(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [],
        }

    @pilt.on_message("messages.getAvailableReactions")
    async def get_available_reactions(client: Client, request: Request):
        return {
            "_": "messages.availableReactions",
            "hash": 0,
            "reactions": [],
        }

    @pilt.on_message("account.getDefaultEmojiStatuses")
    async def get_default_emoji_statuses(client: Client, request: Request):
        return {
            "_": "account.emojiStatuses",
            "hash": 0,
            "statuses": [],
        }

    @pilt.on_message("set_client_DH_params")
    async def set_client_dh_params(client: Client, request: Request):
        print(request.obj)
        print(client.shared)
        raise

    await pilt.serve()


try:
    uvloop.install()
    asyncio.run(main())
except KeyboardInterrupt:
    pass
