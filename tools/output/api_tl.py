{
    "types": [
        {
            "_": "boolFalse",
            "cid": "bc799737",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "boolTrue",
            "cid": "997275b5",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "true",
            "cid": "3fedd339",
            "params": [],
            "ret": "True"
        },
        {
            "_": "vector",
            "cid": "1cb5c415",
            "params": [],
            "ret": "Vector t"
        },
        {
            "_": "error",
            "cid": "c4b9f9bb",
            "params": [
                {
                    "name": "code",
                    "type": "int"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "Error"
        },
        {
            "_": "null",
            "cid": "56730bcc",
            "params": [],
            "ret": "Null"
        },
        {
            "_": "inputPeerEmpty",
            "cid": "7f3b18ea",
            "params": [],
            "ret": "InputPeer"
        },
        {
            "_": "inputPeerSelf",
            "cid": "7da07ec9",
            "params": [],
            "ret": "InputPeer"
        },
        {
            "_": "inputPeerChat",
            "cid": "35a95cb9",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "InputPeer"
        },
        {
            "_": "inputPeerUser",
            "cid": "dde8a54c",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputPeer"
        },
        {
            "_": "inputPeerChannel",
            "cid": "27bcbbfc",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputPeer"
        },
        {
            "_": "inputPeerUserFromMessage",
            "cid": "a87b0a1c",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "InputPeer"
        },
        {
            "_": "inputPeerChannelFromMessage",
            "cid": "bd2a0840",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                }
            ],
            "ret": "InputPeer"
        },
        {
            "_": "inputUserEmpty",
            "cid": "b98886cf",
            "params": [],
            "ret": "InputUser"
        },
        {
            "_": "inputUserSelf",
            "cid": "f7c1b13f",
            "params": [],
            "ret": "InputUser"
        },
        {
            "_": "inputUser",
            "cid": "f21158c6",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputUser"
        },
        {
            "_": "inputUserFromMessage",
            "cid": "1da448e2",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "InputUser"
        },
        {
            "_": "inputPhoneContact",
            "cid": "f392b7f4",
            "params": [
                {
                    "name": "client_id",
                    "type": "long"
                },
                {
                    "name": "phone",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                }
            ],
            "ret": "InputContact"
        },
        {
            "_": "inputFile",
            "cid": "f52ff27f",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "parts",
                    "type": "int"
                },
                {
                    "name": "name",
                    "type": "string"
                },
                {
                    "name": "md5_checksum",
                    "type": "string"
                }
            ],
            "ret": "InputFile"
        },
        {
            "_": "inputFileBig",
            "cid": "fa4f0bb5",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "parts",
                    "type": "int"
                },
                {
                    "name": "name",
                    "type": "string"
                }
            ],
            "ret": "InputFile"
        },
        {
            "_": "inputMediaEmpty",
            "cid": "9664f57f",
            "params": [],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaUploadedPhoto",
            "cid": "1e287d04",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "spoiler",
                    "type": "flags.2?true"
                },
                {
                    "name": "file",
                    "type": "InputFile"
                },
                {
                    "name": "stickers",
                    "type": "flags.0?Vector<InputDocument>"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.1?int"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaPhoto",
            "cid": "b3ba0635",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "spoiler",
                    "type": "flags.1?true"
                },
                {
                    "name": "id",
                    "type": "InputPhoto"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.0?int"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaGeoPoint",
            "cid": "f9c44144",
            "params": [
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaContact",
            "cid": "f8ab7dfb",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "vcard",
                    "type": "string"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaUploadedDocument",
            "cid": "5b38c6c1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "nosound_video",
                    "type": "flags.3?true"
                },
                {
                    "name": "force_file",
                    "type": "flags.4?true"
                },
                {
                    "name": "spoiler",
                    "type": "flags.5?true"
                },
                {
                    "name": "file",
                    "type": "InputFile"
                },
                {
                    "name": "thumb",
                    "type": "flags.2?InputFile"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "attributes",
                    "type": "Vector<DocumentAttribute>"
                },
                {
                    "name": "stickers",
                    "type": "flags.0?Vector<InputDocument>"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.1?int"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaDocument",
            "cid": "33473058",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "spoiler",
                    "type": "flags.2?true"
                },
                {
                    "name": "id",
                    "type": "InputDocument"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.0?int"
                },
                {
                    "name": "query",
                    "type": "flags.1?string"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaVenue",
            "cid": "c13d1c11",
            "params": [
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "address",
                    "type": "string"
                },
                {
                    "name": "provider",
                    "type": "string"
                },
                {
                    "name": "venue_id",
                    "type": "string"
                },
                {
                    "name": "venue_type",
                    "type": "string"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaPhotoExternal",
            "cid": "e5bbfe1a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "spoiler",
                    "type": "flags.1?true"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.0?int"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaDocumentExternal",
            "cid": "fb52dc99",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "spoiler",
                    "type": "flags.1?true"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.0?int"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaGame",
            "cid": "d33f43f3",
            "params": [
                {
                    "name": "id",
                    "type": "InputGame"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaInvoice",
            "cid": "8eb5a6d5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.0?InputWebDocument"
                },
                {
                    "name": "invoice",
                    "type": "Invoice"
                },
                {
                    "name": "payload",
                    "type": "bytes"
                },
                {
                    "name": "provider",
                    "type": "string"
                },
                {
                    "name": "provider_data",
                    "type": "DataJSON"
                },
                {
                    "name": "start_param",
                    "type": "flags.1?string"
                },
                {
                    "name": "extended_media",
                    "type": "flags.2?InputMedia"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaGeoLive",
            "cid": "971fa843",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "stopped",
                    "type": "flags.0?true"
                },
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "heading",
                    "type": "flags.2?int"
                },
                {
                    "name": "period",
                    "type": "flags.1?int"
                },
                {
                    "name": "proximity_notification_radius",
                    "type": "flags.3?int"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaPoll",
            "cid": "f94e5f1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "poll",
                    "type": "Poll"
                },
                {
                    "name": "correct_answers",
                    "type": "flags.0?Vector<bytes>"
                },
                {
                    "name": "solution",
                    "type": "flags.1?string"
                },
                {
                    "name": "solution_entities",
                    "type": "flags.1?Vector<MessageEntity>"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputMediaDice",
            "cid": "e66fbf7b",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "InputMedia"
        },
        {
            "_": "inputChatPhotoEmpty",
            "cid": "1ca48f57",
            "params": [],
            "ret": "InputChatPhoto"
        },
        {
            "_": "inputChatUploadedPhoto",
            "cid": "c642724e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "file",
                    "type": "flags.0?InputFile"
                },
                {
                    "name": "video",
                    "type": "flags.1?InputFile"
                },
                {
                    "name": "video_start_ts",
                    "type": "flags.2?double"
                }
            ],
            "ret": "InputChatPhoto"
        },
        {
            "_": "inputChatPhoto",
            "cid": "8953ad37",
            "params": [
                {
                    "name": "id",
                    "type": "InputPhoto"
                }
            ],
            "ret": "InputChatPhoto"
        },
        {
            "_": "inputGeoPointEmpty",
            "cid": "e4c123d6",
            "params": [],
            "ret": "InputGeoPoint"
        },
        {
            "_": "inputGeoPoint",
            "cid": "48222faf",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "lat",
                    "type": "double"
                },
                {
                    "name": "long",
                    "type": "double"
                },
                {
                    "name": "accuracy_radius",
                    "type": "flags.0?int"
                }
            ],
            "ret": "InputGeoPoint"
        },
        {
            "_": "inputPhotoEmpty",
            "cid": "1cd7bf0d",
            "params": [],
            "ret": "InputPhoto"
        },
        {
            "_": "inputPhoto",
            "cid": "3bb3b94a",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                }
            ],
            "ret": "InputPhoto"
        },
        {
            "_": "inputFileLocation",
            "cid": "dfdaabe1",
            "params": [
                {
                    "name": "volume_id",
                    "type": "long"
                },
                {
                    "name": "local_id",
                    "type": "int"
                },
                {
                    "name": "secret",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputEncryptedFileLocation",
            "cid": "f5235d55",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputDocumentFileLocation",
            "cid": "bad07584",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                },
                {
                    "name": "thumb_size",
                    "type": "string"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputSecureFileLocation",
            "cid": "cbc7ee28",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputTakeoutFileLocation",
            "cid": "29be5899",
            "params": [],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputPhotoFileLocation",
            "cid": "40181ffe",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                },
                {
                    "name": "thumb_size",
                    "type": "string"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputPhotoLegacyFileLocation",
            "cid": "d83466f3",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                },
                {
                    "name": "volume_id",
                    "type": "long"
                },
                {
                    "name": "local_id",
                    "type": "int"
                },
                {
                    "name": "secret",
                    "type": "long"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputPeerPhotoFileLocation",
            "cid": "37257e99",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "big",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "photo_id",
                    "type": "long"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputStickerSetThumb",
            "cid": "9d84f3db",
            "params": [
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "thumb_version",
                    "type": "int"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "inputGroupCallStream",
            "cid": "598a92a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "time_ms",
                    "type": "long"
                },
                {
                    "name": "scale",
                    "type": "int"
                },
                {
                    "name": "video_channel",
                    "type": "flags.0?int"
                },
                {
                    "name": "video_quality",
                    "type": "flags.0?int"
                }
            ],
            "ret": "InputFileLocation"
        },
        {
            "_": "peerUser",
            "cid": "59511722",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "Peer"
        },
        {
            "_": "peerChat",
            "cid": "36c6019a",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "Peer"
        },
        {
            "_": "peerChannel",
            "cid": "a2a5371e",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                }
            ],
            "ret": "Peer"
        },
        {
            "_": "fileUnknown",
            "cid": "aa963b05",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "filePartial",
            "cid": "40bc6f52",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "fileJpeg",
            "cid": "7efe0e",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "fileGif",
            "cid": "cae1aadf",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "filePng",
            "cid": "a4f63c0",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "filePdf",
            "cid": "ae1e508d",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "fileMp3",
            "cid": "528a0677",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "fileMov",
            "cid": "4b09ebbc",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "fileMp4",
            "cid": "b3cea0e4",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "fileWebp",
            "cid": "1081464c",
            "params": [],
            "ret": "storage.FileType"
        },
        {
            "_": "userEmpty",
            "cid": "d3bc4b7a",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "User"
        },
        {
            "_": "user",
            "cid": "8f97c628",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "self",
                    "type": "flags.10?true"
                },
                {
                    "name": "contact",
                    "type": "flags.11?true"
                },
                {
                    "name": "mutual_contact",
                    "type": "flags.12?true"
                },
                {
                    "name": "deleted",
                    "type": "flags.13?true"
                },
                {
                    "name": "bot",
                    "type": "flags.14?true"
                },
                {
                    "name": "bot_chat_history",
                    "type": "flags.15?true"
                },
                {
                    "name": "bot_nochats",
                    "type": "flags.16?true"
                },
                {
                    "name": "verified",
                    "type": "flags.17?true"
                },
                {
                    "name": "restricted",
                    "type": "flags.18?true"
                },
                {
                    "name": "min",
                    "type": "flags.20?true"
                },
                {
                    "name": "bot_inline_geo",
                    "type": "flags.21?true"
                },
                {
                    "name": "support",
                    "type": "flags.23?true"
                },
                {
                    "name": "scam",
                    "type": "flags.24?true"
                },
                {
                    "name": "apply_min_photo",
                    "type": "flags.25?true"
                },
                {
                    "name": "fake",
                    "type": "flags.26?true"
                },
                {
                    "name": "bot_attach_menu",
                    "type": "flags.27?true"
                },
                {
                    "name": "premium",
                    "type": "flags.28?true"
                },
                {
                    "name": "attach_menu_enabled",
                    "type": "flags.29?true"
                },
                {
                    "name": "flags2",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "flags.0?long"
                },
                {
                    "name": "first_name",
                    "type": "flags.1?string"
                },
                {
                    "name": "last_name",
                    "type": "flags.2?string"
                },
                {
                    "name": "username",
                    "type": "flags.3?string"
                },
                {
                    "name": "phone",
                    "type": "flags.4?string"
                },
                {
                    "name": "photo",
                    "type": "flags.5?UserProfilePhoto"
                },
                {
                    "name": "status",
                    "type": "flags.6?UserStatus"
                },
                {
                    "name": "bot_info_version",
                    "type": "flags.14?int"
                },
                {
                    "name": "restriction_reason",
                    "type": "flags.18?Vector<RestrictionReason>"
                },
                {
                    "name": "bot_inline_placeholder",
                    "type": "flags.19?string"
                },
                {
                    "name": "lang_code",
                    "type": "flags.22?string"
                },
                {
                    "name": "emoji_status",
                    "type": "flags.30?EmojiStatus"
                },
                {
                    "name": "usernames",
                    "type": "flags2.0?Vector<Username>"
                }
            ],
            "ret": "User"
        },
        {
            "_": "userProfilePhotoEmpty",
            "cid": "4f11bae1",
            "params": [],
            "ret": "UserProfilePhoto"
        },
        {
            "_": "userProfilePhoto",
            "cid": "82d1f706",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "has_video",
                    "type": "flags.0?true"
                },
                {
                    "name": "personal",
                    "type": "flags.2?true"
                },
                {
                    "name": "photo_id",
                    "type": "long"
                },
                {
                    "name": "stripped_thumb",
                    "type": "flags.1?bytes"
                },
                {
                    "name": "dc_id",
                    "type": "int"
                }
            ],
            "ret": "UserProfilePhoto"
        },
        {
            "_": "userStatusEmpty",
            "cid": "9d05049",
            "params": [],
            "ret": "UserStatus"
        },
        {
            "_": "userStatusOnline",
            "cid": "edb93949",
            "params": [
                {
                    "name": "expires",
                    "type": "int"
                }
            ],
            "ret": "UserStatus"
        },
        {
            "_": "userStatusOffline",
            "cid": "8c703f",
            "params": [
                {
                    "name": "was_online",
                    "type": "int"
                }
            ],
            "ret": "UserStatus"
        },
        {
            "_": "userStatusRecently",
            "cid": "e26f42f1",
            "params": [],
            "ret": "UserStatus"
        },
        {
            "_": "userStatusLastWeek",
            "cid": "7bf09fc",
            "params": [],
            "ret": "UserStatus"
        },
        {
            "_": "userStatusLastMonth",
            "cid": "77ebc742",
            "params": [],
            "ret": "UserStatus"
        },
        {
            "_": "chatEmpty",
            "cid": "29562865",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "Chat"
        },
        {
            "_": "chat",
            "cid": "41cbf256",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "creator",
                    "type": "flags.0?true"
                },
                {
                    "name": "left",
                    "type": "flags.2?true"
                },
                {
                    "name": "deactivated",
                    "type": "flags.5?true"
                },
                {
                    "name": "call_active",
                    "type": "flags.23?true"
                },
                {
                    "name": "call_not_empty",
                    "type": "flags.24?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.25?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "ChatPhoto"
                },
                {
                    "name": "participants_count",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "version",
                    "type": "int"
                },
                {
                    "name": "migrated_to",
                    "type": "flags.6?InputChannel"
                },
                {
                    "name": "admin_rights",
                    "type": "flags.14?ChatAdminRights"
                },
                {
                    "name": "default_banned_rights",
                    "type": "flags.18?ChatBannedRights"
                }
            ],
            "ret": "Chat"
        },
        {
            "_": "chatForbidden",
            "cid": "6592a1a7",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "Chat"
        },
        {
            "_": "channel",
            "cid": "83259464",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "creator",
                    "type": "flags.0?true"
                },
                {
                    "name": "left",
                    "type": "flags.2?true"
                },
                {
                    "name": "broadcast",
                    "type": "flags.5?true"
                },
                {
                    "name": "verified",
                    "type": "flags.7?true"
                },
                {
                    "name": "megagroup",
                    "type": "flags.8?true"
                },
                {
                    "name": "restricted",
                    "type": "flags.9?true"
                },
                {
                    "name": "signatures",
                    "type": "flags.11?true"
                },
                {
                    "name": "min",
                    "type": "flags.12?true"
                },
                {
                    "name": "scam",
                    "type": "flags.19?true"
                },
                {
                    "name": "has_link",
                    "type": "flags.20?true"
                },
                {
                    "name": "has_geo",
                    "type": "flags.21?true"
                },
                {
                    "name": "slowmode_enabled",
                    "type": "flags.22?true"
                },
                {
                    "name": "call_active",
                    "type": "flags.23?true"
                },
                {
                    "name": "call_not_empty",
                    "type": "flags.24?true"
                },
                {
                    "name": "fake",
                    "type": "flags.25?true"
                },
                {
                    "name": "gigagroup",
                    "type": "flags.26?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.27?true"
                },
                {
                    "name": "join_to_send",
                    "type": "flags.28?true"
                },
                {
                    "name": "join_request",
                    "type": "flags.29?true"
                },
                {
                    "name": "forum",
                    "type": "flags.30?true"
                },
                {
                    "name": "flags2",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "flags.13?long"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "username",
                    "type": "flags.6?string"
                },
                {
                    "name": "photo",
                    "type": "ChatPhoto"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "restriction_reason",
                    "type": "flags.9?Vector<RestrictionReason>"
                },
                {
                    "name": "admin_rights",
                    "type": "flags.14?ChatAdminRights"
                },
                {
                    "name": "banned_rights",
                    "type": "flags.15?ChatBannedRights"
                },
                {
                    "name": "default_banned_rights",
                    "type": "flags.18?ChatBannedRights"
                },
                {
                    "name": "participants_count",
                    "type": "flags.17?int"
                },
                {
                    "name": "usernames",
                    "type": "flags2.0?Vector<Username>"
                }
            ],
            "ret": "Chat"
        },
        {
            "_": "channelForbidden",
            "cid": "17d493d5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "broadcast",
                    "type": "flags.5?true"
                },
                {
                    "name": "megagroup",
                    "type": "flags.8?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "until_date",
                    "type": "flags.16?int"
                }
            ],
            "ret": "Chat"
        },
        {
            "_": "chatFull",
            "cid": "c9d31138",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "can_set_username",
                    "type": "flags.7?true"
                },
                {
                    "name": "has_scheduled",
                    "type": "flags.8?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "about",
                    "type": "string"
                },
                {
                    "name": "participants",
                    "type": "ChatParticipants"
                },
                {
                    "name": "chat_photo",
                    "type": "flags.2?Photo"
                },
                {
                    "name": "notify_settings",
                    "type": "PeerNotifySettings"
                },
                {
                    "name": "exported_invite",
                    "type": "flags.13?ExportedChatInvite"
                },
                {
                    "name": "bot_info",
                    "type": "flags.3?Vector<BotInfo>"
                },
                {
                    "name": "pinned_msg_id",
                    "type": "flags.6?int"
                },
                {
                    "name": "folder_id",
                    "type": "flags.11?int"
                },
                {
                    "name": "call",
                    "type": "flags.12?InputGroupCall"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.14?int"
                },
                {
                    "name": "groupcall_default_join_as",
                    "type": "flags.15?Peer"
                },
                {
                    "name": "theme_emoticon",
                    "type": "flags.16?string"
                },
                {
                    "name": "requests_pending",
                    "type": "flags.17?int"
                },
                {
                    "name": "recent_requesters",
                    "type": "flags.17?Vector<long>"
                },
                {
                    "name": "available_reactions",
                    "type": "flags.18?ChatReactions"
                }
            ],
            "ret": "ChatFull"
        },
        {
            "_": "channelFull",
            "cid": "f2355507",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "can_view_participants",
                    "type": "flags.3?true"
                },
                {
                    "name": "can_set_username",
                    "type": "flags.6?true"
                },
                {
                    "name": "can_set_stickers",
                    "type": "flags.7?true"
                },
                {
                    "name": "hidden_prehistory",
                    "type": "flags.10?true"
                },
                {
                    "name": "can_set_location",
                    "type": "flags.16?true"
                },
                {
                    "name": "has_scheduled",
                    "type": "flags.19?true"
                },
                {
                    "name": "can_view_stats",
                    "type": "flags.20?true"
                },
                {
                    "name": "blocked",
                    "type": "flags.22?true"
                },
                {
                    "name": "flags2",
                    "type": "#"
                },
                {
                    "name": "can_delete_channel",
                    "type": "flags2.0?true"
                },
                {
                    "name": "antispam",
                    "type": "flags2.1?true"
                },
                {
                    "name": "participants_hidden",
                    "type": "flags2.2?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "about",
                    "type": "string"
                },
                {
                    "name": "participants_count",
                    "type": "flags.0?int"
                },
                {
                    "name": "admins_count",
                    "type": "flags.1?int"
                },
                {
                    "name": "kicked_count",
                    "type": "flags.2?int"
                },
                {
                    "name": "banned_count",
                    "type": "flags.2?int"
                },
                {
                    "name": "online_count",
                    "type": "flags.13?int"
                },
                {
                    "name": "read_inbox_max_id",
                    "type": "int"
                },
                {
                    "name": "read_outbox_max_id",
                    "type": "int"
                },
                {
                    "name": "unread_count",
                    "type": "int"
                },
                {
                    "name": "chat_photo",
                    "type": "Photo"
                },
                {
                    "name": "notify_settings",
                    "type": "PeerNotifySettings"
                },
                {
                    "name": "exported_invite",
                    "type": "flags.23?ExportedChatInvite"
                },
                {
                    "name": "bot_info",
                    "type": "Vector<BotInfo>"
                },
                {
                    "name": "migrated_from_chat_id",
                    "type": "flags.4?long"
                },
                {
                    "name": "migrated_from_max_id",
                    "type": "flags.4?int"
                },
                {
                    "name": "pinned_msg_id",
                    "type": "flags.5?int"
                },
                {
                    "name": "stickerset",
                    "type": "flags.8?StickerSet"
                },
                {
                    "name": "available_min_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "folder_id",
                    "type": "flags.11?int"
                },
                {
                    "name": "linked_chat_id",
                    "type": "flags.14?long"
                },
                {
                    "name": "location",
                    "type": "flags.15?ChannelLocation"
                },
                {
                    "name": "slowmode_seconds",
                    "type": "flags.17?int"
                },
                {
                    "name": "slowmode_next_send_date",
                    "type": "flags.18?int"
                },
                {
                    "name": "stats_dc",
                    "type": "flags.12?int"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "call",
                    "type": "flags.21?InputGroupCall"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.24?int"
                },
                {
                    "name": "pending_suggestions",
                    "type": "flags.25?Vector<string>"
                },
                {
                    "name": "groupcall_default_join_as",
                    "type": "flags.26?Peer"
                },
                {
                    "name": "theme_emoticon",
                    "type": "flags.27?string"
                },
                {
                    "name": "requests_pending",
                    "type": "flags.28?int"
                },
                {
                    "name": "recent_requesters",
                    "type": "flags.28?Vector<long>"
                },
                {
                    "name": "default_send_as",
                    "type": "flags.29?Peer"
                },
                {
                    "name": "available_reactions",
                    "type": "flags.30?ChatReactions"
                }
            ],
            "ret": "ChatFull"
        },
        {
            "_": "chatParticipant",
            "cid": "c02d4007",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "inviter_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "ChatParticipant"
        },
        {
            "_": "chatParticipantCreator",
            "cid": "e46bcee4",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "ChatParticipant"
        },
        {
            "_": "chatParticipantAdmin",
            "cid": "a0933f5b",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "inviter_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "ChatParticipant"
        },
        {
            "_": "chatParticipantsForbidden",
            "cid": "8763d3e1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "self_participant",
                    "type": "flags.0?ChatParticipant"
                }
            ],
            "ret": "ChatParticipants"
        },
        {
            "_": "chatParticipants",
            "cid": "3cbc93f8",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "participants",
                    "type": "Vector<ChatParticipant>"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "ChatParticipants"
        },
        {
            "_": "chatPhotoEmpty",
            "cid": "37c1011c",
            "params": [],
            "ret": "ChatPhoto"
        },
        {
            "_": "chatPhoto",
            "cid": "1c6e1c11",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "has_video",
                    "type": "flags.0?true"
                },
                {
                    "name": "photo_id",
                    "type": "long"
                },
                {
                    "name": "stripped_thumb",
                    "type": "flags.1?bytes"
                },
                {
                    "name": "dc_id",
                    "type": "int"
                }
            ],
            "ret": "ChatPhoto"
        },
        {
            "_": "messageEmpty",
            "cid": "90a6ca84",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "peer_id",
                    "type": "flags.0?Peer"
                }
            ],
            "ret": "Message"
        },
        {
            "_": "message",
            "cid": "38116ee0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "out",
                    "type": "flags.1?true"
                },
                {
                    "name": "mentioned",
                    "type": "flags.4?true"
                },
                {
                    "name": "media_unread",
                    "type": "flags.5?true"
                },
                {
                    "name": "silent",
                    "type": "flags.13?true"
                },
                {
                    "name": "post",
                    "type": "flags.14?true"
                },
                {
                    "name": "from_scheduled",
                    "type": "flags.18?true"
                },
                {
                    "name": "legacy",
                    "type": "flags.19?true"
                },
                {
                    "name": "edit_hide",
                    "type": "flags.21?true"
                },
                {
                    "name": "pinned",
                    "type": "flags.24?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.26?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "from_id",
                    "type": "flags.8?Peer"
                },
                {
                    "name": "peer_id",
                    "type": "Peer"
                },
                {
                    "name": "fwd_from",
                    "type": "flags.2?MessageFwdHeader"
                },
                {
                    "name": "via_bot_id",
                    "type": "flags.11?long"
                },
                {
                    "name": "reply_to",
                    "type": "flags.3?MessageReplyHeader"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "media",
                    "type": "flags.9?MessageMedia"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.6?ReplyMarkup"
                },
                {
                    "name": "entities",
                    "type": "flags.7?Vector<MessageEntity>"
                },
                {
                    "name": "views",
                    "type": "flags.10?int"
                },
                {
                    "name": "forwards",
                    "type": "flags.10?int"
                },
                {
                    "name": "replies",
                    "type": "flags.23?MessageReplies"
                },
                {
                    "name": "edit_date",
                    "type": "flags.15?int"
                },
                {
                    "name": "post_author",
                    "type": "flags.16?string"
                },
                {
                    "name": "grouped_id",
                    "type": "flags.17?long"
                },
                {
                    "name": "reactions",
                    "type": "flags.20?MessageReactions"
                },
                {
                    "name": "restriction_reason",
                    "type": "flags.22?Vector<RestrictionReason>"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.25?int"
                }
            ],
            "ret": "Message"
        },
        {
            "_": "messageService",
            "cid": "2b085862",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "out",
                    "type": "flags.1?true"
                },
                {
                    "name": "mentioned",
                    "type": "flags.4?true"
                },
                {
                    "name": "media_unread",
                    "type": "flags.5?true"
                },
                {
                    "name": "silent",
                    "type": "flags.13?true"
                },
                {
                    "name": "post",
                    "type": "flags.14?true"
                },
                {
                    "name": "legacy",
                    "type": "flags.19?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "from_id",
                    "type": "flags.8?Peer"
                },
                {
                    "name": "peer_id",
                    "type": "Peer"
                },
                {
                    "name": "reply_to",
                    "type": "flags.3?MessageReplyHeader"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "action",
                    "type": "MessageAction"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.25?int"
                }
            ],
            "ret": "Message"
        },
        {
            "_": "messageMediaEmpty",
            "cid": "3ded6320",
            "params": [],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaPhoto",
            "cid": "695150d7",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "spoiler",
                    "type": "flags.3?true"
                },
                {
                    "name": "photo",
                    "type": "flags.0?Photo"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.2?int"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaGeo",
            "cid": "56e0d474",
            "params": [
                {
                    "name": "geo",
                    "type": "GeoPoint"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaContact",
            "cid": "70322949",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "vcard",
                    "type": "string"
                },
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaUnsupported",
            "cid": "9f84f49e",
            "params": [],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaDocument",
            "cid": "9cb070d7",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "nopremium",
                    "type": "flags.3?true"
                },
                {
                    "name": "spoiler",
                    "type": "flags.4?true"
                },
                {
                    "name": "document",
                    "type": "flags.0?Document"
                },
                {
                    "name": "ttl_seconds",
                    "type": "flags.2?int"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaWebPage",
            "cid": "a32dd600",
            "params": [
                {
                    "name": "webpage",
                    "type": "WebPage"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaVenue",
            "cid": "2ec0533f",
            "params": [
                {
                    "name": "geo",
                    "type": "GeoPoint"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "address",
                    "type": "string"
                },
                {
                    "name": "provider",
                    "type": "string"
                },
                {
                    "name": "venue_id",
                    "type": "string"
                },
                {
                    "name": "venue_type",
                    "type": "string"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaGame",
            "cid": "fdb19008",
            "params": [
                {
                    "name": "game",
                    "type": "Game"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaInvoice",
            "cid": "f6a548d3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "shipping_address_requested",
                    "type": "flags.1?true"
                },
                {
                    "name": "test",
                    "type": "flags.3?true"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.0?WebDocument"
                },
                {
                    "name": "receipt_msg_id",
                    "type": "flags.2?int"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "total_amount",
                    "type": "long"
                },
                {
                    "name": "start_param",
                    "type": "string"
                },
                {
                    "name": "extended_media",
                    "type": "flags.4?MessageExtendedMedia"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaGeoLive",
            "cid": "b940c666",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "geo",
                    "type": "GeoPoint"
                },
                {
                    "name": "heading",
                    "type": "flags.0?int"
                },
                {
                    "name": "period",
                    "type": "int"
                },
                {
                    "name": "proximity_notification_radius",
                    "type": "flags.1?int"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaPoll",
            "cid": "4bd6e798",
            "params": [
                {
                    "name": "poll",
                    "type": "Poll"
                },
                {
                    "name": "results",
                    "type": "PollResults"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageMediaDice",
            "cid": "3f7ee58b",
            "params": [
                {
                    "name": "value",
                    "type": "int"
                },
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "messageActionEmpty",
            "cid": "b6aef7b0",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatCreate",
            "cid": "bd47cbad",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "users",
                    "type": "Vector<long>"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatEditTitle",
            "cid": "b5a1ce5a",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatEditPhoto",
            "cid": "7fcb13a8",
            "params": [
                {
                    "name": "photo",
                    "type": "Photo"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatDeletePhoto",
            "cid": "95e3fbef",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatAddUser",
            "cid": "15cefd00",
            "params": [
                {
                    "name": "users",
                    "type": "Vector<long>"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatDeleteUser",
            "cid": "a43f30cc",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatJoinedByLink",
            "cid": "31224c3",
            "params": [
                {
                    "name": "inviter_id",
                    "type": "long"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChannelCreate",
            "cid": "95d2ac92",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatMigrateTo",
            "cid": "e1037f92",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChannelMigrateFrom",
            "cid": "ea3948e9",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionPinMessage",
            "cid": "94bd38ed",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionHistoryClear",
            "cid": "9fbab604",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionGameScore",
            "cid": "92a72876",
            "params": [
                {
                    "name": "game_id",
                    "type": "long"
                },
                {
                    "name": "score",
                    "type": "int"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionPaymentSentMe",
            "cid": "8f31b327",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "recurring_init",
                    "type": "flags.2?true"
                },
                {
                    "name": "recurring_used",
                    "type": "flags.3?true"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "total_amount",
                    "type": "long"
                },
                {
                    "name": "payload",
                    "type": "bytes"
                },
                {
                    "name": "info",
                    "type": "flags.0?PaymentRequestedInfo"
                },
                {
                    "name": "shipping_option_id",
                    "type": "flags.1?string"
                },
                {
                    "name": "charge",
                    "type": "PaymentCharge"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionPaymentSent",
            "cid": "96163f56",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "recurring_init",
                    "type": "flags.2?true"
                },
                {
                    "name": "recurring_used",
                    "type": "flags.3?true"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "total_amount",
                    "type": "long"
                },
                {
                    "name": "invoice_slug",
                    "type": "flags.0?string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionPhoneCall",
            "cid": "80e11a7f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "video",
                    "type": "flags.2?true"
                },
                {
                    "name": "call_id",
                    "type": "long"
                },
                {
                    "name": "reason",
                    "type": "flags.0?PhoneCallDiscardReason"
                },
                {
                    "name": "duration",
                    "type": "flags.1?int"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionScreenshotTaken",
            "cid": "4792929b",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionCustomAction",
            "cid": "fae69f56",
            "params": [
                {
                    "name": "message",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionBotAllowed",
            "cid": "abe9affe",
            "params": [
                {
                    "name": "domain",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionSecureValuesSentMe",
            "cid": "1b287353",
            "params": [
                {
                    "name": "values",
                    "type": "Vector<SecureValue>"
                },
                {
                    "name": "credentials",
                    "type": "SecureCredentialsEncrypted"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionSecureValuesSent",
            "cid": "d95c6154",
            "params": [
                {
                    "name": "types",
                    "type": "Vector<SecureValueType>"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionContactSignUp",
            "cid": "f3f25f76",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionGeoProximityReached",
            "cid": "98e0d697",
            "params": [
                {
                    "name": "from_id",
                    "type": "Peer"
                },
                {
                    "name": "to_id",
                    "type": "Peer"
                },
                {
                    "name": "distance",
                    "type": "int"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionGroupCall",
            "cid": "7a0d7f42",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "duration",
                    "type": "flags.0?int"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionInviteToGroupCall",
            "cid": "502f92f7",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "users",
                    "type": "Vector<long>"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionSetMessagesTTL",
            "cid": "3c134d7b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "period",
                    "type": "int"
                },
                {
                    "name": "auto_setting_from",
                    "type": "flags.0?long"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionGroupCallScheduled",
            "cid": "b3a07661",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "schedule_date",
                    "type": "int"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionSetChatTheme",
            "cid": "aa786345",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionChatJoinedByRequest",
            "cid": "ebbca3cb",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionWebViewDataSentMe",
            "cid": "47dd8079",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "data",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionWebViewDataSent",
            "cid": "b4c38cb5",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionGiftPremium",
            "cid": "aba0f5c6",
            "params": [
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "amount",
                    "type": "long"
                },
                {
                    "name": "months",
                    "type": "int"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionTopicCreate",
            "cid": "d999256",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "icon_color",
                    "type": "int"
                },
                {
                    "name": "icon_emoji_id",
                    "type": "flags.0?long"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionTopicEdit",
            "cid": "c0944820",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "title",
                    "type": "flags.0?string"
                },
                {
                    "name": "icon_emoji_id",
                    "type": "flags.1?long"
                },
                {
                    "name": "closed",
                    "type": "flags.2?Bool"
                },
                {
                    "name": "hidden",
                    "type": "flags.3?Bool"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionSuggestProfilePhoto",
            "cid": "57de635e",
            "params": [
                {
                    "name": "photo",
                    "type": "Photo"
                }
            ],
            "ret": "MessageAction"
        },
        {
            "_": "messageActionAttachMenuBotAllowed",
            "cid": "e7e75f97",
            "params": [],
            "ret": "MessageAction"
        },
        {
            "_": "dialog",
            "cid": "d58a08c6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.2?true"
                },
                {
                    "name": "unread_mark",
                    "type": "flags.3?true"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "top_message",
                    "type": "int"
                },
                {
                    "name": "read_inbox_max_id",
                    "type": "int"
                },
                {
                    "name": "read_outbox_max_id",
                    "type": "int"
                },
                {
                    "name": "unread_count",
                    "type": "int"
                },
                {
                    "name": "unread_mentions_count",
                    "type": "int"
                },
                {
                    "name": "unread_reactions_count",
                    "type": "int"
                },
                {
                    "name": "notify_settings",
                    "type": "PeerNotifySettings"
                },
                {
                    "name": "pts",
                    "type": "flags.0?int"
                },
                {
                    "name": "draft",
                    "type": "flags.1?DraftMessage"
                },
                {
                    "name": "folder_id",
                    "type": "flags.4?int"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.5?int"
                }
            ],
            "ret": "Dialog"
        },
        {
            "_": "dialogFolder",
            "cid": "71bd134c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.2?true"
                },
                {
                    "name": "folder",
                    "type": "Folder"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "top_message",
                    "type": "int"
                },
                {
                    "name": "unread_muted_peers_count",
                    "type": "int"
                },
                {
                    "name": "unread_unmuted_peers_count",
                    "type": "int"
                },
                {
                    "name": "unread_muted_messages_count",
                    "type": "int"
                },
                {
                    "name": "unread_unmuted_messages_count",
                    "type": "int"
                }
            ],
            "ret": "Dialog"
        },
        {
            "_": "photoEmpty",
            "cid": "2331b22d",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "Photo"
        },
        {
            "_": "photo",
            "cid": "fb197a65",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "has_stickers",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "sizes",
                    "type": "Vector<PhotoSize>"
                },
                {
                    "name": "video_sizes",
                    "type": "flags.1?Vector<VideoSize>"
                },
                {
                    "name": "dc_id",
                    "type": "int"
                }
            ],
            "ret": "Photo"
        },
        {
            "_": "photoSizeEmpty",
            "cid": "e17e23c",
            "params": [
                {
                    "name": "type",
                    "type": "string"
                }
            ],
            "ret": "PhotoSize"
        },
        {
            "_": "photoSize",
            "cid": "75c78e60",
            "params": [
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                },
                {
                    "name": "size",
                    "type": "int"
                }
            ],
            "ret": "PhotoSize"
        },
        {
            "_": "photoCachedSize",
            "cid": "21e1ad6",
            "params": [
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "PhotoSize"
        },
        {
            "_": "photoStrippedSize",
            "cid": "e0b0bc2e",
            "params": [
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "PhotoSize"
        },
        {
            "_": "photoSizeProgressive",
            "cid": "fa3efb95",
            "params": [
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                },
                {
                    "name": "sizes",
                    "type": "Vector<int>"
                }
            ],
            "ret": "PhotoSize"
        },
        {
            "_": "photoPathSize",
            "cid": "d8214d41",
            "params": [
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "PhotoSize"
        },
        {
            "_": "geoPointEmpty",
            "cid": "1117dd5f",
            "params": [],
            "ret": "GeoPoint"
        },
        {
            "_": "geoPoint",
            "cid": "b2a2f663",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "long",
                    "type": "double"
                },
                {
                    "name": "lat",
                    "type": "double"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "accuracy_radius",
                    "type": "flags.0?int"
                }
            ],
            "ret": "GeoPoint"
        },
        {
            "_": "sentCode",
            "cid": "5e002502",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "type",
                    "type": "auth.SentCodeType"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                },
                {
                    "name": "next_type",
                    "type": "flags.1?auth.CodeType"
                },
                {
                    "name": "timeout",
                    "type": "flags.2?int"
                }
            ],
            "ret": "auth.SentCode"
        },
        {
            "_": "authorization",
            "cid": "33fb7bb8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "setup_password_required",
                    "type": "flags.1?true"
                },
                {
                    "name": "otherwise_relogin_days",
                    "type": "flags.1?int"
                },
                {
                    "name": "tmp_sessions",
                    "type": "flags.0?int"
                },
                {
                    "name": "user",
                    "type": "User"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "authorizationSignUpRequired",
            "cid": "44747e9a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "terms_of_service",
                    "type": "flags.0?help.TermsOfService"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "exportedAuthorization",
            "cid": "b434e2b8",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "auth.ExportedAuthorization"
        },
        {
            "_": "inputNotifyPeer",
            "cid": "b8bc5b0c",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "InputNotifyPeer"
        },
        {
            "_": "inputNotifyUsers",
            "cid": "193b4417",
            "params": [],
            "ret": "InputNotifyPeer"
        },
        {
            "_": "inputNotifyChats",
            "cid": "4a95e84e",
            "params": [],
            "ret": "InputNotifyPeer"
        },
        {
            "_": "inputNotifyBroadcasts",
            "cid": "b1db7c7e",
            "params": [],
            "ret": "InputNotifyPeer"
        },
        {
            "_": "inputNotifyForumTopic",
            "cid": "5c467992",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "int"
                }
            ],
            "ret": "InputNotifyPeer"
        },
        {
            "_": "inputPeerNotifySettings",
            "cid": "df1f002b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "show_previews",
                    "type": "flags.0?Bool"
                },
                {
                    "name": "silent",
                    "type": "flags.1?Bool"
                },
                {
                    "name": "mute_until",
                    "type": "flags.2?int"
                },
                {
                    "name": "sound",
                    "type": "flags.3?NotificationSound"
                }
            ],
            "ret": "InputPeerNotifySettings"
        },
        {
            "_": "peerNotifySettings",
            "cid": "a83b0426",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "show_previews",
                    "type": "flags.0?Bool"
                },
                {
                    "name": "silent",
                    "type": "flags.1?Bool"
                },
                {
                    "name": "mute_until",
                    "type": "flags.2?int"
                },
                {
                    "name": "ios_sound",
                    "type": "flags.3?NotificationSound"
                },
                {
                    "name": "android_sound",
                    "type": "flags.4?NotificationSound"
                },
                {
                    "name": "other_sound",
                    "type": "flags.5?NotificationSound"
                }
            ],
            "ret": "PeerNotifySettings"
        },
        {
            "_": "peerSettings",
            "cid": "a518110d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "report_spam",
                    "type": "flags.0?true"
                },
                {
                    "name": "add_contact",
                    "type": "flags.1?true"
                },
                {
                    "name": "block_contact",
                    "type": "flags.2?true"
                },
                {
                    "name": "share_contact",
                    "type": "flags.3?true"
                },
                {
                    "name": "need_contacts_exception",
                    "type": "flags.4?true"
                },
                {
                    "name": "report_geo",
                    "type": "flags.5?true"
                },
                {
                    "name": "autoarchived",
                    "type": "flags.7?true"
                },
                {
                    "name": "invite_members",
                    "type": "flags.8?true"
                },
                {
                    "name": "request_chat_broadcast",
                    "type": "flags.10?true"
                },
                {
                    "name": "geo_distance",
                    "type": "flags.6?int"
                },
                {
                    "name": "request_chat_title",
                    "type": "flags.9?string"
                },
                {
                    "name": "request_chat_date",
                    "type": "flags.9?int"
                }
            ],
            "ret": "PeerSettings"
        },
        {
            "_": "wallPaper",
            "cid": "a437c3ed",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "creator",
                    "type": "flags.0?true"
                },
                {
                    "name": "default",
                    "type": "flags.1?true"
                },
                {
                    "name": "pattern",
                    "type": "flags.3?true"
                },
                {
                    "name": "dark",
                    "type": "flags.4?true"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "slug",
                    "type": "string"
                },
                {
                    "name": "document",
                    "type": "Document"
                },
                {
                    "name": "settings",
                    "type": "flags.2?WallPaperSettings"
                }
            ],
            "ret": "WallPaper"
        },
        {
            "_": "wallPaperNoFile",
            "cid": "e0804116",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "default",
                    "type": "flags.1?true"
                },
                {
                    "name": "dark",
                    "type": "flags.4?true"
                },
                {
                    "name": "settings",
                    "type": "flags.2?WallPaperSettings"
                }
            ],
            "ret": "WallPaper"
        },
        {
            "_": "inputReportReasonSpam",
            "cid": "58dbcab8",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonViolence",
            "cid": "1e22c78d",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonPornography",
            "cid": "2e59d922",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonChildAbuse",
            "cid": "adf44ee3",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonOther",
            "cid": "c1e4a2b1",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonCopyright",
            "cid": "9b89f93a",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonGeoIrrelevant",
            "cid": "dbd4feed",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonFake",
            "cid": "f5ddd6e7",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonIllegalDrugs",
            "cid": "a8eb2be",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "inputReportReasonPersonalDetails",
            "cid": "9ec7863d",
            "params": [],
            "ret": "ReportReason"
        },
        {
            "_": "userFull",
            "cid": "f8d32aed",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "blocked",
                    "type": "flags.0?true"
                },
                {
                    "name": "phone_calls_available",
                    "type": "flags.4?true"
                },
                {
                    "name": "phone_calls_private",
                    "type": "flags.5?true"
                },
                {
                    "name": "can_pin_message",
                    "type": "flags.7?true"
                },
                {
                    "name": "has_scheduled",
                    "type": "flags.12?true"
                },
                {
                    "name": "video_calls_available",
                    "type": "flags.13?true"
                },
                {
                    "name": "voice_messages_forbidden",
                    "type": "flags.20?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "about",
                    "type": "flags.1?string"
                },
                {
                    "name": "settings",
                    "type": "PeerSettings"
                },
                {
                    "name": "personal_photo",
                    "type": "flags.21?Photo"
                },
                {
                    "name": "profile_photo",
                    "type": "flags.2?Photo"
                },
                {
                    "name": "fallback_photo",
                    "type": "flags.22?Photo"
                },
                {
                    "name": "notify_settings",
                    "type": "PeerNotifySettings"
                },
                {
                    "name": "bot_info",
                    "type": "flags.3?BotInfo"
                },
                {
                    "name": "pinned_msg_id",
                    "type": "flags.6?int"
                },
                {
                    "name": "common_chats_count",
                    "type": "int"
                },
                {
                    "name": "folder_id",
                    "type": "flags.11?int"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.14?int"
                },
                {
                    "name": "theme_emoticon",
                    "type": "flags.15?string"
                },
                {
                    "name": "private_forward_name",
                    "type": "flags.16?string"
                },
                {
                    "name": "bot_group_admin_rights",
                    "type": "flags.17?ChatAdminRights"
                },
                {
                    "name": "bot_broadcast_admin_rights",
                    "type": "flags.18?ChatAdminRights"
                },
                {
                    "name": "premium_gifts",
                    "type": "flags.19?Vector<PremiumGiftOption>"
                }
            ],
            "ret": "UserFull"
        },
        {
            "_": "contact",
            "cid": "145ade0b",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "mutual",
                    "type": "Bool"
                }
            ],
            "ret": "Contact"
        },
        {
            "_": "importedContact",
            "cid": "c13e3c50",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "client_id",
                    "type": "long"
                }
            ],
            "ret": "ImportedContact"
        },
        {
            "_": "contactStatus",
            "cid": "16d9703b",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "status",
                    "type": "UserStatus"
                }
            ],
            "ret": "ContactStatus"
        },
        {
            "_": "contactsNotModified",
            "cid": "b74ba9d2",
            "params": [],
            "ret": "contacts.Contacts"
        },
        {
            "_": "contacts",
            "cid": "eae87e42",
            "params": [
                {
                    "name": "contacts",
                    "type": "Vector<Contact>"
                },
                {
                    "name": "saved_count",
                    "type": "int"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.Contacts"
        },
        {
            "_": "importedContacts",
            "cid": "77d01c3b",
            "params": [
                {
                    "name": "imported",
                    "type": "Vector<ImportedContact>"
                },
                {
                    "name": "popular_invites",
                    "type": "Vector<PopularContact>"
                },
                {
                    "name": "retry_contacts",
                    "type": "Vector<long>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.ImportedContacts"
        },
        {
            "_": "blocked",
            "cid": "ade1591",
            "params": [
                {
                    "name": "blocked",
                    "type": "Vector<PeerBlocked>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.Blocked"
        },
        {
            "_": "blockedSlice",
            "cid": "e1664194",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "blocked",
                    "type": "Vector<PeerBlocked>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.Blocked"
        },
        {
            "_": "dialogs",
            "cid": "15ba6c40",
            "params": [
                {
                    "name": "dialogs",
                    "type": "Vector<Dialog>"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.Dialogs"
        },
        {
            "_": "dialogsSlice",
            "cid": "71e094f3",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "dialogs",
                    "type": "Vector<Dialog>"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.Dialogs"
        },
        {
            "_": "dialogsNotModified",
            "cid": "f0e3e596",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                }
            ],
            "ret": "messages.Dialogs"
        },
        {
            "_": "messages",
            "cid": "8c718e87",
            "params": [
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "messagesSlice",
            "cid": "3a54685e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "inexact",
                    "type": "flags.1?true"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "next_rate",
                    "type": "flags.0?int"
                },
                {
                    "name": "offset_id_offset",
                    "type": "flags.2?int"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "channelMessages",
            "cid": "c776ba4e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "inexact",
                    "type": "flags.1?true"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "offset_id_offset",
                    "type": "flags.2?int"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "topics",
                    "type": "Vector<ForumTopic>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "messagesNotModified",
            "cid": "74535f21",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "chats",
            "cid": "64ff9fd5",
            "params": [
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "chatsSlice",
            "cid": "9cd81144",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "chatFull",
            "cid": "e5d7d19c",
            "params": [
                {
                    "name": "full_chat",
                    "type": "ChatFull"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.ChatFull"
        },
        {
            "_": "affectedHistory",
            "cid": "b45c69d1",
            "params": [
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                },
                {
                    "name": "offset",
                    "type": "int"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "inputMessagesFilterEmpty",
            "cid": "57e2f66c",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterPhotos",
            "cid": "9609a51c",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterVideo",
            "cid": "9fc00e65",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterPhotoVideo",
            "cid": "56e9f0e4",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterDocument",
            "cid": "9eddf188",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterUrl",
            "cid": "7ef0dd87",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterGif",
            "cid": "ffc86587",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterVoice",
            "cid": "50f5c392",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterMusic",
            "cid": "3751b49e",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterChatPhotos",
            "cid": "3a20ecb8",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterPhoneCalls",
            "cid": "80c99768",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "missed",
                    "type": "flags.0?true"
                }
            ],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterRoundVoice",
            "cid": "7a7c17a4",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterRoundVideo",
            "cid": "b549da53",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterMyMentions",
            "cid": "c1f8e69a",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterGeo",
            "cid": "e7026d0d",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterContacts",
            "cid": "e062db83",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "inputMessagesFilterPinned",
            "cid": "1bb00451",
            "params": [],
            "ret": "MessagesFilter"
        },
        {
            "_": "updateNewMessage",
            "cid": "1f2b0afd",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateMessageID",
            "cid": "4e90bfd6",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "random_id",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDeleteMessages",
            "cid": "a20db0e5",
            "params": [
                {
                    "name": "messages",
                    "type": "Vector<int>"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateUserTyping",
            "cid": "c01e857f",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "action",
                    "type": "SendMessageAction"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatUserTyping",
            "cid": "83487af0",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "from_id",
                    "type": "Peer"
                },
                {
                    "name": "action",
                    "type": "SendMessageAction"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatParticipants",
            "cid": "7761198",
            "params": [
                {
                    "name": "participants",
                    "type": "ChatParticipants"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateUserStatus",
            "cid": "e5bdf8de",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "status",
                    "type": "UserStatus"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateUserName",
            "cid": "a7848924",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "usernames",
                    "type": "Vector<Username>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateNewEncryptedMessage",
            "cid": "12bcbd9a",
            "params": [
                {
                    "name": "message",
                    "type": "EncryptedMessage"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateEncryptedChatTyping",
            "cid": "1710f156",
            "params": [
                {
                    "name": "chat_id",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateEncryption",
            "cid": "b4a2e88d",
            "params": [
                {
                    "name": "chat",
                    "type": "EncryptedChat"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateEncryptedMessagesRead",
            "cid": "38fe25b7",
            "params": [
                {
                    "name": "chat_id",
                    "type": "int"
                },
                {
                    "name": "max_date",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatParticipantAdd",
            "cid": "3dda5451",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "inviter_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatParticipantDelete",
            "cid": "e32f3d77",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDcOptions",
            "cid": "8e5e9873",
            "params": [
                {
                    "name": "dc_options",
                    "type": "Vector<DcOption>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateNotifySettings",
            "cid": "bec268ef",
            "params": [
                {
                    "name": "peer",
                    "type": "NotifyPeer"
                },
                {
                    "name": "notify_settings",
                    "type": "PeerNotifySettings"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateServiceNotification",
            "cid": "ebe46819",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "popup",
                    "type": "flags.0?true"
                },
                {
                    "name": "inbox_date",
                    "type": "flags.1?int"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "media",
                    "type": "MessageMedia"
                },
                {
                    "name": "entities",
                    "type": "Vector<MessageEntity>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePrivacy",
            "cid": "ee3b272a",
            "params": [
                {
                    "name": "key",
                    "type": "PrivacyKey"
                },
                {
                    "name": "rules",
                    "type": "Vector<PrivacyRule>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateUserPhone",
            "cid": "5492a13",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "phone",
                    "type": "string"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadHistoryInbox",
            "cid": "9c974fdf",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "folder_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "still_unread_count",
                    "type": "int"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadHistoryOutbox",
            "cid": "2f2f21bf",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateWebPage",
            "cid": "7f891213",
            "params": [
                {
                    "name": "webpage",
                    "type": "WebPage"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadMessagesContents",
            "cid": "68c13933",
            "params": [
                {
                    "name": "messages",
                    "type": "Vector<int>"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelTooLong",
            "cid": "108d941f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "pts",
                    "type": "flags.0?int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannel",
            "cid": "635b4c09",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateNewChannelMessage",
            "cid": "62ba04d9",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadChannelInbox",
            "cid": "922e6e10",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "folder_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "still_unread_count",
                    "type": "int"
                },
                {
                    "name": "pts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDeleteChannelMessages",
            "cid": "c32d5b12",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "messages",
                    "type": "Vector<int>"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelMessageViews",
            "cid": "f226ac08",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "views",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatParticipantAdmin",
            "cid": "d7ca61a2",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "is_admin",
                    "type": "Bool"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateNewStickerSet",
            "cid": "688a30aa",
            "params": [
                {
                    "name": "stickerset",
                    "type": "messages.StickerSet"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateStickerSetsOrder",
            "cid": "bb2d201",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "masks",
                    "type": "flags.0?true"
                },
                {
                    "name": "emojis",
                    "type": "flags.1?true"
                },
                {
                    "name": "order",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateStickerSets",
            "cid": "31c24808",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "masks",
                    "type": "flags.0?true"
                },
                {
                    "name": "emojis",
                    "type": "flags.1?true"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateSavedGifs",
            "cid": "9375341e",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateBotInlineQuery",
            "cid": "496f379c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "query",
                    "type": "string"
                },
                {
                    "name": "geo",
                    "type": "flags.0?GeoPoint"
                },
                {
                    "name": "peer_type",
                    "type": "flags.1?InlineQueryPeerType"
                },
                {
                    "name": "offset",
                    "type": "string"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotInlineSend",
            "cid": "12f12a07",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "query",
                    "type": "string"
                },
                {
                    "name": "geo",
                    "type": "flags.0?GeoPoint"
                },
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "msg_id",
                    "type": "flags.1?InputBotInlineMessageID"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateEditChannelMessage",
            "cid": "1b3f4df7",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotCallbackQuery",
            "cid": "b9cfc48d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "chat_instance",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "flags.0?bytes"
                },
                {
                    "name": "game_short_name",
                    "type": "flags.1?string"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateEditMessage",
            "cid": "e40370a3",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateInlineBotCallbackQuery",
            "cid": "691e9052",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "msg_id",
                    "type": "InputBotInlineMessageID"
                },
                {
                    "name": "chat_instance",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "flags.0?bytes"
                },
                {
                    "name": "game_short_name",
                    "type": "flags.1?string"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadChannelOutbox",
            "cid": "b75f99a9",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "max_id",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDraftMessage",
            "cid": "1b49ec6d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "draft",
                    "type": "DraftMessage"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadFeaturedStickers",
            "cid": "571d2742",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateRecentStickers",
            "cid": "9a422c20",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateConfig",
            "cid": "a229dd06",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updatePtsChanged",
            "cid": "3354678f",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateChannelWebPage",
            "cid": "2f2ba99f",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "webpage",
                    "type": "WebPage"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDialogPinned",
            "cid": "6e6fe51c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.0?true"
                },
                {
                    "name": "folder_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "peer",
                    "type": "DialogPeer"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePinnedDialogs",
            "cid": "fa0f3ca2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "folder_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "order",
                    "type": "flags.0?Vector<DialogPeer>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotWebhookJSON",
            "cid": "8317c0c3",
            "params": [
                {
                    "name": "data",
                    "type": "DataJSON"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotWebhookJSONQuery",
            "cid": "9b9240a6",
            "params": [
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "DataJSON"
                },
                {
                    "name": "timeout",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotShippingQuery",
            "cid": "b5aefd7d",
            "params": [
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "payload",
                    "type": "bytes"
                },
                {
                    "name": "shipping_address",
                    "type": "PostAddress"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotPrecheckoutQuery",
            "cid": "8caa9a96",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "payload",
                    "type": "bytes"
                },
                {
                    "name": "info",
                    "type": "flags.0?PaymentRequestedInfo"
                },
                {
                    "name": "shipping_option_id",
                    "type": "flags.1?string"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "total_amount",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePhoneCall",
            "cid": "ab0f6b1e",
            "params": [
                {
                    "name": "phone_call",
                    "type": "PhoneCall"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateLangPackTooLong",
            "cid": "46560264",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateLangPack",
            "cid": "56022f4d",
            "params": [
                {
                    "name": "difference",
                    "type": "LangPackDifference"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateFavedStickers",
            "cid": "e511996d",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateChannelReadMessagesContents",
            "cid": "ea29055d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "messages",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateContactsReset",
            "cid": "7084a7be",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateChannelAvailableMessages",
            "cid": "b23fc698",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "available_min_id",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDialogUnreadMark",
            "cid": "e16459c3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "unread",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "DialogPeer"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateMessagePoll",
            "cid": "aca1657b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "poll_id",
                    "type": "long"
                },
                {
                    "name": "poll",
                    "type": "flags.0?Poll"
                },
                {
                    "name": "results",
                    "type": "PollResults"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatDefaultBannedRights",
            "cid": "54c01850",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "default_banned_rights",
                    "type": "ChatBannedRights"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateFolderPeers",
            "cid": "19360dc0",
            "params": [
                {
                    "name": "folder_peers",
                    "type": "Vector<FolderPeer>"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePeerSettings",
            "cid": "6a7e7366",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "settings",
                    "type": "PeerSettings"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePeerLocated",
            "cid": "b4afcfb0",
            "params": [
                {
                    "name": "peers",
                    "type": "Vector<PeerLocated>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateNewScheduledMessage",
            "cid": "39a51dfb",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDeleteScheduledMessages",
            "cid": "90866cee",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "messages",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateTheme",
            "cid": "8216fba3",
            "params": [
                {
                    "name": "theme",
                    "type": "Theme"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateGeoLiveViewed",
            "cid": "871fb939",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateLoginToken",
            "cid": "564fe691",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateMessagePollVote",
            "cid": "106395c9",
            "params": [
                {
                    "name": "poll_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "options",
                    "type": "Vector<bytes>"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDialogFilter",
            "cid": "26ffde7d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "filter",
                    "type": "flags.0?DialogFilter"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDialogFilterOrder",
            "cid": "a5d72105",
            "params": [
                {
                    "name": "order",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateDialogFilters",
            "cid": "3504914f",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updatePhoneCallSignalingData",
            "cid": "2661bf09",
            "params": [
                {
                    "name": "phone_call_id",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "bytes"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelMessageForwards",
            "cid": "d29a27f4",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "forwards",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadChannelDiscussionInbox",
            "cid": "d6b19546",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "top_msg_id",
                    "type": "int"
                },
                {
                    "name": "read_max_id",
                    "type": "int"
                },
                {
                    "name": "broadcast_id",
                    "type": "flags.0?long"
                },
                {
                    "name": "broadcast_post",
                    "type": "flags.0?int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadChannelDiscussionOutbox",
            "cid": "695c9e7c",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "top_msg_id",
                    "type": "int"
                },
                {
                    "name": "read_max_id",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePeerBlocked",
            "cid": "246a4b22",
            "params": [
                {
                    "name": "peer_id",
                    "type": "Peer"
                },
                {
                    "name": "blocked",
                    "type": "Bool"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelUserTyping",
            "cid": "8c88c923",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "from_id",
                    "type": "Peer"
                },
                {
                    "name": "action",
                    "type": "SendMessageAction"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePinnedMessages",
            "cid": "ed85eab5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "messages",
                    "type": "Vector<int>"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePinnedChannelMessages",
            "cid": "5bb98608",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "messages",
                    "type": "Vector<int>"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChat",
            "cid": "f89a6a4e",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateGroupCallParticipants",
            "cid": "f2ebdb4e",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "participants",
                    "type": "Vector<GroupCallParticipant>"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateGroupCall",
            "cid": "14b24500",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "call",
                    "type": "GroupCall"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePeerHistoryTTL",
            "cid": "bb9bb9a5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.0?int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChatParticipant",
            "cid": "d087663a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "actor_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "prev_participant",
                    "type": "flags.0?ChatParticipant"
                },
                {
                    "name": "new_participant",
                    "type": "flags.1?ChatParticipant"
                },
                {
                    "name": "invite",
                    "type": "flags.2?ExportedChatInvite"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelParticipant",
            "cid": "985d3abb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "actor_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "prev_participant",
                    "type": "flags.0?ChannelParticipant"
                },
                {
                    "name": "new_participant",
                    "type": "flags.1?ChannelParticipant"
                },
                {
                    "name": "invite",
                    "type": "flags.2?ExportedChatInvite"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotStopped",
            "cid": "c4870a49",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "stopped",
                    "type": "Bool"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateGroupCallConnection",
            "cid": "b783982",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "presentation",
                    "type": "flags.0?true"
                },
                {
                    "name": "params",
                    "type": "DataJSON"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotCommands",
            "cid": "4d712f2e",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "commands",
                    "type": "Vector<BotCommand>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updatePendingJoinRequests",
            "cid": "7063c3db",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "requests_pending",
                    "type": "int"
                },
                {
                    "name": "recent_requesters",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotChatInviteRequester",
            "cid": "11dfa986",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "about",
                    "type": "string"
                },
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateMessageReactions",
            "cid": "5e1b3cb8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "reactions",
                    "type": "MessageReactions"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateAttachMenuBots",
            "cid": "17b7a20b",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateWebViewResultSent",
            "cid": "1592b79d",
            "params": [
                {
                    "name": "query_id",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateBotMenuButton",
            "cid": "14b85813",
            "params": [
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "button",
                    "type": "BotMenuButton"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateSavedRingtones",
            "cid": "74d8be99",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateTranscribedAudio",
            "cid": "84cd5a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pending",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "transcription_id",
                    "type": "long"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateReadFeaturedEmojiStickers",
            "cid": "fb4c496c",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateUserEmojiStatus",
            "cid": "28373599",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "emoji_status",
                    "type": "EmojiStatus"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateRecentEmojiStatuses",
            "cid": "30f443db",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateRecentReactions",
            "cid": "6f7863f4",
            "params": [],
            "ret": "Update"
        },
        {
            "_": "updateMoveStickerSetToTop",
            "cid": "86fccf85",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "masks",
                    "type": "flags.0?true"
                },
                {
                    "name": "emojis",
                    "type": "flags.1?true"
                },
                {
                    "name": "stickerset",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateMessageExtendedMedia",
            "cid": "5a73a98c",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "extended_media",
                    "type": "MessageExtendedMedia"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelPinnedTopic",
            "cid": "192efbe3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "topic_id",
                    "type": "int"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateChannelPinnedTopics",
            "cid": "fe198602",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "order",
                    "type": "flags.0?Vector<int>"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "updateUser",
            "cid": "20529438",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "Update"
        },
        {
            "_": "state",
            "cid": "a56c2a3e",
            "params": [
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "qts",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "seq",
                    "type": "int"
                },
                {
                    "name": "unread_count",
                    "type": "int"
                }
            ],
            "ret": "updates.State"
        },
        {
            "_": "differenceEmpty",
            "cid": "5d75a138",
            "params": [
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "seq",
                    "type": "int"
                }
            ],
            "ret": "updates.Difference"
        },
        {
            "_": "difference",
            "cid": "f49ca0",
            "params": [
                {
                    "name": "new_messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "new_encrypted_messages",
                    "type": "Vector<EncryptedMessage>"
                },
                {
                    "name": "other_updates",
                    "type": "Vector<Update>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "state",
                    "type": "updates.State"
                }
            ],
            "ret": "updates.Difference"
        },
        {
            "_": "differenceSlice",
            "cid": "a8fb1981",
            "params": [
                {
                    "name": "new_messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "new_encrypted_messages",
                    "type": "Vector<EncryptedMessage>"
                },
                {
                    "name": "other_updates",
                    "type": "Vector<Update>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "intermediate_state",
                    "type": "updates.State"
                }
            ],
            "ret": "updates.Difference"
        },
        {
            "_": "differenceTooLong",
            "cid": "4afe8f6d",
            "params": [
                {
                    "name": "pts",
                    "type": "int"
                }
            ],
            "ret": "updates.Difference"
        },
        {
            "_": "updatesTooLong",
            "cid": "e317af7e",
            "params": [],
            "ret": "Updates"
        },
        {
            "_": "updateShortMessage",
            "cid": "313bc7f8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "out",
                    "type": "flags.1?true"
                },
                {
                    "name": "mentioned",
                    "type": "flags.4?true"
                },
                {
                    "name": "media_unread",
                    "type": "flags.5?true"
                },
                {
                    "name": "silent",
                    "type": "flags.13?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "fwd_from",
                    "type": "flags.2?MessageFwdHeader"
                },
                {
                    "name": "via_bot_id",
                    "type": "flags.11?long"
                },
                {
                    "name": "reply_to",
                    "type": "flags.3?MessageReplyHeader"
                },
                {
                    "name": "entities",
                    "type": "flags.7?Vector<MessageEntity>"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.25?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "updateShortChatMessage",
            "cid": "4d6deea5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "out",
                    "type": "flags.1?true"
                },
                {
                    "name": "mentioned",
                    "type": "flags.4?true"
                },
                {
                    "name": "media_unread",
                    "type": "flags.5?true"
                },
                {
                    "name": "silent",
                    "type": "flags.13?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "from_id",
                    "type": "long"
                },
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "fwd_from",
                    "type": "flags.2?MessageFwdHeader"
                },
                {
                    "name": "via_bot_id",
                    "type": "flags.11?long"
                },
                {
                    "name": "reply_to",
                    "type": "flags.3?MessageReplyHeader"
                },
                {
                    "name": "entities",
                    "type": "flags.7?Vector<MessageEntity>"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.25?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "updateShort",
            "cid": "78d4dec1",
            "params": [
                {
                    "name": "update",
                    "type": "Update"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "updatesCombined",
            "cid": "725b04c3",
            "params": [
                {
                    "name": "updates",
                    "type": "Vector<Update>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "seq_start",
                    "type": "int"
                },
                {
                    "name": "seq",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "updates",
            "cid": "74ae4240",
            "params": [
                {
                    "name": "updates",
                    "type": "Vector<Update>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "seq",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "updateShortSentMessage",
            "cid": "9015e101",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "out",
                    "type": "flags.1?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "media",
                    "type": "flags.9?MessageMedia"
                },
                {
                    "name": "entities",
                    "type": "flags.7?Vector<MessageEntity>"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.25?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "photos",
            "cid": "8dca6aa5",
            "params": [
                {
                    "name": "photos",
                    "type": "Vector<Photo>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "photos.Photos"
        },
        {
            "_": "photosSlice",
            "cid": "15051f54",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "photos",
                    "type": "Vector<Photo>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "photos.Photos"
        },
        {
            "_": "photo",
            "cid": "20212ca8",
            "params": [
                {
                    "name": "photo",
                    "type": "Photo"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "photos.Photo"
        },
        {
            "_": "file",
            "cid": "96a18d5",
            "params": [
                {
                    "name": "type",
                    "type": "storage.FileType"
                },
                {
                    "name": "mtime",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "upload.File"
        },
        {
            "_": "fileCdnRedirect",
            "cid": "f18cda44",
            "params": [
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "file_token",
                    "type": "bytes"
                },
                {
                    "name": "encryption_key",
                    "type": "bytes"
                },
                {
                    "name": "encryption_iv",
                    "type": "bytes"
                },
                {
                    "name": "file_hashes",
                    "type": "Vector<FileHash>"
                }
            ],
            "ret": "upload.File"
        },
        {
            "_": "dcOption",
            "cid": "18b7a10d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "ipv6",
                    "type": "flags.0?true"
                },
                {
                    "name": "media_only",
                    "type": "flags.1?true"
                },
                {
                    "name": "tcpo_only",
                    "type": "flags.2?true"
                },
                {
                    "name": "cdn",
                    "type": "flags.3?true"
                },
                {
                    "name": "static",
                    "type": "flags.4?true"
                },
                {
                    "name": "this_port_only",
                    "type": "flags.5?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "ip_address",
                    "type": "string"
                },
                {
                    "name": "port",
                    "type": "int"
                },
                {
                    "name": "secret",
                    "type": "flags.10?bytes"
                }
            ],
            "ret": "DcOption"
        },
        {
            "_": "config",
            "cid": "232566ac",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "phonecalls_enabled",
                    "type": "flags.1?true"
                },
                {
                    "name": "default_p2p_contacts",
                    "type": "flags.3?true"
                },
                {
                    "name": "preload_featured_stickers",
                    "type": "flags.4?true"
                },
                {
                    "name": "ignore_phone_entities",
                    "type": "flags.5?true"
                },
                {
                    "name": "revoke_pm_inbox",
                    "type": "flags.6?true"
                },
                {
                    "name": "blocked_mode",
                    "type": "flags.8?true"
                },
                {
                    "name": "pfs_enabled",
                    "type": "flags.13?true"
                },
                {
                    "name": "force_try_ipv6",
                    "type": "flags.14?true"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "expires",
                    "type": "int"
                },
                {
                    "name": "test_mode",
                    "type": "Bool"
                },
                {
                    "name": "this_dc",
                    "type": "int"
                },
                {
                    "name": "dc_options",
                    "type": "Vector<DcOption>"
                },
                {
                    "name": "dc_txt_domain_name",
                    "type": "string"
                },
                {
                    "name": "chat_size_max",
                    "type": "int"
                },
                {
                    "name": "megagroup_size_max",
                    "type": "int"
                },
                {
                    "name": "forwarded_count_max",
                    "type": "int"
                },
                {
                    "name": "online_update_period_ms",
                    "type": "int"
                },
                {
                    "name": "offline_blur_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "offline_idle_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "online_cloud_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "notify_cloud_delay_ms",
                    "type": "int"
                },
                {
                    "name": "notify_default_delay_ms",
                    "type": "int"
                },
                {
                    "name": "push_chat_period_ms",
                    "type": "int"
                },
                {
                    "name": "push_chat_limit",
                    "type": "int"
                },
                {
                    "name": "saved_gifs_limit",
                    "type": "int"
                },
                {
                    "name": "edit_time_limit",
                    "type": "int"
                },
                {
                    "name": "revoke_time_limit",
                    "type": "int"
                },
                {
                    "name": "revoke_pm_time_limit",
                    "type": "int"
                },
                {
                    "name": "rating_e_decay",
                    "type": "int"
                },
                {
                    "name": "stickers_recent_limit",
                    "type": "int"
                },
                {
                    "name": "stickers_faved_limit",
                    "type": "int"
                },
                {
                    "name": "channels_read_media_period",
                    "type": "int"
                },
                {
                    "name": "tmp_sessions",
                    "type": "flags.0?int"
                },
                {
                    "name": "pinned_dialogs_count_max",
                    "type": "int"
                },
                {
                    "name": "pinned_infolder_count_max",
                    "type": "int"
                },
                {
                    "name": "call_receive_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "call_ring_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "call_connect_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "call_packet_timeout_ms",
                    "type": "int"
                },
                {
                    "name": "me_url_prefix",
                    "type": "string"
                },
                {
                    "name": "autoupdate_url_prefix",
                    "type": "flags.7?string"
                },
                {
                    "name": "gif_search_username",
                    "type": "flags.9?string"
                },
                {
                    "name": "venue_search_username",
                    "type": "flags.10?string"
                },
                {
                    "name": "img_search_username",
                    "type": "flags.11?string"
                },
                {
                    "name": "static_maps_provider",
                    "type": "flags.12?string"
                },
                {
                    "name": "caption_length_max",
                    "type": "int"
                },
                {
                    "name": "message_length_max",
                    "type": "int"
                },
                {
                    "name": "webfile_dc_id",
                    "type": "int"
                },
                {
                    "name": "suggested_lang_code",
                    "type": "flags.2?string"
                },
                {
                    "name": "lang_pack_version",
                    "type": "flags.2?int"
                },
                {
                    "name": "base_lang_pack_version",
                    "type": "flags.2?int"
                },
                {
                    "name": "reactions_default",
                    "type": "flags.15?Reaction"
                }
            ],
            "ret": "Config"
        },
        {
            "_": "nearestDc",
            "cid": "8e1a1775",
            "params": [
                {
                    "name": "country",
                    "type": "string"
                },
                {
                    "name": "this_dc",
                    "type": "int"
                },
                {
                    "name": "nearest_dc",
                    "type": "int"
                }
            ],
            "ret": "NearestDc"
        },
        {
            "_": "appUpdate",
            "cid": "ccbbce30",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "can_not_skip",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "version",
                    "type": "string"
                },
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "Vector<MessageEntity>"
                },
                {
                    "name": "document",
                    "type": "flags.1?Document"
                },
                {
                    "name": "url",
                    "type": "flags.2?string"
                },
                {
                    "name": "sticker",
                    "type": "flags.3?Document"
                }
            ],
            "ret": "help.AppUpdate"
        },
        {
            "_": "noAppUpdate",
            "cid": "c45a6536",
            "params": [],
            "ret": "help.AppUpdate"
        },
        {
            "_": "inviteText",
            "cid": "18cb9f78",
            "params": [
                {
                    "name": "message",
                    "type": "string"
                }
            ],
            "ret": "help.InviteText"
        },
        {
            "_": "encryptedChatEmpty",
            "cid": "ab7ec0a0",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "encryptedChatWaiting",
            "cid": "66b25953",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "encryptedChatRequested",
            "cid": "48f1d94c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "folder_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                },
                {
                    "name": "g_a",
                    "type": "bytes"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "encryptedChat",
            "cid": "61f0d4c7",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                },
                {
                    "name": "g_a_or_b",
                    "type": "bytes"
                },
                {
                    "name": "key_fingerprint",
                    "type": "long"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "encryptedChatDiscarded",
            "cid": "1e1c7c45",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "history_deleted",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "inputEncryptedChat",
            "cid": "f141b5e1",
            "params": [
                {
                    "name": "chat_id",
                    "type": "int"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputEncryptedChat"
        },
        {
            "_": "encryptedFileEmpty",
            "cid": "c21f497e",
            "params": [],
            "ret": "EncryptedFile"
        },
        {
            "_": "encryptedFile",
            "cid": "a8008cd8",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "size",
                    "type": "long"
                },
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "key_fingerprint",
                    "type": "int"
                }
            ],
            "ret": "EncryptedFile"
        },
        {
            "_": "inputEncryptedFileEmpty",
            "cid": "1837c364",
            "params": [],
            "ret": "InputEncryptedFile"
        },
        {
            "_": "inputEncryptedFileUploaded",
            "cid": "64bd0306",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "parts",
                    "type": "int"
                },
                {
                    "name": "md5_checksum",
                    "type": "string"
                },
                {
                    "name": "key_fingerprint",
                    "type": "int"
                }
            ],
            "ret": "InputEncryptedFile"
        },
        {
            "_": "inputEncryptedFile",
            "cid": "5a17b5e5",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputEncryptedFile"
        },
        {
            "_": "inputEncryptedFileBigUploaded",
            "cid": "2dc173c8",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "parts",
                    "type": "int"
                },
                {
                    "name": "key_fingerprint",
                    "type": "int"
                }
            ],
            "ret": "InputEncryptedFile"
        },
        {
            "_": "encryptedMessage",
            "cid": "ed18c118",
            "params": [
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "chat_id",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                },
                {
                    "name": "file",
                    "type": "EncryptedFile"
                }
            ],
            "ret": "EncryptedMessage"
        },
        {
            "_": "encryptedMessageService",
            "cid": "23734b06",
            "params": [
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "chat_id",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "EncryptedMessage"
        },
        {
            "_": "dhConfigNotModified",
            "cid": "c0e24635",
            "params": [
                {
                    "name": "random",
                    "type": "bytes"
                }
            ],
            "ret": "messages.DhConfig"
        },
        {
            "_": "dhConfig",
            "cid": "2c221edd",
            "params": [
                {
                    "name": "g",
                    "type": "int"
                },
                {
                    "name": "p",
                    "type": "bytes"
                },
                {
                    "name": "version",
                    "type": "int"
                },
                {
                    "name": "random",
                    "type": "bytes"
                }
            ],
            "ret": "messages.DhConfig"
        },
        {
            "_": "sentEncryptedMessage",
            "cid": "560f8935",
            "params": [
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "messages.SentEncryptedMessage"
        },
        {
            "_": "sentEncryptedFile",
            "cid": "9493ff32",
            "params": [
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "file",
                    "type": "EncryptedFile"
                }
            ],
            "ret": "messages.SentEncryptedMessage"
        },
        {
            "_": "inputDocumentEmpty",
            "cid": "72f0eaae",
            "params": [],
            "ret": "InputDocument"
        },
        {
            "_": "inputDocument",
            "cid": "1abfb575",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                }
            ],
            "ret": "InputDocument"
        },
        {
            "_": "documentEmpty",
            "cid": "36f8c871",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "Document"
        },
        {
            "_": "document",
            "cid": "8fd4c4d8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "file_reference",
                    "type": "bytes"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "size",
                    "type": "long"
                },
                {
                    "name": "thumbs",
                    "type": "flags.0?Vector<PhotoSize>"
                },
                {
                    "name": "video_thumbs",
                    "type": "flags.1?Vector<VideoSize>"
                },
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "attributes",
                    "type": "Vector<DocumentAttribute>"
                }
            ],
            "ret": "Document"
        },
        {
            "_": "support",
            "cid": "17c6b5f6",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "user",
                    "type": "User"
                }
            ],
            "ret": "help.Support"
        },
        {
            "_": "notifyPeer",
            "cid": "9fd40bd8",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                }
            ],
            "ret": "NotifyPeer"
        },
        {
            "_": "notifyUsers",
            "cid": "b4c83b4c",
            "params": [],
            "ret": "NotifyPeer"
        },
        {
            "_": "notifyChats",
            "cid": "c007cec3",
            "params": [],
            "ret": "NotifyPeer"
        },
        {
            "_": "notifyBroadcasts",
            "cid": "d612e8ef",
            "params": [],
            "ret": "NotifyPeer"
        },
        {
            "_": "notifyForumTopic",
            "cid": "226e6308",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "top_msg_id",
                    "type": "int"
                }
            ],
            "ret": "NotifyPeer"
        },
        {
            "_": "sendMessageTypingAction",
            "cid": "16bf744e",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageCancelAction",
            "cid": "fd5ec8f5",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageRecordVideoAction",
            "cid": "a187d66f",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageUploadVideoAction",
            "cid": "e9763aec",
            "params": [
                {
                    "name": "progress",
                    "type": "int"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageRecordAudioAction",
            "cid": "d52f73f7",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageUploadAudioAction",
            "cid": "f351d7ab",
            "params": [
                {
                    "name": "progress",
                    "type": "int"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageUploadPhotoAction",
            "cid": "d1d34a26",
            "params": [
                {
                    "name": "progress",
                    "type": "int"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageUploadDocumentAction",
            "cid": "aa0cd9e4",
            "params": [
                {
                    "name": "progress",
                    "type": "int"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageGeoLocationAction",
            "cid": "176f8ba1",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageChooseContactAction",
            "cid": "628cbc6f",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageGamePlayAction",
            "cid": "dd6a8f48",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageRecordRoundAction",
            "cid": "88f27fbc",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageUploadRoundAction",
            "cid": "243e1c66",
            "params": [
                {
                    "name": "progress",
                    "type": "int"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "speakingInGroupCallAction",
            "cid": "d92c2285",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageHistoryImportAction",
            "cid": "dbda9246",
            "params": [
                {
                    "name": "progress",
                    "type": "int"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageChooseStickerAction",
            "cid": "b05ac6b1",
            "params": [],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageEmojiInteraction",
            "cid": "25972bcb",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "interaction",
                    "type": "DataJSON"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "sendMessageEmojiInteractionSeen",
            "cid": "b665902e",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "SendMessageAction"
        },
        {
            "_": "found",
            "cid": "b3134d9d",
            "params": [
                {
                    "name": "my_results",
                    "type": "Vector<Peer>"
                },
                {
                    "name": "results",
                    "type": "Vector<Peer>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.Found"
        },
        {
            "_": "inputPrivacyKeyStatusTimestamp",
            "cid": "4f96cb18",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyChatInvite",
            "cid": "bdfb0426",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyPhoneCall",
            "cid": "fabadc5f",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyPhoneP2P",
            "cid": "db9e70d2",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyForwards",
            "cid": "a4dd4c08",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyProfilePhoto",
            "cid": "5719bacc",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyPhoneNumber",
            "cid": "352dafa",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyAddedByPhone",
            "cid": "d1219bdd",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "inputPrivacyKeyVoiceMessages",
            "cid": "aee69d68",
            "params": [],
            "ret": "InputPrivacyKey"
        },
        {
            "_": "privacyKeyStatusTimestamp",
            "cid": "bc2eab30",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyChatInvite",
            "cid": "500e6dfa",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyPhoneCall",
            "cid": "3d662b7b",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyPhoneP2P",
            "cid": "39491cc8",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyForwards",
            "cid": "69ec56a3",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyProfilePhoto",
            "cid": "96151fed",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyPhoneNumber",
            "cid": "d19ae46d",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyAddedByPhone",
            "cid": "42ffd42b",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "privacyKeyVoiceMessages",
            "cid": "697f414",
            "params": [],
            "ret": "PrivacyKey"
        },
        {
            "_": "inputPrivacyValueAllowContacts",
            "cid": "d09e07b",
            "params": [],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueAllowAll",
            "cid": "184b35ce",
            "params": [],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueAllowUsers",
            "cid": "131cc67f",
            "params": [
                {
                    "name": "users",
                    "type": "Vector<InputUser>"
                }
            ],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueDisallowContacts",
            "cid": "ba52007",
            "params": [],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueDisallowAll",
            "cid": "d66b66c9",
            "params": [],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueDisallowUsers",
            "cid": "90110467",
            "params": [
                {
                    "name": "users",
                    "type": "Vector<InputUser>"
                }
            ],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueAllowChatParticipants",
            "cid": "840649cf",
            "params": [
                {
                    "name": "chats",
                    "type": "Vector<long>"
                }
            ],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "inputPrivacyValueDisallowChatParticipants",
            "cid": "e94f0f86",
            "params": [
                {
                    "name": "chats",
                    "type": "Vector<long>"
                }
            ],
            "ret": "InputPrivacyRule"
        },
        {
            "_": "privacyValueAllowContacts",
            "cid": "fffe1bac",
            "params": [],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueAllowAll",
            "cid": "65427b82",
            "params": [],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueAllowUsers",
            "cid": "b8905fb2",
            "params": [
                {
                    "name": "users",
                    "type": "Vector<long>"
                }
            ],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueDisallowContacts",
            "cid": "f888fa1a",
            "params": [],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueDisallowAll",
            "cid": "8b73e763",
            "params": [],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueDisallowUsers",
            "cid": "e4621141",
            "params": [
                {
                    "name": "users",
                    "type": "Vector<long>"
                }
            ],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueAllowChatParticipants",
            "cid": "6b134e8e",
            "params": [
                {
                    "name": "chats",
                    "type": "Vector<long>"
                }
            ],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyValueDisallowChatParticipants",
            "cid": "41c87565",
            "params": [
                {
                    "name": "chats",
                    "type": "Vector<long>"
                }
            ],
            "ret": "PrivacyRule"
        },
        {
            "_": "privacyRules",
            "cid": "50a04e45",
            "params": [
                {
                    "name": "rules",
                    "type": "Vector<PrivacyRule>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "account.PrivacyRules"
        },
        {
            "_": "accountDaysTTL",
            "cid": "b8d0afdf",
            "params": [
                {
                    "name": "days",
                    "type": "int"
                }
            ],
            "ret": "AccountDaysTTL"
        },
        {
            "_": "documentAttributeImageSize",
            "cid": "6c37c15c",
            "params": [
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                }
            ],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeAnimated",
            "cid": "11b58939",
            "params": [],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeSticker",
            "cid": "6319d612",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "mask",
                    "type": "flags.1?true"
                },
                {
                    "name": "alt",
                    "type": "string"
                },
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "mask_coords",
                    "type": "flags.0?MaskCoords"
                }
            ],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeVideo",
            "cid": "ef02ce6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "round_message",
                    "type": "flags.0?true"
                },
                {
                    "name": "supports_streaming",
                    "type": "flags.1?true"
                },
                {
                    "name": "duration",
                    "type": "int"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                }
            ],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeAudio",
            "cid": "9852f9c6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "voice",
                    "type": "flags.10?true"
                },
                {
                    "name": "duration",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "flags.0?string"
                },
                {
                    "name": "performer",
                    "type": "flags.1?string"
                },
                {
                    "name": "waveform",
                    "type": "flags.2?bytes"
                }
            ],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeFilename",
            "cid": "15590068",
            "params": [
                {
                    "name": "file_name",
                    "type": "string"
                }
            ],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeHasStickers",
            "cid": "9801d2f7",
            "params": [],
            "ret": "DocumentAttribute"
        },
        {
            "_": "documentAttributeCustomEmoji",
            "cid": "fd149899",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "free",
                    "type": "flags.0?true"
                },
                {
                    "name": "text_color",
                    "type": "flags.1?true"
                },
                {
                    "name": "alt",
                    "type": "string"
                },
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                }
            ],
            "ret": "DocumentAttribute"
        },
        {
            "_": "stickersNotModified",
            "cid": "f1749a22",
            "params": [],
            "ret": "messages.Stickers"
        },
        {
            "_": "stickers",
            "cid": "30a6ec7e",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "stickers",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "messages.Stickers"
        },
        {
            "_": "stickerPack",
            "cid": "12b299d4",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                },
                {
                    "name": "documents",
                    "type": "Vector<long>"
                }
            ],
            "ret": "StickerPack"
        },
        {
            "_": "allStickersNotModified",
            "cid": "e86602c3",
            "params": [],
            "ret": "messages.AllStickers"
        },
        {
            "_": "allStickers",
            "cid": "cdbbcebb",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "sets",
                    "type": "Vector<StickerSet>"
                }
            ],
            "ret": "messages.AllStickers"
        },
        {
            "_": "affectedMessages",
            "cid": "84d19185",
            "params": [
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                }
            ],
            "ret": "messages.AffectedMessages"
        },
        {
            "_": "webPageEmpty",
            "cid": "eb1477e8",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "WebPage"
        },
        {
            "_": "webPagePending",
            "cid": "c586da1c",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "WebPage"
        },
        {
            "_": "webPage",
            "cid": "e89c45b2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "display_url",
                    "type": "string"
                },
                {
                    "name": "hash",
                    "type": "int"
                },
                {
                    "name": "type",
                    "type": "flags.0?string"
                },
                {
                    "name": "site_name",
                    "type": "flags.1?string"
                },
                {
                    "name": "title",
                    "type": "flags.2?string"
                },
                {
                    "name": "description",
                    "type": "flags.3?string"
                },
                {
                    "name": "photo",
                    "type": "flags.4?Photo"
                },
                {
                    "name": "embed_url",
                    "type": "flags.5?string"
                },
                {
                    "name": "embed_type",
                    "type": "flags.5?string"
                },
                {
                    "name": "embed_width",
                    "type": "flags.6?int"
                },
                {
                    "name": "embed_height",
                    "type": "flags.6?int"
                },
                {
                    "name": "duration",
                    "type": "flags.7?int"
                },
                {
                    "name": "author",
                    "type": "flags.8?string"
                },
                {
                    "name": "document",
                    "type": "flags.9?Document"
                },
                {
                    "name": "cached_page",
                    "type": "flags.10?Page"
                },
                {
                    "name": "attributes",
                    "type": "flags.12?Vector<WebPageAttribute>"
                }
            ],
            "ret": "WebPage"
        },
        {
            "_": "webPageNotModified",
            "cid": "7311ca11",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "cached_page_views",
                    "type": "flags.0?int"
                }
            ],
            "ret": "WebPage"
        },
        {
            "_": "authorization",
            "cid": "ad01d61d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "current",
                    "type": "flags.0?true"
                },
                {
                    "name": "official_app",
                    "type": "flags.1?true"
                },
                {
                    "name": "password_pending",
                    "type": "flags.2?true"
                },
                {
                    "name": "encrypted_requests_disabled",
                    "type": "flags.3?true"
                },
                {
                    "name": "call_requests_disabled",
                    "type": "flags.4?true"
                },
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "device_model",
                    "type": "string"
                },
                {
                    "name": "platform",
                    "type": "string"
                },
                {
                    "name": "system_version",
                    "type": "string"
                },
                {
                    "name": "api_id",
                    "type": "int"
                },
                {
                    "name": "app_name",
                    "type": "string"
                },
                {
                    "name": "app_version",
                    "type": "string"
                },
                {
                    "name": "date_created",
                    "type": "int"
                },
                {
                    "name": "date_active",
                    "type": "int"
                },
                {
                    "name": "ip",
                    "type": "string"
                },
                {
                    "name": "country",
                    "type": "string"
                },
                {
                    "name": "region",
                    "type": "string"
                }
            ],
            "ret": "Authorization"
        },
        {
            "_": "authorizations",
            "cid": "4bff8ea0",
            "params": [
                {
                    "name": "authorization_ttl_days",
                    "type": "int"
                },
                {
                    "name": "authorizations",
                    "type": "Vector<Authorization>"
                }
            ],
            "ret": "account.Authorizations"
        },
        {
            "_": "password",
            "cid": "957b50fb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "has_recovery",
                    "type": "flags.0?true"
                },
                {
                    "name": "has_secure_values",
                    "type": "flags.1?true"
                },
                {
                    "name": "has_password",
                    "type": "flags.2?true"
                },
                {
                    "name": "current_algo",
                    "type": "flags.2?PasswordKdfAlgo"
                },
                {
                    "name": "srp_B",
                    "type": "flags.2?bytes"
                },
                {
                    "name": "srp_id",
                    "type": "flags.2?long"
                },
                {
                    "name": "hint",
                    "type": "flags.3?string"
                },
                {
                    "name": "email_unconfirmed_pattern",
                    "type": "flags.4?string"
                },
                {
                    "name": "new_algo",
                    "type": "PasswordKdfAlgo"
                },
                {
                    "name": "new_secure_algo",
                    "type": "SecurePasswordKdfAlgo"
                },
                {
                    "name": "secure_random",
                    "type": "bytes"
                },
                {
                    "name": "pending_reset_date",
                    "type": "flags.5?int"
                },
                {
                    "name": "login_email_pattern",
                    "type": "flags.6?string"
                }
            ],
            "ret": "account.Password"
        },
        {
            "_": "passwordSettings",
            "cid": "9a5c33e5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "email",
                    "type": "flags.0?string"
                },
                {
                    "name": "secure_settings",
                    "type": "flags.1?SecureSecretSettings"
                }
            ],
            "ret": "account.PasswordSettings"
        },
        {
            "_": "passwordInputSettings",
            "cid": "c23727c9",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "new_algo",
                    "type": "flags.0?PasswordKdfAlgo"
                },
                {
                    "name": "new_password_hash",
                    "type": "flags.0?bytes"
                },
                {
                    "name": "hint",
                    "type": "flags.0?string"
                },
                {
                    "name": "email",
                    "type": "flags.1?string"
                },
                {
                    "name": "new_secure_settings",
                    "type": "flags.2?SecureSecretSettings"
                }
            ],
            "ret": "account.PasswordInputSettings"
        },
        {
            "_": "passwordRecovery",
            "cid": "137948a5",
            "params": [
                {
                    "name": "email_pattern",
                    "type": "string"
                }
            ],
            "ret": "auth.PasswordRecovery"
        },
        {
            "_": "receivedNotifyMessage",
            "cid": "a384b779",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "flags",
                    "type": "int"
                }
            ],
            "ret": "ReceivedNotifyMessage"
        },
        {
            "_": "chatInviteExported",
            "cid": "ab4a819",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "revoked",
                    "type": "flags.0?true"
                },
                {
                    "name": "permanent",
                    "type": "flags.5?true"
                },
                {
                    "name": "request_needed",
                    "type": "flags.6?true"
                },
                {
                    "name": "link",
                    "type": "string"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "start_date",
                    "type": "flags.4?int"
                },
                {
                    "name": "expire_date",
                    "type": "flags.1?int"
                },
                {
                    "name": "usage_limit",
                    "type": "flags.2?int"
                },
                {
                    "name": "usage",
                    "type": "flags.3?int"
                },
                {
                    "name": "requested",
                    "type": "flags.7?int"
                },
                {
                    "name": "title",
                    "type": "flags.8?string"
                }
            ],
            "ret": "ExportedChatInvite"
        },
        {
            "_": "chatInvitePublicJoinRequests",
            "cid": "ed107ab7",
            "params": [],
            "ret": "ExportedChatInvite"
        },
        {
            "_": "chatInviteAlready",
            "cid": "5a686d7c",
            "params": [
                {
                    "name": "chat",
                    "type": "Chat"
                }
            ],
            "ret": "ChatInvite"
        },
        {
            "_": "chatInvite",
            "cid": "300c44c1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel",
                    "type": "flags.0?true"
                },
                {
                    "name": "broadcast",
                    "type": "flags.1?true"
                },
                {
                    "name": "public",
                    "type": "flags.2?true"
                },
                {
                    "name": "megagroup",
                    "type": "flags.3?true"
                },
                {
                    "name": "request_needed",
                    "type": "flags.6?true"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "about",
                    "type": "flags.5?string"
                },
                {
                    "name": "photo",
                    "type": "Photo"
                },
                {
                    "name": "participants_count",
                    "type": "int"
                },
                {
                    "name": "participants",
                    "type": "flags.4?Vector<User>"
                }
            ],
            "ret": "ChatInvite"
        },
        {
            "_": "chatInvitePeek",
            "cid": "61695cb0",
            "params": [
                {
                    "name": "chat",
                    "type": "Chat"
                },
                {
                    "name": "expires",
                    "type": "int"
                }
            ],
            "ret": "ChatInvite"
        },
        {
            "_": "inputStickerSetEmpty",
            "cid": "ffb62b95",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetID",
            "cid": "9de7a269",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetShortName",
            "cid": "861cc8a0",
            "params": [
                {
                    "name": "short_name",
                    "type": "string"
                }
            ],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetAnimatedEmoji",
            "cid": "28703c8",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetDice",
            "cid": "e67f520e",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetAnimatedEmojiAnimations",
            "cid": "cde3739",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetPremiumGifts",
            "cid": "c88b3b02",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetEmojiGenericAnimations",
            "cid": "4c4d4ce",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetEmojiDefaultStatuses",
            "cid": "29d0f5ee",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "inputStickerSetEmojiDefaultTopicIcons",
            "cid": "44c1f8e9",
            "params": [],
            "ret": "InputStickerSet"
        },
        {
            "_": "stickerSet",
            "cid": "2dd14edc",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "archived",
                    "type": "flags.1?true"
                },
                {
                    "name": "official",
                    "type": "flags.2?true"
                },
                {
                    "name": "masks",
                    "type": "flags.3?true"
                },
                {
                    "name": "animated",
                    "type": "flags.5?true"
                },
                {
                    "name": "videos",
                    "type": "flags.6?true"
                },
                {
                    "name": "emojis",
                    "type": "flags.7?true"
                },
                {
                    "name": "installed_date",
                    "type": "flags.0?int"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "short_name",
                    "type": "string"
                },
                {
                    "name": "thumbs",
                    "type": "flags.4?Vector<PhotoSize>"
                },
                {
                    "name": "thumb_dc_id",
                    "type": "flags.4?int"
                },
                {
                    "name": "thumb_version",
                    "type": "flags.4?int"
                },
                {
                    "name": "thumb_document_id",
                    "type": "flags.8?long"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "StickerSet"
        },
        {
            "_": "stickerSet",
            "cid": "6e153f16",
            "params": [
                {
                    "name": "set",
                    "type": "StickerSet"
                },
                {
                    "name": "packs",
                    "type": "Vector<StickerPack>"
                },
                {
                    "name": "keywords",
                    "type": "Vector<StickerKeyword>"
                },
                {
                    "name": "documents",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "stickerSetNotModified",
            "cid": "d3f924eb",
            "params": [],
            "ret": "messages.StickerSet"
        },
        {
            "_": "botCommand",
            "cid": "c27ac8c7",
            "params": [
                {
                    "name": "command",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                }
            ],
            "ret": "BotCommand"
        },
        {
            "_": "botInfo",
            "cid": "8f300b57",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "user_id",
                    "type": "flags.0?long"
                },
                {
                    "name": "description",
                    "type": "flags.1?string"
                },
                {
                    "name": "description_photo",
                    "type": "flags.4?Photo"
                },
                {
                    "name": "description_document",
                    "type": "flags.5?Document"
                },
                {
                    "name": "commands",
                    "type": "flags.2?Vector<BotCommand>"
                },
                {
                    "name": "menu_button",
                    "type": "flags.3?BotMenuButton"
                }
            ],
            "ret": "BotInfo"
        },
        {
            "_": "keyboardButton",
            "cid": "a2fa4880",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonUrl",
            "cid": "258aff05",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonCallback",
            "cid": "35bbdb6b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "requires_password",
                    "type": "flags.0?true"
                },
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "data",
                    "type": "bytes"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonRequestPhone",
            "cid": "b16a6c29",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonRequestGeoLocation",
            "cid": "fc796b3f",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonSwitchInline",
            "cid": "568a748",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "same_peer",
                    "type": "flags.0?true"
                },
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "query",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonGame",
            "cid": "50f41ccf",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonBuy",
            "cid": "afd93fbb",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonUrlAuth",
            "cid": "10b78d29",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "fwd_text",
                    "type": "flags.0?string"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "button_id",
                    "type": "int"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "inputKeyboardButtonUrlAuth",
            "cid": "d02e7fd4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "request_write_access",
                    "type": "flags.0?true"
                },
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "fwd_text",
                    "type": "flags.1?string"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "bot",
                    "type": "InputUser"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonRequestPoll",
            "cid": "bbc7515d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "quiz",
                    "type": "flags.0?Bool"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "inputKeyboardButtonUserProfile",
            "cid": "e988037b",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonUserProfile",
            "cid": "308660c1",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonWebView",
            "cid": "13767230",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonSimpleWebView",
            "cid": "a0c0505c",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "KeyboardButton"
        },
        {
            "_": "keyboardButtonRow",
            "cid": "77608b83",
            "params": [
                {
                    "name": "buttons",
                    "type": "Vector<KeyboardButton>"
                }
            ],
            "ret": "KeyboardButtonRow"
        },
        {
            "_": "replyKeyboardHide",
            "cid": "a03e5b85",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "selective",
                    "type": "flags.2?true"
                }
            ],
            "ret": "ReplyMarkup"
        },
        {
            "_": "replyKeyboardForceReply",
            "cid": "86b40b08",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "single_use",
                    "type": "flags.1?true"
                },
                {
                    "name": "selective",
                    "type": "flags.2?true"
                },
                {
                    "name": "placeholder",
                    "type": "flags.3?string"
                }
            ],
            "ret": "ReplyMarkup"
        },
        {
            "_": "replyKeyboardMarkup",
            "cid": "85dd99d1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "resize",
                    "type": "flags.0?true"
                },
                {
                    "name": "single_use",
                    "type": "flags.1?true"
                },
                {
                    "name": "selective",
                    "type": "flags.2?true"
                },
                {
                    "name": "persistent",
                    "type": "flags.4?true"
                },
                {
                    "name": "rows",
                    "type": "Vector<KeyboardButtonRow>"
                },
                {
                    "name": "placeholder",
                    "type": "flags.3?string"
                }
            ],
            "ret": "ReplyMarkup"
        },
        {
            "_": "replyInlineMarkup",
            "cid": "48a30254",
            "params": [
                {
                    "name": "rows",
                    "type": "Vector<KeyboardButtonRow>"
                }
            ],
            "ret": "ReplyMarkup"
        },
        {
            "_": "messageEntityUnknown",
            "cid": "bb92ba95",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityMention",
            "cid": "fa04579d",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityHashtag",
            "cid": "6f635b0d",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityBotCommand",
            "cid": "6cef8ac7",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityUrl",
            "cid": "6ed02538",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityEmail",
            "cid": "64e475c2",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityBold",
            "cid": "bd610bc9",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityItalic",
            "cid": "826f8b60",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityCode",
            "cid": "28a20571",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityPre",
            "cid": "73924be0",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                },
                {
                    "name": "language",
                    "type": "string"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityTextUrl",
            "cid": "76a6d327",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                },
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityMentionName",
            "cid": "dc7b1140",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "inputMessageEntityMentionName",
            "cid": "208e68c9",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityPhone",
            "cid": "9b69e34b",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityCashtag",
            "cid": "4c4e743f",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityUnderline",
            "cid": "9c4e7e8b",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityStrike",
            "cid": "bf0693d4",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityBlockquote",
            "cid": "20df5d0",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityBankCard",
            "cid": "761e6af4",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntitySpoiler",
            "cid": "32ca960f",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "messageEntityCustomEmoji",
            "cid": "c8cf05f8",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "length",
                    "type": "int"
                },
                {
                    "name": "document_id",
                    "type": "long"
                }
            ],
            "ret": "MessageEntity"
        },
        {
            "_": "inputChannelEmpty",
            "cid": "ee8c1e86",
            "params": [],
            "ret": "InputChannel"
        },
        {
            "_": "inputChannel",
            "cid": "f35aec28",
            "params": [
                {
                    "name": "channel_id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputChannel"
        },
        {
            "_": "inputChannelFromMessage",
            "cid": "5b934f9d",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "channel_id",
                    "type": "long"
                }
            ],
            "ret": "InputChannel"
        },
        {
            "_": "resolvedPeer",
            "cid": "7f077ad9",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.ResolvedPeer"
        },
        {
            "_": "messageRange",
            "cid": "ae30253",
            "params": [
                {
                    "name": "min_id",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "int"
                }
            ],
            "ret": "MessageRange"
        },
        {
            "_": "channelDifferenceEmpty",
            "cid": "3e11affb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "final",
                    "type": "flags.0?true"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "timeout",
                    "type": "flags.1?int"
                }
            ],
            "ret": "updates.ChannelDifference"
        },
        {
            "_": "channelDifferenceTooLong",
            "cid": "a4bcc6fe",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "final",
                    "type": "flags.0?true"
                },
                {
                    "name": "timeout",
                    "type": "flags.1?int"
                },
                {
                    "name": "dialog",
                    "type": "Dialog"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "updates.ChannelDifference"
        },
        {
            "_": "channelDifference",
            "cid": "2064674e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "final",
                    "type": "flags.0?true"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "timeout",
                    "type": "flags.1?int"
                },
                {
                    "name": "new_messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "other_updates",
                    "type": "Vector<Update>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "updates.ChannelDifference"
        },
        {
            "_": "channelMessagesFilterEmpty",
            "cid": "94d42ee7",
            "params": [],
            "ret": "ChannelMessagesFilter"
        },
        {
            "_": "channelMessagesFilter",
            "cid": "cd77d957",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "exclude_new_messages",
                    "type": "flags.1?true"
                },
                {
                    "name": "ranges",
                    "type": "Vector<MessageRange>"
                }
            ],
            "ret": "ChannelMessagesFilter"
        },
        {
            "_": "channelParticipant",
            "cid": "c00c07c0",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "ChannelParticipant"
        },
        {
            "_": "channelParticipantSelf",
            "cid": "35a8bfa7",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "via_request",
                    "type": "flags.0?true"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "inviter_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "ChannelParticipant"
        },
        {
            "_": "channelParticipantCreator",
            "cid": "2fe601d3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "admin_rights",
                    "type": "ChatAdminRights"
                },
                {
                    "name": "rank",
                    "type": "flags.0?string"
                }
            ],
            "ret": "ChannelParticipant"
        },
        {
            "_": "channelParticipantAdmin",
            "cid": "34c3bb53",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "can_edit",
                    "type": "flags.0?true"
                },
                {
                    "name": "self",
                    "type": "flags.1?true"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "inviter_id",
                    "type": "flags.1?long"
                },
                {
                    "name": "promoted_by",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_rights",
                    "type": "ChatAdminRights"
                },
                {
                    "name": "rank",
                    "type": "flags.2?string"
                }
            ],
            "ret": "ChannelParticipant"
        },
        {
            "_": "channelParticipantBanned",
            "cid": "6df8014e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "left",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "kicked_by",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "banned_rights",
                    "type": "ChatBannedRights"
                }
            ],
            "ret": "ChannelParticipant"
        },
        {
            "_": "channelParticipantLeft",
            "cid": "1b03f006",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                }
            ],
            "ret": "ChannelParticipant"
        },
        {
            "_": "channelParticipantsRecent",
            "cid": "de3f3c79",
            "params": [],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsAdmins",
            "cid": "b4608969",
            "params": [],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsKicked",
            "cid": "a3b54985",
            "params": [
                {
                    "name": "q",
                    "type": "string"
                }
            ],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsBots",
            "cid": "b0d1865b",
            "params": [],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsBanned",
            "cid": "1427a5e1",
            "params": [
                {
                    "name": "q",
                    "type": "string"
                }
            ],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsSearch",
            "cid": "656ac4b",
            "params": [
                {
                    "name": "q",
                    "type": "string"
                }
            ],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsContacts",
            "cid": "bb6ae88d",
            "params": [
                {
                    "name": "q",
                    "type": "string"
                }
            ],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipantsMentions",
            "cid": "e04b5ceb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "q",
                    "type": "flags.0?string"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.1?int"
                }
            ],
            "ret": "ChannelParticipantsFilter"
        },
        {
            "_": "channelParticipants",
            "cid": "9ab0feaf",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "participants",
                    "type": "Vector<ChannelParticipant>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "channels.ChannelParticipants"
        },
        {
            "_": "channelParticipantsNotModified",
            "cid": "f0173fe9",
            "params": [],
            "ret": "channels.ChannelParticipants"
        },
        {
            "_": "channelParticipant",
            "cid": "dfb80317",
            "params": [
                {
                    "name": "participant",
                    "type": "ChannelParticipant"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "channels.ChannelParticipant"
        },
        {
            "_": "termsOfService",
            "cid": "780a0310",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "popup",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "DataJSON"
                },
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "Vector<MessageEntity>"
                },
                {
                    "name": "min_age_confirm",
                    "type": "flags.1?int"
                }
            ],
            "ret": "help.TermsOfService"
        },
        {
            "_": "savedGifsNotModified",
            "cid": "e8025ca2",
            "params": [],
            "ret": "messages.SavedGifs"
        },
        {
            "_": "savedGifs",
            "cid": "84a02a0d",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "gifs",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "messages.SavedGifs"
        },
        {
            "_": "inputBotInlineMessageMediaAuto",
            "cid": "3380c786",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.1?Vector<MessageEntity>"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineMessageText",
            "cid": "3dcd7a87",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.0?true"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.1?Vector<MessageEntity>"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineMessageMediaGeo",
            "cid": "96929a85",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "heading",
                    "type": "flags.0?int"
                },
                {
                    "name": "period",
                    "type": "flags.1?int"
                },
                {
                    "name": "proximity_notification_radius",
                    "type": "flags.3?int"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineMessageMediaVenue",
            "cid": "417bbf11",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "address",
                    "type": "string"
                },
                {
                    "name": "provider",
                    "type": "string"
                },
                {
                    "name": "venue_id",
                    "type": "string"
                },
                {
                    "name": "venue_type",
                    "type": "string"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineMessageMediaContact",
            "cid": "a6edbffd",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "vcard",
                    "type": "string"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineMessageGame",
            "cid": "4b425864",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineMessageMediaInvoice",
            "cid": "d7e78225",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.0?InputWebDocument"
                },
                {
                    "name": "invoice",
                    "type": "Invoice"
                },
                {
                    "name": "payload",
                    "type": "bytes"
                },
                {
                    "name": "provider",
                    "type": "string"
                },
                {
                    "name": "provider_data",
                    "type": "DataJSON"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "InputBotInlineMessage"
        },
        {
            "_": "inputBotInlineResult",
            "cid": "88bf9319",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "flags.1?string"
                },
                {
                    "name": "description",
                    "type": "flags.2?string"
                },
                {
                    "name": "url",
                    "type": "flags.3?string"
                },
                {
                    "name": "thumb",
                    "type": "flags.4?InputWebDocument"
                },
                {
                    "name": "content",
                    "type": "flags.5?InputWebDocument"
                },
                {
                    "name": "send_message",
                    "type": "InputBotInlineMessage"
                }
            ],
            "ret": "InputBotInlineResult"
        },
        {
            "_": "inputBotInlineResultPhoto",
            "cid": "a8d864a7",
            "params": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "InputPhoto"
                },
                {
                    "name": "send_message",
                    "type": "InputBotInlineMessage"
                }
            ],
            "ret": "InputBotInlineResult"
        },
        {
            "_": "inputBotInlineResultDocument",
            "cid": "fff8fdc4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "flags.1?string"
                },
                {
                    "name": "description",
                    "type": "flags.2?string"
                },
                {
                    "name": "document",
                    "type": "InputDocument"
                },
                {
                    "name": "send_message",
                    "type": "InputBotInlineMessage"
                }
            ],
            "ret": "InputBotInlineResult"
        },
        {
            "_": "inputBotInlineResultGame",
            "cid": "4fa417f2",
            "params": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "short_name",
                    "type": "string"
                },
                {
                    "name": "send_message",
                    "type": "InputBotInlineMessage"
                }
            ],
            "ret": "InputBotInlineResult"
        },
        {
            "_": "botInlineMessageMediaAuto",
            "cid": "764cf810",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.1?Vector<MessageEntity>"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "BotInlineMessage"
        },
        {
            "_": "botInlineMessageText",
            "cid": "8c7f65e2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.0?true"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.1?Vector<MessageEntity>"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "BotInlineMessage"
        },
        {
            "_": "botInlineMessageMediaGeo",
            "cid": "51846fd",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "geo",
                    "type": "GeoPoint"
                },
                {
                    "name": "heading",
                    "type": "flags.0?int"
                },
                {
                    "name": "period",
                    "type": "flags.1?int"
                },
                {
                    "name": "proximity_notification_radius",
                    "type": "flags.3?int"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "BotInlineMessage"
        },
        {
            "_": "botInlineMessageMediaVenue",
            "cid": "8a86659c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "geo",
                    "type": "GeoPoint"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "address",
                    "type": "string"
                },
                {
                    "name": "provider",
                    "type": "string"
                },
                {
                    "name": "venue_id",
                    "type": "string"
                },
                {
                    "name": "venue_type",
                    "type": "string"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "BotInlineMessage"
        },
        {
            "_": "botInlineMessageMediaContact",
            "cid": "18d1cdc2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "vcard",
                    "type": "string"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "BotInlineMessage"
        },
        {
            "_": "botInlineMessageMediaInvoice",
            "cid": "354a9b09",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "shipping_address_requested",
                    "type": "flags.1?true"
                },
                {
                    "name": "test",
                    "type": "flags.3?true"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.0?WebDocument"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "total_amount",
                    "type": "long"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                }
            ],
            "ret": "BotInlineMessage"
        },
        {
            "_": "botInlineResult",
            "cid": "11965f3a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "flags.1?string"
                },
                {
                    "name": "description",
                    "type": "flags.2?string"
                },
                {
                    "name": "url",
                    "type": "flags.3?string"
                },
                {
                    "name": "thumb",
                    "type": "flags.4?WebDocument"
                },
                {
                    "name": "content",
                    "type": "flags.5?WebDocument"
                },
                {
                    "name": "send_message",
                    "type": "BotInlineMessage"
                }
            ],
            "ret": "BotInlineResult"
        },
        {
            "_": "botInlineMediaResult",
            "cid": "17db940b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.0?Photo"
                },
                {
                    "name": "document",
                    "type": "flags.1?Document"
                },
                {
                    "name": "title",
                    "type": "flags.2?string"
                },
                {
                    "name": "description",
                    "type": "flags.3?string"
                },
                {
                    "name": "send_message",
                    "type": "BotInlineMessage"
                }
            ],
            "ret": "BotInlineResult"
        },
        {
            "_": "botResults",
            "cid": "947ca848",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "gallery",
                    "type": "flags.0?true"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "next_offset",
                    "type": "flags.1?string"
                },
                {
                    "name": "switch_pm",
                    "type": "flags.2?InlineBotSwitchPM"
                },
                {
                    "name": "results",
                    "type": "Vector<BotInlineResult>"
                },
                {
                    "name": "cache_time",
                    "type": "int"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.BotResults"
        },
        {
            "_": "exportedMessageLink",
            "cid": "5dab1af4",
            "params": [
                {
                    "name": "link",
                    "type": "string"
                },
                {
                    "name": "html",
                    "type": "string"
                }
            ],
            "ret": "ExportedMessageLink"
        },
        {
            "_": "messageFwdHeader",
            "cid": "5f777dce",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "imported",
                    "type": "flags.7?true"
                },
                {
                    "name": "from_id",
                    "type": "flags.0?Peer"
                },
                {
                    "name": "from_name",
                    "type": "flags.5?string"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "channel_post",
                    "type": "flags.2?int"
                },
                {
                    "name": "post_author",
                    "type": "flags.3?string"
                },
                {
                    "name": "saved_from_peer",
                    "type": "flags.4?Peer"
                },
                {
                    "name": "saved_from_msg_id",
                    "type": "flags.4?int"
                },
                {
                    "name": "psa_type",
                    "type": "flags.6?string"
                }
            ],
            "ret": "MessageFwdHeader"
        },
        {
            "_": "codeTypeSms",
            "cid": "72a3158c",
            "params": [],
            "ret": "auth.CodeType"
        },
        {
            "_": "codeTypeCall",
            "cid": "741cd3e3",
            "params": [],
            "ret": "auth.CodeType"
        },
        {
            "_": "codeTypeFlashCall",
            "cid": "226ccefb",
            "params": [],
            "ret": "auth.CodeType"
        },
        {
            "_": "codeTypeMissedCall",
            "cid": "d61ad6ee",
            "params": [],
            "ret": "auth.CodeType"
        },
        {
            "_": "codeTypeFragmentSms",
            "cid": "6ed998c",
            "params": [],
            "ret": "auth.CodeType"
        },
        {
            "_": "sentCodeTypeApp",
            "cid": "3dbb5986",
            "params": [
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeSms",
            "cid": "c000bba2",
            "params": [
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeCall",
            "cid": "5353e5a7",
            "params": [
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeFlashCall",
            "cid": "ab03c6d9",
            "params": [
                {
                    "name": "pattern",
                    "type": "string"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeMissedCall",
            "cid": "82006484",
            "params": [
                {
                    "name": "prefix",
                    "type": "string"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeEmailCode",
            "cid": "5a159841",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "apple_signin_allowed",
                    "type": "flags.0?true"
                },
                {
                    "name": "google_signin_allowed",
                    "type": "flags.1?true"
                },
                {
                    "name": "email_pattern",
                    "type": "string"
                },
                {
                    "name": "length",
                    "type": "int"
                },
                {
                    "name": "next_phone_login_date",
                    "type": "flags.2?int"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeSetUpEmailRequired",
            "cid": "a5491dea",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "apple_signin_allowed",
                    "type": "flags.0?true"
                },
                {
                    "name": "google_signin_allowed",
                    "type": "flags.1?true"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "sentCodeTypeFragmentSms",
            "cid": "d9565c39",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "auth.SentCodeType"
        },
        {
            "_": "botCallbackAnswer",
            "cid": "36585ea4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "alert",
                    "type": "flags.1?true"
                },
                {
                    "name": "has_url",
                    "type": "flags.3?true"
                },
                {
                    "name": "native_ui",
                    "type": "flags.4?true"
                },
                {
                    "name": "message",
                    "type": "flags.0?string"
                },
                {
                    "name": "url",
                    "type": "flags.2?string"
                },
                {
                    "name": "cache_time",
                    "type": "int"
                }
            ],
            "ret": "messages.BotCallbackAnswer"
        },
        {
            "_": "messageEditData",
            "cid": "26b5dde6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "caption",
                    "type": "flags.0?true"
                }
            ],
            "ret": "messages.MessageEditData"
        },
        {
            "_": "inputBotInlineMessageID",
            "cid": "890c3d89",
            "params": [
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputBotInlineMessageID"
        },
        {
            "_": "inputBotInlineMessageID64",
            "cid": "b6d915d7",
            "params": [
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "owner_id",
                    "type": "long"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputBotInlineMessageID"
        },
        {
            "_": "inlineBotSwitchPM",
            "cid": "3c20629f",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "start_param",
                    "type": "string"
                }
            ],
            "ret": "InlineBotSwitchPM"
        },
        {
            "_": "peerDialogs",
            "cid": "3371c354",
            "params": [
                {
                    "name": "dialogs",
                    "type": "Vector<Dialog>"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "state",
                    "type": "updates.State"
                }
            ],
            "ret": "messages.PeerDialogs"
        },
        {
            "_": "topPeer",
            "cid": "edcdc05b",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "rating",
                    "type": "double"
                }
            ],
            "ret": "TopPeer"
        },
        {
            "_": "topPeerCategoryBotsPM",
            "cid": "ab661b5b",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryBotsInline",
            "cid": "148677e2",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryCorrespondents",
            "cid": "637b7ed",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryGroups",
            "cid": "bd17a14a",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryChannels",
            "cid": "161d9628",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryPhoneCalls",
            "cid": "1e76a78c",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryForwardUsers",
            "cid": "a8406ca9",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryForwardChats",
            "cid": "fbeec0f0",
            "params": [],
            "ret": "TopPeerCategory"
        },
        {
            "_": "topPeerCategoryPeers",
            "cid": "fb834291",
            "params": [
                {
                    "name": "category",
                    "type": "TopPeerCategory"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "peers",
                    "type": "Vector<TopPeer>"
                }
            ],
            "ret": "TopPeerCategoryPeers"
        },
        {
            "_": "topPeersNotModified",
            "cid": "de266ef5",
            "params": [],
            "ret": "contacts.TopPeers"
        },
        {
            "_": "topPeers",
            "cid": "70b772a8",
            "params": [
                {
                    "name": "categories",
                    "type": "Vector<TopPeerCategoryPeers>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "contacts.TopPeers"
        },
        {
            "_": "topPeersDisabled",
            "cid": "b52c939d",
            "params": [],
            "ret": "contacts.TopPeers"
        },
        {
            "_": "draftMessageEmpty",
            "cid": "1b0c841a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "date",
                    "type": "flags.0?int"
                }
            ],
            "ret": "DraftMessage"
        },
        {
            "_": "draftMessage",
            "cid": "fd8e711f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.1?true"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "DraftMessage"
        },
        {
            "_": "featuredStickersNotModified",
            "cid": "c6dc0c66",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                }
            ],
            "ret": "messages.FeaturedStickers"
        },
        {
            "_": "featuredStickers",
            "cid": "be382906",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "premium",
                    "type": "flags.0?true"
                },
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "sets",
                    "type": "Vector<StickerSetCovered>"
                },
                {
                    "name": "unread",
                    "type": "Vector<long>"
                }
            ],
            "ret": "messages.FeaturedStickers"
        },
        {
            "_": "recentStickersNotModified",
            "cid": "b17f890",
            "params": [],
            "ret": "messages.RecentStickers"
        },
        {
            "_": "recentStickers",
            "cid": "88d37c56",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "packs",
                    "type": "Vector<StickerPack>"
                },
                {
                    "name": "stickers",
                    "type": "Vector<Document>"
                },
                {
                    "name": "dates",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.RecentStickers"
        },
        {
            "_": "archivedStickers",
            "cid": "4fcba9c8",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "sets",
                    "type": "Vector<StickerSetCovered>"
                }
            ],
            "ret": "messages.ArchivedStickers"
        },
        {
            "_": "stickerSetInstallResultSuccess",
            "cid": "38641628",
            "params": [],
            "ret": "messages.StickerSetInstallResult"
        },
        {
            "_": "stickerSetInstallResultArchive",
            "cid": "35e410a8",
            "params": [
                {
                    "name": "sets",
                    "type": "Vector<StickerSetCovered>"
                }
            ],
            "ret": "messages.StickerSetInstallResult"
        },
        {
            "_": "stickerSetCovered",
            "cid": "6410a5d2",
            "params": [
                {
                    "name": "set",
                    "type": "StickerSet"
                },
                {
                    "name": "cover",
                    "type": "Document"
                }
            ],
            "ret": "StickerSetCovered"
        },
        {
            "_": "stickerSetMultiCovered",
            "cid": "3407e51b",
            "params": [
                {
                    "name": "set",
                    "type": "StickerSet"
                },
                {
                    "name": "covers",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "StickerSetCovered"
        },
        {
            "_": "stickerSetFullCovered",
            "cid": "40d13c0e",
            "params": [
                {
                    "name": "set",
                    "type": "StickerSet"
                },
                {
                    "name": "packs",
                    "type": "Vector<StickerPack>"
                },
                {
                    "name": "keywords",
                    "type": "Vector<StickerKeyword>"
                },
                {
                    "name": "documents",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "StickerSetCovered"
        },
        {
            "_": "stickerSetNoCovered",
            "cid": "77b15d1c",
            "params": [
                {
                    "name": "set",
                    "type": "StickerSet"
                }
            ],
            "ret": "StickerSetCovered"
        },
        {
            "_": "maskCoords",
            "cid": "aed6dbb2",
            "params": [
                {
                    "name": "n",
                    "type": "int"
                },
                {
                    "name": "x",
                    "type": "double"
                },
                {
                    "name": "y",
                    "type": "double"
                },
                {
                    "name": "zoom",
                    "type": "double"
                }
            ],
            "ret": "MaskCoords"
        },
        {
            "_": "inputStickeredMediaPhoto",
            "cid": "4a992157",
            "params": [
                {
                    "name": "id",
                    "type": "InputPhoto"
                }
            ],
            "ret": "InputStickeredMedia"
        },
        {
            "_": "inputStickeredMediaDocument",
            "cid": "438865b",
            "params": [
                {
                    "name": "id",
                    "type": "InputDocument"
                }
            ],
            "ret": "InputStickeredMedia"
        },
        {
            "_": "game",
            "cid": "bdf9653b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "short_name",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "Photo"
                },
                {
                    "name": "document",
                    "type": "flags.0?Document"
                }
            ],
            "ret": "Game"
        },
        {
            "_": "inputGameID",
            "cid": "32c3e77",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputGame"
        },
        {
            "_": "inputGameShortName",
            "cid": "c331e80a",
            "params": [
                {
                    "name": "bot_id",
                    "type": "InputUser"
                },
                {
                    "name": "short_name",
                    "type": "string"
                }
            ],
            "ret": "InputGame"
        },
        {
            "_": "highScore",
            "cid": "73a379eb",
            "params": [
                {
                    "name": "pos",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "score",
                    "type": "int"
                }
            ],
            "ret": "HighScore"
        },
        {
            "_": "highScores",
            "cid": "9a3bfd99",
            "params": [
                {
                    "name": "scores",
                    "type": "Vector<HighScore>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.HighScores"
        },
        {
            "_": "textEmpty",
            "cid": "dc3d824f",
            "params": [],
            "ret": "RichText"
        },
        {
            "_": "textPlain",
            "cid": "744694e0",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textBold",
            "cid": "6724abc4",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textItalic",
            "cid": "d912a59c",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textUnderline",
            "cid": "c12622c4",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textStrike",
            "cid": "9bf8bb95",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textFixed",
            "cid": "6c3f19b9",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textUrl",
            "cid": "3c2884c1",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "webpage_id",
                    "type": "long"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textEmail",
            "cid": "de5a0dd6",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "email",
                    "type": "string"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textConcat",
            "cid": "7e6260d7",
            "params": [
                {
                    "name": "texts",
                    "type": "Vector<RichText>"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textSubscript",
            "cid": "ed6a8504",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textSuperscript",
            "cid": "c7fb5e01",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textMarked",
            "cid": "34b8621",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textPhone",
            "cid": "1ccb966a",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "phone",
                    "type": "string"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textImage",
            "cid": "81ccf4f",
            "params": [
                {
                    "name": "document_id",
                    "type": "long"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "textAnchor",
            "cid": "35553762",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "name",
                    "type": "string"
                }
            ],
            "ret": "RichText"
        },
        {
            "_": "pageBlockUnsupported",
            "cid": "13567e8a",
            "params": [],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockTitle",
            "cid": "70abc3fd",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockSubtitle",
            "cid": "8ffa9a1f",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockAuthorDate",
            "cid": "baafe5e0",
            "params": [
                {
                    "name": "author",
                    "type": "RichText"
                },
                {
                    "name": "published_date",
                    "type": "int"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockHeader",
            "cid": "bfd064ec",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockSubheader",
            "cid": "f12bb6e1",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockParagraph",
            "cid": "467a0766",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockPreformatted",
            "cid": "c070d93e",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "language",
                    "type": "string"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockFooter",
            "cid": "48870999",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockDivider",
            "cid": "db20b188",
            "params": [],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockAnchor",
            "cid": "ce0d37b0",
            "params": [
                {
                    "name": "name",
                    "type": "string"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockList",
            "cid": "e4e88011",
            "params": [
                {
                    "name": "items",
                    "type": "Vector<PageListItem>"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockBlockquote",
            "cid": "263d7c26",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "caption",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockPullquote",
            "cid": "4f4456d3",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "caption",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockPhoto",
            "cid": "1759c560",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "photo_id",
                    "type": "long"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                },
                {
                    "name": "url",
                    "type": "flags.0?string"
                },
                {
                    "name": "webpage_id",
                    "type": "flags.0?long"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockVideo",
            "cid": "7c8fe7b6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "autoplay",
                    "type": "flags.0?true"
                },
                {
                    "name": "loop",
                    "type": "flags.1?true"
                },
                {
                    "name": "video_id",
                    "type": "long"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockCover",
            "cid": "39f23300",
            "params": [
                {
                    "name": "cover",
                    "type": "PageBlock"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockEmbed",
            "cid": "a8718dc5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "full_width",
                    "type": "flags.0?true"
                },
                {
                    "name": "allow_scrolling",
                    "type": "flags.3?true"
                },
                {
                    "name": "url",
                    "type": "flags.1?string"
                },
                {
                    "name": "html",
                    "type": "flags.2?string"
                },
                {
                    "name": "poster_photo_id",
                    "type": "flags.4?long"
                },
                {
                    "name": "w",
                    "type": "flags.5?int"
                },
                {
                    "name": "h",
                    "type": "flags.5?int"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockEmbedPost",
            "cid": "f259a80b",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "webpage_id",
                    "type": "long"
                },
                {
                    "name": "author_photo_id",
                    "type": "long"
                },
                {
                    "name": "author",
                    "type": "string"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "blocks",
                    "type": "Vector<PageBlock>"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockCollage",
            "cid": "65a0fa4d",
            "params": [
                {
                    "name": "items",
                    "type": "Vector<PageBlock>"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockSlideshow",
            "cid": "31f9590",
            "params": [
                {
                    "name": "items",
                    "type": "Vector<PageBlock>"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockChannel",
            "cid": "ef1751b5",
            "params": [
                {
                    "name": "channel",
                    "type": "Chat"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockAudio",
            "cid": "804361ea",
            "params": [
                {
                    "name": "audio_id",
                    "type": "long"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockKicker",
            "cid": "1e148390",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockTable",
            "cid": "bf4dea82",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "bordered",
                    "type": "flags.0?true"
                },
                {
                    "name": "striped",
                    "type": "flags.1?true"
                },
                {
                    "name": "title",
                    "type": "RichText"
                },
                {
                    "name": "rows",
                    "type": "Vector<PageTableRow>"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockOrderedList",
            "cid": "9a8ae1e1",
            "params": [
                {
                    "name": "items",
                    "type": "Vector<PageListOrderedItem>"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockDetails",
            "cid": "76768bed",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "open",
                    "type": "flags.0?true"
                },
                {
                    "name": "blocks",
                    "type": "Vector<PageBlock>"
                },
                {
                    "name": "title",
                    "type": "RichText"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockRelatedArticles",
            "cid": "16115a96",
            "params": [
                {
                    "name": "title",
                    "type": "RichText"
                },
                {
                    "name": "articles",
                    "type": "Vector<PageRelatedArticle>"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "pageBlockMap",
            "cid": "a44f3ef6",
            "params": [
                {
                    "name": "geo",
                    "type": "GeoPoint"
                },
                {
                    "name": "zoom",
                    "type": "int"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                },
                {
                    "name": "caption",
                    "type": "PageCaption"
                }
            ],
            "ret": "PageBlock"
        },
        {
            "_": "phoneCallDiscardReasonMissed",
            "cid": "85e42301",
            "params": [],
            "ret": "PhoneCallDiscardReason"
        },
        {
            "_": "phoneCallDiscardReasonDisconnect",
            "cid": "e095c1a0",
            "params": [],
            "ret": "PhoneCallDiscardReason"
        },
        {
            "_": "phoneCallDiscardReasonHangup",
            "cid": "57adc690",
            "params": [],
            "ret": "PhoneCallDiscardReason"
        },
        {
            "_": "phoneCallDiscardReasonBusy",
            "cid": "faf7e8c9",
            "params": [],
            "ret": "PhoneCallDiscardReason"
        },
        {
            "_": "dataJSON",
            "cid": "7d748d04",
            "params": [
                {
                    "name": "data",
                    "type": "string"
                }
            ],
            "ret": "DataJSON"
        },
        {
            "_": "labeledPrice",
            "cid": "cb296bf8",
            "params": [
                {
                    "name": "label",
                    "type": "string"
                },
                {
                    "name": "amount",
                    "type": "long"
                }
            ],
            "ret": "LabeledPrice"
        },
        {
            "_": "invoice",
            "cid": "3e85a91b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "test",
                    "type": "flags.0?true"
                },
                {
                    "name": "name_requested",
                    "type": "flags.1?true"
                },
                {
                    "name": "phone_requested",
                    "type": "flags.2?true"
                },
                {
                    "name": "email_requested",
                    "type": "flags.3?true"
                },
                {
                    "name": "shipping_address_requested",
                    "type": "flags.4?true"
                },
                {
                    "name": "flexible",
                    "type": "flags.5?true"
                },
                {
                    "name": "phone_to_provider",
                    "type": "flags.6?true"
                },
                {
                    "name": "email_to_provider",
                    "type": "flags.7?true"
                },
                {
                    "name": "recurring",
                    "type": "flags.9?true"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "prices",
                    "type": "Vector<LabeledPrice>"
                },
                {
                    "name": "max_tip_amount",
                    "type": "flags.8?long"
                },
                {
                    "name": "suggested_tip_amounts",
                    "type": "flags.8?Vector<long>"
                },
                {
                    "name": "recurring_terms_url",
                    "type": "flags.9?string"
                }
            ],
            "ret": "Invoice"
        },
        {
            "_": "paymentCharge",
            "cid": "ea02c27e",
            "params": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "provider_charge_id",
                    "type": "string"
                }
            ],
            "ret": "PaymentCharge"
        },
        {
            "_": "postAddress",
            "cid": "1e8caaeb",
            "params": [
                {
                    "name": "street_line1",
                    "type": "string"
                },
                {
                    "name": "street_line2",
                    "type": "string"
                },
                {
                    "name": "city",
                    "type": "string"
                },
                {
                    "name": "state",
                    "type": "string"
                },
                {
                    "name": "country_iso2",
                    "type": "string"
                },
                {
                    "name": "post_code",
                    "type": "string"
                }
            ],
            "ret": "PostAddress"
        },
        {
            "_": "paymentRequestedInfo",
            "cid": "909c3f94",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "name",
                    "type": "flags.0?string"
                },
                {
                    "name": "phone",
                    "type": "flags.1?string"
                },
                {
                    "name": "email",
                    "type": "flags.2?string"
                },
                {
                    "name": "shipping_address",
                    "type": "flags.3?PostAddress"
                }
            ],
            "ret": "PaymentRequestedInfo"
        },
        {
            "_": "paymentSavedCredentialsCard",
            "cid": "cdc27a1f",
            "params": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "PaymentSavedCredentials"
        },
        {
            "_": "webDocument",
            "cid": "1c570ed1",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "size",
                    "type": "int"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "attributes",
                    "type": "Vector<DocumentAttribute>"
                }
            ],
            "ret": "WebDocument"
        },
        {
            "_": "webDocumentNoProxy",
            "cid": "f9c8bcc6",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "size",
                    "type": "int"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "attributes",
                    "type": "Vector<DocumentAttribute>"
                }
            ],
            "ret": "WebDocument"
        },
        {
            "_": "inputWebDocument",
            "cid": "9bed434d",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "size",
                    "type": "int"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "attributes",
                    "type": "Vector<DocumentAttribute>"
                }
            ],
            "ret": "InputWebDocument"
        },
        {
            "_": "inputWebFileLocation",
            "cid": "c239d686",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputWebFileLocation"
        },
        {
            "_": "inputWebFileGeoPointLocation",
            "cid": "9f2221c9",
            "params": [
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                },
                {
                    "name": "zoom",
                    "type": "int"
                },
                {
                    "name": "scale",
                    "type": "int"
                }
            ],
            "ret": "InputWebFileLocation"
        },
        {
            "_": "inputWebFileAudioAlbumThumbLocation",
            "cid": "f46fe924",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "small",
                    "type": "flags.2?true"
                },
                {
                    "name": "document",
                    "type": "flags.0?InputDocument"
                },
                {
                    "name": "title",
                    "type": "flags.1?string"
                },
                {
                    "name": "performer",
                    "type": "flags.1?string"
                }
            ],
            "ret": "InputWebFileLocation"
        },
        {
            "_": "webFile",
            "cid": "21e753bc",
            "params": [
                {
                    "name": "size",
                    "type": "int"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "file_type",
                    "type": "storage.FileType"
                },
                {
                    "name": "mtime",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "upload.WebFile"
        },
        {
            "_": "paymentForm",
            "cid": "a0058751",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "can_save_credentials",
                    "type": "flags.2?true"
                },
                {
                    "name": "password_missing",
                    "type": "flags.3?true"
                },
                {
                    "name": "form_id",
                    "type": "long"
                },
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.5?WebDocument"
                },
                {
                    "name": "invoice",
                    "type": "Invoice"
                },
                {
                    "name": "provider_id",
                    "type": "long"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "native_provider",
                    "type": "flags.4?string"
                },
                {
                    "name": "native_params",
                    "type": "flags.4?DataJSON"
                },
                {
                    "name": "additional_methods",
                    "type": "flags.6?Vector<PaymentFormMethod>"
                },
                {
                    "name": "saved_info",
                    "type": "flags.0?PaymentRequestedInfo"
                },
                {
                    "name": "saved_credentials",
                    "type": "flags.1?Vector<PaymentSavedCredentials>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "payments.PaymentForm"
        },
        {
            "_": "validatedRequestedInfo",
            "cid": "d1451883",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "flags.0?string"
                },
                {
                    "name": "shipping_options",
                    "type": "flags.1?Vector<ShippingOption>"
                }
            ],
            "ret": "payments.ValidatedRequestedInfo"
        },
        {
            "_": "paymentResult",
            "cid": "4e5f810d",
            "params": [
                {
                    "name": "updates",
                    "type": "Updates"
                }
            ],
            "ret": "payments.PaymentResult"
        },
        {
            "_": "paymentVerificationNeeded",
            "cid": "d8411139",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "payments.PaymentResult"
        },
        {
            "_": "paymentReceipt",
            "cid": "70c4fe03",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "provider_id",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "description",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.2?WebDocument"
                },
                {
                    "name": "invoice",
                    "type": "Invoice"
                },
                {
                    "name": "info",
                    "type": "flags.0?PaymentRequestedInfo"
                },
                {
                    "name": "shipping",
                    "type": "flags.1?ShippingOption"
                },
                {
                    "name": "tip_amount",
                    "type": "flags.3?long"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "total_amount",
                    "type": "long"
                },
                {
                    "name": "credentials_title",
                    "type": "string"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "payments.PaymentReceipt"
        },
        {
            "_": "savedInfo",
            "cid": "fb8fe43c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "has_saved_credentials",
                    "type": "flags.1?true"
                },
                {
                    "name": "saved_info",
                    "type": "flags.0?PaymentRequestedInfo"
                }
            ],
            "ret": "payments.SavedInfo"
        },
        {
            "_": "inputPaymentCredentialsSaved",
            "cid": "c10eb2cf",
            "params": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "tmp_password",
                    "type": "bytes"
                }
            ],
            "ret": "InputPaymentCredentials"
        },
        {
            "_": "inputPaymentCredentials",
            "cid": "3417d728",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "save",
                    "type": "flags.0?true"
                },
                {
                    "name": "data",
                    "type": "DataJSON"
                }
            ],
            "ret": "InputPaymentCredentials"
        },
        {
            "_": "inputPaymentCredentialsApplePay",
            "cid": "aa1c39f",
            "params": [
                {
                    "name": "payment_data",
                    "type": "DataJSON"
                }
            ],
            "ret": "InputPaymentCredentials"
        },
        {
            "_": "inputPaymentCredentialsGooglePay",
            "cid": "8ac32801",
            "params": [
                {
                    "name": "payment_token",
                    "type": "DataJSON"
                }
            ],
            "ret": "InputPaymentCredentials"
        },
        {
            "_": "tmpPassword",
            "cid": "db64fd34",
            "params": [
                {
                    "name": "tmp_password",
                    "type": "bytes"
                },
                {
                    "name": "valid_until",
                    "type": "int"
                }
            ],
            "ret": "account.TmpPassword"
        },
        {
            "_": "shippingOption",
            "cid": "b6213cdf",
            "params": [
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "prices",
                    "type": "Vector<LabeledPrice>"
                }
            ],
            "ret": "ShippingOption"
        },
        {
            "_": "inputStickerSetItem",
            "cid": "ffa0a496",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "document",
                    "type": "InputDocument"
                },
                {
                    "name": "emoji",
                    "type": "string"
                },
                {
                    "name": "mask_coords",
                    "type": "flags.0?MaskCoords"
                }
            ],
            "ret": "InputStickerSetItem"
        },
        {
            "_": "inputPhoneCall",
            "cid": "1e36fded",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputPhoneCall"
        },
        {
            "_": "phoneCallEmpty",
            "cid": "5366c915",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "PhoneCall"
        },
        {
            "_": "phoneCallWaiting",
            "cid": "c5226f17",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "video",
                    "type": "flags.6?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                },
                {
                    "name": "receive_date",
                    "type": "flags.0?int"
                }
            ],
            "ret": "PhoneCall"
        },
        {
            "_": "phoneCallRequested",
            "cid": "14b0ed0c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "video",
                    "type": "flags.6?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                },
                {
                    "name": "g_a_hash",
                    "type": "bytes"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                }
            ],
            "ret": "PhoneCall"
        },
        {
            "_": "phoneCallAccepted",
            "cid": "3660c311",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "video",
                    "type": "flags.6?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                },
                {
                    "name": "g_b",
                    "type": "bytes"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                }
            ],
            "ret": "PhoneCall"
        },
        {
            "_": "phoneCall",
            "cid": "967f7c67",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "p2p_allowed",
                    "type": "flags.5?true"
                },
                {
                    "name": "video",
                    "type": "flags.6?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "participant_id",
                    "type": "long"
                },
                {
                    "name": "g_a_or_b",
                    "type": "bytes"
                },
                {
                    "name": "key_fingerprint",
                    "type": "long"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                },
                {
                    "name": "connections",
                    "type": "Vector<PhoneConnection>"
                },
                {
                    "name": "start_date",
                    "type": "int"
                }
            ],
            "ret": "PhoneCall"
        },
        {
            "_": "phoneCallDiscarded",
            "cid": "50ca4de1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "need_rating",
                    "type": "flags.2?true"
                },
                {
                    "name": "need_debug",
                    "type": "flags.3?true"
                },
                {
                    "name": "video",
                    "type": "flags.6?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "reason",
                    "type": "flags.0?PhoneCallDiscardReason"
                },
                {
                    "name": "duration",
                    "type": "flags.1?int"
                }
            ],
            "ret": "PhoneCall"
        },
        {
            "_": "phoneConnection",
            "cid": "9cc123c7",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "tcp",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "ip",
                    "type": "string"
                },
                {
                    "name": "ipv6",
                    "type": "string"
                },
                {
                    "name": "port",
                    "type": "int"
                },
                {
                    "name": "peer_tag",
                    "type": "bytes"
                }
            ],
            "ret": "PhoneConnection"
        },
        {
            "_": "phoneConnectionWebrtc",
            "cid": "635fe375",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "turn",
                    "type": "flags.0?true"
                },
                {
                    "name": "stun",
                    "type": "flags.1?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "ip",
                    "type": "string"
                },
                {
                    "name": "ipv6",
                    "type": "string"
                },
                {
                    "name": "port",
                    "type": "int"
                },
                {
                    "name": "username",
                    "type": "string"
                },
                {
                    "name": "password",
                    "type": "string"
                }
            ],
            "ret": "PhoneConnection"
        },
        {
            "_": "phoneCallProtocol",
            "cid": "fc878fc8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "udp_p2p",
                    "type": "flags.0?true"
                },
                {
                    "name": "udp_reflector",
                    "type": "flags.1?true"
                },
                {
                    "name": "min_layer",
                    "type": "int"
                },
                {
                    "name": "max_layer",
                    "type": "int"
                },
                {
                    "name": "library_versions",
                    "type": "Vector<string>"
                }
            ],
            "ret": "PhoneCallProtocol"
        },
        {
            "_": "phoneCall",
            "cid": "ec82e140",
            "params": [
                {
                    "name": "phone_call",
                    "type": "PhoneCall"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "phone.PhoneCall"
        },
        {
            "_": "cdnFileReuploadNeeded",
            "cid": "eea8e46e",
            "params": [
                {
                    "name": "request_token",
                    "type": "bytes"
                }
            ],
            "ret": "upload.CdnFile"
        },
        {
            "_": "cdnFile",
            "cid": "a99fca4f",
            "params": [
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "upload.CdnFile"
        },
        {
            "_": "cdnPublicKey",
            "cid": "c982eaba",
            "params": [
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "public_key",
                    "type": "string"
                }
            ],
            "ret": "CdnPublicKey"
        },
        {
            "_": "cdnConfig",
            "cid": "5725e40a",
            "params": [
                {
                    "name": "public_keys",
                    "type": "Vector<CdnPublicKey>"
                }
            ],
            "ret": "CdnConfig"
        },
        {
            "_": "langPackString",
            "cid": "cad181f6",
            "params": [
                {
                    "name": "key",
                    "type": "string"
                },
                {
                    "name": "value",
                    "type": "string"
                }
            ],
            "ret": "LangPackString"
        },
        {
            "_": "langPackStringPluralized",
            "cid": "6c47ac9f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "key",
                    "type": "string"
                },
                {
                    "name": "zero_value",
                    "type": "flags.0?string"
                },
                {
                    "name": "one_value",
                    "type": "flags.1?string"
                },
                {
                    "name": "two_value",
                    "type": "flags.2?string"
                },
                {
                    "name": "few_value",
                    "type": "flags.3?string"
                },
                {
                    "name": "many_value",
                    "type": "flags.4?string"
                },
                {
                    "name": "other_value",
                    "type": "string"
                }
            ],
            "ret": "LangPackString"
        },
        {
            "_": "langPackStringDeleted",
            "cid": "2979eeb2",
            "params": [
                {
                    "name": "key",
                    "type": "string"
                }
            ],
            "ret": "LangPackString"
        },
        {
            "_": "langPackDifference",
            "cid": "f385c1f6",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "from_version",
                    "type": "int"
                },
                {
                    "name": "version",
                    "type": "int"
                },
                {
                    "name": "strings",
                    "type": "Vector<LangPackString>"
                }
            ],
            "ret": "LangPackDifference"
        },
        {
            "_": "langPackLanguage",
            "cid": "eeca5ce3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "official",
                    "type": "flags.0?true"
                },
                {
                    "name": "rtl",
                    "type": "flags.2?true"
                },
                {
                    "name": "beta",
                    "type": "flags.3?true"
                },
                {
                    "name": "name",
                    "type": "string"
                },
                {
                    "name": "native_name",
                    "type": "string"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "base_lang_code",
                    "type": "flags.1?string"
                },
                {
                    "name": "plural_code",
                    "type": "string"
                },
                {
                    "name": "strings_count",
                    "type": "int"
                },
                {
                    "name": "translated_count",
                    "type": "int"
                },
                {
                    "name": "translations_url",
                    "type": "string"
                }
            ],
            "ret": "LangPackLanguage"
        },
        {
            "_": "channelAdminLogEventActionChangeTitle",
            "cid": "e6dfb825",
            "params": [
                {
                    "name": "prev_value",
                    "type": "string"
                },
                {
                    "name": "new_value",
                    "type": "string"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeAbout",
            "cid": "55188a2e",
            "params": [
                {
                    "name": "prev_value",
                    "type": "string"
                },
                {
                    "name": "new_value",
                    "type": "string"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeUsername",
            "cid": "6a4afc38",
            "params": [
                {
                    "name": "prev_value",
                    "type": "string"
                },
                {
                    "name": "new_value",
                    "type": "string"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangePhoto",
            "cid": "434bd2af",
            "params": [
                {
                    "name": "prev_photo",
                    "type": "Photo"
                },
                {
                    "name": "new_photo",
                    "type": "Photo"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleInvites",
            "cid": "1b7907ae",
            "params": [
                {
                    "name": "new_value",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleSignatures",
            "cid": "26ae0971",
            "params": [
                {
                    "name": "new_value",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionUpdatePinned",
            "cid": "e9e82c18",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionEditMessage",
            "cid": "709b2405",
            "params": [
                {
                    "name": "prev_message",
                    "type": "Message"
                },
                {
                    "name": "new_message",
                    "type": "Message"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionDeleteMessage",
            "cid": "42e047bb",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantJoin",
            "cid": "183040d3",
            "params": [],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantLeave",
            "cid": "f89777f2",
            "params": [],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantInvite",
            "cid": "e31c34d8",
            "params": [
                {
                    "name": "participant",
                    "type": "ChannelParticipant"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantToggleBan",
            "cid": "e6d83d7e",
            "params": [
                {
                    "name": "prev_participant",
                    "type": "ChannelParticipant"
                },
                {
                    "name": "new_participant",
                    "type": "ChannelParticipant"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantToggleAdmin",
            "cid": "d5676710",
            "params": [
                {
                    "name": "prev_participant",
                    "type": "ChannelParticipant"
                },
                {
                    "name": "new_participant",
                    "type": "ChannelParticipant"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeStickerSet",
            "cid": "b1c3caa7",
            "params": [
                {
                    "name": "prev_stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "new_stickerset",
                    "type": "InputStickerSet"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionTogglePreHistoryHidden",
            "cid": "5f5c95f1",
            "params": [
                {
                    "name": "new_value",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionDefaultBannedRights",
            "cid": "2df5fc0a",
            "params": [
                {
                    "name": "prev_banned_rights",
                    "type": "ChatBannedRights"
                },
                {
                    "name": "new_banned_rights",
                    "type": "ChatBannedRights"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionStopPoll",
            "cid": "8f079643",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeLinkedChat",
            "cid": "50c7ac8",
            "params": [
                {
                    "name": "prev_value",
                    "type": "long"
                },
                {
                    "name": "new_value",
                    "type": "long"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeLocation",
            "cid": "e6b76ae",
            "params": [
                {
                    "name": "prev_value",
                    "type": "ChannelLocation"
                },
                {
                    "name": "new_value",
                    "type": "ChannelLocation"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleSlowMode",
            "cid": "53909779",
            "params": [
                {
                    "name": "prev_value",
                    "type": "int"
                },
                {
                    "name": "new_value",
                    "type": "int"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionStartGroupCall",
            "cid": "23209745",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionDiscardGroupCall",
            "cid": "db9f9140",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantMute",
            "cid": "f92424d2",
            "params": [
                {
                    "name": "participant",
                    "type": "GroupCallParticipant"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantUnmute",
            "cid": "e64429c0",
            "params": [
                {
                    "name": "participant",
                    "type": "GroupCallParticipant"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleGroupCallSetting",
            "cid": "56d6a247",
            "params": [
                {
                    "name": "join_muted",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantJoinByInvite",
            "cid": "5cdada77",
            "params": [
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionExportedInviteDelete",
            "cid": "5a50fca4",
            "params": [
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionExportedInviteRevoke",
            "cid": "410a134e",
            "params": [
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionExportedInviteEdit",
            "cid": "e90ebb59",
            "params": [
                {
                    "name": "prev_invite",
                    "type": "ExportedChatInvite"
                },
                {
                    "name": "new_invite",
                    "type": "ExportedChatInvite"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantVolume",
            "cid": "3e7f6847",
            "params": [
                {
                    "name": "participant",
                    "type": "GroupCallParticipant"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeHistoryTTL",
            "cid": "6e941a38",
            "params": [
                {
                    "name": "prev_value",
                    "type": "int"
                },
                {
                    "name": "new_value",
                    "type": "int"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionParticipantJoinByRequest",
            "cid": "afb6144a",
            "params": [
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                },
                {
                    "name": "approved_by",
                    "type": "long"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleNoForwards",
            "cid": "cb2ac766",
            "params": [
                {
                    "name": "new_value",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionSendMessage",
            "cid": "278f2868",
            "params": [
                {
                    "name": "message",
                    "type": "Message"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeAvailableReactions",
            "cid": "be4e0ef8",
            "params": [
                {
                    "name": "prev_value",
                    "type": "ChatReactions"
                },
                {
                    "name": "new_value",
                    "type": "ChatReactions"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionChangeUsernames",
            "cid": "f04fb3a9",
            "params": [
                {
                    "name": "prev_value",
                    "type": "Vector<string>"
                },
                {
                    "name": "new_value",
                    "type": "Vector<string>"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleForum",
            "cid": "2cc6383",
            "params": [
                {
                    "name": "new_value",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionCreateTopic",
            "cid": "58707d28",
            "params": [
                {
                    "name": "topic",
                    "type": "ForumTopic"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionEditTopic",
            "cid": "f06fe208",
            "params": [
                {
                    "name": "prev_topic",
                    "type": "ForumTopic"
                },
                {
                    "name": "new_topic",
                    "type": "ForumTopic"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionDeleteTopic",
            "cid": "ae168909",
            "params": [
                {
                    "name": "topic",
                    "type": "ForumTopic"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionPinTopic",
            "cid": "5d8d353b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "prev_topic",
                    "type": "flags.0?ForumTopic"
                },
                {
                    "name": "new_topic",
                    "type": "flags.1?ForumTopic"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEventActionToggleAntiSpam",
            "cid": "64f36dfc",
            "params": [
                {
                    "name": "new_value",
                    "type": "Bool"
                }
            ],
            "ret": "ChannelAdminLogEventAction"
        },
        {
            "_": "channelAdminLogEvent",
            "cid": "1fad68cd",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "action",
                    "type": "ChannelAdminLogEventAction"
                }
            ],
            "ret": "ChannelAdminLogEvent"
        },
        {
            "_": "adminLogResults",
            "cid": "ed8af74d",
            "params": [
                {
                    "name": "events",
                    "type": "Vector<ChannelAdminLogEvent>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "channels.AdminLogResults"
        },
        {
            "_": "channelAdminLogEventsFilter",
            "cid": "ea107ae4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "join",
                    "type": "flags.0?true"
                },
                {
                    "name": "leave",
                    "type": "flags.1?true"
                },
                {
                    "name": "invite",
                    "type": "flags.2?true"
                },
                {
                    "name": "ban",
                    "type": "flags.3?true"
                },
                {
                    "name": "unban",
                    "type": "flags.4?true"
                },
                {
                    "name": "kick",
                    "type": "flags.5?true"
                },
                {
                    "name": "unkick",
                    "type": "flags.6?true"
                },
                {
                    "name": "promote",
                    "type": "flags.7?true"
                },
                {
                    "name": "demote",
                    "type": "flags.8?true"
                },
                {
                    "name": "info",
                    "type": "flags.9?true"
                },
                {
                    "name": "settings",
                    "type": "flags.10?true"
                },
                {
                    "name": "pinned",
                    "type": "flags.11?true"
                },
                {
                    "name": "edit",
                    "type": "flags.12?true"
                },
                {
                    "name": "delete",
                    "type": "flags.13?true"
                },
                {
                    "name": "group_call",
                    "type": "flags.14?true"
                },
                {
                    "name": "invites",
                    "type": "flags.15?true"
                },
                {
                    "name": "send",
                    "type": "flags.16?true"
                },
                {
                    "name": "forums",
                    "type": "flags.17?true"
                }
            ],
            "ret": "ChannelAdminLogEventsFilter"
        },
        {
            "_": "popularContact",
            "cid": "5ce14175",
            "params": [
                {
                    "name": "client_id",
                    "type": "long"
                },
                {
                    "name": "importers",
                    "type": "int"
                }
            ],
            "ret": "PopularContact"
        },
        {
            "_": "favedStickersNotModified",
            "cid": "9e8fa6d3",
            "params": [],
            "ret": "messages.FavedStickers"
        },
        {
            "_": "favedStickers",
            "cid": "2cb51097",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "packs",
                    "type": "Vector<StickerPack>"
                },
                {
                    "name": "stickers",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "messages.FavedStickers"
        },
        {
            "_": "recentMeUrlUnknown",
            "cid": "46e1d13d",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "RecentMeUrl"
        },
        {
            "_": "recentMeUrlUser",
            "cid": "b92c09e2",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "user_id",
                    "type": "long"
                }
            ],
            "ret": "RecentMeUrl"
        },
        {
            "_": "recentMeUrlChat",
            "cid": "b2da71d2",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "RecentMeUrl"
        },
        {
            "_": "recentMeUrlChatInvite",
            "cid": "eb49081d",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "chat_invite",
                    "type": "ChatInvite"
                }
            ],
            "ret": "RecentMeUrl"
        },
        {
            "_": "recentMeUrlStickerSet",
            "cid": "bc0a57dc",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "set",
                    "type": "StickerSetCovered"
                }
            ],
            "ret": "RecentMeUrl"
        },
        {
            "_": "recentMeUrls",
            "cid": "e0310d7",
            "params": [
                {
                    "name": "urls",
                    "type": "Vector<RecentMeUrl>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "help.RecentMeUrls"
        },
        {
            "_": "inputSingleMedia",
            "cid": "1cc6e91f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "media",
                    "type": "InputMedia"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.0?Vector<MessageEntity>"
                }
            ],
            "ret": "InputSingleMedia"
        },
        {
            "_": "webAuthorization",
            "cid": "a6f8f452",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "domain",
                    "type": "string"
                },
                {
                    "name": "browser",
                    "type": "string"
                },
                {
                    "name": "platform",
                    "type": "string"
                },
                {
                    "name": "date_created",
                    "type": "int"
                },
                {
                    "name": "date_active",
                    "type": "int"
                },
                {
                    "name": "ip",
                    "type": "string"
                },
                {
                    "name": "region",
                    "type": "string"
                }
            ],
            "ret": "WebAuthorization"
        },
        {
            "_": "webAuthorizations",
            "cid": "ed56c9fc",
            "params": [
                {
                    "name": "authorizations",
                    "type": "Vector<WebAuthorization>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "account.WebAuthorizations"
        },
        {
            "_": "inputMessageID",
            "cid": "a676a322",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "InputMessage"
        },
        {
            "_": "inputMessageReplyTo",
            "cid": "bad88395",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "InputMessage"
        },
        {
            "_": "inputMessagePinned",
            "cid": "86872538",
            "params": [],
            "ret": "InputMessage"
        },
        {
            "_": "inputMessageCallbackQuery",
            "cid": "acfa1a7e",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "query_id",
                    "type": "long"
                }
            ],
            "ret": "InputMessage"
        },
        {
            "_": "inputDialogPeer",
            "cid": "fcaafeb7",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "InputDialogPeer"
        },
        {
            "_": "inputDialogPeerFolder",
            "cid": "64600527",
            "params": [
                {
                    "name": "folder_id",
                    "type": "int"
                }
            ],
            "ret": "InputDialogPeer"
        },
        {
            "_": "dialogPeer",
            "cid": "e56dbf05",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                }
            ],
            "ret": "DialogPeer"
        },
        {
            "_": "dialogPeerFolder",
            "cid": "514519e2",
            "params": [
                {
                    "name": "folder_id",
                    "type": "int"
                }
            ],
            "ret": "DialogPeer"
        },
        {
            "_": "foundStickerSetsNotModified",
            "cid": "d54b65d",
            "params": [],
            "ret": "messages.FoundStickerSets"
        },
        {
            "_": "foundStickerSets",
            "cid": "8af09dd2",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "sets",
                    "type": "Vector<StickerSetCovered>"
                }
            ],
            "ret": "messages.FoundStickerSets"
        },
        {
            "_": "fileHash",
            "cid": "f39b035c",
            "params": [
                {
                    "name": "offset",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "bytes"
                }
            ],
            "ret": "FileHash"
        },
        {
            "_": "inputClientProxy",
            "cid": "75588b3f",
            "params": [
                {
                    "name": "address",
                    "type": "string"
                },
                {
                    "name": "port",
                    "type": "int"
                }
            ],
            "ret": "InputClientProxy"
        },
        {
            "_": "termsOfServiceUpdateEmpty",
            "cid": "e3309f7f",
            "params": [
                {
                    "name": "expires",
                    "type": "int"
                }
            ],
            "ret": "help.TermsOfServiceUpdate"
        },
        {
            "_": "termsOfServiceUpdate",
            "cid": "28ecf961",
            "params": [
                {
                    "name": "expires",
                    "type": "int"
                },
                {
                    "name": "terms_of_service",
                    "type": "help.TermsOfService"
                }
            ],
            "ret": "help.TermsOfServiceUpdate"
        },
        {
            "_": "inputSecureFileUploaded",
            "cid": "3334b0f0",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "parts",
                    "type": "int"
                },
                {
                    "name": "md5_checksum",
                    "type": "string"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "secret",
                    "type": "bytes"
                }
            ],
            "ret": "InputSecureFile"
        },
        {
            "_": "inputSecureFile",
            "cid": "5367e5be",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputSecureFile"
        },
        {
            "_": "secureFileEmpty",
            "cid": "64199744",
            "params": [],
            "ret": "SecureFile"
        },
        {
            "_": "secureFile",
            "cid": "7d09c27e",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "size",
                    "type": "long"
                },
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "secret",
                    "type": "bytes"
                }
            ],
            "ret": "SecureFile"
        },
        {
            "_": "secureData",
            "cid": "8aeabec3",
            "params": [
                {
                    "name": "data",
                    "type": "bytes"
                },
                {
                    "name": "data_hash",
                    "type": "bytes"
                },
                {
                    "name": "secret",
                    "type": "bytes"
                }
            ],
            "ret": "SecureData"
        },
        {
            "_": "securePlainPhone",
            "cid": "7d6099dd",
            "params": [
                {
                    "name": "phone",
                    "type": "string"
                }
            ],
            "ret": "SecurePlainData"
        },
        {
            "_": "securePlainEmail",
            "cid": "21ec5a5f",
            "params": [
                {
                    "name": "email",
                    "type": "string"
                }
            ],
            "ret": "SecurePlainData"
        },
        {
            "_": "secureValueTypePersonalDetails",
            "cid": "9d2a81e3",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypePassport",
            "cid": "3dac6a00",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeDriverLicense",
            "cid": "6e425c4",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeIdentityCard",
            "cid": "a0d0744b",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeInternalPassport",
            "cid": "99a48f23",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeAddress",
            "cid": "cbe31e26",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeUtilityBill",
            "cid": "fc36954e",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeBankStatement",
            "cid": "89137c0d",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeRentalAgreement",
            "cid": "8b883488",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypePassportRegistration",
            "cid": "99e3806a",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeTemporaryRegistration",
            "cid": "ea02ec33",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypePhone",
            "cid": "b320aadb",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValueTypeEmail",
            "cid": "8e3ca7ee",
            "params": [],
            "ret": "SecureValueType"
        },
        {
            "_": "secureValue",
            "cid": "187fa0ca",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "data",
                    "type": "flags.0?SecureData"
                },
                {
                    "name": "front_side",
                    "type": "flags.1?SecureFile"
                },
                {
                    "name": "reverse_side",
                    "type": "flags.2?SecureFile"
                },
                {
                    "name": "selfie",
                    "type": "flags.3?SecureFile"
                },
                {
                    "name": "translation",
                    "type": "flags.6?Vector<SecureFile>"
                },
                {
                    "name": "files",
                    "type": "flags.4?Vector<SecureFile>"
                },
                {
                    "name": "plain_data",
                    "type": "flags.5?SecurePlainData"
                },
                {
                    "name": "hash",
                    "type": "bytes"
                }
            ],
            "ret": "SecureValue"
        },
        {
            "_": "inputSecureValue",
            "cid": "db21d0a7",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "data",
                    "type": "flags.0?SecureData"
                },
                {
                    "name": "front_side",
                    "type": "flags.1?InputSecureFile"
                },
                {
                    "name": "reverse_side",
                    "type": "flags.2?InputSecureFile"
                },
                {
                    "name": "selfie",
                    "type": "flags.3?InputSecureFile"
                },
                {
                    "name": "translation",
                    "type": "flags.6?Vector<InputSecureFile>"
                },
                {
                    "name": "files",
                    "type": "flags.4?Vector<InputSecureFile>"
                },
                {
                    "name": "plain_data",
                    "type": "flags.5?SecurePlainData"
                }
            ],
            "ret": "InputSecureValue"
        },
        {
            "_": "secureValueHash",
            "cid": "ed1ecdb0",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "hash",
                    "type": "bytes"
                }
            ],
            "ret": "SecureValueHash"
        },
        {
            "_": "secureValueErrorData",
            "cid": "e8a40bd9",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "data_hash",
                    "type": "bytes"
                },
                {
                    "name": "field",
                    "type": "string"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorFrontSide",
            "cid": "be3dfa",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorReverseSide",
            "cid": "868a2aa5",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorSelfie",
            "cid": "e537ced6",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorFile",
            "cid": "7a700873",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorFiles",
            "cid": "666220e9",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "Vector<bytes>"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueError",
            "cid": "869d758f",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "hash",
                    "type": "bytes"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorTranslationFile",
            "cid": "a1144770",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "bytes"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureValueErrorTranslationFiles",
            "cid": "34636dd8",
            "params": [
                {
                    "name": "type",
                    "type": "SecureValueType"
                },
                {
                    "name": "file_hash",
                    "type": "Vector<bytes>"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "SecureValueError"
        },
        {
            "_": "secureCredentialsEncrypted",
            "cid": "33f0ea47",
            "params": [
                {
                    "name": "data",
                    "type": "bytes"
                },
                {
                    "name": "hash",
                    "type": "bytes"
                },
                {
                    "name": "secret",
                    "type": "bytes"
                }
            ],
            "ret": "SecureCredentialsEncrypted"
        },
        {
            "_": "authorizationForm",
            "cid": "ad2e1cd8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "required_types",
                    "type": "Vector<SecureRequiredType>"
                },
                {
                    "name": "values",
                    "type": "Vector<SecureValue>"
                },
                {
                    "name": "errors",
                    "type": "Vector<SecureValueError>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "privacy_policy_url",
                    "type": "flags.0?string"
                }
            ],
            "ret": "account.AuthorizationForm"
        },
        {
            "_": "sentEmailCode",
            "cid": "811f854f",
            "params": [
                {
                    "name": "email_pattern",
                    "type": "string"
                },
                {
                    "name": "length",
                    "type": "int"
                }
            ],
            "ret": "account.SentEmailCode"
        },
        {
            "_": "deepLinkInfoEmpty",
            "cid": "66afa166",
            "params": [],
            "ret": "help.DeepLinkInfo"
        },
        {
            "_": "deepLinkInfo",
            "cid": "6a4ee832",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "update_app",
                    "type": "flags.0?true"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.1?Vector<MessageEntity>"
                }
            ],
            "ret": "help.DeepLinkInfo"
        },
        {
            "_": "savedPhoneContact",
            "cid": "1142bd56",
            "params": [
                {
                    "name": "phone",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "SavedContact"
        },
        {
            "_": "takeout",
            "cid": "4dba4501",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "account.Takeout"
        },
        {
            "_": "passwordKdfAlgoUnknown",
            "cid": "d45ab096",
            "params": [],
            "ret": "PasswordKdfAlgo"
        },
        {
            "_": "passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow",
            "cid": "3a912d4a",
            "params": [
                {
                    "name": "salt1",
                    "type": "bytes"
                },
                {
                    "name": "salt2",
                    "type": "bytes"
                },
                {
                    "name": "g",
                    "type": "int"
                },
                {
                    "name": "p",
                    "type": "bytes"
                }
            ],
            "ret": "PasswordKdfAlgo"
        },
        {
            "_": "securePasswordKdfAlgoUnknown",
            "cid": "4a8537",
            "params": [],
            "ret": "SecurePasswordKdfAlgo"
        },
        {
            "_": "securePasswordKdfAlgoPBKDF2HMACSHA512iter100000",
            "cid": "bbf2dda0",
            "params": [
                {
                    "name": "salt",
                    "type": "bytes"
                }
            ],
            "ret": "SecurePasswordKdfAlgo"
        },
        {
            "_": "securePasswordKdfAlgoSHA512",
            "cid": "86471d92",
            "params": [
                {
                    "name": "salt",
                    "type": "bytes"
                }
            ],
            "ret": "SecurePasswordKdfAlgo"
        },
        {
            "_": "secureSecretSettings",
            "cid": "1527bcac",
            "params": [
                {
                    "name": "secure_algo",
                    "type": "SecurePasswordKdfAlgo"
                },
                {
                    "name": "secure_secret",
                    "type": "bytes"
                },
                {
                    "name": "secure_secret_id",
                    "type": "long"
                }
            ],
            "ret": "SecureSecretSettings"
        },
        {
            "_": "inputCheckPasswordEmpty",
            "cid": "9880f658",
            "params": [],
            "ret": "InputCheckPasswordSRP"
        },
        {
            "_": "inputCheckPasswordSRP",
            "cid": "d27ff082",
            "params": [
                {
                    "name": "srp_id",
                    "type": "long"
                },
                {
                    "name": "A",
                    "type": "bytes"
                },
                {
                    "name": "M1",
                    "type": "bytes"
                }
            ],
            "ret": "InputCheckPasswordSRP"
        },
        {
            "_": "secureRequiredType",
            "cid": "829d99da",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "native_names",
                    "type": "flags.0?true"
                },
                {
                    "name": "selfie_required",
                    "type": "flags.1?true"
                },
                {
                    "name": "translation_required",
                    "type": "flags.2?true"
                },
                {
                    "name": "type",
                    "type": "SecureValueType"
                }
            ],
            "ret": "SecureRequiredType"
        },
        {
            "_": "secureRequiredTypeOneOf",
            "cid": "27477b4",
            "params": [
                {
                    "name": "types",
                    "type": "Vector<SecureRequiredType>"
                }
            ],
            "ret": "SecureRequiredType"
        },
        {
            "_": "passportConfigNotModified",
            "cid": "bfb9f457",
            "params": [],
            "ret": "help.PassportConfig"
        },
        {
            "_": "passportConfig",
            "cid": "a098d6af",
            "params": [
                {
                    "name": "hash",
                    "type": "int"
                },
                {
                    "name": "countries_langs",
                    "type": "DataJSON"
                }
            ],
            "ret": "help.PassportConfig"
        },
        {
            "_": "inputAppEvent",
            "cid": "1d1b1245",
            "params": [
                {
                    "name": "time",
                    "type": "double"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "peer",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "JSONValue"
                }
            ],
            "ret": "InputAppEvent"
        },
        {
            "_": "jsonObjectValue",
            "cid": "c0de1bd9",
            "params": [
                {
                    "name": "key",
                    "type": "string"
                },
                {
                    "name": "value",
                    "type": "JSONValue"
                }
            ],
            "ret": "JSONObjectValue"
        },
        {
            "_": "jsonNull",
            "cid": "3f6d7b68",
            "params": [],
            "ret": "JSONValue"
        },
        {
            "_": "jsonBool",
            "cid": "c7345e6a",
            "params": [
                {
                    "name": "value",
                    "type": "Bool"
                }
            ],
            "ret": "JSONValue"
        },
        {
            "_": "jsonNumber",
            "cid": "2be0dfa4",
            "params": [
                {
                    "name": "value",
                    "type": "double"
                }
            ],
            "ret": "JSONValue"
        },
        {
            "_": "jsonString",
            "cid": "b71e767a",
            "params": [
                {
                    "name": "value",
                    "type": "string"
                }
            ],
            "ret": "JSONValue"
        },
        {
            "_": "jsonArray",
            "cid": "f7444763",
            "params": [
                {
                    "name": "value",
                    "type": "Vector<JSONValue>"
                }
            ],
            "ret": "JSONValue"
        },
        {
            "_": "jsonObject",
            "cid": "99c1d49d",
            "params": [
                {
                    "name": "value",
                    "type": "Vector<JSONObjectValue>"
                }
            ],
            "ret": "JSONValue"
        },
        {
            "_": "pageTableCell",
            "cid": "34566b6a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "header",
                    "type": "flags.0?true"
                },
                {
                    "name": "align_center",
                    "type": "flags.3?true"
                },
                {
                    "name": "align_right",
                    "type": "flags.4?true"
                },
                {
                    "name": "valign_middle",
                    "type": "flags.5?true"
                },
                {
                    "name": "valign_bottom",
                    "type": "flags.6?true"
                },
                {
                    "name": "text",
                    "type": "flags.7?RichText"
                },
                {
                    "name": "colspan",
                    "type": "flags.1?int"
                },
                {
                    "name": "rowspan",
                    "type": "flags.2?int"
                }
            ],
            "ret": "PageTableCell"
        },
        {
            "_": "pageTableRow",
            "cid": "e0c0c5e5",
            "params": [
                {
                    "name": "cells",
                    "type": "Vector<PageTableCell>"
                }
            ],
            "ret": "PageTableRow"
        },
        {
            "_": "pageCaption",
            "cid": "6f747657",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                },
                {
                    "name": "credit",
                    "type": "RichText"
                }
            ],
            "ret": "PageCaption"
        },
        {
            "_": "pageListItemText",
            "cid": "b92fb6cd",
            "params": [
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageListItem"
        },
        {
            "_": "pageListItemBlocks",
            "cid": "25e073fc",
            "params": [
                {
                    "name": "blocks",
                    "type": "Vector<PageBlock>"
                }
            ],
            "ret": "PageListItem"
        },
        {
            "_": "pageListOrderedItemText",
            "cid": "5e068047",
            "params": [
                {
                    "name": "num",
                    "type": "string"
                },
                {
                    "name": "text",
                    "type": "RichText"
                }
            ],
            "ret": "PageListOrderedItem"
        },
        {
            "_": "pageListOrderedItemBlocks",
            "cid": "98dd8936",
            "params": [
                {
                    "name": "num",
                    "type": "string"
                },
                {
                    "name": "blocks",
                    "type": "Vector<PageBlock>"
                }
            ],
            "ret": "PageListOrderedItem"
        },
        {
            "_": "pageRelatedArticle",
            "cid": "b390dc08",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "webpage_id",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "flags.0?string"
                },
                {
                    "name": "description",
                    "type": "flags.1?string"
                },
                {
                    "name": "photo_id",
                    "type": "flags.2?long"
                },
                {
                    "name": "author",
                    "type": "flags.3?string"
                },
                {
                    "name": "published_date",
                    "type": "flags.4?int"
                }
            ],
            "ret": "PageRelatedArticle"
        },
        {
            "_": "page",
            "cid": "98657f0d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "part",
                    "type": "flags.0?true"
                },
                {
                    "name": "rtl",
                    "type": "flags.1?true"
                },
                {
                    "name": "v2",
                    "type": "flags.2?true"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "blocks",
                    "type": "Vector<PageBlock>"
                },
                {
                    "name": "photos",
                    "type": "Vector<Photo>"
                },
                {
                    "name": "documents",
                    "type": "Vector<Document>"
                },
                {
                    "name": "views",
                    "type": "flags.3?int"
                }
            ],
            "ret": "Page"
        },
        {
            "_": "supportName",
            "cid": "8c05f1c9",
            "params": [
                {
                    "name": "name",
                    "type": "string"
                }
            ],
            "ret": "help.SupportName"
        },
        {
            "_": "userInfoEmpty",
            "cid": "f3ae2eed",
            "params": [],
            "ret": "help.UserInfo"
        },
        {
            "_": "userInfo",
            "cid": "1eb3758",
            "params": [
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "Vector<MessageEntity>"
                },
                {
                    "name": "author",
                    "type": "string"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "help.UserInfo"
        },
        {
            "_": "pollAnswer",
            "cid": "6ca9c2e9",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "option",
                    "type": "bytes"
                }
            ],
            "ret": "PollAnswer"
        },
        {
            "_": "poll",
            "cid": "86e18161",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "closed",
                    "type": "flags.0?true"
                },
                {
                    "name": "public_voters",
                    "type": "flags.1?true"
                },
                {
                    "name": "multiple_choice",
                    "type": "flags.2?true"
                },
                {
                    "name": "quiz",
                    "type": "flags.3?true"
                },
                {
                    "name": "question",
                    "type": "string"
                },
                {
                    "name": "answers",
                    "type": "Vector<PollAnswer>"
                },
                {
                    "name": "close_period",
                    "type": "flags.4?int"
                },
                {
                    "name": "close_date",
                    "type": "flags.5?int"
                }
            ],
            "ret": "Poll"
        },
        {
            "_": "pollAnswerVoters",
            "cid": "3b6ddad2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "chosen",
                    "type": "flags.0?true"
                },
                {
                    "name": "correct",
                    "type": "flags.1?true"
                },
                {
                    "name": "option",
                    "type": "bytes"
                },
                {
                    "name": "voters",
                    "type": "int"
                }
            ],
            "ret": "PollAnswerVoters"
        },
        {
            "_": "pollResults",
            "cid": "dcb82ea3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "min",
                    "type": "flags.0?true"
                },
                {
                    "name": "results",
                    "type": "flags.1?Vector<PollAnswerVoters>"
                },
                {
                    "name": "total_voters",
                    "type": "flags.2?int"
                },
                {
                    "name": "recent_voters",
                    "type": "flags.3?Vector<long>"
                },
                {
                    "name": "solution",
                    "type": "flags.4?string"
                },
                {
                    "name": "solution_entities",
                    "type": "flags.4?Vector<MessageEntity>"
                }
            ],
            "ret": "PollResults"
        },
        {
            "_": "chatOnlines",
            "cid": "f041e250",
            "params": [
                {
                    "name": "onlines",
                    "type": "int"
                }
            ],
            "ret": "ChatOnlines"
        },
        {
            "_": "statsURL",
            "cid": "47a971e0",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "StatsURL"
        },
        {
            "_": "chatAdminRights",
            "cid": "5fb224d5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "change_info",
                    "type": "flags.0?true"
                },
                {
                    "name": "post_messages",
                    "type": "flags.1?true"
                },
                {
                    "name": "edit_messages",
                    "type": "flags.2?true"
                },
                {
                    "name": "delete_messages",
                    "type": "flags.3?true"
                },
                {
                    "name": "ban_users",
                    "type": "flags.4?true"
                },
                {
                    "name": "invite_users",
                    "type": "flags.5?true"
                },
                {
                    "name": "pin_messages",
                    "type": "flags.7?true"
                },
                {
                    "name": "add_admins",
                    "type": "flags.9?true"
                },
                {
                    "name": "anonymous",
                    "type": "flags.10?true"
                },
                {
                    "name": "manage_call",
                    "type": "flags.11?true"
                },
                {
                    "name": "other",
                    "type": "flags.12?true"
                },
                {
                    "name": "manage_topics",
                    "type": "flags.13?true"
                }
            ],
            "ret": "ChatAdminRights"
        },
        {
            "_": "chatBannedRights",
            "cid": "9f120418",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "view_messages",
                    "type": "flags.0?true"
                },
                {
                    "name": "send_messages",
                    "type": "flags.1?true"
                },
                {
                    "name": "send_media",
                    "type": "flags.2?true"
                },
                {
                    "name": "send_stickers",
                    "type": "flags.3?true"
                },
                {
                    "name": "send_gifs",
                    "type": "flags.4?true"
                },
                {
                    "name": "send_games",
                    "type": "flags.5?true"
                },
                {
                    "name": "send_inline",
                    "type": "flags.6?true"
                },
                {
                    "name": "embed_links",
                    "type": "flags.7?true"
                },
                {
                    "name": "send_polls",
                    "type": "flags.8?true"
                },
                {
                    "name": "change_info",
                    "type": "flags.10?true"
                },
                {
                    "name": "invite_users",
                    "type": "flags.15?true"
                },
                {
                    "name": "pin_messages",
                    "type": "flags.17?true"
                },
                {
                    "name": "manage_topics",
                    "type": "flags.18?true"
                },
                {
                    "name": "until_date",
                    "type": "int"
                }
            ],
            "ret": "ChatBannedRights"
        },
        {
            "_": "inputWallPaper",
            "cid": "e630b979",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputWallPaper"
        },
        {
            "_": "inputWallPaperSlug",
            "cid": "72091c80",
            "params": [
                {
                    "name": "slug",
                    "type": "string"
                }
            ],
            "ret": "InputWallPaper"
        },
        {
            "_": "inputWallPaperNoFile",
            "cid": "967a462e",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "InputWallPaper"
        },
        {
            "_": "wallPapersNotModified",
            "cid": "1c199183",
            "params": [],
            "ret": "account.WallPapers"
        },
        {
            "_": "wallPapers",
            "cid": "cdc3858c",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "wallpapers",
                    "type": "Vector<WallPaper>"
                }
            ],
            "ret": "account.WallPapers"
        },
        {
            "_": "codeSettings",
            "cid": "8a6469c2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "allow_flashcall",
                    "type": "flags.0?true"
                },
                {
                    "name": "current_number",
                    "type": "flags.1?true"
                },
                {
                    "name": "allow_app_hash",
                    "type": "flags.4?true"
                },
                {
                    "name": "allow_missed_call",
                    "type": "flags.5?true"
                },
                {
                    "name": "logout_tokens",
                    "type": "flags.6?Vector<bytes>"
                }
            ],
            "ret": "CodeSettings"
        },
        {
            "_": "wallPaperSettings",
            "cid": "1dc1bca4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "blur",
                    "type": "flags.1?true"
                },
                {
                    "name": "motion",
                    "type": "flags.2?true"
                },
                {
                    "name": "background_color",
                    "type": "flags.0?int"
                },
                {
                    "name": "second_background_color",
                    "type": "flags.4?int"
                },
                {
                    "name": "third_background_color",
                    "type": "flags.5?int"
                },
                {
                    "name": "fourth_background_color",
                    "type": "flags.6?int"
                },
                {
                    "name": "intensity",
                    "type": "flags.3?int"
                },
                {
                    "name": "rotation",
                    "type": "flags.4?int"
                }
            ],
            "ret": "WallPaperSettings"
        },
        {
            "_": "autoDownloadSettings",
            "cid": "8efab953",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "disabled",
                    "type": "flags.0?true"
                },
                {
                    "name": "video_preload_large",
                    "type": "flags.1?true"
                },
                {
                    "name": "audio_preload_next",
                    "type": "flags.2?true"
                },
                {
                    "name": "phonecalls_less_data",
                    "type": "flags.3?true"
                },
                {
                    "name": "photo_size_max",
                    "type": "int"
                },
                {
                    "name": "video_size_max",
                    "type": "long"
                },
                {
                    "name": "file_size_max",
                    "type": "long"
                },
                {
                    "name": "video_upload_maxbitrate",
                    "type": "int"
                }
            ],
            "ret": "AutoDownloadSettings"
        },
        {
            "_": "autoDownloadSettings",
            "cid": "63cacf26",
            "params": [
                {
                    "name": "low",
                    "type": "AutoDownloadSettings"
                },
                {
                    "name": "medium",
                    "type": "AutoDownloadSettings"
                },
                {
                    "name": "high",
                    "type": "AutoDownloadSettings"
                }
            ],
            "ret": "account.AutoDownloadSettings"
        },
        {
            "_": "emojiKeyword",
            "cid": "d5b3b9f9",
            "params": [
                {
                    "name": "keyword",
                    "type": "string"
                },
                {
                    "name": "emoticons",
                    "type": "Vector<string>"
                }
            ],
            "ret": "EmojiKeyword"
        },
        {
            "_": "emojiKeywordDeleted",
            "cid": "236df622",
            "params": [
                {
                    "name": "keyword",
                    "type": "string"
                },
                {
                    "name": "emoticons",
                    "type": "Vector<string>"
                }
            ],
            "ret": "EmojiKeyword"
        },
        {
            "_": "emojiKeywordsDifference",
            "cid": "5cc761bd",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "from_version",
                    "type": "int"
                },
                {
                    "name": "version",
                    "type": "int"
                },
                {
                    "name": "keywords",
                    "type": "Vector<EmojiKeyword>"
                }
            ],
            "ret": "EmojiKeywordsDifference"
        },
        {
            "_": "emojiURL",
            "cid": "a575739d",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "EmojiURL"
        },
        {
            "_": "emojiLanguage",
            "cid": "b3fb5361",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "EmojiLanguage"
        },
        {
            "_": "folder",
            "cid": "ff544e65",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "autofill_new_broadcasts",
                    "type": "flags.0?true"
                },
                {
                    "name": "autofill_public_groups",
                    "type": "flags.1?true"
                },
                {
                    "name": "autofill_new_correspondents",
                    "type": "flags.2?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "photo",
                    "type": "flags.3?ChatPhoto"
                }
            ],
            "ret": "Folder"
        },
        {
            "_": "inputFolderPeer",
            "cid": "fbd2c296",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "folder_id",
                    "type": "int"
                }
            ],
            "ret": "InputFolderPeer"
        },
        {
            "_": "folderPeer",
            "cid": "e9baa668",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "folder_id",
                    "type": "int"
                }
            ],
            "ret": "FolderPeer"
        },
        {
            "_": "searchCounter",
            "cid": "e844ebff",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "inexact",
                    "type": "flags.1?true"
                },
                {
                    "name": "filter",
                    "type": "MessagesFilter"
                },
                {
                    "name": "count",
                    "type": "int"
                }
            ],
            "ret": "messages.SearchCounter"
        },
        {
            "_": "urlAuthResultRequest",
            "cid": "92d33a0e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "request_write_access",
                    "type": "flags.0?true"
                },
                {
                    "name": "bot",
                    "type": "User"
                },
                {
                    "name": "domain",
                    "type": "string"
                }
            ],
            "ret": "UrlAuthResult"
        },
        {
            "_": "urlAuthResultAccepted",
            "cid": "8f8c0e4e",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "UrlAuthResult"
        },
        {
            "_": "urlAuthResultDefault",
            "cid": "a9d6db1f",
            "params": [],
            "ret": "UrlAuthResult"
        },
        {
            "_": "channelLocationEmpty",
            "cid": "bfb5ad8b",
            "params": [],
            "ret": "ChannelLocation"
        },
        {
            "_": "channelLocation",
            "cid": "209b82db",
            "params": [
                {
                    "name": "geo_point",
                    "type": "GeoPoint"
                },
                {
                    "name": "address",
                    "type": "string"
                }
            ],
            "ret": "ChannelLocation"
        },
        {
            "_": "peerLocated",
            "cid": "ca461b5d",
            "params": [
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "expires",
                    "type": "int"
                },
                {
                    "name": "distance",
                    "type": "int"
                }
            ],
            "ret": "PeerLocated"
        },
        {
            "_": "peerSelfLocated",
            "cid": "f8ec284b",
            "params": [
                {
                    "name": "expires",
                    "type": "int"
                }
            ],
            "ret": "PeerLocated"
        },
        {
            "_": "restrictionReason",
            "cid": "d072acb4",
            "params": [
                {
                    "name": "platform",
                    "type": "string"
                },
                {
                    "name": "reason",
                    "type": "string"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "RestrictionReason"
        },
        {
            "_": "inputTheme",
            "cid": "3c5693e9",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputTheme"
        },
        {
            "_": "inputThemeSlug",
            "cid": "f5890df1",
            "params": [
                {
                    "name": "slug",
                    "type": "string"
                }
            ],
            "ret": "InputTheme"
        },
        {
            "_": "theme",
            "cid": "a00e67d6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "creator",
                    "type": "flags.0?true"
                },
                {
                    "name": "default",
                    "type": "flags.1?true"
                },
                {
                    "name": "for_chat",
                    "type": "flags.5?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "slug",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "document",
                    "type": "flags.2?Document"
                },
                {
                    "name": "settings",
                    "type": "flags.3?Vector<ThemeSettings>"
                },
                {
                    "name": "emoticon",
                    "type": "flags.6?string"
                },
                {
                    "name": "installs_count",
                    "type": "flags.4?int"
                }
            ],
            "ret": "Theme"
        },
        {
            "_": "themesNotModified",
            "cid": "f41eb622",
            "params": [],
            "ret": "account.Themes"
        },
        {
            "_": "themes",
            "cid": "9a3d8c6d",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "themes",
                    "type": "Vector<Theme>"
                }
            ],
            "ret": "account.Themes"
        },
        {
            "_": "loginToken",
            "cid": "629f1980",
            "params": [
                {
                    "name": "expires",
                    "type": "int"
                },
                {
                    "name": "token",
                    "type": "bytes"
                }
            ],
            "ret": "auth.LoginToken"
        },
        {
            "_": "loginTokenMigrateTo",
            "cid": "68e9916",
            "params": [
                {
                    "name": "dc_id",
                    "type": "int"
                },
                {
                    "name": "token",
                    "type": "bytes"
                }
            ],
            "ret": "auth.LoginToken"
        },
        {
            "_": "loginTokenSuccess",
            "cid": "390d5c5e",
            "params": [
                {
                    "name": "authorization",
                    "type": "auth.Authorization"
                }
            ],
            "ret": "auth.LoginToken"
        },
        {
            "_": "contentSettings",
            "cid": "57e28221",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "sensitive_enabled",
                    "type": "flags.0?true"
                },
                {
                    "name": "sensitive_can_change",
                    "type": "flags.1?true"
                }
            ],
            "ret": "account.ContentSettings"
        },
        {
            "_": "inactiveChats",
            "cid": "a927fec5",
            "params": [
                {
                    "name": "dates",
                    "type": "Vector<int>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.InactiveChats"
        },
        {
            "_": "baseThemeClassic",
            "cid": "c3a12462",
            "params": [],
            "ret": "BaseTheme"
        },
        {
            "_": "baseThemeDay",
            "cid": "fbd81688",
            "params": [],
            "ret": "BaseTheme"
        },
        {
            "_": "baseThemeNight",
            "cid": "b7b31ea8",
            "params": [],
            "ret": "BaseTheme"
        },
        {
            "_": "baseThemeTinted",
            "cid": "6d5f77ee",
            "params": [],
            "ret": "BaseTheme"
        },
        {
            "_": "baseThemeArctic",
            "cid": "5b11125a",
            "params": [],
            "ret": "BaseTheme"
        },
        {
            "_": "inputThemeSettings",
            "cid": "8fde504f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "message_colors_animated",
                    "type": "flags.2?true"
                },
                {
                    "name": "base_theme",
                    "type": "BaseTheme"
                },
                {
                    "name": "accent_color",
                    "type": "int"
                },
                {
                    "name": "outbox_accent_color",
                    "type": "flags.3?int"
                },
                {
                    "name": "message_colors",
                    "type": "flags.0?Vector<int>"
                },
                {
                    "name": "wallpaper",
                    "type": "flags.1?InputWallPaper"
                },
                {
                    "name": "wallpaper_settings",
                    "type": "flags.1?WallPaperSettings"
                }
            ],
            "ret": "InputThemeSettings"
        },
        {
            "_": "themeSettings",
            "cid": "fa58b6d4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "message_colors_animated",
                    "type": "flags.2?true"
                },
                {
                    "name": "base_theme",
                    "type": "BaseTheme"
                },
                {
                    "name": "accent_color",
                    "type": "int"
                },
                {
                    "name": "outbox_accent_color",
                    "type": "flags.3?int"
                },
                {
                    "name": "message_colors",
                    "type": "flags.0?Vector<int>"
                },
                {
                    "name": "wallpaper",
                    "type": "flags.1?WallPaper"
                }
            ],
            "ret": "ThemeSettings"
        },
        {
            "_": "webPageAttributeTheme",
            "cid": "54b56617",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "documents",
                    "type": "flags.0?Vector<Document>"
                },
                {
                    "name": "settings",
                    "type": "flags.1?ThemeSettings"
                }
            ],
            "ret": "WebPageAttribute"
        },
        {
            "_": "messageUserVote",
            "cid": "34d247b4",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "option",
                    "type": "bytes"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "MessageUserVote"
        },
        {
            "_": "messageUserVoteInputOption",
            "cid": "3ca5b0ec",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "MessageUserVote"
        },
        {
            "_": "messageUserVoteMultiple",
            "cid": "8a65e557",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "options",
                    "type": "Vector<bytes>"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "MessageUserVote"
        },
        {
            "_": "votesList",
            "cid": "823f649",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "votes",
                    "type": "Vector<MessageUserVote>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "next_offset",
                    "type": "flags.0?string"
                }
            ],
            "ret": "messages.VotesList"
        },
        {
            "_": "bankCardOpenUrl",
            "cid": "f568028a",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "name",
                    "type": "string"
                }
            ],
            "ret": "BankCardOpenUrl"
        },
        {
            "_": "bankCardData",
            "cid": "3e24e573",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "open_urls",
                    "type": "Vector<BankCardOpenUrl>"
                }
            ],
            "ret": "payments.BankCardData"
        },
        {
            "_": "dialogFilter",
            "cid": "7438f7e8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "contacts",
                    "type": "flags.0?true"
                },
                {
                    "name": "non_contacts",
                    "type": "flags.1?true"
                },
                {
                    "name": "groups",
                    "type": "flags.2?true"
                },
                {
                    "name": "broadcasts",
                    "type": "flags.3?true"
                },
                {
                    "name": "bots",
                    "type": "flags.4?true"
                },
                {
                    "name": "exclude_muted",
                    "type": "flags.11?true"
                },
                {
                    "name": "exclude_read",
                    "type": "flags.12?true"
                },
                {
                    "name": "exclude_archived",
                    "type": "flags.13?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "emoticon",
                    "type": "flags.25?string"
                },
                {
                    "name": "pinned_peers",
                    "type": "Vector<InputPeer>"
                },
                {
                    "name": "include_peers",
                    "type": "Vector<InputPeer>"
                },
                {
                    "name": "exclude_peers",
                    "type": "Vector<InputPeer>"
                }
            ],
            "ret": "DialogFilter"
        },
        {
            "_": "dialogFilterDefault",
            "cid": "363293ae",
            "params": [],
            "ret": "DialogFilter"
        },
        {
            "_": "dialogFilterSuggested",
            "cid": "77744d4a",
            "params": [
                {
                    "name": "filter",
                    "type": "DialogFilter"
                },
                {
                    "name": "description",
                    "type": "string"
                }
            ],
            "ret": "DialogFilterSuggested"
        },
        {
            "_": "statsDateRangeDays",
            "cid": "b637edaf",
            "params": [
                {
                    "name": "min_date",
                    "type": "int"
                },
                {
                    "name": "max_date",
                    "type": "int"
                }
            ],
            "ret": "StatsDateRangeDays"
        },
        {
            "_": "statsAbsValueAndPrev",
            "cid": "cb43acde",
            "params": [
                {
                    "name": "current",
                    "type": "double"
                },
                {
                    "name": "previous",
                    "type": "double"
                }
            ],
            "ret": "StatsAbsValueAndPrev"
        },
        {
            "_": "statsPercentValue",
            "cid": "cbce2fe0",
            "params": [
                {
                    "name": "part",
                    "type": "double"
                },
                {
                    "name": "total",
                    "type": "double"
                }
            ],
            "ret": "StatsPercentValue"
        },
        {
            "_": "statsGraphAsync",
            "cid": "4a27eb2d",
            "params": [
                {
                    "name": "token",
                    "type": "string"
                }
            ],
            "ret": "StatsGraph"
        },
        {
            "_": "statsGraphError",
            "cid": "bedc9822",
            "params": [
                {
                    "name": "error",
                    "type": "string"
                }
            ],
            "ret": "StatsGraph"
        },
        {
            "_": "statsGraph",
            "cid": "8ea464b6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "json",
                    "type": "DataJSON"
                },
                {
                    "name": "zoom_token",
                    "type": "flags.0?string"
                }
            ],
            "ret": "StatsGraph"
        },
        {
            "_": "messageInteractionCounters",
            "cid": "ad4fc9bd",
            "params": [
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "views",
                    "type": "int"
                },
                {
                    "name": "forwards",
                    "type": "int"
                }
            ],
            "ret": "MessageInteractionCounters"
        },
        {
            "_": "broadcastStats",
            "cid": "bdf78394",
            "params": [
                {
                    "name": "period",
                    "type": "StatsDateRangeDays"
                },
                {
                    "name": "followers",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "views_per_post",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "shares_per_post",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "enabled_notifications",
                    "type": "StatsPercentValue"
                },
                {
                    "name": "growth_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "followers_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "mute_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "top_hours_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "interactions_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "iv_interactions_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "views_by_source_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "new_followers_by_source_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "languages_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "recent_message_interactions",
                    "type": "Vector<MessageInteractionCounters>"
                }
            ],
            "ret": "stats.BroadcastStats"
        },
        {
            "_": "promoDataEmpty",
            "cid": "98f6ac75",
            "params": [
                {
                    "name": "expires",
                    "type": "int"
                }
            ],
            "ret": "help.PromoData"
        },
        {
            "_": "promoData",
            "cid": "8c39793f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "proxy",
                    "type": "flags.0?true"
                },
                {
                    "name": "expires",
                    "type": "int"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "psa_type",
                    "type": "flags.1?string"
                },
                {
                    "name": "psa_message",
                    "type": "flags.2?string"
                }
            ],
            "ret": "help.PromoData"
        },
        {
            "_": "videoSize",
            "cid": "de33b094",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "type",
                    "type": "string"
                },
                {
                    "name": "w",
                    "type": "int"
                },
                {
                    "name": "h",
                    "type": "int"
                },
                {
                    "name": "size",
                    "type": "int"
                },
                {
                    "name": "video_start_ts",
                    "type": "flags.0?double"
                }
            ],
            "ret": "VideoSize"
        },
        {
            "_": "statsGroupTopPoster",
            "cid": "9d04af9b",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "messages",
                    "type": "int"
                },
                {
                    "name": "avg_chars",
                    "type": "int"
                }
            ],
            "ret": "StatsGroupTopPoster"
        },
        {
            "_": "statsGroupTopAdmin",
            "cid": "d7584c87",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "deleted",
                    "type": "int"
                },
                {
                    "name": "kicked",
                    "type": "int"
                },
                {
                    "name": "banned",
                    "type": "int"
                }
            ],
            "ret": "StatsGroupTopAdmin"
        },
        {
            "_": "statsGroupTopInviter",
            "cid": "535f779d",
            "params": [
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "invitations",
                    "type": "int"
                }
            ],
            "ret": "StatsGroupTopInviter"
        },
        {
            "_": "megagroupStats",
            "cid": "ef7ff916",
            "params": [
                {
                    "name": "period",
                    "type": "StatsDateRangeDays"
                },
                {
                    "name": "members",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "messages",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "viewers",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "posters",
                    "type": "StatsAbsValueAndPrev"
                },
                {
                    "name": "growth_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "members_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "new_members_by_source_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "languages_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "messages_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "actions_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "top_hours_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "weekdays_graph",
                    "type": "StatsGraph"
                },
                {
                    "name": "top_posters",
                    "type": "Vector<StatsGroupTopPoster>"
                },
                {
                    "name": "top_admins",
                    "type": "Vector<StatsGroupTopAdmin>"
                },
                {
                    "name": "top_inviters",
                    "type": "Vector<StatsGroupTopInviter>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "stats.MegagroupStats"
        },
        {
            "_": "globalPrivacySettings",
            "cid": "bea2f424",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "archive_and_mute_new_noncontact_peers",
                    "type": "flags.0?Bool"
                }
            ],
            "ret": "GlobalPrivacySettings"
        },
        {
            "_": "countryCode",
            "cid": "4203c5ef",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "country_code",
                    "type": "string"
                },
                {
                    "name": "prefixes",
                    "type": "flags.0?Vector<string>"
                },
                {
                    "name": "patterns",
                    "type": "flags.1?Vector<string>"
                }
            ],
            "ret": "help.CountryCode"
        },
        {
            "_": "country",
            "cid": "c3878e23",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "hidden",
                    "type": "flags.0?true"
                },
                {
                    "name": "iso2",
                    "type": "string"
                },
                {
                    "name": "default_name",
                    "type": "string"
                },
                {
                    "name": "name",
                    "type": "flags.1?string"
                },
                {
                    "name": "country_codes",
                    "type": "Vector<help.CountryCode>"
                }
            ],
            "ret": "help.Country"
        },
        {
            "_": "countriesListNotModified",
            "cid": "93cc1f32",
            "params": [],
            "ret": "help.CountriesList"
        },
        {
            "_": "countriesList",
            "cid": "87d0759e",
            "params": [
                {
                    "name": "countries",
                    "type": "Vector<help.Country>"
                },
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "help.CountriesList"
        },
        {
            "_": "messageViews",
            "cid": "455b853d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "views",
                    "type": "flags.0?int"
                },
                {
                    "name": "forwards",
                    "type": "flags.1?int"
                },
                {
                    "name": "replies",
                    "type": "flags.2?MessageReplies"
                }
            ],
            "ret": "MessageViews"
        },
        {
            "_": "messageViews",
            "cid": "b6c4f543",
            "params": [
                {
                    "name": "views",
                    "type": "Vector<MessageViews>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.MessageViews"
        },
        {
            "_": "discussionMessage",
            "cid": "a6341782",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "max_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "read_inbox_max_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "read_outbox_max_id",
                    "type": "flags.2?int"
                },
                {
                    "name": "unread_count",
                    "type": "int"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.DiscussionMessage"
        },
        {
            "_": "messageReplyHeader",
            "cid": "a6d57763",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "reply_to_scheduled",
                    "type": "flags.2?true"
                },
                {
                    "name": "forum_topic",
                    "type": "flags.3?true"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "int"
                },
                {
                    "name": "reply_to_peer_id",
                    "type": "flags.0?Peer"
                },
                {
                    "name": "reply_to_top_id",
                    "type": "flags.1?int"
                }
            ],
            "ret": "MessageReplyHeader"
        },
        {
            "_": "messageReplies",
            "cid": "83d60fc2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "comments",
                    "type": "flags.0?true"
                },
                {
                    "name": "replies",
                    "type": "int"
                },
                {
                    "name": "replies_pts",
                    "type": "int"
                },
                {
                    "name": "recent_repliers",
                    "type": "flags.1?Vector<Peer>"
                },
                {
                    "name": "channel_id",
                    "type": "flags.0?long"
                },
                {
                    "name": "max_id",
                    "type": "flags.2?int"
                },
                {
                    "name": "read_max_id",
                    "type": "flags.3?int"
                }
            ],
            "ret": "MessageReplies"
        },
        {
            "_": "peerBlocked",
            "cid": "e8fd8014",
            "params": [
                {
                    "name": "peer_id",
                    "type": "Peer"
                },
                {
                    "name": "date",
                    "type": "int"
                }
            ],
            "ret": "PeerBlocked"
        },
        {
            "_": "messageStats",
            "cid": "8999f295",
            "params": [
                {
                    "name": "views_graph",
                    "type": "StatsGraph"
                }
            ],
            "ret": "stats.MessageStats"
        },
        {
            "_": "groupCallDiscarded",
            "cid": "7780bcb4",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "duration",
                    "type": "int"
                }
            ],
            "ret": "GroupCall"
        },
        {
            "_": "groupCall",
            "cid": "d597650c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "join_muted",
                    "type": "flags.1?true"
                },
                {
                    "name": "can_change_join_muted",
                    "type": "flags.2?true"
                },
                {
                    "name": "join_date_asc",
                    "type": "flags.6?true"
                },
                {
                    "name": "schedule_start_subscribed",
                    "type": "flags.8?true"
                },
                {
                    "name": "can_start_video",
                    "type": "flags.9?true"
                },
                {
                    "name": "record_video_active",
                    "type": "flags.11?true"
                },
                {
                    "name": "rtmp_stream",
                    "type": "flags.12?true"
                },
                {
                    "name": "listeners_hidden",
                    "type": "flags.13?true"
                },
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                },
                {
                    "name": "participants_count",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "flags.3?string"
                },
                {
                    "name": "stream_dc_id",
                    "type": "flags.4?int"
                },
                {
                    "name": "record_start_date",
                    "type": "flags.5?int"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.7?int"
                },
                {
                    "name": "unmuted_video_count",
                    "type": "flags.10?int"
                },
                {
                    "name": "unmuted_video_limit",
                    "type": "int"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "GroupCall"
        },
        {
            "_": "inputGroupCall",
            "cid": "d8aa840f",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "access_hash",
                    "type": "long"
                }
            ],
            "ret": "InputGroupCall"
        },
        {
            "_": "groupCallParticipant",
            "cid": "eba636fe",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "muted",
                    "type": "flags.0?true"
                },
                {
                    "name": "left",
                    "type": "flags.1?true"
                },
                {
                    "name": "can_self_unmute",
                    "type": "flags.2?true"
                },
                {
                    "name": "just_joined",
                    "type": "flags.4?true"
                },
                {
                    "name": "versioned",
                    "type": "flags.5?true"
                },
                {
                    "name": "min",
                    "type": "flags.8?true"
                },
                {
                    "name": "muted_by_you",
                    "type": "flags.9?true"
                },
                {
                    "name": "volume_by_admin",
                    "type": "flags.10?true"
                },
                {
                    "name": "self",
                    "type": "flags.12?true"
                },
                {
                    "name": "video_joined",
                    "type": "flags.15?true"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "active_date",
                    "type": "flags.3?int"
                },
                {
                    "name": "source",
                    "type": "int"
                },
                {
                    "name": "volume",
                    "type": "flags.7?int"
                },
                {
                    "name": "about",
                    "type": "flags.11?string"
                },
                {
                    "name": "raise_hand_rating",
                    "type": "flags.13?long"
                },
                {
                    "name": "video",
                    "type": "flags.6?GroupCallParticipantVideo"
                },
                {
                    "name": "presentation",
                    "type": "flags.14?GroupCallParticipantVideo"
                }
            ],
            "ret": "GroupCallParticipant"
        },
        {
            "_": "groupCall",
            "cid": "9e727aad",
            "params": [
                {
                    "name": "call",
                    "type": "GroupCall"
                },
                {
                    "name": "participants",
                    "type": "Vector<GroupCallParticipant>"
                },
                {
                    "name": "participants_next_offset",
                    "type": "string"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "phone.GroupCall"
        },
        {
            "_": "groupParticipants",
            "cid": "f47751b6",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "participants",
                    "type": "Vector<GroupCallParticipant>"
                },
                {
                    "name": "next_offset",
                    "type": "string"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "version",
                    "type": "int"
                }
            ],
            "ret": "phone.GroupParticipants"
        },
        {
            "_": "inlineQueryPeerTypeSameBotPM",
            "cid": "3081ed9d",
            "params": [],
            "ret": "InlineQueryPeerType"
        },
        {
            "_": "inlineQueryPeerTypePM",
            "cid": "833c0fac",
            "params": [],
            "ret": "InlineQueryPeerType"
        },
        {
            "_": "inlineQueryPeerTypeChat",
            "cid": "d766c50a",
            "params": [],
            "ret": "InlineQueryPeerType"
        },
        {
            "_": "inlineQueryPeerTypeMegagroup",
            "cid": "5ec4be43",
            "params": [],
            "ret": "InlineQueryPeerType"
        },
        {
            "_": "inlineQueryPeerTypeBroadcast",
            "cid": "6334ee9a",
            "params": [],
            "ret": "InlineQueryPeerType"
        },
        {
            "_": "historyImport",
            "cid": "1662af0b",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "messages.HistoryImport"
        },
        {
            "_": "historyImportParsed",
            "cid": "5e0fb7b9",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pm",
                    "type": "flags.0?true"
                },
                {
                    "name": "group",
                    "type": "flags.1?true"
                },
                {
                    "name": "title",
                    "type": "flags.2?string"
                }
            ],
            "ret": "messages.HistoryImportParsed"
        },
        {
            "_": "affectedFoundMessages",
            "cid": "ef8d3e6c",
            "params": [
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_count",
                    "type": "int"
                },
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "messages",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.AffectedFoundMessages"
        },
        {
            "_": "chatInviteImporter",
            "cid": "8c5adfd9",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "requested",
                    "type": "flags.0?true"
                },
                {
                    "name": "user_id",
                    "type": "long"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "about",
                    "type": "flags.2?string"
                },
                {
                    "name": "approved_by",
                    "type": "flags.1?long"
                }
            ],
            "ret": "ChatInviteImporter"
        },
        {
            "_": "exportedChatInvites",
            "cid": "bdc62dcc",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "invites",
                    "type": "Vector<ExportedChatInvite>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.ExportedChatInvites"
        },
        {
            "_": "exportedChatInvite",
            "cid": "1871be50",
            "params": [
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.ExportedChatInvite"
        },
        {
            "_": "exportedChatInviteReplaced",
            "cid": "222600ef",
            "params": [
                {
                    "name": "invite",
                    "type": "ExportedChatInvite"
                },
                {
                    "name": "new_invite",
                    "type": "ExportedChatInvite"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.ExportedChatInvite"
        },
        {
            "_": "chatInviteImporters",
            "cid": "81b6b00a",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "importers",
                    "type": "Vector<ChatInviteImporter>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.ChatInviteImporters"
        },
        {
            "_": "chatAdminWithInvites",
            "cid": "f2ecef23",
            "params": [
                {
                    "name": "admin_id",
                    "type": "long"
                },
                {
                    "name": "invites_count",
                    "type": "int"
                },
                {
                    "name": "revoked_invites_count",
                    "type": "int"
                }
            ],
            "ret": "ChatAdminWithInvites"
        },
        {
            "_": "chatAdminsWithInvites",
            "cid": "b69b72d7",
            "params": [
                {
                    "name": "admins",
                    "type": "Vector<ChatAdminWithInvites>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.ChatAdminsWithInvites"
        },
        {
            "_": "checkedHistoryImportPeer",
            "cid": "a24de717",
            "params": [
                {
                    "name": "confirm_text",
                    "type": "string"
                }
            ],
            "ret": "messages.CheckedHistoryImportPeer"
        },
        {
            "_": "joinAsPeers",
            "cid": "afe5623f",
            "params": [
                {
                    "name": "peers",
                    "type": "Vector<Peer>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "phone.JoinAsPeers"
        },
        {
            "_": "exportedGroupCallInvite",
            "cid": "204bd158",
            "params": [
                {
                    "name": "link",
                    "type": "string"
                }
            ],
            "ret": "phone.ExportedGroupCallInvite"
        },
        {
            "_": "groupCallParticipantVideoSourceGroup",
            "cid": "dcb118b7",
            "params": [
                {
                    "name": "semantics",
                    "type": "string"
                },
                {
                    "name": "sources",
                    "type": "Vector<int>"
                }
            ],
            "ret": "GroupCallParticipantVideoSourceGroup"
        },
        {
            "_": "groupCallParticipantVideo",
            "cid": "67753ac8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "paused",
                    "type": "flags.0?true"
                },
                {
                    "name": "endpoint",
                    "type": "string"
                },
                {
                    "name": "source_groups",
                    "type": "Vector<GroupCallParticipantVideoSourceGroup>"
                },
                {
                    "name": "audio_source",
                    "type": "flags.1?int"
                }
            ],
            "ret": "GroupCallParticipantVideo"
        },
        {
            "_": "suggestedShortName",
            "cid": "85fea03f",
            "params": [
                {
                    "name": "short_name",
                    "type": "string"
                }
            ],
            "ret": "stickers.SuggestedShortName"
        },
        {
            "_": "botCommandScopeDefault",
            "cid": "2f6cb2ab",
            "params": [],
            "ret": "BotCommandScope"
        },
        {
            "_": "botCommandScopeUsers",
            "cid": "3c4f04d8",
            "params": [],
            "ret": "BotCommandScope"
        },
        {
            "_": "botCommandScopeChats",
            "cid": "6fe1a881",
            "params": [],
            "ret": "BotCommandScope"
        },
        {
            "_": "botCommandScopeChatAdmins",
            "cid": "b9aa606a",
            "params": [],
            "ret": "BotCommandScope"
        },
        {
            "_": "botCommandScopePeer",
            "cid": "db9d897d",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "BotCommandScope"
        },
        {
            "_": "botCommandScopePeerAdmins",
            "cid": "3fd863d1",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "BotCommandScope"
        },
        {
            "_": "botCommandScopePeerUser",
            "cid": "a1321f3",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "BotCommandScope"
        },
        {
            "_": "resetPasswordFailedWait",
            "cid": "e3779861",
            "params": [
                {
                    "name": "retry_date",
                    "type": "int"
                }
            ],
            "ret": "account.ResetPasswordResult"
        },
        {
            "_": "resetPasswordRequestedWait",
            "cid": "e9effc7d",
            "params": [
                {
                    "name": "until_date",
                    "type": "int"
                }
            ],
            "ret": "account.ResetPasswordResult"
        },
        {
            "_": "resetPasswordOk",
            "cid": "e926d63e",
            "params": [],
            "ret": "account.ResetPasswordResult"
        },
        {
            "_": "sponsoredMessage",
            "cid": "3a836df8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "recommended",
                    "type": "flags.5?true"
                },
                {
                    "name": "show_peer_photo",
                    "type": "flags.6?true"
                },
                {
                    "name": "random_id",
                    "type": "bytes"
                },
                {
                    "name": "from_id",
                    "type": "flags.3?Peer"
                },
                {
                    "name": "chat_invite",
                    "type": "flags.4?ChatInvite"
                },
                {
                    "name": "chat_invite_hash",
                    "type": "flags.4?string"
                },
                {
                    "name": "channel_post",
                    "type": "flags.2?int"
                },
                {
                    "name": "start_param",
                    "type": "flags.0?string"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.1?Vector<MessageEntity>"
                }
            ],
            "ret": "SponsoredMessage"
        },
        {
            "_": "sponsoredMessages",
            "cid": "c9ee1d87",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "posts_between",
                    "type": "flags.0?int"
                },
                {
                    "name": "messages",
                    "type": "Vector<SponsoredMessage>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.SponsoredMessages"
        },
        {
            "_": "sponsoredMessagesEmpty",
            "cid": "1839490f",
            "params": [],
            "ret": "messages.SponsoredMessages"
        },
        {
            "_": "searchResultsCalendarPeriod",
            "cid": "c9b0539f",
            "params": [
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "min_msg_id",
                    "type": "int"
                },
                {
                    "name": "max_msg_id",
                    "type": "int"
                },
                {
                    "name": "count",
                    "type": "int"
                }
            ],
            "ret": "SearchResultsCalendarPeriod"
        },
        {
            "_": "searchResultsCalendar",
            "cid": "147ee23c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "inexact",
                    "type": "flags.0?true"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "min_date",
                    "type": "int"
                },
                {
                    "name": "min_msg_id",
                    "type": "int"
                },
                {
                    "name": "offset_id_offset",
                    "type": "flags.1?int"
                },
                {
                    "name": "periods",
                    "type": "Vector<SearchResultsCalendarPeriod>"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.SearchResultsCalendar"
        },
        {
            "_": "searchResultPosition",
            "cid": "7f648b67",
            "params": [
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "offset",
                    "type": "int"
                }
            ],
            "ret": "SearchResultsPosition"
        },
        {
            "_": "searchResultsPositions",
            "cid": "53b22baf",
            "params": [
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "positions",
                    "type": "Vector<SearchResultsPosition>"
                }
            ],
            "ret": "messages.SearchResultsPositions"
        },
        {
            "_": "sendAsPeers",
            "cid": "f496b0c6",
            "params": [
                {
                    "name": "peers",
                    "type": "Vector<SendAsPeer>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "channels.SendAsPeers"
        },
        {
            "_": "userFull",
            "cid": "3b6d152e",
            "params": [
                {
                    "name": "full_user",
                    "type": "UserFull"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "users.UserFull"
        },
        {
            "_": "peerSettings",
            "cid": "6880b94d",
            "params": [
                {
                    "name": "settings",
                    "type": "PeerSettings"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "messages.PeerSettings"
        },
        {
            "_": "loggedOut",
            "cid": "c3a2835f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "future_auth_token",
                    "type": "flags.0?bytes"
                }
            ],
            "ret": "auth.LoggedOut"
        },
        {
            "_": "reactionCount",
            "cid": "a3d1cb80",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "chosen_order",
                    "type": "flags.0?int"
                },
                {
                    "name": "reaction",
                    "type": "Reaction"
                },
                {
                    "name": "count",
                    "type": "int"
                }
            ],
            "ret": "ReactionCount"
        },
        {
            "_": "messageReactions",
            "cid": "4f2b9479",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "min",
                    "type": "flags.0?true"
                },
                {
                    "name": "can_see_list",
                    "type": "flags.2?true"
                },
                {
                    "name": "results",
                    "type": "Vector<ReactionCount>"
                },
                {
                    "name": "recent_reactions",
                    "type": "flags.1?Vector<MessagePeerReaction>"
                }
            ],
            "ret": "MessageReactions"
        },
        {
            "_": "messageReactionsList",
            "cid": "31bd492d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "reactions",
                    "type": "Vector<MessagePeerReaction>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "next_offset",
                    "type": "flags.0?string"
                }
            ],
            "ret": "messages.MessageReactionsList"
        },
        {
            "_": "availableReaction",
            "cid": "c077ec01",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "inactive",
                    "type": "flags.0?true"
                },
                {
                    "name": "premium",
                    "type": "flags.2?true"
                },
                {
                    "name": "reaction",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "static_icon",
                    "type": "Document"
                },
                {
                    "name": "appear_animation",
                    "type": "Document"
                },
                {
                    "name": "select_animation",
                    "type": "Document"
                },
                {
                    "name": "activate_animation",
                    "type": "Document"
                },
                {
                    "name": "effect_animation",
                    "type": "Document"
                },
                {
                    "name": "around_animation",
                    "type": "flags.1?Document"
                },
                {
                    "name": "center_icon",
                    "type": "flags.1?Document"
                }
            ],
            "ret": "AvailableReaction"
        },
        {
            "_": "availableReactionsNotModified",
            "cid": "9f071957",
            "params": [],
            "ret": "messages.AvailableReactions"
        },
        {
            "_": "availableReactions",
            "cid": "768e3aad",
            "params": [
                {
                    "name": "hash",
                    "type": "int"
                },
                {
                    "name": "reactions",
                    "type": "Vector<AvailableReaction>"
                }
            ],
            "ret": "messages.AvailableReactions"
        },
        {
            "_": "translateNoResult",
            "cid": "67ca4737",
            "params": [],
            "ret": "messages.TranslatedText"
        },
        {
            "_": "translateResultText",
            "cid": "a214f7d0",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "messages.TranslatedText"
        },
        {
            "_": "messagePeerReaction",
            "cid": "b156fe9c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "big",
                    "type": "flags.0?true"
                },
                {
                    "name": "unread",
                    "type": "flags.1?true"
                },
                {
                    "name": "peer_id",
                    "type": "Peer"
                },
                {
                    "name": "reaction",
                    "type": "Reaction"
                }
            ],
            "ret": "MessagePeerReaction"
        },
        {
            "_": "groupCallStreamChannel",
            "cid": "80eb48af",
            "params": [
                {
                    "name": "channel",
                    "type": "int"
                },
                {
                    "name": "scale",
                    "type": "int"
                },
                {
                    "name": "last_timestamp_ms",
                    "type": "long"
                }
            ],
            "ret": "GroupCallStreamChannel"
        },
        {
            "_": "groupCallStreamChannels",
            "cid": "d0e482b2",
            "params": [
                {
                    "name": "channels",
                    "type": "Vector<GroupCallStreamChannel>"
                }
            ],
            "ret": "phone.GroupCallStreamChannels"
        },
        {
            "_": "groupCallStreamRtmpUrl",
            "cid": "2dbf3432",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "key",
                    "type": "string"
                }
            ],
            "ret": "phone.GroupCallStreamRtmpUrl"
        },
        {
            "_": "attachMenuBotIconColor",
            "cid": "4576f3f0",
            "params": [
                {
                    "name": "name",
                    "type": "string"
                },
                {
                    "name": "color",
                    "type": "int"
                }
            ],
            "ret": "AttachMenuBotIconColor"
        },
        {
            "_": "attachMenuBotIcon",
            "cid": "b2a7386b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "name",
                    "type": "string"
                },
                {
                    "name": "icon",
                    "type": "Document"
                },
                {
                    "name": "colors",
                    "type": "flags.0?Vector<AttachMenuBotIconColor>"
                }
            ],
            "ret": "AttachMenuBotIcon"
        },
        {
            "_": "attachMenuBot",
            "cid": "c8aa2cd2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "inactive",
                    "type": "flags.0?true"
                },
                {
                    "name": "has_settings",
                    "type": "flags.1?true"
                },
                {
                    "name": "request_write_access",
                    "type": "flags.2?true"
                },
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "short_name",
                    "type": "string"
                },
                {
                    "name": "peer_types",
                    "type": "Vector<AttachMenuPeerType>"
                },
                {
                    "name": "icons",
                    "type": "Vector<AttachMenuBotIcon>"
                }
            ],
            "ret": "AttachMenuBot"
        },
        {
            "_": "attachMenuBotsNotModified",
            "cid": "f1d88a5c",
            "params": [],
            "ret": "AttachMenuBots"
        },
        {
            "_": "attachMenuBots",
            "cid": "3c4301c0",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "bots",
                    "type": "Vector<AttachMenuBot>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "AttachMenuBots"
        },
        {
            "_": "attachMenuBotsBot",
            "cid": "93bf667f",
            "params": [
                {
                    "name": "bot",
                    "type": "AttachMenuBot"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "AttachMenuBotsBot"
        },
        {
            "_": "webViewResultUrl",
            "cid": "c14557c",
            "params": [
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "WebViewResult"
        },
        {
            "_": "simpleWebViewResultUrl",
            "cid": "882f76bb",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "SimpleWebViewResult"
        },
        {
            "_": "webViewMessageSent",
            "cid": "c94511c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "msg_id",
                    "type": "flags.0?InputBotInlineMessageID"
                }
            ],
            "ret": "WebViewMessageSent"
        },
        {
            "_": "botMenuButtonDefault",
            "cid": "7533a588",
            "params": [],
            "ret": "BotMenuButton"
        },
        {
            "_": "botMenuButtonCommands",
            "cid": "4258c205",
            "params": [],
            "ret": "BotMenuButton"
        },
        {
            "_": "botMenuButton",
            "cid": "c7b57ce6",
            "params": [
                {
                    "name": "text",
                    "type": "string"
                },
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "BotMenuButton"
        },
        {
            "_": "savedRingtonesNotModified",
            "cid": "fbf6e8b1",
            "params": [],
            "ret": "account.SavedRingtones"
        },
        {
            "_": "savedRingtones",
            "cid": "c1e92cc5",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "ringtones",
                    "type": "Vector<Document>"
                }
            ],
            "ret": "account.SavedRingtones"
        },
        {
            "_": "notificationSoundDefault",
            "cid": "97e8bebe",
            "params": [],
            "ret": "NotificationSound"
        },
        {
            "_": "notificationSoundNone",
            "cid": "6f0c34df",
            "params": [],
            "ret": "NotificationSound"
        },
        {
            "_": "notificationSoundLocal",
            "cid": "830b9ae4",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "data",
                    "type": "string"
                }
            ],
            "ret": "NotificationSound"
        },
        {
            "_": "notificationSoundRingtone",
            "cid": "ff6c8049",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                }
            ],
            "ret": "NotificationSound"
        },
        {
            "_": "savedRingtone",
            "cid": "b7263f6d",
            "params": [],
            "ret": "account.SavedRingtone"
        },
        {
            "_": "savedRingtoneConverted",
            "cid": "1f307eb7",
            "params": [
                {
                    "name": "document",
                    "type": "Document"
                }
            ],
            "ret": "account.SavedRingtone"
        },
        {
            "_": "attachMenuPeerTypeSameBotPM",
            "cid": "7d6be90e",
            "params": [],
            "ret": "AttachMenuPeerType"
        },
        {
            "_": "attachMenuPeerTypeBotPM",
            "cid": "c32bfa1a",
            "params": [],
            "ret": "AttachMenuPeerType"
        },
        {
            "_": "attachMenuPeerTypePM",
            "cid": "f146d31f",
            "params": [],
            "ret": "AttachMenuPeerType"
        },
        {
            "_": "attachMenuPeerTypeChat",
            "cid": "509113f",
            "params": [],
            "ret": "AttachMenuPeerType"
        },
        {
            "_": "attachMenuPeerTypeBroadcast",
            "cid": "7bfbdefc",
            "params": [],
            "ret": "AttachMenuPeerType"
        },
        {
            "_": "inputInvoiceMessage",
            "cid": "c5b56859",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "InputInvoice"
        },
        {
            "_": "inputInvoiceSlug",
            "cid": "c326caef",
            "params": [
                {
                    "name": "slug",
                    "type": "string"
                }
            ],
            "ret": "InputInvoice"
        },
        {
            "_": "exportedInvoice",
            "cid": "aed0cbd9",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                }
            ],
            "ret": "payments.ExportedInvoice"
        },
        {
            "_": "transcribedAudio",
            "cid": "93752c52",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pending",
                    "type": "flags.0?true"
                },
                {
                    "name": "transcription_id",
                    "type": "long"
                },
                {
                    "name": "text",
                    "type": "string"
                }
            ],
            "ret": "messages.TranscribedAudio"
        },
        {
            "_": "premiumPromo",
            "cid": "5334759c",
            "params": [
                {
                    "name": "status_text",
                    "type": "string"
                },
                {
                    "name": "status_entities",
                    "type": "Vector<MessageEntity>"
                },
                {
                    "name": "video_sections",
                    "type": "Vector<string>"
                },
                {
                    "name": "videos",
                    "type": "Vector<Document>"
                },
                {
                    "name": "period_options",
                    "type": "Vector<PremiumSubscriptionOption>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                }
            ],
            "ret": "help.PremiumPromo"
        },
        {
            "_": "inputStorePaymentPremiumSubscription",
            "cid": "a6751e66",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "restore",
                    "type": "flags.0?true"
                }
            ],
            "ret": "InputStorePaymentPurpose"
        },
        {
            "_": "inputStorePaymentGiftPremium",
            "cid": "616f7fe8",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "amount",
                    "type": "long"
                }
            ],
            "ret": "InputStorePaymentPurpose"
        },
        {
            "_": "premiumGiftOption",
            "cid": "74c34319",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "months",
                    "type": "int"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "amount",
                    "type": "long"
                },
                {
                    "name": "bot_url",
                    "type": "string"
                },
                {
                    "name": "store_product",
                    "type": "flags.0?string"
                }
            ],
            "ret": "PremiumGiftOption"
        },
        {
            "_": "paymentFormMethod",
            "cid": "88f8f21b",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "PaymentFormMethod"
        },
        {
            "_": "emojiStatusEmpty",
            "cid": "2de11aae",
            "params": [],
            "ret": "EmojiStatus"
        },
        {
            "_": "emojiStatus",
            "cid": "929b619d",
            "params": [
                {
                    "name": "document_id",
                    "type": "long"
                }
            ],
            "ret": "EmojiStatus"
        },
        {
            "_": "emojiStatusUntil",
            "cid": "fa30a8c7",
            "params": [
                {
                    "name": "document_id",
                    "type": "long"
                },
                {
                    "name": "until",
                    "type": "int"
                }
            ],
            "ret": "EmojiStatus"
        },
        {
            "_": "emojiStatusesNotModified",
            "cid": "d08ce645",
            "params": [],
            "ret": "account.EmojiStatuses"
        },
        {
            "_": "emojiStatuses",
            "cid": "90c467d1",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "statuses",
                    "type": "Vector<EmojiStatus>"
                }
            ],
            "ret": "account.EmojiStatuses"
        },
        {
            "_": "reactionEmpty",
            "cid": "79f5d419",
            "params": [],
            "ret": "Reaction"
        },
        {
            "_": "reactionEmoji",
            "cid": "1b2286b8",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "Reaction"
        },
        {
            "_": "reactionCustomEmoji",
            "cid": "8935fc73",
            "params": [
                {
                    "name": "document_id",
                    "type": "long"
                }
            ],
            "ret": "Reaction"
        },
        {
            "_": "chatReactionsNone",
            "cid": "eafc32bc",
            "params": [],
            "ret": "ChatReactions"
        },
        {
            "_": "chatReactionsAll",
            "cid": "52928bca",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "allow_custom",
                    "type": "flags.0?true"
                }
            ],
            "ret": "ChatReactions"
        },
        {
            "_": "chatReactionsSome",
            "cid": "661d4037",
            "params": [
                {
                    "name": "reactions",
                    "type": "Vector<Reaction>"
                }
            ],
            "ret": "ChatReactions"
        },
        {
            "_": "reactionsNotModified",
            "cid": "b06fdbdf",
            "params": [],
            "ret": "messages.Reactions"
        },
        {
            "_": "reactions",
            "cid": "eafdf716",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "reactions",
                    "type": "Vector<Reaction>"
                }
            ],
            "ret": "messages.Reactions"
        },
        {
            "_": "emailVerifyPurposeLoginSetup",
            "cid": "4345be73",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                }
            ],
            "ret": "EmailVerifyPurpose"
        },
        {
            "_": "emailVerifyPurposeLoginChange",
            "cid": "527d22eb",
            "params": [],
            "ret": "EmailVerifyPurpose"
        },
        {
            "_": "emailVerifyPurposePassport",
            "cid": "bbf51685",
            "params": [],
            "ret": "EmailVerifyPurpose"
        },
        {
            "_": "emailVerificationCode",
            "cid": "922e55a9",
            "params": [
                {
                    "name": "code",
                    "type": "string"
                }
            ],
            "ret": "EmailVerification"
        },
        {
            "_": "emailVerificationGoogle",
            "cid": "db909ec2",
            "params": [
                {
                    "name": "token",
                    "type": "string"
                }
            ],
            "ret": "EmailVerification"
        },
        {
            "_": "emailVerificationApple",
            "cid": "96d074fd",
            "params": [
                {
                    "name": "token",
                    "type": "string"
                }
            ],
            "ret": "EmailVerification"
        },
        {
            "_": "emailVerified",
            "cid": "2b96cd1b",
            "params": [
                {
                    "name": "email",
                    "type": "string"
                }
            ],
            "ret": "account.EmailVerified"
        },
        {
            "_": "emailVerifiedLogin",
            "cid": "e1bb0d61",
            "params": [
                {
                    "name": "email",
                    "type": "string"
                },
                {
                    "name": "sent_code",
                    "type": "auth.SentCode"
                }
            ],
            "ret": "account.EmailVerified"
        },
        {
            "_": "premiumSubscriptionOption",
            "cid": "b6f11ebe",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "current",
                    "type": "flags.1?true"
                },
                {
                    "name": "can_purchase_upgrade",
                    "type": "flags.2?true"
                },
                {
                    "name": "months",
                    "type": "int"
                },
                {
                    "name": "currency",
                    "type": "string"
                },
                {
                    "name": "amount",
                    "type": "long"
                },
                {
                    "name": "bot_url",
                    "type": "string"
                },
                {
                    "name": "store_product",
                    "type": "flags.0?string"
                }
            ],
            "ret": "PremiumSubscriptionOption"
        },
        {
            "_": "sendAsPeer",
            "cid": "b81c7034",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "premium_required",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "Peer"
                }
            ],
            "ret": "SendAsPeer"
        },
        {
            "_": "messageExtendedMediaPreview",
            "cid": "ad628cc8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "w",
                    "type": "flags.0?int"
                },
                {
                    "name": "h",
                    "type": "flags.0?int"
                },
                {
                    "name": "thumb",
                    "type": "flags.1?PhotoSize"
                },
                {
                    "name": "video_duration",
                    "type": "flags.2?int"
                }
            ],
            "ret": "MessageExtendedMedia"
        },
        {
            "_": "messageExtendedMedia",
            "cid": "ee479c64",
            "params": [
                {
                    "name": "media",
                    "type": "MessageMedia"
                }
            ],
            "ret": "MessageExtendedMedia"
        },
        {
            "_": "stickerKeyword",
            "cid": "fcfeb29c",
            "params": [
                {
                    "name": "document_id",
                    "type": "long"
                },
                {
                    "name": "keyword",
                    "type": "Vector<string>"
                }
            ],
            "ret": "StickerKeyword"
        },
        {
            "_": "username",
            "cid": "b4073647",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "editable",
                    "type": "flags.0?true"
                },
                {
                    "name": "active",
                    "type": "flags.1?true"
                },
                {
                    "name": "username",
                    "type": "string"
                }
            ],
            "ret": "Username"
        },
        {
            "_": "forumTopicDeleted",
            "cid": "23f109b",
            "params": [
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "ForumTopic"
        },
        {
            "_": "forumTopic",
            "cid": "71701da9",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "my",
                    "type": "flags.1?true"
                },
                {
                    "name": "closed",
                    "type": "flags.2?true"
                },
                {
                    "name": "pinned",
                    "type": "flags.3?true"
                },
                {
                    "name": "short",
                    "type": "flags.5?true"
                },
                {
                    "name": "hidden",
                    "type": "flags.6?true"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "icon_color",
                    "type": "int"
                },
                {
                    "name": "icon_emoji_id",
                    "type": "flags.0?long"
                },
                {
                    "name": "top_message",
                    "type": "int"
                },
                {
                    "name": "read_inbox_max_id",
                    "type": "int"
                },
                {
                    "name": "read_outbox_max_id",
                    "type": "int"
                },
                {
                    "name": "unread_count",
                    "type": "int"
                },
                {
                    "name": "unread_mentions_count",
                    "type": "int"
                },
                {
                    "name": "unread_reactions_count",
                    "type": "int"
                },
                {
                    "name": "from_id",
                    "type": "Peer"
                },
                {
                    "name": "notify_settings",
                    "type": "PeerNotifySettings"
                },
                {
                    "name": "draft",
                    "type": "flags.4?DraftMessage"
                }
            ],
            "ret": "ForumTopic"
        },
        {
            "_": "forumTopics",
            "cid": "367617d3",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "order_by_create_date",
                    "type": "flags.0?true"
                },
                {
                    "name": "count",
                    "type": "int"
                },
                {
                    "name": "topics",
                    "type": "Vector<ForumTopic>"
                },
                {
                    "name": "messages",
                    "type": "Vector<Message>"
                },
                {
                    "name": "chats",
                    "type": "Vector<Chat>"
                },
                {
                    "name": "users",
                    "type": "Vector<User>"
                },
                {
                    "name": "pts",
                    "type": "int"
                }
            ],
            "ret": "messages.ForumTopics"
        },
        {
            "_": "defaultHistoryTTL",
            "cid": "43b46b20",
            "params": [
                {
                    "name": "period",
                    "type": "int"
                }
            ],
            "ret": "DefaultHistoryTTL"
        },
        {
            "_": "exportedContactToken",
            "cid": "41bf109b",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "expires",
                    "type": "int"
                }
            ],
            "ret": "ExportedContactToken"
        }
    ],
    "functions": [
        {
            "_": "invokeAfterMsg",
            "cid": "cb9f372d",
            "params": [
                {
                    "name": "msg_id",
                    "type": "long"
                },
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "invokeAfterMsgs",
            "cid": "3dc4b4f0",
            "params": [
                {
                    "name": "msg_ids",
                    "type": "Vector<long>"
                },
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "initConnection",
            "cid": "c1cd5ea9",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "api_id",
                    "type": "int"
                },
                {
                    "name": "device_model",
                    "type": "string"
                },
                {
                    "name": "system_version",
                    "type": "string"
                },
                {
                    "name": "app_version",
                    "type": "string"
                },
                {
                    "name": "system_lang_code",
                    "type": "string"
                },
                {
                    "name": "lang_pack",
                    "type": "string"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "proxy",
                    "type": "flags.0?InputClientProxy"
                },
                {
                    "name": "params",
                    "type": "flags.1?JSONValue"
                },
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "invokeWithLayer",
            "cid": "da9b0d0d",
            "params": [
                {
                    "name": "layer",
                    "type": "int"
                },
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "invokeWithoutUpdates",
            "cid": "bf9459b7",
            "params": [
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "invokeWithMessagesRange",
            "cid": "365275f2",
            "params": [
                {
                    "name": "range",
                    "type": "MessageRange"
                },
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "invokeWithTakeout",
            "cid": "aca9fd2e",
            "params": [
                {
                    "name": "takeout_id",
                    "type": "long"
                },
                {
                    "name": "query",
                    "type": "!X"
                }
            ],
            "ret": "X"
        },
        {
            "_": "sendCode",
            "cid": "a677244f",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "api_id",
                    "type": "int"
                },
                {
                    "name": "api_hash",
                    "type": "string"
                },
                {
                    "name": "settings",
                    "type": "CodeSettings"
                }
            ],
            "ret": "auth.SentCode"
        },
        {
            "_": "signUp",
            "cid": "80eee427",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "signIn",
            "cid": "8d52a951",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                },
                {
                    "name": "phone_code",
                    "type": "flags.0?string"
                },
                {
                    "name": "email_verification",
                    "type": "flags.1?EmailVerification"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "logOut",
            "cid": "3e72ba19",
            "params": [],
            "ret": "auth.LoggedOut"
        },
        {
            "_": "resetAuthorizations",
            "cid": "9fab0d1a",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "exportAuthorization",
            "cid": "e5bfffcd",
            "params": [
                {
                    "name": "dc_id",
                    "type": "int"
                }
            ],
            "ret": "auth.ExportedAuthorization"
        },
        {
            "_": "importAuthorization",
            "cid": "a57a7dad",
            "params": [
                {
                    "name": "id",
                    "type": "long"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "bindTempAuthKey",
            "cid": "cdd42a05",
            "params": [
                {
                    "name": "perm_auth_key_id",
                    "type": "long"
                },
                {
                    "name": "nonce",
                    "type": "long"
                },
                {
                    "name": "expires_at",
                    "type": "int"
                },
                {
                    "name": "encrypted_message",
                    "type": "bytes"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "importBotAuthorization",
            "cid": "67a3ff2c",
            "params": [
                {
                    "name": "flags",
                    "type": "int"
                },
                {
                    "name": "api_id",
                    "type": "int"
                },
                {
                    "name": "api_hash",
                    "type": "string"
                },
                {
                    "name": "bot_auth_token",
                    "type": "string"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "checkPassword",
            "cid": "d18b4d16",
            "params": [
                {
                    "name": "password",
                    "type": "InputCheckPasswordSRP"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "requestPasswordRecovery",
            "cid": "d897bc66",
            "params": [],
            "ret": "auth.PasswordRecovery"
        },
        {
            "_": "recoverPassword",
            "cid": "37096c70",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "code",
                    "type": "string"
                },
                {
                    "name": "new_settings",
                    "type": "flags.0?account.PasswordInputSettings"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "resendCode",
            "cid": "3ef1a9bf",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                }
            ],
            "ret": "auth.SentCode"
        },
        {
            "_": "cancelCode",
            "cid": "1f040578",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "dropTempAuthKeys",
            "cid": "8e48a188",
            "params": [
                {
                    "name": "except_auth_keys",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "exportLoginToken",
            "cid": "b7e085fe",
            "params": [
                {
                    "name": "api_id",
                    "type": "int"
                },
                {
                    "name": "api_hash",
                    "type": "string"
                },
                {
                    "name": "except_ids",
                    "type": "Vector<long>"
                }
            ],
            "ret": "auth.LoginToken"
        },
        {
            "_": "importLoginToken",
            "cid": "95ac5ce4",
            "params": [
                {
                    "name": "token",
                    "type": "bytes"
                }
            ],
            "ret": "auth.LoginToken"
        },
        {
            "_": "acceptLoginToken",
            "cid": "e894ad4d",
            "params": [
                {
                    "name": "token",
                    "type": "bytes"
                }
            ],
            "ret": "Authorization"
        },
        {
            "_": "checkRecoveryPassword",
            "cid": "d36bf79",
            "params": [
                {
                    "name": "code",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "importWebTokenAuthorization",
            "cid": "2db873a9",
            "params": [
                {
                    "name": "api_id",
                    "type": "int"
                },
                {
                    "name": "api_hash",
                    "type": "string"
                },
                {
                    "name": "web_auth_token",
                    "type": "string"
                }
            ],
            "ret": "auth.Authorization"
        },
        {
            "_": "registerDevice",
            "cid": "ec86017a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_muted",
                    "type": "flags.0?true"
                },
                {
                    "name": "token_type",
                    "type": "int"
                },
                {
                    "name": "token",
                    "type": "string"
                },
                {
                    "name": "app_sandbox",
                    "type": "Bool"
                },
                {
                    "name": "secret",
                    "type": "bytes"
                },
                {
                    "name": "other_uids",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "unregisterDevice",
            "cid": "6a0d3206",
            "params": [
                {
                    "name": "token_type",
                    "type": "int"
                },
                {
                    "name": "token",
                    "type": "string"
                },
                {
                    "name": "other_uids",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "updateNotifySettings",
            "cid": "84be5b93",
            "params": [
                {
                    "name": "peer",
                    "type": "InputNotifyPeer"
                },
                {
                    "name": "settings",
                    "type": "InputPeerNotifySettings"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getNotifySettings",
            "cid": "12b3ad31",
            "params": [
                {
                    "name": "peer",
                    "type": "InputNotifyPeer"
                }
            ],
            "ret": "PeerNotifySettings"
        },
        {
            "_": "resetNotifySettings",
            "cid": "db7e1747",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "updateProfile",
            "cid": "78515775",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "first_name",
                    "type": "flags.0?string"
                },
                {
                    "name": "last_name",
                    "type": "flags.1?string"
                },
                {
                    "name": "about",
                    "type": "flags.2?string"
                }
            ],
            "ret": "User"
        },
        {
            "_": "updateStatus",
            "cid": "6628562c",
            "params": [
                {
                    "name": "offline",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getWallPapers",
            "cid": "7967d36",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "account.WallPapers"
        },
        {
            "_": "reportPeer",
            "cid": "c5ba3d86",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "reason",
                    "type": "ReportReason"
                },
                {
                    "name": "message",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "checkUsername",
            "cid": "2714d86c",
            "params": [
                {
                    "name": "username",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "updateUsername",
            "cid": "3e0bdd7c",
            "params": [
                {
                    "name": "username",
                    "type": "string"
                }
            ],
            "ret": "User"
        },
        {
            "_": "getPrivacy",
            "cid": "dadbc950",
            "params": [
                {
                    "name": "key",
                    "type": "InputPrivacyKey"
                }
            ],
            "ret": "account.PrivacyRules"
        },
        {
            "_": "setPrivacy",
            "cid": "c9f81ce8",
            "params": [
                {
                    "name": "key",
                    "type": "InputPrivacyKey"
                },
                {
                    "name": "rules",
                    "type": "Vector<InputPrivacyRule>"
                }
            ],
            "ret": "account.PrivacyRules"
        },
        {
            "_": "deleteAccount",
            "cid": "a2c0cf74",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "reason",
                    "type": "string"
                },
                {
                    "name": "password",
                    "type": "flags.0?InputCheckPasswordSRP"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getAccountTTL",
            "cid": "8fc711d",
            "params": [],
            "ret": "AccountDaysTTL"
        },
        {
            "_": "setAccountTTL",
            "cid": "2442485e",
            "params": [
                {
                    "name": "ttl",
                    "type": "AccountDaysTTL"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendChangePhoneCode",
            "cid": "82574ae5",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "settings",
                    "type": "CodeSettings"
                }
            ],
            "ret": "auth.SentCode"
        },
        {
            "_": "changePhone",
            "cid": "70c32edb",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                },
                {
                    "name": "phone_code",
                    "type": "string"
                }
            ],
            "ret": "User"
        },
        {
            "_": "updateDeviceLocked",
            "cid": "38df3532",
            "params": [
                {
                    "name": "period",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getAuthorizations",
            "cid": "e320c158",
            "params": [],
            "ret": "account.Authorizations"
        },
        {
            "_": "resetAuthorization",
            "cid": "df77f3bc",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getPassword",
            "cid": "548a30f5",
            "params": [],
            "ret": "account.Password"
        },
        {
            "_": "getPasswordSettings",
            "cid": "9cd4eaf9",
            "params": [
                {
                    "name": "password",
                    "type": "InputCheckPasswordSRP"
                }
            ],
            "ret": "account.PasswordSettings"
        },
        {
            "_": "updatePasswordSettings",
            "cid": "a59b102f",
            "params": [
                {
                    "name": "password",
                    "type": "InputCheckPasswordSRP"
                },
                {
                    "name": "new_settings",
                    "type": "account.PasswordInputSettings"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendConfirmPhoneCode",
            "cid": "1b3faa88",
            "params": [
                {
                    "name": "hash",
                    "type": "string"
                },
                {
                    "name": "settings",
                    "type": "CodeSettings"
                }
            ],
            "ret": "auth.SentCode"
        },
        {
            "_": "confirmPhone",
            "cid": "5f2178c3",
            "params": [
                {
                    "name": "phone_code_hash",
                    "type": "string"
                },
                {
                    "name": "phone_code",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getTmpPassword",
            "cid": "449e0b51",
            "params": [
                {
                    "name": "password",
                    "type": "InputCheckPasswordSRP"
                },
                {
                    "name": "period",
                    "type": "int"
                }
            ],
            "ret": "account.TmpPassword"
        },
        {
            "_": "getWebAuthorizations",
            "cid": "182e6d6f",
            "params": [],
            "ret": "account.WebAuthorizations"
        },
        {
            "_": "resetWebAuthorization",
            "cid": "2d01b9ef",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "resetWebAuthorizations",
            "cid": "682d2594",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "getAllSecureValues",
            "cid": "b288bc7d",
            "params": [],
            "ret": "Vector<SecureValue>"
        },
        {
            "_": "getSecureValue",
            "cid": "73665bc2",
            "params": [
                {
                    "name": "types",
                    "type": "Vector<SecureValueType>"
                }
            ],
            "ret": "Vector<SecureValue>"
        },
        {
            "_": "saveSecureValue",
            "cid": "899fe31d",
            "params": [
                {
                    "name": "value",
                    "type": "InputSecureValue"
                },
                {
                    "name": "secure_secret_id",
                    "type": "long"
                }
            ],
            "ret": "SecureValue"
        },
        {
            "_": "deleteSecureValue",
            "cid": "b880bc4b",
            "params": [
                {
                    "name": "types",
                    "type": "Vector<SecureValueType>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getAuthorizationForm",
            "cid": "a929597a",
            "params": [
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "scope",
                    "type": "string"
                },
                {
                    "name": "public_key",
                    "type": "string"
                }
            ],
            "ret": "account.AuthorizationForm"
        },
        {
            "_": "acceptAuthorization",
            "cid": "f3ed4c73",
            "params": [
                {
                    "name": "bot_id",
                    "type": "long"
                },
                {
                    "name": "scope",
                    "type": "string"
                },
                {
                    "name": "public_key",
                    "type": "string"
                },
                {
                    "name": "value_hashes",
                    "type": "Vector<SecureValueHash>"
                },
                {
                    "name": "credentials",
                    "type": "SecureCredentialsEncrypted"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendVerifyPhoneCode",
            "cid": "a5a356f9",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "settings",
                    "type": "CodeSettings"
                }
            ],
            "ret": "auth.SentCode"
        },
        {
            "_": "verifyPhone",
            "cid": "4dd3a7f6",
            "params": [
                {
                    "name": "phone_number",
                    "type": "string"
                },
                {
                    "name": "phone_code_hash",
                    "type": "string"
                },
                {
                    "name": "phone_code",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendVerifyEmailCode",
            "cid": "98e037bb",
            "params": [
                {
                    "name": "purpose",
                    "type": "EmailVerifyPurpose"
                },
                {
                    "name": "email",
                    "type": "string"
                }
            ],
            "ret": "account.SentEmailCode"
        },
        {
            "_": "verifyEmail",
            "cid": "32da4cf",
            "params": [
                {
                    "name": "purpose",
                    "type": "EmailVerifyPurpose"
                },
                {
                    "name": "verification",
                    "type": "EmailVerification"
                }
            ],
            "ret": "account.EmailVerified"
        },
        {
            "_": "initTakeoutSession",
            "cid": "8ef3eab0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "contacts",
                    "type": "flags.0?true"
                },
                {
                    "name": "message_users",
                    "type": "flags.1?true"
                },
                {
                    "name": "message_chats",
                    "type": "flags.2?true"
                },
                {
                    "name": "message_megagroups",
                    "type": "flags.3?true"
                },
                {
                    "name": "message_channels",
                    "type": "flags.4?true"
                },
                {
                    "name": "files",
                    "type": "flags.5?true"
                },
                {
                    "name": "file_max_size",
                    "type": "flags.5?long"
                }
            ],
            "ret": "account.Takeout"
        },
        {
            "_": "finishTakeoutSession",
            "cid": "1d2652ee",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "success",
                    "type": "flags.0?true"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "confirmPasswordEmail",
            "cid": "8fdf1920",
            "params": [
                {
                    "name": "code",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "resendPasswordEmail",
            "cid": "7a7f2a15",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "cancelPasswordEmail",
            "cid": "c1cbd5b6",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "getContactSignUpNotification",
            "cid": "9f07c728",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "setContactSignUpNotification",
            "cid": "cff43f61",
            "params": [
                {
                    "name": "silent",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getNotifyExceptions",
            "cid": "53577479",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "compare_sound",
                    "type": "flags.1?true"
                },
                {
                    "name": "peer",
                    "type": "flags.0?InputNotifyPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getWallPaper",
            "cid": "fc8ddbea",
            "params": [
                {
                    "name": "wallpaper",
                    "type": "InputWallPaper"
                }
            ],
            "ret": "WallPaper"
        },
        {
            "_": "uploadWallPaper",
            "cid": "dd853661",
            "params": [
                {
                    "name": "file",
                    "type": "InputFile"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                },
                {
                    "name": "settings",
                    "type": "WallPaperSettings"
                }
            ],
            "ret": "WallPaper"
        },
        {
            "_": "saveWallPaper",
            "cid": "6c5a5b37",
            "params": [
                {
                    "name": "wallpaper",
                    "type": "InputWallPaper"
                },
                {
                    "name": "unsave",
                    "type": "Bool"
                },
                {
                    "name": "settings",
                    "type": "WallPaperSettings"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "installWallPaper",
            "cid": "feed5769",
            "params": [
                {
                    "name": "wallpaper",
                    "type": "InputWallPaper"
                },
                {
                    "name": "settings",
                    "type": "WallPaperSettings"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "resetWallPapers",
            "cid": "bb3b9804",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "getAutoDownloadSettings",
            "cid": "56da0b3f",
            "params": [],
            "ret": "account.AutoDownloadSettings"
        },
        {
            "_": "saveAutoDownloadSettings",
            "cid": "76f36233",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "low",
                    "type": "flags.0?true"
                },
                {
                    "name": "high",
                    "type": "flags.1?true"
                },
                {
                    "name": "settings",
                    "type": "AutoDownloadSettings"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "uploadTheme",
            "cid": "1c3db333",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "file",
                    "type": "InputFile"
                },
                {
                    "name": "thumb",
                    "type": "flags.0?InputFile"
                },
                {
                    "name": "file_name",
                    "type": "string"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                }
            ],
            "ret": "Document"
        },
        {
            "_": "createTheme",
            "cid": "652e4400",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "slug",
                    "type": "string"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "document",
                    "type": "flags.2?InputDocument"
                },
                {
                    "name": "settings",
                    "type": "flags.3?Vector<InputThemeSettings>"
                }
            ],
            "ret": "Theme"
        },
        {
            "_": "updateTheme",
            "cid": "2bf40ccc",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "format",
                    "type": "string"
                },
                {
                    "name": "theme",
                    "type": "InputTheme"
                },
                {
                    "name": "slug",
                    "type": "flags.0?string"
                },
                {
                    "name": "title",
                    "type": "flags.1?string"
                },
                {
                    "name": "document",
                    "type": "flags.2?InputDocument"
                },
                {
                    "name": "settings",
                    "type": "flags.3?Vector<InputThemeSettings>"
                }
            ],
            "ret": "Theme"
        },
        {
            "_": "saveTheme",
            "cid": "f257106c",
            "params": [
                {
                    "name": "theme",
                    "type": "InputTheme"
                },
                {
                    "name": "unsave",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "installTheme",
            "cid": "c727bb3b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "dark",
                    "type": "flags.0?true"
                },
                {
                    "name": "theme",
                    "type": "flags.1?InputTheme"
                },
                {
                    "name": "format",
                    "type": "flags.2?string"
                },
                {
                    "name": "base_theme",
                    "type": "flags.3?BaseTheme"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getTheme",
            "cid": "3a5869ec",
            "params": [
                {
                    "name": "format",
                    "type": "string"
                },
                {
                    "name": "theme",
                    "type": "InputTheme"
                }
            ],
            "ret": "Theme"
        },
        {
            "_": "getThemes",
            "cid": "7206e458",
            "params": [
                {
                    "name": "format",
                    "type": "string"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "account.Themes"
        },
        {
            "_": "setContentSettings",
            "cid": "b574b16b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "sensitive_enabled",
                    "type": "flags.0?true"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getContentSettings",
            "cid": "8b9b4dae",
            "params": [],
            "ret": "account.ContentSettings"
        },
        {
            "_": "getMultiWallPapers",
            "cid": "65ad71dc",
            "params": [
                {
                    "name": "wallpapers",
                    "type": "Vector<InputWallPaper>"
                }
            ],
            "ret": "Vector<WallPaper>"
        },
        {
            "_": "getGlobalPrivacySettings",
            "cid": "eb2b4cf6",
            "params": [],
            "ret": "GlobalPrivacySettings"
        },
        {
            "_": "setGlobalPrivacySettings",
            "cid": "1edaaac2",
            "params": [
                {
                    "name": "settings",
                    "type": "GlobalPrivacySettings"
                }
            ],
            "ret": "GlobalPrivacySettings"
        },
        {
            "_": "reportProfilePhoto",
            "cid": "fa8cc6f5",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "photo_id",
                    "type": "InputPhoto"
                },
                {
                    "name": "reason",
                    "type": "ReportReason"
                },
                {
                    "name": "message",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "resetPassword",
            "cid": "9308ce1b",
            "params": [],
            "ret": "account.ResetPasswordResult"
        },
        {
            "_": "declinePasswordReset",
            "cid": "4c9409f6",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "getChatThemes",
            "cid": "d638de89",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "account.Themes"
        },
        {
            "_": "setAuthorizationTTL",
            "cid": "bf899aa0",
            "params": [
                {
                    "name": "authorization_ttl_days",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "changeAuthorizationSettings",
            "cid": "40f48462",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "hash",
                    "type": "long"
                },
                {
                    "name": "encrypted_requests_disabled",
                    "type": "flags.0?Bool"
                },
                {
                    "name": "call_requests_disabled",
                    "type": "flags.1?Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getSavedRingtones",
            "cid": "e1902288",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "account.SavedRingtones"
        },
        {
            "_": "saveRingtone",
            "cid": "3dea5b03",
            "params": [
                {
                    "name": "id",
                    "type": "InputDocument"
                },
                {
                    "name": "unsave",
                    "type": "Bool"
                }
            ],
            "ret": "account.SavedRingtone"
        },
        {
            "_": "uploadRingtone",
            "cid": "831a83a2",
            "params": [
                {
                    "name": "file",
                    "type": "InputFile"
                },
                {
                    "name": "file_name",
                    "type": "string"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                }
            ],
            "ret": "Document"
        },
        {
            "_": "updateEmojiStatus",
            "cid": "fbd3de6b",
            "params": [
                {
                    "name": "emoji_status",
                    "type": "EmojiStatus"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getDefaultEmojiStatuses",
            "cid": "d6753386",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "account.EmojiStatuses"
        },
        {
            "_": "getRecentEmojiStatuses",
            "cid": "f578105",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "account.EmojiStatuses"
        },
        {
            "_": "clearRecentEmojiStatuses",
            "cid": "18201aae",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "reorderUsernames",
            "cid": "ef500eab",
            "params": [
                {
                    "name": "order",
                    "type": "Vector<string>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "toggleUsername",
            "cid": "58d6b376",
            "params": [
                {
                    "name": "username",
                    "type": "string"
                },
                {
                    "name": "active",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getUsers",
            "cid": "d91a548",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<InputUser>"
                }
            ],
            "ret": "Vector<User>"
        },
        {
            "_": "getFullUser",
            "cid": "b60f5918",
            "params": [
                {
                    "name": "id",
                    "type": "InputUser"
                }
            ],
            "ret": "users.UserFull"
        },
        {
            "_": "setSecureValueErrors",
            "cid": "90c894b5",
            "params": [
                {
                    "name": "id",
                    "type": "InputUser"
                },
                {
                    "name": "errors",
                    "type": "Vector<SecureValueError>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getContactIDs",
            "cid": "7adc669d",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "Vector<int>"
        },
        {
            "_": "getStatuses",
            "cid": "c4a353ee",
            "params": [],
            "ret": "Vector<ContactStatus>"
        },
        {
            "_": "getContacts",
            "cid": "5dd69e12",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "contacts.Contacts"
        },
        {
            "_": "importContacts",
            "cid": "2c800be5",
            "params": [
                {
                    "name": "contacts",
                    "type": "Vector<InputContact>"
                }
            ],
            "ret": "contacts.ImportedContacts"
        },
        {
            "_": "deleteContacts",
            "cid": "96a0e00",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<InputUser>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "deleteByPhones",
            "cid": "1013fd9e",
            "params": [
                {
                    "name": "phones",
                    "type": "Vector<string>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "block",
            "cid": "68cc1411",
            "params": [
                {
                    "name": "id",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "unblock",
            "cid": "bea65d50",
            "params": [
                {
                    "name": "id",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getBlocked",
            "cid": "f57c350f",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "contacts.Blocked"
        },
        {
            "_": "search",
            "cid": "11f812d8",
            "params": [
                {
                    "name": "q",
                    "type": "string"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "contacts.Found"
        },
        {
            "_": "resolveUsername",
            "cid": "f93ccba3",
            "params": [
                {
                    "name": "username",
                    "type": "string"
                }
            ],
            "ret": "contacts.ResolvedPeer"
        },
        {
            "_": "getTopPeers",
            "cid": "973478b6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "correspondents",
                    "type": "flags.0?true"
                },
                {
                    "name": "bots_pm",
                    "type": "flags.1?true"
                },
                {
                    "name": "bots_inline",
                    "type": "flags.2?true"
                },
                {
                    "name": "phone_calls",
                    "type": "flags.3?true"
                },
                {
                    "name": "forward_users",
                    "type": "flags.4?true"
                },
                {
                    "name": "forward_chats",
                    "type": "flags.5?true"
                },
                {
                    "name": "groups",
                    "type": "flags.10?true"
                },
                {
                    "name": "channels",
                    "type": "flags.15?true"
                },
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "contacts.TopPeers"
        },
        {
            "_": "resetTopPeerRating",
            "cid": "1ae373ac",
            "params": [
                {
                    "name": "category",
                    "type": "TopPeerCategory"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "resetSaved",
            "cid": "879537f1",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "getSaved",
            "cid": "82f1e39f",
            "params": [],
            "ret": "Vector<SavedContact>"
        },
        {
            "_": "toggleTopPeers",
            "cid": "8514bdda",
            "params": [
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "addContact",
            "cid": "e8f463d0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "add_phone_privacy_exception",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "InputUser"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "phone",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "acceptContact",
            "cid": "f831a20f",
            "params": [
                {
                    "name": "id",
                    "type": "InputUser"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getLocated",
            "cid": "d348bc44",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "background",
                    "type": "flags.1?true"
                },
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "self_expires",
                    "type": "flags.0?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "blockFromReplies",
            "cid": "29a8962c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "delete_message",
                    "type": "flags.0?true"
                },
                {
                    "name": "delete_history",
                    "type": "flags.1?true"
                },
                {
                    "name": "report_spam",
                    "type": "flags.2?true"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "resolvePhone",
            "cid": "8af94344",
            "params": [
                {
                    "name": "phone",
                    "type": "string"
                }
            ],
            "ret": "contacts.ResolvedPeer"
        },
        {
            "_": "exportContactToken",
            "cid": "f8654027",
            "params": [],
            "ret": "ExportedContactToken"
        },
        {
            "_": "importContactToken",
            "cid": "13005788",
            "params": [
                {
                    "name": "token",
                    "type": "string"
                }
            ],
            "ret": "User"
        },
        {
            "_": "getMessages",
            "cid": "63c66506",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<InputMessage>"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "getDialogs",
            "cid": "a0f4cb4f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "exclude_pinned",
                    "type": "flags.0?true"
                },
                {
                    "name": "folder_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "offset_date",
                    "type": "int"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "offset_peer",
                    "type": "InputPeer"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Dialogs"
        },
        {
            "_": "getHistory",
            "cid": "4423e6c5",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "offset_date",
                    "type": "int"
                },
                {
                    "name": "add_offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "min_id",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "search",
            "cid": "a0fda762",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "q",
                    "type": "string"
                },
                {
                    "name": "from_id",
                    "type": "flags.0?InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "filter",
                    "type": "MessagesFilter"
                },
                {
                    "name": "min_date",
                    "type": "int"
                },
                {
                    "name": "max_date",
                    "type": "int"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "add_offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "min_id",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "readHistory",
            "cid": "e306d3a",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "max_id",
                    "type": "int"
                }
            ],
            "ret": "messages.AffectedMessages"
        },
        {
            "_": "deleteHistory",
            "cid": "b08f922a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "just_clear",
                    "type": "flags.0?true"
                },
                {
                    "name": "revoke",
                    "type": "flags.1?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "min_date",
                    "type": "flags.2?int"
                },
                {
                    "name": "max_date",
                    "type": "flags.3?int"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "deleteMessages",
            "cid": "e58e95d2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "revoke",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.AffectedMessages"
        },
        {
            "_": "receivedMessages",
            "cid": "5a954c0",
            "params": [
                {
                    "name": "max_id",
                    "type": "int"
                }
            ],
            "ret": "Vector<ReceivedNotifyMessage>"
        },
        {
            "_": "setTyping",
            "cid": "58943ee2",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "action",
                    "type": "SendMessageAction"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendMessage",
            "cid": "1cc20387",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.1?true"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "background",
                    "type": "flags.6?true"
                },
                {
                    "name": "clear_draft",
                    "type": "flags.7?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.14?true"
                },
                {
                    "name": "update_stickersets_order",
                    "type": "flags.15?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.10?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "sendMedia",
            "cid": "7547c966",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "background",
                    "type": "flags.6?true"
                },
                {
                    "name": "clear_draft",
                    "type": "flags.7?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.14?true"
                },
                {
                    "name": "update_stickersets_order",
                    "type": "flags.15?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "media",
                    "type": "InputMedia"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.10?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "forwardMessages",
            "cid": "c661bbc4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "background",
                    "type": "flags.6?true"
                },
                {
                    "name": "with_my_score",
                    "type": "flags.8?true"
                },
                {
                    "name": "drop_author",
                    "type": "flags.11?true"
                },
                {
                    "name": "drop_media_captions",
                    "type": "flags.12?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.14?true"
                },
                {
                    "name": "from_peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                },
                {
                    "name": "random_id",
                    "type": "Vector<long>"
                },
                {
                    "name": "to_peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.10?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "reportSpam",
            "cid": "cf1592db",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getPeerSettings",
            "cid": "efd9a6a2",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "messages.PeerSettings"
        },
        {
            "_": "report",
            "cid": "8953ab4e",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                },
                {
                    "name": "reason",
                    "type": "ReportReason"
                },
                {
                    "name": "message",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getChats",
            "cid": "49e9528f",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<long>"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "getFullChat",
            "cid": "aeb00b34",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "messages.ChatFull"
        },
        {
            "_": "editChatTitle",
            "cid": "73783ffd",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editChatPhoto",
            "cid": "35ddd674",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "photo",
                    "type": "InputChatPhoto"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "addChatUser",
            "cid": "f24753e3",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "fwd_limit",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "deleteChatUser",
            "cid": "a2185cab",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "revoke_history",
                    "type": "flags.0?true"
                },
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "createChat",
            "cid": "34a818",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "users",
                    "type": "Vector<InputUser>"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.0?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getDhConfig",
            "cid": "26cf8950",
            "params": [
                {
                    "name": "version",
                    "type": "int"
                },
                {
                    "name": "random_length",
                    "type": "int"
                }
            ],
            "ret": "messages.DhConfig"
        },
        {
            "_": "requestEncryption",
            "cid": "f64daf43",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "random_id",
                    "type": "int"
                },
                {
                    "name": "g_a",
                    "type": "bytes"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "acceptEncryption",
            "cid": "3dbc0415",
            "params": [
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "g_b",
                    "type": "bytes"
                },
                {
                    "name": "key_fingerprint",
                    "type": "long"
                }
            ],
            "ret": "EncryptedChat"
        },
        {
            "_": "discardEncryption",
            "cid": "f393aea0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "delete_history",
                    "type": "flags.0?true"
                },
                {
                    "name": "chat_id",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "setEncryptedTyping",
            "cid": "791451ed",
            "params": [
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "typing",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "readEncryptedHistory",
            "cid": "7f4b690a",
            "params": [
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "max_date",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendEncrypted",
            "cid": "44fa7a15",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "bytes"
                }
            ],
            "ret": "messages.SentEncryptedMessage"
        },
        {
            "_": "sendEncryptedFile",
            "cid": "5559481d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "bytes"
                },
                {
                    "name": "file",
                    "type": "InputEncryptedFile"
                }
            ],
            "ret": "messages.SentEncryptedMessage"
        },
        {
            "_": "sendEncryptedService",
            "cid": "32d439a4",
            "params": [
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "bytes"
                }
            ],
            "ret": "messages.SentEncryptedMessage"
        },
        {
            "_": "receivedQueue",
            "cid": "55a5bb66",
            "params": [
                {
                    "name": "max_qts",
                    "type": "int"
                }
            ],
            "ret": "Vector<long>"
        },
        {
            "_": "reportEncryptedSpam",
            "cid": "4b0c8c0f",
            "params": [
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "readMessageContents",
            "cid": "36a73f77",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.AffectedMessages"
        },
        {
            "_": "getStickers",
            "cid": "d5a5d3a1",
            "params": [
                {
                    "name": "emoticon",
                    "type": "string"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Stickers"
        },
        {
            "_": "getAllStickers",
            "cid": "b8a0a1a8",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.AllStickers"
        },
        {
            "_": "getWebPagePreview",
            "cid": "8b68b0cc",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "exportChatInvite",
            "cid": "a02ce5d5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "legacy_revoke_permanent",
                    "type": "flags.2?true"
                },
                {
                    "name": "request_needed",
                    "type": "flags.3?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "expire_date",
                    "type": "flags.0?int"
                },
                {
                    "name": "usage_limit",
                    "type": "flags.1?int"
                },
                {
                    "name": "title",
                    "type": "flags.4?string"
                }
            ],
            "ret": "ExportedChatInvite"
        },
        {
            "_": "checkChatInvite",
            "cid": "3eadb1bb",
            "params": [
                {
                    "name": "hash",
                    "type": "string"
                }
            ],
            "ret": "ChatInvite"
        },
        {
            "_": "importChatInvite",
            "cid": "6c50051c",
            "params": [
                {
                    "name": "hash",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getStickerSet",
            "cid": "c8a0ec74",
            "params": [
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "installStickerSet",
            "cid": "c78fe460",
            "params": [
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "archived",
                    "type": "Bool"
                }
            ],
            "ret": "messages.StickerSetInstallResult"
        },
        {
            "_": "uninstallStickerSet",
            "cid": "f96e55de",
            "params": [
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "startBot",
            "cid": "e6df7378",
            "params": [
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "start_param",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getMessagesViews",
            "cid": "5784d3e1",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                },
                {
                    "name": "increment",
                    "type": "Bool"
                }
            ],
            "ret": "messages.MessageViews"
        },
        {
            "_": "editChatAdmin",
            "cid": "a85bd1c2",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "is_admin",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "migrateChat",
            "cid": "a2875319",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "searchGlobal",
            "cid": "4bc6589a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "folder_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "q",
                    "type": "string"
                },
                {
                    "name": "filter",
                    "type": "MessagesFilter"
                },
                {
                    "name": "min_date",
                    "type": "int"
                },
                {
                    "name": "max_date",
                    "type": "int"
                },
                {
                    "name": "offset_rate",
                    "type": "int"
                },
                {
                    "name": "offset_peer",
                    "type": "InputPeer"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "reorderStickerSets",
            "cid": "78337739",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "masks",
                    "type": "flags.0?true"
                },
                {
                    "name": "emojis",
                    "type": "flags.1?true"
                },
                {
                    "name": "order",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getDocumentByHash",
            "cid": "b1f2061f",
            "params": [
                {
                    "name": "sha256",
                    "type": "bytes"
                },
                {
                    "name": "size",
                    "type": "long"
                },
                {
                    "name": "mime_type",
                    "type": "string"
                }
            ],
            "ret": "Document"
        },
        {
            "_": "getSavedGifs",
            "cid": "5cf09635",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.SavedGifs"
        },
        {
            "_": "saveGif",
            "cid": "327a30cb",
            "params": [
                {
                    "name": "id",
                    "type": "InputDocument"
                },
                {
                    "name": "unsave",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getInlineBotResults",
            "cid": "514e999d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "geo_point",
                    "type": "flags.0?InputGeoPoint"
                },
                {
                    "name": "query",
                    "type": "string"
                },
                {
                    "name": "offset",
                    "type": "string"
                }
            ],
            "ret": "messages.BotResults"
        },
        {
            "_": "setInlineBotResults",
            "cid": "eb5ea206",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "gallery",
                    "type": "flags.0?true"
                },
                {
                    "name": "private",
                    "type": "flags.1?true"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "results",
                    "type": "Vector<InputBotInlineResult>"
                },
                {
                    "name": "cache_time",
                    "type": "int"
                },
                {
                    "name": "next_offset",
                    "type": "flags.2?string"
                },
                {
                    "name": "switch_pm",
                    "type": "flags.3?InlineBotSwitchPM"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendInlineBotResult",
            "cid": "d3fbdccb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "background",
                    "type": "flags.6?true"
                },
                {
                    "name": "clear_draft",
                    "type": "flags.7?true"
                },
                {
                    "name": "hide_via",
                    "type": "flags.11?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "id",
                    "type": "string"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.10?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getMessageEditData",
            "cid": "fda68d36",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "messages.MessageEditData"
        },
        {
            "_": "editMessage",
            "cid": "48f71778",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.1?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "message",
                    "type": "flags.11?string"
                },
                {
                    "name": "media",
                    "type": "flags.14?InputMedia"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.15?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editInlineBotMessage",
            "cid": "83557dba",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.1?true"
                },
                {
                    "name": "id",
                    "type": "InputBotInlineMessageID"
                },
                {
                    "name": "message",
                    "type": "flags.11?string"
                },
                {
                    "name": "media",
                    "type": "flags.14?InputMedia"
                },
                {
                    "name": "reply_markup",
                    "type": "flags.2?ReplyMarkup"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getBotCallbackAnswer",
            "cid": "9342ca07",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "game",
                    "type": "flags.1?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "data",
                    "type": "flags.0?bytes"
                },
                {
                    "name": "password",
                    "type": "flags.2?InputCheckPasswordSRP"
                }
            ],
            "ret": "messages.BotCallbackAnswer"
        },
        {
            "_": "setBotCallbackAnswer",
            "cid": "d58f130a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "alert",
                    "type": "flags.1?true"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "message",
                    "type": "flags.0?string"
                },
                {
                    "name": "url",
                    "type": "flags.2?string"
                },
                {
                    "name": "cache_time",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getPeerDialogs",
            "cid": "e470bcfd",
            "params": [
                {
                    "name": "peers",
                    "type": "Vector<InputDialogPeer>"
                }
            ],
            "ret": "messages.PeerDialogs"
        },
        {
            "_": "saveDraft",
            "cid": "b4331e3f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "no_webpage",
                    "type": "flags.1?true"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.2?int"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "flags.3?Vector<MessageEntity>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getAllDrafts",
            "cid": "6a3f8d65",
            "params": [],
            "ret": "Updates"
        },
        {
            "_": "getFeaturedStickers",
            "cid": "64780b14",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.FeaturedStickers"
        },
        {
            "_": "readFeaturedStickers",
            "cid": "5b118126",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getRecentStickers",
            "cid": "9da9403b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "attached",
                    "type": "flags.0?true"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.RecentStickers"
        },
        {
            "_": "saveRecentSticker",
            "cid": "392718f8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "attached",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "InputDocument"
                },
                {
                    "name": "unsave",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "clearRecentStickers",
            "cid": "8999602d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "attached",
                    "type": "flags.0?true"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getArchivedStickers",
            "cid": "57f17692",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "masks",
                    "type": "flags.0?true"
                },
                {
                    "name": "emojis",
                    "type": "flags.1?true"
                },
                {
                    "name": "offset_id",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.ArchivedStickers"
        },
        {
            "_": "getMaskStickers",
            "cid": "640f82b8",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.AllStickers"
        },
        {
            "_": "getAttachedStickers",
            "cid": "cc5b67cc",
            "params": [
                {
                    "name": "media",
                    "type": "InputStickeredMedia"
                }
            ],
            "ret": "Vector<StickerSetCovered>"
        },
        {
            "_": "setGameScore",
            "cid": "8ef8ecc0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "edit_message",
                    "type": "flags.0?true"
                },
                {
                    "name": "force",
                    "type": "flags.1?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "score",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "setInlineGameScore",
            "cid": "15ad9f64",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "edit_message",
                    "type": "flags.0?true"
                },
                {
                    "name": "force",
                    "type": "flags.1?true"
                },
                {
                    "name": "id",
                    "type": "InputBotInlineMessageID"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "score",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getGameHighScores",
            "cid": "e822649d",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "messages.HighScores"
        },
        {
            "_": "getInlineGameHighScores",
            "cid": "f635e1b",
            "params": [
                {
                    "name": "id",
                    "type": "InputBotInlineMessageID"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "messages.HighScores"
        },
        {
            "_": "getCommonChats",
            "cid": "e40ca104",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "max_id",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "getAllChats",
            "cid": "875f74be",
            "params": [
                {
                    "name": "except_ids",
                    "type": "Vector<long>"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "getWebPage",
            "cid": "32ca8f91",
            "params": [
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "WebPage"
        },
        {
            "_": "toggleDialogPin",
            "cid": "a731e257",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pinned",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputDialogPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "reorderPinnedDialogs",
            "cid": "3b1adf37",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "force",
                    "type": "flags.0?true"
                },
                {
                    "name": "folder_id",
                    "type": "int"
                },
                {
                    "name": "order",
                    "type": "Vector<InputDialogPeer>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getPinnedDialogs",
            "cid": "d6b94df2",
            "params": [
                {
                    "name": "folder_id",
                    "type": "int"
                }
            ],
            "ret": "messages.PeerDialogs"
        },
        {
            "_": "setBotShippingResults",
            "cid": "e5f672fa",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "error",
                    "type": "flags.0?string"
                },
                {
                    "name": "shipping_options",
                    "type": "flags.1?Vector<ShippingOption>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "setBotPrecheckoutResults",
            "cid": "9c2dd95",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "success",
                    "type": "flags.1?true"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "error",
                    "type": "flags.0?string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "uploadMedia",
            "cid": "519bc2b1",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "media",
                    "type": "InputMedia"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "sendScreenshotNotification",
            "cid": "c97df020",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "int"
                },
                {
                    "name": "random_id",
                    "type": "long"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getFavedStickers",
            "cid": "4f1aaa9",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.FavedStickers"
        },
        {
            "_": "faveSticker",
            "cid": "b9ffc55b",
            "params": [
                {
                    "name": "id",
                    "type": "InputDocument"
                },
                {
                    "name": "unfave",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getUnreadMentions",
            "cid": "f107e790",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "add_offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "min_id",
                    "type": "int"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "readMentions",
            "cid": "36e5bf4d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "getRecentLocations",
            "cid": "702a40e0",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "sendMultiMedia",
            "cid": "b6f11a1c",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "background",
                    "type": "flags.6?true"
                },
                {
                    "name": "clear_draft",
                    "type": "flags.7?true"
                },
                {
                    "name": "noforwards",
                    "type": "flags.14?true"
                },
                {
                    "name": "update_stickersets_order",
                    "type": "flags.15?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "multi_media",
                    "type": "Vector<InputSingleMedia>"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.10?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "uploadEncryptedFile",
            "cid": "5057c497",
            "params": [
                {
                    "name": "peer",
                    "type": "InputEncryptedChat"
                },
                {
                    "name": "file",
                    "type": "InputEncryptedFile"
                }
            ],
            "ret": "EncryptedFile"
        },
        {
            "_": "searchStickerSets",
            "cid": "35705b8a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "exclude_featured",
                    "type": "flags.0?true"
                },
                {
                    "name": "q",
                    "type": "string"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.FoundStickerSets"
        },
        {
            "_": "getSplitRanges",
            "cid": "1cff7e08",
            "params": [],
            "ret": "Vector<MessageRange>"
        },
        {
            "_": "markDialogUnread",
            "cid": "c286d98f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "unread",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputDialogPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getDialogUnreadMarks",
            "cid": "22e24e22",
            "params": [],
            "ret": "Vector<DialogPeer>"
        },
        {
            "_": "clearAllDrafts",
            "cid": "7e58ee9c",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "updatePinnedMessage",
            "cid": "d2aaf7ec",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.0?true"
                },
                {
                    "name": "unpin",
                    "type": "flags.1?true"
                },
                {
                    "name": "pm_oneside",
                    "type": "flags.2?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "sendVote",
            "cid": "10ea6184",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "options",
                    "type": "Vector<bytes>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getPollResults",
            "cid": "73bb643b",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getOnlines",
            "cid": "6e2be050",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "ChatOnlines"
        },
        {
            "_": "editChatAbout",
            "cid": "def60797",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "about",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "editChatDefaultBannedRights",
            "cid": "a5866b41",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "banned_rights",
                    "type": "ChatBannedRights"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getEmojiKeywords",
            "cid": "35a0e062",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "EmojiKeywordsDifference"
        },
        {
            "_": "getEmojiKeywordsDifference",
            "cid": "1508b6af",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "from_version",
                    "type": "int"
                }
            ],
            "ret": "EmojiKeywordsDifference"
        },
        {
            "_": "getEmojiKeywordsLanguages",
            "cid": "4e9963b2",
            "params": [
                {
                    "name": "lang_codes",
                    "type": "Vector<string>"
                }
            ],
            "ret": "Vector<EmojiLanguage>"
        },
        {
            "_": "getEmojiURL",
            "cid": "d5b10c26",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "EmojiURL"
        },
        {
            "_": "getSearchCounters",
            "cid": "ae7cc1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "filters",
                    "type": "Vector<MessagesFilter>"
                }
            ],
            "ret": "Vector<messages.SearchCounter>"
        },
        {
            "_": "requestUrlAuth",
            "cid": "198fb446",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "flags.1?InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "button_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "url",
                    "type": "flags.2?string"
                }
            ],
            "ret": "UrlAuthResult"
        },
        {
            "_": "acceptUrlAuth",
            "cid": "b12c7125",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "write_allowed",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "flags.1?InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "button_id",
                    "type": "flags.1?int"
                },
                {
                    "name": "url",
                    "type": "flags.2?string"
                }
            ],
            "ret": "UrlAuthResult"
        },
        {
            "_": "hidePeerSettingsBar",
            "cid": "4facb138",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getScheduledHistory",
            "cid": "f516760b",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "getScheduledMessages",
            "cid": "bdbb0464",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "sendScheduledMessages",
            "cid": "bd38850a",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "deleteScheduledMessages",
            "cid": "59ae2b16",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getPollVotes",
            "cid": "b86e380e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "option",
                    "type": "flags.0?bytes"
                },
                {
                    "name": "offset",
                    "type": "flags.1?string"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.VotesList"
        },
        {
            "_": "toggleStickerSets",
            "cid": "b5052fea",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "uninstall",
                    "type": "flags.0?true"
                },
                {
                    "name": "archive",
                    "type": "flags.1?true"
                },
                {
                    "name": "unarchive",
                    "type": "flags.2?true"
                },
                {
                    "name": "stickersets",
                    "type": "Vector<InputStickerSet>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getDialogFilters",
            "cid": "f19ed96d",
            "params": [],
            "ret": "Vector<DialogFilter>"
        },
        {
            "_": "getSuggestedDialogFilters",
            "cid": "a29cd42c",
            "params": [],
            "ret": "Vector<DialogFilterSuggested>"
        },
        {
            "_": "updateDialogFilter",
            "cid": "1ad4a04a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "filter",
                    "type": "flags.0?DialogFilter"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "updateDialogFiltersOrder",
            "cid": "c563c1e4",
            "params": [
                {
                    "name": "order",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getOldFeaturedStickers",
            "cid": "7ed094a1",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.FeaturedStickers"
        },
        {
            "_": "getReplies",
            "cid": "22ddd30c",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "offset_date",
                    "type": "int"
                },
                {
                    "name": "add_offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "min_id",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "getDiscussionMessage",
            "cid": "446972fd",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "messages.DiscussionMessage"
        },
        {
            "_": "readDiscussion",
            "cid": "f731a9f4",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "read_max_id",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "unpinAllMessages",
            "cid": "ee22b9a8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "deleteChat",
            "cid": "5bd0ee50",
            "params": [
                {
                    "name": "chat_id",
                    "type": "long"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "deletePhoneCallHistory",
            "cid": "f9cbe409",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "revoke",
                    "type": "flags.0?true"
                }
            ],
            "ret": "messages.AffectedFoundMessages"
        },
        {
            "_": "checkHistoryImport",
            "cid": "43fe19f3",
            "params": [
                {
                    "name": "import_head",
                    "type": "string"
                }
            ],
            "ret": "messages.HistoryImportParsed"
        },
        {
            "_": "initHistoryImport",
            "cid": "34090c3b",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "file",
                    "type": "InputFile"
                },
                {
                    "name": "media_count",
                    "type": "int"
                }
            ],
            "ret": "messages.HistoryImport"
        },
        {
            "_": "uploadImportedMedia",
            "cid": "2a862092",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "import_id",
                    "type": "long"
                },
                {
                    "name": "file_name",
                    "type": "string"
                },
                {
                    "name": "media",
                    "type": "InputMedia"
                }
            ],
            "ret": "MessageMedia"
        },
        {
            "_": "startHistoryImport",
            "cid": "b43df344",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "import_id",
                    "type": "long"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getExportedChatInvites",
            "cid": "a2b5a3f6",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "revoked",
                    "type": "flags.3?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "admin_id",
                    "type": "InputUser"
                },
                {
                    "name": "offset_date",
                    "type": "flags.2?int"
                },
                {
                    "name": "offset_link",
                    "type": "flags.2?string"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.ExportedChatInvites"
        },
        {
            "_": "getExportedChatInvite",
            "cid": "73746f5c",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "link",
                    "type": "string"
                }
            ],
            "ret": "messages.ExportedChatInvite"
        },
        {
            "_": "editExportedChatInvite",
            "cid": "bdca2f75",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "revoked",
                    "type": "flags.2?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "link",
                    "type": "string"
                },
                {
                    "name": "expire_date",
                    "type": "flags.0?int"
                },
                {
                    "name": "usage_limit",
                    "type": "flags.1?int"
                },
                {
                    "name": "request_needed",
                    "type": "flags.3?Bool"
                },
                {
                    "name": "title",
                    "type": "flags.4?string"
                }
            ],
            "ret": "messages.ExportedChatInvite"
        },
        {
            "_": "deleteRevokedExportedChatInvites",
            "cid": "56987bd5",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "admin_id",
                    "type": "InputUser"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "deleteExportedChatInvite",
            "cid": "d464a42b",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "link",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getAdminsWithInvites",
            "cid": "3920e6ef",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "messages.ChatAdminsWithInvites"
        },
        {
            "_": "getChatInviteImporters",
            "cid": "df04dd4e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "requested",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "link",
                    "type": "flags.1?string"
                },
                {
                    "name": "q",
                    "type": "flags.2?string"
                },
                {
                    "name": "offset_date",
                    "type": "int"
                },
                {
                    "name": "offset_user",
                    "type": "InputUser"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.ChatInviteImporters"
        },
        {
            "_": "setHistoryTTL",
            "cid": "b80e5fe4",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "period",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "checkHistoryImportPeer",
            "cid": "5dc60f03",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "messages.CheckedHistoryImportPeer"
        },
        {
            "_": "setChatTheme",
            "cid": "e63be13f",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "emoticon",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getMessageReadParticipants",
            "cid": "2c6f97b7",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "Vector<long>"
        },
        {
            "_": "getSearchResultsCalendar",
            "cid": "49f0bde9",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "filter",
                    "type": "MessagesFilter"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "offset_date",
                    "type": "int"
                }
            ],
            "ret": "messages.SearchResultsCalendar"
        },
        {
            "_": "getSearchResultsPositions",
            "cid": "6e9583a3",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "filter",
                    "type": "MessagesFilter"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.SearchResultsPositions"
        },
        {
            "_": "hideChatJoinRequest",
            "cid": "7fe7e815",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "approved",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "hideAllChatJoinRequests",
            "cid": "e085f4ea",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "approved",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "link",
                    "type": "flags.1?string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "toggleNoForwards",
            "cid": "b11eafa2",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "saveDefaultSendAs",
            "cid": "ccfddf96",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "send_as",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendReaction",
            "cid": "d30d78d4",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "big",
                    "type": "flags.1?true"
                },
                {
                    "name": "add_to_recent",
                    "type": "flags.2?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "reaction",
                    "type": "flags.0?Vector<Reaction>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getMessagesReactions",
            "cid": "8bba90e6",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getMessageReactionsList",
            "cid": "461b3f48",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "reaction",
                    "type": "flags.0?Reaction"
                },
                {
                    "name": "offset",
                    "type": "flags.1?string"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.MessageReactionsList"
        },
        {
            "_": "setChatAvailableReactions",
            "cid": "feb16771",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "available_reactions",
                    "type": "ChatReactions"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getAvailableReactions",
            "cid": "18dea0ac",
            "params": [
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "messages.AvailableReactions"
        },
        {
            "_": "setDefaultReaction",
            "cid": "4f47a016",
            "params": [
                {
                    "name": "reaction",
                    "type": "Reaction"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "translateText",
            "cid": "24ce6dee",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "flags.0?InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "text",
                    "type": "flags.1?string"
                },
                {
                    "name": "from_lang",
                    "type": "flags.2?string"
                },
                {
                    "name": "to_lang",
                    "type": "string"
                }
            ],
            "ret": "messages.TranslatedText"
        },
        {
            "_": "getUnreadReactions",
            "cid": "3223495b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "add_offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "int"
                },
                {
                    "name": "min_id",
                    "type": "int"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "readReactions",
            "cid": "54aa7f8e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.0?int"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "searchSentMedia",
            "cid": "107e31a0",
            "params": [
                {
                    "name": "q",
                    "type": "string"
                },
                {
                    "name": "filter",
                    "type": "MessagesFilter"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "getAttachMenuBots",
            "cid": "16fcc2cb",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "AttachMenuBots"
        },
        {
            "_": "getAttachMenuBot",
            "cid": "77216192",
            "params": [
                {
                    "name": "bot",
                    "type": "InputUser"
                }
            ],
            "ret": "AttachMenuBotsBot"
        },
        {
            "_": "toggleBotInAttachMenu",
            "cid": "69f59d69",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "write_allowed",
                    "type": "flags.0?true"
                },
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "requestWebView",
            "cid": "178b480b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "from_bot_menu",
                    "type": "flags.4?true"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "url",
                    "type": "flags.1?string"
                },
                {
                    "name": "start_param",
                    "type": "flags.3?string"
                },
                {
                    "name": "theme_params",
                    "type": "flags.2?DataJSON"
                },
                {
                    "name": "platform",
                    "type": "string"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "WebViewResult"
        },
        {
            "_": "prolongWebView",
            "cid": "7ff34309",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "silent",
                    "type": "flags.5?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "reply_to_msg_id",
                    "type": "flags.0?int"
                },
                {
                    "name": "top_msg_id",
                    "type": "flags.9?int"
                },
                {
                    "name": "send_as",
                    "type": "flags.13?InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "requestSimpleWebView",
            "cid": "299bec8e",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "url",
                    "type": "string"
                },
                {
                    "name": "theme_params",
                    "type": "flags.0?DataJSON"
                },
                {
                    "name": "platform",
                    "type": "string"
                }
            ],
            "ret": "SimpleWebViewResult"
        },
        {
            "_": "sendWebViewResultMessage",
            "cid": "a4314f5",
            "params": [
                {
                    "name": "bot_query_id",
                    "type": "string"
                },
                {
                    "name": "result",
                    "type": "InputBotInlineResult"
                }
            ],
            "ret": "WebViewMessageSent"
        },
        {
            "_": "sendWebViewData",
            "cid": "dc0242c8",
            "params": [
                {
                    "name": "bot",
                    "type": "InputUser"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "button_text",
                    "type": "string"
                },
                {
                    "name": "data",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "transcribeAudio",
            "cid": "269e9a49",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "messages.TranscribedAudio"
        },
        {
            "_": "rateTranscribedAudio",
            "cid": "7f1d072f",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "transcription_id",
                    "type": "long"
                },
                {
                    "name": "good",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getCustomEmojiDocuments",
            "cid": "d9ab0f54",
            "params": [
                {
                    "name": "document_id",
                    "type": "Vector<long>"
                }
            ],
            "ret": "Vector<Document>"
        },
        {
            "_": "getEmojiStickers",
            "cid": "fbfca18f",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.AllStickers"
        },
        {
            "_": "getFeaturedEmojiStickers",
            "cid": "ecf6736",
            "params": [
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.FeaturedStickers"
        },
        {
            "_": "reportReaction",
            "cid": "3f64c076",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "int"
                },
                {
                    "name": "reaction_peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getTopReactions",
            "cid": "bb8125ba",
            "params": [
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Reactions"
        },
        {
            "_": "getRecentReactions",
            "cid": "39461db2",
            "params": [
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "messages.Reactions"
        },
        {
            "_": "clearRecentReactions",
            "cid": "9dfeefb4",
            "params": [],
            "ret": "Bool"
        },
        {
            "_": "getExtendedMedia",
            "cid": "84f80814",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "setDefaultHistoryTTL",
            "cid": "9eb51445",
            "params": [
                {
                    "name": "period",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getDefaultHistoryTTL",
            "cid": "658b7188",
            "params": [],
            "ret": "DefaultHistoryTTL"
        },
        {
            "_": "getState",
            "cid": "edd4882a",
            "params": [],
            "ret": "updates.State"
        },
        {
            "_": "getDifference",
            "cid": "25939651",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "pts_total_limit",
                    "type": "flags.0?int"
                },
                {
                    "name": "date",
                    "type": "int"
                },
                {
                    "name": "qts",
                    "type": "int"
                }
            ],
            "ret": "updates.Difference"
        },
        {
            "_": "getChannelDifference",
            "cid": "3173d78",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "force",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "filter",
                    "type": "ChannelMessagesFilter"
                },
                {
                    "name": "pts",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "updates.ChannelDifference"
        },
        {
            "_": "updateProfilePhoto",
            "cid": "1c3d5956",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "fallback",
                    "type": "flags.0?true"
                },
                {
                    "name": "id",
                    "type": "InputPhoto"
                }
            ],
            "ret": "photos.Photo"
        },
        {
            "_": "uploadProfilePhoto",
            "cid": "89f30f69",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "fallback",
                    "type": "flags.3?true"
                },
                {
                    "name": "file",
                    "type": "flags.0?InputFile"
                },
                {
                    "name": "video",
                    "type": "flags.1?InputFile"
                },
                {
                    "name": "video_start_ts",
                    "type": "flags.2?double"
                }
            ],
            "ret": "photos.Photo"
        },
        {
            "_": "deletePhotos",
            "cid": "87cf7f2f",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<InputPhoto>"
                }
            ],
            "ret": "Vector<long>"
        },
        {
            "_": "getUserPhotos",
            "cid": "91cd32a8",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "max_id",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "photos.Photos"
        },
        {
            "_": "uploadContactProfilePhoto",
            "cid": "b91a83bf",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "suggest",
                    "type": "flags.3?true"
                },
                {
                    "name": "save",
                    "type": "flags.4?true"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "file",
                    "type": "flags.0?InputFile"
                },
                {
                    "name": "video",
                    "type": "flags.1?InputFile"
                },
                {
                    "name": "video_start_ts",
                    "type": "flags.2?double"
                }
            ],
            "ret": "photos.Photo"
        },
        {
            "_": "saveFilePart",
            "cid": "b304a621",
            "params": [
                {
                    "name": "file_id",
                    "type": "long"
                },
                {
                    "name": "file_part",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getFile",
            "cid": "be5335be",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "precise",
                    "type": "flags.0?true"
                },
                {
                    "name": "cdn_supported",
                    "type": "flags.1?true"
                },
                {
                    "name": "location",
                    "type": "InputFileLocation"
                },
                {
                    "name": "offset",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "upload.File"
        },
        {
            "_": "saveBigFilePart",
            "cid": "de7b673d",
            "params": [
                {
                    "name": "file_id",
                    "type": "long"
                },
                {
                    "name": "file_part",
                    "type": "int"
                },
                {
                    "name": "file_total_parts",
                    "type": "int"
                },
                {
                    "name": "bytes",
                    "type": "bytes"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getWebFile",
            "cid": "24e6818d",
            "params": [
                {
                    "name": "location",
                    "type": "InputWebFileLocation"
                },
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "upload.WebFile"
        },
        {
            "_": "getCdnFile",
            "cid": "395f69da",
            "params": [
                {
                    "name": "file_token",
                    "type": "bytes"
                },
                {
                    "name": "offset",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "upload.CdnFile"
        },
        {
            "_": "reuploadCdnFile",
            "cid": "9b2754a8",
            "params": [
                {
                    "name": "file_token",
                    "type": "bytes"
                },
                {
                    "name": "request_token",
                    "type": "bytes"
                }
            ],
            "ret": "Vector<FileHash>"
        },
        {
            "_": "getCdnFileHashes",
            "cid": "91dc3f31",
            "params": [
                {
                    "name": "file_token",
                    "type": "bytes"
                },
                {
                    "name": "offset",
                    "type": "long"
                }
            ],
            "ret": "Vector<FileHash>"
        },
        {
            "_": "getFileHashes",
            "cid": "9156982a",
            "params": [
                {
                    "name": "location",
                    "type": "InputFileLocation"
                },
                {
                    "name": "offset",
                    "type": "long"
                }
            ],
            "ret": "Vector<FileHash>"
        },
        {
            "_": "getConfig",
            "cid": "c4f9186b",
            "params": [],
            "ret": "Config"
        },
        {
            "_": "getNearestDc",
            "cid": "1fb33026",
            "params": [],
            "ret": "NearestDc"
        },
        {
            "_": "getAppUpdate",
            "cid": "522d5a7d",
            "params": [
                {
                    "name": "source",
                    "type": "string"
                }
            ],
            "ret": "help.AppUpdate"
        },
        {
            "_": "getInviteText",
            "cid": "4d392343",
            "params": [],
            "ret": "help.InviteText"
        },
        {
            "_": "getSupport",
            "cid": "9cdf08cd",
            "params": [],
            "ret": "help.Support"
        },
        {
            "_": "getAppChangelog",
            "cid": "9010ef6f",
            "params": [
                {
                    "name": "prev_app_version",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "setBotUpdatesStatus",
            "cid": "ec22cfcd",
            "params": [
                {
                    "name": "pending_updates_count",
                    "type": "int"
                },
                {
                    "name": "message",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getCdnConfig",
            "cid": "52029342",
            "params": [],
            "ret": "CdnConfig"
        },
        {
            "_": "getRecentMeUrls",
            "cid": "3dc0f114",
            "params": [
                {
                    "name": "referer",
                    "type": "string"
                }
            ],
            "ret": "help.RecentMeUrls"
        },
        {
            "_": "getTermsOfServiceUpdate",
            "cid": "2ca51fd1",
            "params": [],
            "ret": "help.TermsOfServiceUpdate"
        },
        {
            "_": "acceptTermsOfService",
            "cid": "ee72f79a",
            "params": [
                {
                    "name": "id",
                    "type": "DataJSON"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getDeepLinkInfo",
            "cid": "3fedc75f",
            "params": [
                {
                    "name": "path",
                    "type": "string"
                }
            ],
            "ret": "help.DeepLinkInfo"
        },
        {
            "_": "getAppConfig",
            "cid": "98914110",
            "params": [],
            "ret": "JSONValue"
        },
        {
            "_": "saveAppLog",
            "cid": "6f02f748",
            "params": [
                {
                    "name": "events",
                    "type": "Vector<InputAppEvent>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getPassportConfig",
            "cid": "c661ad08",
            "params": [
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "help.PassportConfig"
        },
        {
            "_": "getSupportName",
            "cid": "d360e72c",
            "params": [],
            "ret": "help.SupportName"
        },
        {
            "_": "getUserInfo",
            "cid": "38a08d3",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "help.UserInfo"
        },
        {
            "_": "editUserInfo",
            "cid": "66b91b70",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "message",
                    "type": "string"
                },
                {
                    "name": "entities",
                    "type": "Vector<MessageEntity>"
                }
            ],
            "ret": "help.UserInfo"
        },
        {
            "_": "getPromoData",
            "cid": "c0977421",
            "params": [],
            "ret": "help.PromoData"
        },
        {
            "_": "hidePromoData",
            "cid": "1e251c95",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "dismissSuggestion",
            "cid": "f50dbaa1",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "suggestion",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getCountriesList",
            "cid": "735787a8",
            "params": [
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "hash",
                    "type": "int"
                }
            ],
            "ret": "help.CountriesList"
        },
        {
            "_": "getPremiumPromo",
            "cid": "b81b93d4",
            "params": [],
            "ret": "help.PremiumPromo"
        },
        {
            "_": "readHistory",
            "cid": "cc104937",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "max_id",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "deleteMessages",
            "cid": "84c1fd4e",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.AffectedMessages"
        },
        {
            "_": "reportSpam",
            "cid": "f44a8315",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "participant",
                    "type": "InputPeer"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getMessages",
            "cid": "ad8c9a23",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "id",
                    "type": "Vector<InputMessage>"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "getParticipants",
            "cid": "77ced9d0",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "filter",
                    "type": "ChannelParticipantsFilter"
                },
                {
                    "name": "offset",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                },
                {
                    "name": "hash",
                    "type": "long"
                }
            ],
            "ret": "channels.ChannelParticipants"
        },
        {
            "_": "getParticipant",
            "cid": "a0ab6cc6",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "participant",
                    "type": "InputPeer"
                }
            ],
            "ret": "channels.ChannelParticipant"
        },
        {
            "_": "getChannels",
            "cid": "a7f6bbb",
            "params": [
                {
                    "name": "id",
                    "type": "Vector<InputChannel>"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "getFullChannel",
            "cid": "8736a09",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "messages.ChatFull"
        },
        {
            "_": "createChannel",
            "cid": "91006707",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "broadcast",
                    "type": "flags.0?true"
                },
                {
                    "name": "megagroup",
                    "type": "flags.1?true"
                },
                {
                    "name": "for_import",
                    "type": "flags.3?true"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "about",
                    "type": "string"
                },
                {
                    "name": "geo_point",
                    "type": "flags.2?InputGeoPoint"
                },
                {
                    "name": "address",
                    "type": "flags.2?string"
                },
                {
                    "name": "ttl_period",
                    "type": "flags.4?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editAdmin",
            "cid": "d33c8902",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "admin_rights",
                    "type": "ChatAdminRights"
                },
                {
                    "name": "rank",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editTitle",
            "cid": "566decd0",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editPhoto",
            "cid": "f12e57c9",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "photo",
                    "type": "InputChatPhoto"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "checkUsername",
            "cid": "10e6bd2c",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "username",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "updateUsername",
            "cid": "3514b3de",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "username",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "joinChannel",
            "cid": "24b524c5",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "leaveChannel",
            "cid": "f836aa95",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "inviteToChannel",
            "cid": "199f3a6c",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "users",
                    "type": "Vector<InputUser>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "deleteChannel",
            "cid": "c0111fe3",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "exportMessageLink",
            "cid": "e63fadeb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "grouped",
                    "type": "flags.0?true"
                },
                {
                    "name": "thread",
                    "type": "flags.1?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "id",
                    "type": "int"
                }
            ],
            "ret": "ExportedMessageLink"
        },
        {
            "_": "toggleSignatures",
            "cid": "1f69b606",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getAdminedPublicChannels",
            "cid": "f8b036af",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "by_location",
                    "type": "flags.0?true"
                },
                {
                    "name": "check_limit",
                    "type": "flags.1?true"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "editBanned",
            "cid": "96e6cd81",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "participant",
                    "type": "InputPeer"
                },
                {
                    "name": "banned_rights",
                    "type": "ChatBannedRights"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getAdminLog",
            "cid": "33ddf480",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "q",
                    "type": "string"
                },
                {
                    "name": "events_filter",
                    "type": "flags.0?ChannelAdminLogEventsFilter"
                },
                {
                    "name": "admins",
                    "type": "flags.1?Vector<InputUser>"
                },
                {
                    "name": "max_id",
                    "type": "long"
                },
                {
                    "name": "min_id",
                    "type": "long"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "channels.AdminLogResults"
        },
        {
            "_": "setStickers",
            "cid": "ea8ca4f9",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "readMessageContents",
            "cid": "eab5dc38",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "id",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "deleteHistory",
            "cid": "9baa9647",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "for_everyone",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "max_id",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "togglePreHistoryHidden",
            "cid": "eabbb94c",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getLeftChannels",
            "cid": "8341ecc0",
            "params": [
                {
                    "name": "offset",
                    "type": "int"
                }
            ],
            "ret": "messages.Chats"
        },
        {
            "_": "getGroupsForDiscussion",
            "cid": "f5dad378",
            "params": [],
            "ret": "messages.Chats"
        },
        {
            "_": "setDiscussionGroup",
            "cid": "40582bb2",
            "params": [
                {
                    "name": "broadcast",
                    "type": "InputChannel"
                },
                {
                    "name": "group",
                    "type": "InputChannel"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "editCreator",
            "cid": "8f38cd1f",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "password",
                    "type": "InputCheckPasswordSRP"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editLocation",
            "cid": "58e63f6d",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "geo_point",
                    "type": "InputGeoPoint"
                },
                {
                    "name": "address",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "toggleSlowMode",
            "cid": "edd49ef0",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "seconds",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getInactiveChannels",
            "cid": "11e831ee",
            "params": [],
            "ret": "messages.InactiveChats"
        },
        {
            "_": "convertToGigagroup",
            "cid": "b290c69",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "viewSponsoredMessage",
            "cid": "beaedb94",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "random_id",
                    "type": "bytes"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getSponsoredMessages",
            "cid": "ec210fbf",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "messages.SponsoredMessages"
        },
        {
            "_": "getSendAs",
            "cid": "dc770ee",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "channels.SendAsPeers"
        },
        {
            "_": "deleteParticipantHistory",
            "cid": "367544db",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "participant",
                    "type": "InputPeer"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "toggleJoinToSend",
            "cid": "e4cb9580",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "toggleJoinRequest",
            "cid": "4c2985b6",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "reorderUsernames",
            "cid": "b45ced1d",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "order",
                    "type": "Vector<string>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "toggleUsername",
            "cid": "50f24105",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "username",
                    "type": "string"
                },
                {
                    "name": "active",
                    "type": "Bool"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "deactivateAllUsernames",
            "cid": "a245dd3",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "toggleForum",
            "cid": "a4298b29",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "createForumTopic",
            "cid": "f40c0224",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "icon_color",
                    "type": "flags.0?int"
                },
                {
                    "name": "icon_emoji_id",
                    "type": "flags.3?long"
                },
                {
                    "name": "random_id",
                    "type": "long"
                },
                {
                    "name": "send_as",
                    "type": "flags.2?InputPeer"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getForumTopics",
            "cid": "de560d1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "q",
                    "type": "flags.0?string"
                },
                {
                    "name": "offset_date",
                    "type": "int"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "offset_topic",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.ForumTopics"
        },
        {
            "_": "getForumTopicsByID",
            "cid": "b0831eb9",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "topics",
                    "type": "Vector<int>"
                }
            ],
            "ret": "messages.ForumTopics"
        },
        {
            "_": "editForumTopic",
            "cid": "f4dfa185",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "topic_id",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "flags.0?string"
                },
                {
                    "name": "icon_emoji_id",
                    "type": "flags.1?long"
                },
                {
                    "name": "closed",
                    "type": "flags.2?Bool"
                },
                {
                    "name": "hidden",
                    "type": "flags.3?Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "updatePinnedForumTopic",
            "cid": "6c2d9026",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "topic_id",
                    "type": "int"
                },
                {
                    "name": "pinned",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "deleteTopicHistory",
            "cid": "34435f2d",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "top_msg_id",
                    "type": "int"
                }
            ],
            "ret": "messages.AffectedHistory"
        },
        {
            "_": "reorderPinnedForumTopics",
            "cid": "2950a18f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "force",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "order",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "toggleAntiSpam",
            "cid": "68f3e4eb",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "reportAntiSpamFalsePositive",
            "cid": "a850a693",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "toggleParticipantsHidden",
            "cid": "6a6e7854",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "enabled",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "sendCustomRequest",
            "cid": "aa2769ed",
            "params": [
                {
                    "name": "custom_method",
                    "type": "string"
                },
                {
                    "name": "params",
                    "type": "DataJSON"
                }
            ],
            "ret": "DataJSON"
        },
        {
            "_": "answerWebhookJSONQuery",
            "cid": "e6213f4d",
            "params": [
                {
                    "name": "query_id",
                    "type": "long"
                },
                {
                    "name": "data",
                    "type": "DataJSON"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "setBotCommands",
            "cid": "517165a",
            "params": [
                {
                    "name": "scope",
                    "type": "BotCommandScope"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "commands",
                    "type": "Vector<BotCommand>"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "resetBotCommands",
            "cid": "3d8de0f9",
            "params": [
                {
                    "name": "scope",
                    "type": "BotCommandScope"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getBotCommands",
            "cid": "e34c0dd6",
            "params": [
                {
                    "name": "scope",
                    "type": "BotCommandScope"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "Vector<BotCommand>"
        },
        {
            "_": "setBotMenuButton",
            "cid": "4504d54f",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "button",
                    "type": "BotMenuButton"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getBotMenuButton",
            "cid": "9c60eb28",
            "params": [
                {
                    "name": "user_id",
                    "type": "InputUser"
                }
            ],
            "ret": "BotMenuButton"
        },
        {
            "_": "setBotBroadcastDefaultAdminRights",
            "cid": "788464e1",
            "params": [
                {
                    "name": "admin_rights",
                    "type": "ChatAdminRights"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "setBotGroupDefaultAdminRights",
            "cid": "925ec9ea",
            "params": [
                {
                    "name": "admin_rights",
                    "type": "ChatAdminRights"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getPaymentForm",
            "cid": "37148dbb",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "invoice",
                    "type": "InputInvoice"
                },
                {
                    "name": "theme_params",
                    "type": "flags.0?DataJSON"
                }
            ],
            "ret": "payments.PaymentForm"
        },
        {
            "_": "getPaymentReceipt",
            "cid": "2478d1cc",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "payments.PaymentReceipt"
        },
        {
            "_": "validateRequestedInfo",
            "cid": "b6c8f12b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "save",
                    "type": "flags.0?true"
                },
                {
                    "name": "invoice",
                    "type": "InputInvoice"
                },
                {
                    "name": "info",
                    "type": "PaymentRequestedInfo"
                }
            ],
            "ret": "payments.ValidatedRequestedInfo"
        },
        {
            "_": "sendPaymentForm",
            "cid": "2d03522f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "form_id",
                    "type": "long"
                },
                {
                    "name": "invoice",
                    "type": "InputInvoice"
                },
                {
                    "name": "requested_info_id",
                    "type": "flags.0?string"
                },
                {
                    "name": "shipping_option_id",
                    "type": "flags.1?string"
                },
                {
                    "name": "credentials",
                    "type": "InputPaymentCredentials"
                },
                {
                    "name": "tip_amount",
                    "type": "flags.2?long"
                }
            ],
            "ret": "payments.PaymentResult"
        },
        {
            "_": "getSavedInfo",
            "cid": "227d824b",
            "params": [],
            "ret": "payments.SavedInfo"
        },
        {
            "_": "clearSavedInfo",
            "cid": "d83d70c1",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "credentials",
                    "type": "flags.0?true"
                },
                {
                    "name": "info",
                    "type": "flags.1?true"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getBankCardData",
            "cid": "2e79d779",
            "params": [
                {
                    "name": "number",
                    "type": "string"
                }
            ],
            "ret": "payments.BankCardData"
        },
        {
            "_": "exportInvoice",
            "cid": "f91b065",
            "params": [
                {
                    "name": "invoice_media",
                    "type": "InputMedia"
                }
            ],
            "ret": "payments.ExportedInvoice"
        },
        {
            "_": "assignAppStoreTransaction",
            "cid": "80ed747d",
            "params": [
                {
                    "name": "receipt",
                    "type": "bytes"
                },
                {
                    "name": "purpose",
                    "type": "InputStorePaymentPurpose"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "assignPlayMarketTransaction",
            "cid": "dffd50d3",
            "params": [
                {
                    "name": "receipt",
                    "type": "DataJSON"
                },
                {
                    "name": "purpose",
                    "type": "InputStorePaymentPurpose"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "canPurchasePremium",
            "cid": "9fc19eb6",
            "params": [
                {
                    "name": "purpose",
                    "type": "InputStorePaymentPurpose"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "createStickerSet",
            "cid": "9021ab67",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "masks",
                    "type": "flags.0?true"
                },
                {
                    "name": "animated",
                    "type": "flags.1?true"
                },
                {
                    "name": "videos",
                    "type": "flags.4?true"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "title",
                    "type": "string"
                },
                {
                    "name": "short_name",
                    "type": "string"
                },
                {
                    "name": "thumb",
                    "type": "flags.2?InputDocument"
                },
                {
                    "name": "stickers",
                    "type": "Vector<InputStickerSetItem>"
                },
                {
                    "name": "software",
                    "type": "flags.3?string"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "removeStickerFromSet",
            "cid": "f7760f51",
            "params": [
                {
                    "name": "sticker",
                    "type": "InputDocument"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "changeStickerPosition",
            "cid": "ffb6d4ca",
            "params": [
                {
                    "name": "sticker",
                    "type": "InputDocument"
                },
                {
                    "name": "position",
                    "type": "int"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "addStickerToSet",
            "cid": "8653febe",
            "params": [
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "sticker",
                    "type": "InputStickerSetItem"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "setStickerSetThumb",
            "cid": "9a364e30",
            "params": [
                {
                    "name": "stickerset",
                    "type": "InputStickerSet"
                },
                {
                    "name": "thumb",
                    "type": "InputDocument"
                }
            ],
            "ret": "messages.StickerSet"
        },
        {
            "_": "checkShortName",
            "cid": "284b3639",
            "params": [
                {
                    "name": "short_name",
                    "type": "string"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "suggestShortName",
            "cid": "4dafc503",
            "params": [
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "stickers.SuggestedShortName"
        },
        {
            "_": "getCallConfig",
            "cid": "55451fa9",
            "params": [],
            "ret": "DataJSON"
        },
        {
            "_": "requestCall",
            "cid": "42ff96ed",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "video",
                    "type": "flags.0?true"
                },
                {
                    "name": "user_id",
                    "type": "InputUser"
                },
                {
                    "name": "random_id",
                    "type": "int"
                },
                {
                    "name": "g_a_hash",
                    "type": "bytes"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                }
            ],
            "ret": "phone.PhoneCall"
        },
        {
            "_": "acceptCall",
            "cid": "3bd2b4a0",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "g_b",
                    "type": "bytes"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                }
            ],
            "ret": "phone.PhoneCall"
        },
        {
            "_": "confirmCall",
            "cid": "2efe1722",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "g_a",
                    "type": "bytes"
                },
                {
                    "name": "key_fingerprint",
                    "type": "long"
                },
                {
                    "name": "protocol",
                    "type": "PhoneCallProtocol"
                }
            ],
            "ret": "phone.PhoneCall"
        },
        {
            "_": "receivedCall",
            "cid": "17d54f61",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "discardCall",
            "cid": "b2cbc1c0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "video",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "duration",
                    "type": "int"
                },
                {
                    "name": "reason",
                    "type": "PhoneCallDiscardReason"
                },
                {
                    "name": "connection_id",
                    "type": "long"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "setCallRating",
            "cid": "59ead627",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "user_initiative",
                    "type": "flags.0?true"
                },
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "rating",
                    "type": "int"
                },
                {
                    "name": "comment",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "saveCallDebug",
            "cid": "277add7e",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "debug",
                    "type": "DataJSON"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "sendSignalingData",
            "cid": "ff7a9383",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "data",
                    "type": "bytes"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "createGroupCall",
            "cid": "48cdc6d8",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "rtmp_stream",
                    "type": "flags.2?true"
                },
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "random_id",
                    "type": "int"
                },
                {
                    "name": "title",
                    "type": "flags.0?string"
                },
                {
                    "name": "schedule_date",
                    "type": "flags.1?int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "joinGroupCall",
            "cid": "b132ff7b",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "muted",
                    "type": "flags.0?true"
                },
                {
                    "name": "video_stopped",
                    "type": "flags.2?true"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "join_as",
                    "type": "InputPeer"
                },
                {
                    "name": "invite_hash",
                    "type": "flags.1?string"
                },
                {
                    "name": "params",
                    "type": "DataJSON"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "leaveGroupCall",
            "cid": "500377f9",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "source",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "inviteToGroupCall",
            "cid": "7b393160",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "users",
                    "type": "Vector<InputUser>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "discardGroupCall",
            "cid": "7a777135",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "toggleGroupCallSettings",
            "cid": "74bbb43d",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "reset_invite_hash",
                    "type": "flags.1?true"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "join_muted",
                    "type": "flags.0?Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getGroupCall",
            "cid": "41845db",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "phone.GroupCall"
        },
        {
            "_": "getGroupParticipants",
            "cid": "c558d8ab",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "ids",
                    "type": "Vector<InputPeer>"
                },
                {
                    "name": "sources",
                    "type": "Vector<int>"
                },
                {
                    "name": "offset",
                    "type": "string"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "phone.GroupParticipants"
        },
        {
            "_": "checkGroupCall",
            "cid": "b59cf977",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "sources",
                    "type": "Vector<int>"
                }
            ],
            "ret": "Vector<int>"
        },
        {
            "_": "toggleGroupCallRecord",
            "cid": "f128c708",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "start",
                    "type": "flags.0?true"
                },
                {
                    "name": "video",
                    "type": "flags.2?true"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "title",
                    "type": "flags.1?string"
                },
                {
                    "name": "video_portrait",
                    "type": "flags.2?Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editGroupCallParticipant",
            "cid": "a5273abf",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "participant",
                    "type": "InputPeer"
                },
                {
                    "name": "muted",
                    "type": "flags.0?Bool"
                },
                {
                    "name": "volume",
                    "type": "flags.1?int"
                },
                {
                    "name": "raise_hand",
                    "type": "flags.2?Bool"
                },
                {
                    "name": "video_stopped",
                    "type": "flags.3?Bool"
                },
                {
                    "name": "video_paused",
                    "type": "flags.4?Bool"
                },
                {
                    "name": "presentation_paused",
                    "type": "flags.5?Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "editGroupCallTitle",
            "cid": "1ca6ac0a",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "title",
                    "type": "string"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getGroupCallJoinAs",
            "cid": "ef7c213a",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                }
            ],
            "ret": "phone.JoinAsPeers"
        },
        {
            "_": "exportGroupCallInvite",
            "cid": "e6aa647f",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "can_self_unmute",
                    "type": "flags.0?true"
                },
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "phone.ExportedGroupCallInvite"
        },
        {
            "_": "toggleGroupCallStartSubscription",
            "cid": "219c34e6",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "subscribed",
                    "type": "Bool"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "startScheduledGroupCall",
            "cid": "5680e342",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "saveDefaultGroupCallJoinAs",
            "cid": "575e1f8c",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "join_as",
                    "type": "InputPeer"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "joinGroupCallPresentation",
            "cid": "cbea6bc4",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                },
                {
                    "name": "params",
                    "type": "DataJSON"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "leaveGroupCallPresentation",
            "cid": "1c50d144",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getGroupCallStreamChannels",
            "cid": "1ab21940",
            "params": [
                {
                    "name": "call",
                    "type": "InputGroupCall"
                }
            ],
            "ret": "phone.GroupCallStreamChannels"
        },
        {
            "_": "getGroupCallStreamRtmpUrl",
            "cid": "deb3abbf",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPeer"
                },
                {
                    "name": "revoke",
                    "type": "Bool"
                }
            ],
            "ret": "phone.GroupCallStreamRtmpUrl"
        },
        {
            "_": "saveCallLog",
            "cid": "41248786",
            "params": [
                {
                    "name": "peer",
                    "type": "InputPhoneCall"
                },
                {
                    "name": "file",
                    "type": "InputFile"
                }
            ],
            "ret": "Bool"
        },
        {
            "_": "getLangPack",
            "cid": "f2f2330a",
            "params": [
                {
                    "name": "lang_pack",
                    "type": "string"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "LangPackDifference"
        },
        {
            "_": "getStrings",
            "cid": "efea3803",
            "params": [
                {
                    "name": "lang_pack",
                    "type": "string"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "keys",
                    "type": "Vector<string>"
                }
            ],
            "ret": "Vector<LangPackString>"
        },
        {
            "_": "getDifference",
            "cid": "cd984aa5",
            "params": [
                {
                    "name": "lang_pack",
                    "type": "string"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                },
                {
                    "name": "from_version",
                    "type": "int"
                }
            ],
            "ret": "LangPackDifference"
        },
        {
            "_": "getLanguages",
            "cid": "42c6978f",
            "params": [
                {
                    "name": "lang_pack",
                    "type": "string"
                }
            ],
            "ret": "Vector<LangPackLanguage>"
        },
        {
            "_": "getLanguage",
            "cid": "6a596502",
            "params": [
                {
                    "name": "lang_pack",
                    "type": "string"
                },
                {
                    "name": "lang_code",
                    "type": "string"
                }
            ],
            "ret": "LangPackLanguage"
        },
        {
            "_": "editPeerFolders",
            "cid": "6847d0ab",
            "params": [
                {
                    "name": "folder_peers",
                    "type": "Vector<InputFolderPeer>"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "deleteFolder",
            "cid": "1c295881",
            "params": [
                {
                    "name": "folder_id",
                    "type": "int"
                }
            ],
            "ret": "Updates"
        },
        {
            "_": "getBroadcastStats",
            "cid": "ab42441a",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "dark",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "stats.BroadcastStats"
        },
        {
            "_": "loadAsyncGraph",
            "cid": "621d5fa0",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "token",
                    "type": "string"
                },
                {
                    "name": "x",
                    "type": "flags.0?long"
                }
            ],
            "ret": "StatsGraph"
        },
        {
            "_": "getMegagroupStats",
            "cid": "dcdf8607",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "dark",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                }
            ],
            "ret": "stats.MegagroupStats"
        },
        {
            "_": "getMessagePublicForwards",
            "cid": "5630281b",
            "params": [
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                },
                {
                    "name": "offset_rate",
                    "type": "int"
                },
                {
                    "name": "offset_peer",
                    "type": "InputPeer"
                },
                {
                    "name": "offset_id",
                    "type": "int"
                },
                {
                    "name": "limit",
                    "type": "int"
                }
            ],
            "ret": "messages.Messages"
        },
        {
            "_": "getMessageStats",
            "cid": "b6e0a3f5",
            "params": [
                {
                    "name": "flags",
                    "type": "#"
                },
                {
                    "name": "dark",
                    "type": "flags.0?true"
                },
                {
                    "name": "channel",
                    "type": "InputChannel"
                },
                {
                    "name": "msg_id",
                    "type": "int"
                }
            ],
            "ret": "stats.MessageStats"
        }
    ],
    "layer": 151
}