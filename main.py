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

    logger.info("Pubkey fingerprint: {fp:x}", fp=get_public_key_fingerprint(public_key))

    pilt = Server(
        server_keys=Keys(
            private_key=private_key,
            public_key=public_key,
        )
    )

    @pilt.on_message("ping")
    async def pong(client: Client, request: Request):
        print(request.obj, request.msg_id)
        await request.answer(
            {
                "_": "pong",
                "msg_id": request.msg_id,
                "ping_id": request.obj.ping_id,
            }
        )
        logger.success("Sent ping ping_id={ping_id}", ping_id=request.obj.ping_id)

    @pilt.on_message("invokeWithLayer")
    async def invoke_with_layer(client: Client, request: Request):
        await client.propagate(
            Request(
                client=client,
                obj=request.obj.query,
                msg_id=request.msg_id,
                seq_no=request.seq_no,
            )
        )

    @pilt.on_message("invokeWithoutUpdates")
    async def invoke_without_updates(client: Client, request: Request):
        await client.propagate(
            Request(
                client=client,
                obj=request.obj.query,
                msg_id=request.msg_id,
                seq_no=request.seq_no,
            )
        )

    @pilt.on_message("initConnection")
    async def init_connection(client: Client, request: Request):
        # hmm yes yes, I trust you client
        # the api id is always correct, it has always been!

        print(request.obj.api_id)

        await client.propagate(
            Request(
                client=client,
                obj=request.obj.query,
                msg_id=request.msg_id,
                seq_no=request.seq_no,
            )
        )

    @pilt.on_message("help.getConfig")
    async def get_config(client: Client, request: Request):
        import time

        await request.answer(
            {
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
                "revoke_time_limit": int(2 ** 31 - 1),
                "revoke_pm_time_limit": int(2 ** 31 - 1),
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
        )

    @pilt.on_message("auth.sendCode")
    async def send_code(client: Client, request: Request):
        from binascii import crc32

        code = 69696
        code = str(code).encode()

        await request.answer(
            {
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
        )
    
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

        await request.answer(
            {
                "_": "auth.authorization",
                "setup_password_required": False,
                "user": TL.from_dict(user),
            }
        )

    @pilt.on_message("updates.getState")
    async def get_state(client: Client, request: Request):
        import time

        await request.answer(
            {
                "_": "updates.state",
                "pts": 0,
                "qts": 0,
                "date": int(time.time()),
                "seq": 0,
                "unread_count": 0,
            }
        )

    @pilt.on_message("users.getFullUser")
    async def get_full_user(client: Client, request: Request):
        import time

        if request.obj.id._ == "inputUserSelf":
            return await request.answer(
                {
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
                    "users": [
                        TL.from_dict(user)
                    ],
                }
            )
        logger.warning("id: inputUser is not inputUserSelf: not implemented")

    await pilt.serve()

try:
    uvloop.install()
    asyncio.run(main())
except KeyboardInterrupt:
    pass
