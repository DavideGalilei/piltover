import asyncio
import time
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

    fp = get_public_key_fingerprint(public_key, signed=True)
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

    @pilt.on_message("msgs_ack")
    async def msgs_ack(client: Client, request: Request):
        print(request.obj, request.msg_id)
        return False

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

    @pilt.on_message("invokeAfterMsg")
    async def invoke_after_msg(client: Client, request: Request):
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
        return {
            "_": "config",
            "date": int(time.time()),
            "expires": int(time.time() + 60 * 10),
            "test_mode": False,
            "this_dc": 2,
            "dc_options": [
                TL.from_dict(
                    {
                        "_": "dcOption",
                        "this_port_only": True,
                        "id": 2,
                        "ip_address": "127.0.0.1",
                        "port": 4430,
                    },
                )
            ],
            "dc_txt_domain_name": "aa",
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
        "contact": False,
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

    durov = {
        "_": "user",
        "self": True,
        "contact": False,
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
        "id": 42123,
        "access_hash": 0,
        "first_name": "Pavel",
        "last_name": "Durov",
        "username": "durov7",
        "phone": "+4442123",
        "status": TL.from_dict(
            {
                "_": "userStatusOnline",
                "expires": int(time.time() + 9000),
            }
        ),
        "lang_code": "en",
    }

    durov_message = {
        "_": "message",
        "id": 456,
        "peer_id": TL.from_dict({"_": "peerUser", "user_id": durov["id"]}),
        "date": int(time.time() - 150),
        "message": "Приветик",
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

    @pilt.on_message("langpack.getLanguages_72")
    async def get_languages_72(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [
                TL.from_dict(
                    {
                        "_": "langPackLanguage_72",
                        "name": "Gramz",
                        "native_name": "Le Gramz",
                        "lang_code": "grz",
                    }
                )
            ]
        }

    @pilt.on_message("langpack.getLanguages")
    async def get_languages(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [
                TL.from_dict(
                    {
                        "_": "langPackLanguage",
                        "name": "Gramz",
                        "native_name": "Le Gramz",
                        "lang_code": "grz",
                    }
                )
            ]
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
                                    "country_code": "42",
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

    @pilt.on_message("messages.setTyping")
    async def set_typing(client: Client, request: Request):
        return {"_": "boolTrue"}

    @pilt.on_message("messages.getPeerSettings")
    async def get_peer_settings(client: Client, request: Request):
        return {
            "_": "peerSettings",
        }

    @pilt.on_message("messages.getScheduledHistory")
    async def get_scheduled_history(client: Client, request: Request):
        return {
            "_": "messages.messages",
            "messages": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("messages.getEmojiKeywordsLanguages")
    async def get_emoji_keywords_languages(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [],
        }

    @pilt.on_message("messages.getPeerDialogs")
    async def get_peer_dialogs(client: Client, request: Request):
        return {
            "_": "messages.peerDialogs",
            "dialogs": [
                TL.from_dict(
                    {
                        "_": "dialog",
                        "peer": TL.from_dict({"_": "peerUser", "user_id": durov["id"]}),
                        "top_message": 0,
                        "read_inbox_max_id": 0,
                        "read_outbox_max_id": 0,
                        "unread_count": 0,
                        "unread_mentions_count": 0,
                        "unread_reactions_count": 0,
                        "notify_settings": await get_notify_settings(client, request),
                        # "draft": TL.from_dict(
                        #     {
                        #         "_": "draftMessage",
                        #         "message": "Hii",
                        #         "date": int(time.time() - 20),
                        #     }
                        # ),
                    }
                )
            ],
            "messages": [
                TL.from_dict(
                    # {
                    #     "_": "messageService",
                    #     "id": 123,
                    #     "peer_id": TL.from_dict({"_": "peerUser", "user_id": durov["id"]}),
                    #     "date": int(time.time()),
                    #     "action": TL.from_dict({"_": "messageActionContactSignUp"}),
                    # }
                    durov_message,
                )
            ],
            "chats": [],
            "users": [
                TL.from_dict(durov),
            ],
            "state": await get_state(client, request),
        }

    @pilt.on_message("messages.getHistory")
    async def get_history(client: Client, request: Request):
        if request.obj.peer.user_id == durov["id"]:
            return {
                "_": "messages.messages",
                "messages": [
                    TL.from_dict(durov_message),
                ],
                "chats": [],
                "users": [],
            }

        if request.obj.offset_id != 0:
            return {
                "_": "messages.messages",
                "messages": [],
                "chats": [],
                "users": [],
            }

        return {
            "_": "messages.messages",
            "messages": [
                TL.from_dict(
                    {
                        "_": "message",
                        "out": True,
                        "mentioned": True,
                        "media_unread": False,
                        "silent": False,
                        "post": True,
                        "from_scheduled": False,
                        "legacy": True,
                        "edit_hide": True,
                        "pinned": False,
                        "noforwards": False,
                        "id": 1,
                        "from_id": TL.from_dict(
                            {
                                "_": "peerUser",
                                "user_id": user["id"],
                            }
                        ),
                        "peer_id": TL.from_dict(
                            {
                                "_": "peerUser",
                                "user_id": user["id"],
                            }
                        ),
                        # "fwd_from": FlagsOf("flags", 2, "MessageFwdHeader"),
                        # "via_bot_id": FlagsOf("flags", 11, Int64(signed=False)),
                        # "reply_to": FlagsOf("flags", 3, "MessageReplyHeader"),
                        "date": int(time.time() - 120),
                        "message": "aaaaaa",
                        "media": None,
                        # "reply_markup": FlagsOf("flags", 6, "ReplyMarkup"),
                        "entities": None,
                        "views": 40,
                        "forwards": None,
                        "edit_date": None,
                        "post_author": None,
                        "grouped_id": None,
                        "reactions": None,
                        "restriction_reason": None,
                        "ttl_period": None,
                    }
                )
            ],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("account.updateStatus")
    async def update_status(client: Client, request: Request):
        return {
            "_": "boolTrue",
        }

    @pilt.on_message("messages.sendMessage")
    async def send_message(client: Client, request: Request):
        return {
            "_": "updateShortSentMessage",
            "out": True,
            "id": 2,
            "pts": 2,
            "pts_count": 2,
            "date": int(time.time()),
        }

    @pilt.on_message("messages.readHistory")
    async def read_history(client: Client, request: Request):
        return {
            "_": "messages.affectedMessages",
            "pts": 3,
            "pts_count": 1,
        }

    @pilt.on_message("destroy_session")
    async def destroy_session(client: Client, request: Request):
        return {
            "_": "destroy_session_ok",
            "session_id": request.obj.session_id,
        }

    @pilt.on_message("rpc_drop_answer")
    async def rpc_drop_answer(client: Client, request: Request):
        return {"_": "rpc_answer_unknown"}

    @pilt.on_message("messages.getWebPage")
    async def get_web_page(client: Client, request: Request):
        return {
            "_": "webPageEmpty",
            "id": 0,
        }

    @pilt.on_message("photos.getUserPhotos")
    async def get_user_photos(client: Client, request: Request):
        return {
            "_": "photos.photos",
            "photos": [],
            "users": [TL.from_dict(user)],
        }

    @pilt.on_message("messages.getStickerSet_71")
    async def get_sticker_set_71(client: Client, request: Request):
        return {
            "_": "rpc_error",
            "error_code": 406,
            "error_message": "STICKERSET_INVALID",
        }

    @pilt.on_message("messages.getStickerSet")
    async def get_sticker_set(client: Client, request: Request):
        import random

        return {
            "_": "messages.stickerSet",
            "set": TL.from_dict(
                {
                    "_": "stickerSet",
                    "official": True,
                    "id": random.randint(1000000, 9000000),
                    "access_hash": random.randint(1000000, 9000000),
                    "title": "Picker Stack",
                    "short_name": random.randbytes(5).hex(),
                    "count": 0,
                    "hash": 0,
                }
            ),
            "packs": [],
            "keywords": [],
            "documents": [],
        }

    @pilt.on_message("account.updateProfile")
    async def update_profile(client: Client, request: Request):
        if request.obj.first_name is not None:
            user["first_name"] = request.obj.first_name
        if request.obj.last_name is not None:
            user["last_name"] = request.obj.last_name
        if request.obj.about is not None:
            user["about"] = request.obj.about
        return user

    @pilt.on_message("messages.getTopReactions")
    async def get_top_reactions(client: Client, request: Request):
        return {
            "_": "messages.reactions",
            "hash": 0,
            "reactions": [],
        }

    @pilt.on_message("messages.getRecentReactions")
    async def get_recent_reactions(client: Client, request: Request):
        return {
            "_": "messages.reactions",
            "hash": 0,
            "reactions": [],
        }

    @pilt.on_message("messages.getDialogs")
    async def get_dialogs(client: Client, request: Request):
        return {
            "_": "messages.dialogs",
            "dialogs": [],
            "messages": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("messages.getAttachMenuBots")
    async def get_attach_menu_bots(client: Client, request: Request):
        return {
            "_": "attachMenuBots",
            "hash": 0,
            "bots": [],
            "users": [],
        }

    @pilt.on_message("account.getNotifySettings")
    async def get_notify_settings(client: Client, request: Request):
        return {
            "_": "peerNotifySettings",
            "show_previews": True,
            "silent": False,
        }

    @pilt.on_message("contacts.getContacts")
    async def get_contacts(client: Client, request: Request):
        return {
            "_": "contacts.contacts",
            "contacts": [],
            "saved_count": 0,
            "users": [],
        }

    @pilt.on_message("help.getTermsOfServiceUpdate")
    async def get_terms_of_service_update(client: Client, request: Request):
        return {
            "_": "help.termsOfServiceUpdateEmpty",
            "expires": int(time.time() + 9000),
        }

    @pilt.on_message("messages.getPinnedDialogs")
    async def get_pinned_dialogs(client: Client, request: Request):
        return {
            "_": "messages.peerDialogs",
            "dialogs": [],
            "messages": [],
            "chats": [],
            "users": [],
            "state": await get_state(client, request),
        }

    @pilt.on_message("messages.reorderPinnedDialogs")
    async def reorder_pinned_dialogs(client: Client, request: Request):
        return {"_": "boolTrue"}

    @pilt.on_message("help.getPromoData")
    async def get_promo_data(client: Client, request: Request):
        return {
            "_": "help.promoDataEmpty",
            "expires": int(time.time() + 9000),
        }

    @pilt.on_message("messages.getStickers")
    async def get_stickers(client: Client, request: Request):
        return {
            "_": "messages.stickers",
            "hash": 0,
            "stickers": [],
        }

    @pilt.on_message("contacts.resolveUsername")
    async def resolve_username(client: Client, request: Request):
        return {
            "_": "rpc_error",
            "error_code": 400,
            "error_message": "USERNAME_NOT_OCCUPIED",
        }

    @pilt.on_message("help.getPremiumPromo")
    async def get_premium_promo(client: Client, request: Request):
        return {
            "_": "help.premiumPromo",
            "status_text": "Premium Lol",
            "status_entities": [],
            "video_sections": [],
            "videos": [],
            "period_options": [
                TL.from_dict(
                    {
                        "_": "premiumSubscriptionOption",
                        "months": 7,
                        "currency": "EUR",
                        "amount": 169,
                        "bot_url": "t.me/spambot",

                    }
                )
            ],
            "users": [],
        }

    @pilt.on_message("account.getThemes")
    async def get_themes(client: Client, request: Request):
        return {
            "_": "account.themes",
            "hash": 0,
            "themes": [],
        }

    @pilt.on_message("account.getGlobalPrivacySettings")
    async def get_global_privacy_settings(client: Client, request: Request):
        return {
            "_": "globalPrivacySettings",
            "archive_and_mute_new_noncontact_peers": False,
        }

    @pilt.on_message("account.getContentSettings")
    async def get_content_settings(client: Client, request: Request):
        return {
            "_": "account.contentSettings",
            "sensitive_enabled": True,
            "sensitive_can_change": True,
        }

    @pilt.on_message("account.getContactSignUpNotification")
    async def get_contact_sign_up_notification(client: Client, request: Request):
        return {"_": "boolTrue"}

    @pilt.on_message("account.getPassword")
    async def get_password(client: Client, request: Request):
        return {
            "_": "account.password",
            "has_password": False,
            "new_algo": TL.from_dict(
                {
                    "_": "passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow",
                    "salt1": b"asd",
                    "salt2": b"asd",
                    "g": 2,
                    "p": b"a" * (2048 // 8),
                }
            ),
            "new_secure_algo": TL.from_dict(
                {
                    "_": "securePasswordKdfAlgoSHA512",
                    "salt": b"1234",
                }
            ),
            "secure_random": b"levlam",
        }

    @pilt.on_message("account.getPrivacy")
    async def get_privacy(client: Client, request: Request):
        return {
            "_": "account.privacyRules",
            "rules": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("contacts.getBlocked")
    async def get_blocked(client: Client, request: Request):
        return {
            "_": "contacts.blocked",
            "blocked": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("account.getAuthorizations")
    async def get_authorizations(client: Client, request: Request):
        return {
            "_": "account.authorizations",
            "authorization_ttl_days": 15,
            "authorizations": [
                TL.from_dict(
                    {
                        "_": "authorization",
                        "current": True,
                        "official_app": True,
                        "encrypted_requests_disabled": True,
                        "call_requests_disabled": True,
                        "hash": 0,
                        "device_model": "Blackberry",
                        "platform": "Desktop",
                        "system_version": "42.777.3",
                        "api_id": 12345,
                        "app_name": "DTeskdop",
                        "app_version": "1.2.3",
                        "date_created": int(time.time() - 20),
                        "date_active": int(time.time()),
                        "ip": "127.0.0.1",
                        "country": "Y-Land",
                        "region": "Telegram HQ",
                    }
                )
            ],
        }

    @pilt.on_message("account.getAccountTTL")
    async def get_account_ttl(client: Client, request: Request):
        return {
            "_": "accountDaysTTL",
            "days": 15,
        }

    @pilt.on_message("messages.getDefaultHistoryTTL")
    async def get_default_history_ttl(client: Client, request: Request):
        return {
            "_": "defaultHistoryTTL",
            "period": 10,
        }

    @pilt.on_message("account.registerDevice")
    async def register_device(client: Client, request: Request):
        return {"_": "boolTrue"}

    @pilt.on_message("contacts.search")
    async def contacts_search(client: Client, request: Request):
        return {
            "_": "contacts.found",
            "my_results": [],
            "results": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("messages.getSearchResultsPositions")
    async def get_search_results_positions(client: Client, request: Request):
        return {
            "_": "messages.searchResultsPositions",
            "count": 0,
            "positions": [],
        }

    @pilt.on_message("messages.search")
    async def messages_search(client: Client, request: Request):
        return {
            "_": "messages.messages",
            "messages": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("messages.getSearchCounters")
    async def get_search_counters(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [
                TL.from_dict(
                    {
                        "_": "messages.searchCounter",
                        "filter": flt,
                        "count": 0,
                    }
                )
                for flt
                in request.obj.filters
            ]
        }

    @pilt.on_message("help.getInviteText")
    async def get_invite_text(client: Client, request: Request):
        return {
            "_": "help.inviteText",
            "message": "🐳",
        }

    @pilt.on_message("help.saveAppLog")
    async def save_app_log(client: Client, request: Request):
        return {"_": "boolTrue"}

    @pilt.on_message("messages.getSuggestedDialogFilters")
    async def get_suggested_dialog_filters(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [],
        }

    @pilt.on_message("contacts.getTopPeers")
    async def get_top_peers(client: Client, request: Request):
        return {
            "_": "contacts.topPeers",
            "categories": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("messages.getFeaturedStickers")
    @pilt.on_message("messages.getFeaturedEmojiStickers")
    async def get_featured_stickers(client: Client, request: Request):
        return {
            "_": "messages.featuredStickers",
            "hash": 0,
            "count": 0,
            "sets": [],
            "unread": [],
        }

    @pilt.on_message("messages.getAllDrafts")
    async def get_all_drafts(client: Client, request: Request):
        return {
            "_": "updates",
            "updates": [],  # list of updateDraftMessage
            "users": [],
            "chats": [],
            "date": int(time.time()),
            "seq": 0,
        }

    @pilt.on_message("contacts.getStatuses")
    async def get_statuses(client: Client, request: Request):
        return {
            "_": "vector",
            "data": [],
        }

    @pilt.on_message("messages.getFavedStickers")
    async def get_faved_stickers(client: Client, request: Request):
        return {
            "_": "messages.favedStickers",
            "hash": 0,
            "packs": [],
            "stickers": [],
        }

    @pilt.on_message("messages.searchGlobal")
    async def search_global(client: Client, request: Request):
        return {
            "_": "messages.messages",
            "messages": [],
            "chats": [],
            "users": [],
        }

    @pilt.on_message("account.checkUsername")
    async def check_username(client: Client, request: Request):
        return {"_": "boolTrue"}

    @pilt.on_message("account.updateUsername")
    async def update_username(client: Client, request: Request):
        user["username"] = request.obj.username
        return user


    await pilt.serve()


try:
    uvloop.install()
    asyncio.run(main())
except KeyboardInterrupt:
    pass
