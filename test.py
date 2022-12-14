import logging

import pyrogram
from pyrogram import Client

print(pyrogram.__file__)
logging.basicConfig(level=logging.DEBUG)

app = Client(
    "test",
    api_id=12345,
    api_hash="test",
    in_memory=True,
    phone_number="42777",
    phone_code=42,
)

app.run()
