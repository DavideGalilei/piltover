import logging

from pyrogram import Client, idle
from pyrogram.raw.functions.ping import Ping

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

    pong = app.invoke(Ping(ping_id=12345))
    print("GOT PONG:", pong)

    idle()  # sleep forever
