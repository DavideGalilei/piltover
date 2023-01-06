# piltover 🐳
An experimental Telegram server written from scratch in Python.

## TODO
- Fix ping issues: TDesktop deadlocks after several minutes
- Give correct `msg_id`/`seq_no` according to the [Telegram specification](https://core.telegram.org/mtproto/description#message-identifier-msg-id)
- A Websocket proxy for Telegram Web (WebZ / WebK). A work in progress temporary implementation is in `tools/websocket_proxy.js`
- Updates handling: `pts` / `qts` / etc...
- Refactor the TL de/serialization module, the code is messy (e.g. make custom boxed types for List/int/str/bytes)
- Refactor the server `authorize()` method
- Support multiple server keys, to automatically switch to [RSA_PAD](https://core.telegram.org/mtproto/auth_key#presenting-proof-of-work-server-authentication) for official clients, whilst keeping clients like pyrogram/telethon working with the old method. Currently handled manually in `server.py`: `old = False`
- Support TL from multiple layers, and layer-based handlers. Add fallbacks eventually
- Add a `tests` folder with patched pyrogram/telethon/* clients and assertions
- Use custom exceptions instead of python assertions: `assert` statements are disabled in python -O, leading to missing important checks
- Add missing security checks, e.g. check of `g_a`/`g_b`
- Refactor the `main.py` code, and use a database for auth keys/messages/users/updates (probably with SQLAlchemy and alambic due to reliable database migrations)
- Improve README
- MTProxy support maybe? Obfuscation is already implemented, so why not
- HTTP/UDP support? Probably Telegram itself forgot those exist

# Purpose
This project is currently not meant to be used to host custom Telegram instances, as most **security measures are <ins>currently</ins> barely in place**. For now, it can be used by MTProto clients developers to understand why their code fails, whereas Telegram just closes the connection with a -404 code.

That being said, it is planned in future to make it usable for most basic Telegram featues, including but not limited to sending and receiving messages, media, search, etc...

This can be really useful for bots developers that would like to have a testing sandbox that doesn't ratelimit their bots.

The server is meant to be used as a library, providing 100% control of every answer
- TODO: allow the user to override `authorize()`

### **Example**
An example quick-start (incomplete) code would look like this:
```python
import asyncio
from piltover.server import Server, Client, Request
from piltover.utils import gen_keys

async def main():
    pilt = Server(server_keys=gen_keys())
    # Running on localhost
    # Port: 4430

    @pilt.on_message("ping")
    async def pong(client: Client, request: Request):
        print("Received ping:", request.obj)

        return {
            "_": "pong",
            "msg_id": request.msg_id,
            "ping_id": request.obj.ping_id,
        }

    await pilt.serve()

asyncio.run(main())
```

```shell
$ python3 -m pip install -U -r requirements.txt
$ python3 main.py
# Server running on 127.0.0.1:4430...
```

Of course, this minimal setup is far from complete, and will only work for auth key generation and pings.

# Development setup
## **General steps**
### **1. Clone the repo:**
```shell
$ git clone https://github.com/DavideGalilei/piltover
$ cd piltover
```

### **2. Setup a virtual environment (optional)**
```shell
$ python3 -m virtualenv venv
$ source venv/bin/activate
```

### **3. Initial setup**
```shell
$ python3 -m pip install -U -r requirements.txt
$ python3 tools/gen_tl.py update
$ python3 main.py
```
Now wait until it loads correctly and fire a Ctrl-C to stop the process.

> **You should see a line looking like this at the beginning**
> ```yml
> 2023-01-06 18:12:18.900 | INFO     | __main__:main:48 - Pubkey fingerprint: -5087c676da5acb3d (af78398925a534c3)
> ```

**Get the fingerprint hex string and save it for later (some clients need it)**. In this case, the unsigned fingerprint is `af78398925a534c3`, but only for this example. Do not reuse this key fingerprint, as it will be different in your setup.

### **4. Extract public key number and exponent**
At this point, two files should have been generated in your directory. Namely, `data/secrets/privkey.asc` and `data/secrets/pubkey.asc`. Keep in mind that some clients might need the PKCS1 public key in the normal ascii format.

Some others like pyrogram, do not have a RSA key parser and hardcode the number/exponent. To extract it, you can use [this command](https://github.com/pyrogram/pyrogram/blob/b19764d5dc9e2d59a4ccbb7f520f78505800656b/pyrogram/crypto/rsa.py#L26):

```shell
$ grep -v -- - data/secrets/pubkey.asc | tr -d \\n | base64 -d | openssl asn1parse -inform DER -i
```

An example output would look like this:
```yml
    0:d=0  hl=4 l= 266 cons: SEQUENCE          
    4:d=1  hl=4 l= 257 prim:  INTEGER           :C3AE9457FDB44F47B91B9389401933F2D0B27357FE116ED7640798784829FDBC66295169D1D323AB664FD6920EFBAAC8725DA7EACAA491D1F1EEC8259CA68E4CFE86FC6823C903A323DE46C0E64B8DD5C93A188711C1BF78FCBE0C99904227A66C9135241DD8B92A0AD88AB3A6734BC13B57FA38614BB2AA79F3EF0920D577928F7E689B7B5B0A1A8A48DA9D7E4C28F2A8F1AAEDA22AC4DA05324C1CB67538ADFE1AC3201B34A85189B0765E6C79FF443433837B540D6295BF9EE95B8CDA709868C450BE9730C9FCC7442011129AFB45187C2A1913A4974709E9666865C4F06067E981BF57950A0395B45C3A7322FD36F77D803FF97897BC00D5687A3CB575D1
  265:d=1  hl=2 l=   3 prim:  INTEGER           :010001
```

**Note the exponent (`010001`) and the prime number: (`C3AE94...B575D1`). Save those values for later.**

### **Pyrogram**
- `git clone --depth=1 https://github.com/pyrogram/pyrogram`
- Edit this dictionary: https://github.com/pyrogram/pyrogram/blob/b19764d5dc9e2d59a4ccbb7f520f78505800656b/pyrogram/crypto/rsa.py#L33
  - The key is the **server fingerprint**, the value is formed by this expression: `PublicKey(int(`**prime**` 16), int(`**exponent**`, 16))`
  - Replace those values, (optional: delete the rest of the keys)
- Edit the datacenters ips in this file: https://github.com/pyrogram/pyrogram/blob/b19764d5dc9e2d59a4ccbb7f520f78505800656b/pyrogram/session/internals/data_center.py#L22
  - Every ip should become `"127.0.0.1"` (localhost)
  - In the `DataCenter.__new__` method below, replace every return with `return (ip, `**4430**`)`, instead of ports 80/443
- Install in development mode with `python3 -m pip install -e .`
- Ready to use, run the server and check if `test.py` works

### **Telethon**
- `git clone --depth=1 https://github.com/pyrogram/pyrogram`
- Edit these variables: https://github.com/LonamiWebs/Telethon/blob/2007c83c9e1b1c85e60e4eca8e8651fcb120ee88/telethon/client/telegrambaseclient.py#L21-L24
  - ```python
    DEFAULT_DC_ID = 2
    DEFAULT_IPV4_IP = '127.0.0.1'
    DEFAULT_IPV6_IP = '2001:67c:4e8:f002::a'
    DEFAULT_PORT = 4430
  - Just make sure that the default dc is 2, the ipv4 is localhost, and the default port is 4430. We don't really use ipv6 anyway...
- Add the rsa public key:
  - Edit this file: https://github.com/LonamiWebs/Telethon/blob/2007c83c9e1b1c85e60e4eca8e8651fcb120ee88/telethon/crypto/rsa.py#L85
  - Ideally, delete all the existing keys
  - Take your server's public key from the `data/secrets/pubkey.asc` file, and add it there with `add_key("""`**key here**`""", old=False)`
- Install in development mode with `python3 -m pip install -e .`
- Ready to use, run the server and check if `telethon_test.py` works

### **TDesktop**
- Edit this file: https://github.com/telegramdesktop/tdesktop/blob/2acedca6b740f6471b6ebe2e0c500bec32a0a94c/Telegram/SourceFiles/mtproto/mtproto_dc_options.cpp#L31-L78
  - As always, replace every ip with `127.0.0.1` (localhost), and every port with `4430`
  - Remove the existing rsa keys, and replace them with your own, taken from the `data/secrets/pubkey.asc` file on your piltover folder. **Important:** check the newlines thoroughly and make sure they are there, or it won't work.
- Build the program, ideally with GitHub Actions
- Put the executable in a folder, e.g. `tdesk`
- Since we don't save the auth keys, you should delete the leftover files from tdesktop at every run. You can do this conveniently and run your custom TDesktop with this command:
- ```shell
  $ rm -rf tdata/ DebugLogs/ log.txt && c && ./Telegram
  ```

### **Telegram Android (recommended: Owlgram)**
- Clone the repo and follow the basic setup instructions
- Edit this file: https://github.com/OwlGramDev/OwlGram/blob/master/TMessagesProj/jni/tgnet/ConnectionsManager.cpp#L1702-L1756
  - Replace every ip with your local ip address. It can be `127.0.0.1` (localhost) only in the case you're running the app with an emulator on the same machine the server is running. Otherwise, change it with e.g. `192.168.1.35` (the LAN ip address of your machine).
  - Replace every port with `4430`
- Edit this file: https://github.com/OwlGramDev/OwlGram/blob/master/TMessagesProj/jni/tgnet/Handshake.cpp#L355-L372  
  - Remove the existing rsa keys, and replace them with your own, taken from the `data/secrets/pubkey.asc` file on your piltover folder. **Important:** check the newlines thoroughly and make sure they are there, or it won't work. This took me way too much debugging time to realize that the missing newlines was the cause of the app crashes.
- Build the app, and see if it works.

### **Telegram WebK / WebZ**
- #TODO: a websocket proxy utility is needed before continuing. The server doesn't support direct websocket connections yet

### **NimGram**
- #TODO: the client is currently under active development and refactoring, so I will wait until a working version is released

### Telegram X/TDLib
- #TODO: add instructions. I didn't figure out how yet.

#### *Make a pull request if you want to add instructions for your own client.*

# How it works
- The client connects with TCP sockets to the server (websockets for web clients)
- The first bytes sent within a new connection determine the used [transport](https://core.telegram.org/mtproto/mtproto-transports)
  - `0xef`: Abridged
  - `0xeeeeeeee`: Intermediate
  - `0xdddddddd`: Padded Intermediate
  - `[length: 4 bytes][0x00000000]`: TCP Full, distinguishable by the empty `seq_no` (`0x00000000`)
  - `[presumably random bytes]`: *Usually* and [Obfuscated](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation) transport
  - To distinguish between `TCP Full` and `Obfuscated` transports, a buffered reader is needed, to allow for peeking the stream without consuming it.
- **Type Language** (TL) Data Serialization
  - In piltover, the TL de/serialization is JIT (Just In Time), allowing for an easy json-like interface at the cost of slow type checking at runtime (#TODO: do something about this) without complex code-generation parsers
  - The TL parser (`tools/gen_tl.py`) utility uses **`jinja2`** to generate the `api_tl.py` / `mtproto_tl.py` files from the official TDesktop repo. (#TODO retrieve as much old schema layers for multi-layer support)
- [**Authorization Key**](https://core.telegram.org/mtproto/auth_key) generation
  - An authorization process starts, done by the `authorize()` method of the piltover's `Server` class.
  - Generate random prime numbers for `pq` decomposition, a proof of work to avoid clients' DoS to the server
  - Either use an old algorithm or `RSA_PAD` to encrypt the inner data payload
  - The server checks the stuff it needs to check, the client too
  - If everything went correctly, we are authorized
  - It is worth noting that every auth key has its own id (the 8 lower order bytes of `SHA1(auth_key)`)
  - Apart from the auth key id, every session has its own arbitrary (client provided) session_id, bound to the auth key. #TODO: Piltover doesn't currently check this value
- **Sign in / sign up process**
  - Client sends `invokeWithLayer(initConnection(getConfig(...)))`
  - Client signs in with number / sms
  - Run the server and see the logs to find out more...

# Why
One day my Telegram account stopped working properly, due to an internal server error originated from a supposedly corrupted message I forwarded. Every time the client tried to fetch new messages from private chats, it would face a `[500 STORE_INVALID_OBJECT_TYPE]` error. Hopefully, the bug has been fixed ~1/2 days after being reported, but the fact that it happened at all motivated me enough to try and make my own server. In several days I managed to make it *kinda* work :)

# Miscellaneous
List of other server implementations I found:
- https://github.com/teamgram/teamgram-server
- https://github.com/aykutalparslan/Telegram-Server, moved to https://github.com/aykutalparslan/Ferrite
- https://github.com/loyldg/mytelegram
- https://github.com/nebula-chat/telegramd (now gone, probably moved to teamgram: https://github.com/nebula-chat/chatengine)

Various applications similar to Telegram (probably using a custom MTProto backend):
- https://nebula.chat/
- https://potato.im/
- https://icq.com/ (not sure about this one, but the clients are a copycat of Telegram's)
