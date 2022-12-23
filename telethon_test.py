from telethon import TelegramClient
from telethon.network.connection.tcpintermediate import ConnectionTcpIntermediate

# Remember to use your own values from my.telegram.org!
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
client = TelegramClient(
    session=None,
    api_id=api_id,
    api_hash=api_hash,
    connection=ConnectionTcpIntermediate,
)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())


with client:
    client.loop.run_until_complete(main())
