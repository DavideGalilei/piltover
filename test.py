import logging

from pyrogram import Client, idle

logging.basicConfig(level=logging.DEBUG)

app = Client(
    "test",
    api_id=12345,
    api_hash="test",
    in_memory=True,
    phone_number="42777",
    phone_code="69696",
    # no_updates=True,
)

with app:
    print(app.get_me())
    idle()  # sleep forever
