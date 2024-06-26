# piltover 🐳

An experimental Telegram server written from scratch in Python. Development
chat: linked group to [@ChameleonGram](https://t.me/ChameleonGram).

## TODO

- [ ] WebK gets stuck on `sendCode()`. (note to self: inspect the MTProto workers in `chrome://inspect/#workers`)
- [x] Multiple sessions handling for: ~~Give correct `msg_id`/`seq_no` according
      to the
      [Telegram specification](https://core.telegram.org/mtproto/description#message-identifier-msg-id)~~
- [x] ~~A Websocket proxy for Telegram Web (WebZ / WebK). A work in progress
      temporary implementation is in `tools/websocket_proxy.js`~~
- [ ] Updates handling: `pts`, `qts`, etc.
- [ ] Refactor the TL de/serialization module since the code is messy (e.g. make
      custom boxed types for list/int/str/bytes).
- [ ] Refactor the server `authorize()` method.
- [ ] Support multiple server keys to automatically switch to
      [RSA_PAD](https://core.telegram.org/mtproto/auth_key#presenting-proof-of-work-server-authentication)
      for official clients, whilst keeping clients like Pyrogram/Telethon
      working with the old method. Currently handled manually in `server.py`:
      `old = False`
- [ ] Support TL from multiple layers, and layer-based handlers. Add fallbacks
      eventually.
- [ ] Add a `tests/` directory with patched assertions from client libraries.
- [ ] Use custom exceptions instead of Python assertions: `assert` statements
      are disabled with `python -O`, leading to missing important checks.
- [ ] Add missing security checks, e.g., checking of `g_a`/`g_b`.
- [ ] Refactor `piltover/__main__.py`, and use a database for auth
      keys/messages/users/updates (probably with SQLAlchemy and alambic due to
      reliable database migrations).
- [ ] MTProxy support maybe? Obfuscation is already implemented, so why not?
- [ ] HTTP/UDP support? Probably Telegram itself forgot those also exist.
- [ ] Switch to hypercorn for the tcp server maybe?
- [ ] Improve the README.

## Purpose

This project is currently not meant to be used to host custom Telegram
instances, as most **security measures are <u>currently</u> barely in place**.
For now, it can be used by MTProto clients developers to understand why their
code fails, whereas Telegram just closes the connection with a -404 error code.

That being said, it is planned in future to make it usable for most basic
Telegram featues, including but not limited to, sending and receiving text and
media messages, media, search.

This can be really useful for bots developers that would like to have a testing
sandbox that doesn't ratelimit their bots.

The server is meant to be used as a library, providing 100% control of every
answer

- TODO: allow the user to override `authorize()`

## Example

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
$ poetry install --no-root
$ poetry run python -m piltover
# Server running on 127.0.0.1:4430...
```

Of course, this minimal setup is far from complete, and will only work for auth
key generation and pings.

## Development setup

### **General steps**

#### **1. Clone the repo:**

```shell
$ git clone https://github.com/DavideGalilei/piltover
$ cd piltover
```

#### **2. Install poetry**

Follow instructions at: https://python-poetry.org/docs/#installation

#### **3. Initial setup**

```shell
$ poetry install --no-root
$ poetry run python tools/gen_tl.py update
$ poetry run python -m piltover
```

Now wait until it loads correctly and fire a Ctrl-C to stop the process.

> **You should see a line looking like this at the beginning**
>
> ```yml
> 2023-11-05 19:52:31.171 | INFO     | __main__:main:49 - Pubkey fingerprint: -6bff292cf4837025 (9400d6d30b7c8fdb)
> ```

**Get the fingerprint hex string and save it for later (some clients need it)**.
In this case, the unsigned fingerprint is `9400d6d30b7c8fdb`, but only for this
example. Do not reuse this key fingerprint, as it will be different in your
setup.

#### **4. Extract public key number and exponent**

At this point, two files should have been generated in your directory. Namely,
`data/secrets/privkey.asc` and `data/secrets/pubkey.asc`. Keep in mind that some
clients might need the PKCS1 public key in the normal ascii format.

Some others like pyrogram, do not have a RSA key parser and hardcode the
number/exponent. To extract it, you can use
[this command](https://github.com/pyrogram/pyrogram/blob/b19764d5dc9e2d59a4ccbb7f520f78505800656b/pyrogram/crypto/rsa.py#L26):

```shell
$ grep -v -- - data/secrets/pubkey.asc | tr -d \\n | base64 -d | openssl asn1parse -inform DER -i
```

An example output would look like this:

```yml
  0:d=0  hl=4 l= 266 cons: SEQUENCE          
  4:d=1  hl=4 l= 257 prim:  INTEGER           :C3AE9457FDB44F47B91B9389401933F2D0B27357FE116ED7640798784829FDBC66295169D1D323AB664FD6920EFBAAC8725DA7EACAA491D1F1EEC8259CA68E4CFE86FC6823C903A323DE46C0E64B8DD5C93A188711C1BF78FCBE0C99904227A66C9135241DD8B92A0AD88AB3A6734BC13B57FA38614BB2AA79F3EF0920D577928F7E689B7B5B0A1A8A48DA9D7E4C28F2A8F1AAEDA22AC4DA05324C1CB67538ADFE1AC3201B34A85189B0765E6C79FF443433837B540D6295BF9EE95B8CDA709868C450BE9730C9FCC7442011129AFB45187C2A1913A4974709E9666865C4F06067E981BF57950A0395B45C3A7322FD36F77D803FF97897BC00D5687A3CB575D1
265:d=1  hl=2 l=   3 prim:  INTEGER           :010001
```

**Note the exponent (`010001`) and the prime number: (`C3AE94...B575D1`). Save
those values for later.**

### **Pyrogram**

- `git clone --depth=1 https://github.com/pyrogram/pyrogram`
- Edit this dictionary:
  https://github.com/pyrogram/pyrogram/blob/b19764d5dc9e2d59a4ccbb7f520f78505800656b/pyrogram/crypto/rsa.py#L33
  - The key is the **server fingerprint**, the value is formed by this
    expression: `PublicKey(int(` **prime** `16), int(` **exponent** `, 16))`
  - Replace those values, (optional: delete the rest of the keys)
- Edit the datacenters ips in
  [this file](https://github.com/pyrogram/pyrogram/blob/b19764d5dc9e2d59a4ccbb7f520f78505800656b/pyrogram/session/internals/data_center.py#L22):
  - Every ip should become `"127.0.0.1"` (localhost)
  - In the `DataCenter.__new__` method below, replace every return with
    `return (ip,` **4430** `)`, instead of ports 80/443
- Install in development mode with `python3 -m pip install -e .`
- Ready to use, run the server and check if `test.py` works

### **Telethon**

- `git clone --depth=1 https://github.com/LonamiWebs/telethon`
- Edit these variables:
  https://github.com/LonamiWebs/Telethon/blob/2007c83c9e1b1c85e60e4eca8e8651fcb120ee88/telethon/client/telegrambaseclient.py#L21-L24
  - ```python
    DEFAULT_DC_ID = 2
    DEFAULT_IPV4_IP = '127.0.0.1'
    DEFAULT_IPV6_IP = '2001:67c:4e8:f002::a'
    DEFAULT_PORT = 4430
    ```
  - Just make sure that the default dc is 2, the ipv4 is localhost, and the
    default port is 4430. We don't really use ipv6 anyway...
- Add the rsa public key:
  - Edit this file:
    https://github.com/LonamiWebs/Telethon/blob/2007c83c9e1b1c85e60e4eca8e8651fcb120ee88/telethon/crypto/rsa.py#L85
  - Ideally, delete all the existing keys
  - Take your server's public key from the `data/secrets/pubkey.asc` file, and
    add it there with `add_key("""` **key here** `""", old=False)`
- Install in development mode with `python3 -m pip install -e .`
- Ready to use, run the server and check if `telethon_test.py` works

### **Telegram Desktop**

- Edit
  [this file](https://github.com/telegramdesktop/tdesktop/blob/2acedca6b740f6471b6ebe2e0c500bec32a0a94c/Telegram/SourceFiles/mtproto/mtproto_dc_options.cpp#L31-L78):
  - As always, replace every ip with `127.0.0.1` (localhost), and every port
    with `4430`
  - Remove the existing rsa keys, and replace them with your own, taken from the
    `data/secrets/pubkey.asc` file on your piltover folder. **Important:** check
    the newlines thoroughly and make sure they are there, or it won't work.
- Build the program, ideally with GitHub Actions
- Put the executable in a folder, e.g. `tdesk`
- Since we don't save the auth keys, you should delete the leftover files from
  tdesktop at every run. You can do this conveniently and run your custom
  TDesktop with this command:

```shell
$ rm -rf tdata/ DebugLogs/ log.txt && c && ./Telegram
```

### **Telegram for Android**

- Clone the repo (optional: checkout the commit I used)
```shell
$ git clone https://github.com/DrKLO/Telegram.git
$ cd Telegram
$ # Optional: checkout the commit I used
$ git checkout 5bc1c3dce0e9108615c784a565051e54246fe0cb
```
- Edit this file:
  https://github.com/DrKLO/Telegram/blob/5bc1c3dce0e9108615c784a565051e54246fe0cb/TMessagesProj/jni/tgnet/ConnectionsManager.cpp#L1779-L1839
  - Replace every ip with your local ip address. It can be `127.0.0.1`
    (localhost) only in the case you're running the app with an emulator on the
    same machine the server is running. Otherwise, change it with e.g.
    `192.168.1.35` (the LAN ip address of your machine, which you can obtain by running `ip -c a`).
  - Replace every port with `4430`
  - Either delete or change IPv6 addresses to `::1` (localhost). This will break the
    IPv6 support, but if you know what you're doing, you can change it to your ipv6 address.
  - In DataCenters like DC2 there are multiple ip addresses, you should delete the extra ones and change only the first one.
- Edit this file:
  https://github.com/DrKLO/Telegram/blob/5bc1c3dce0e9108615c784a565051e54246fe0cb/TMessagesProj/jni/tgnet/Handshake.cpp#L366-L385
  - Remove the existing rsa keys, and replace them with your own, taken from the
    `data/secrets/pubkey.asc` file on your piltover folder. **Important:** check
    the newlines thoroughly and make sure they are there, or it won't work. This
    took me way too much debugging time to realize that the missing newlines was
    the cause of the app crashes.
  - Change the unsigned fingerprint with the one you got from the server logs (e.g. `9400d6d30b7c8fdb`)
- If you haven't already, check the official repo for the build instructions.
Generally, remember to edit `TMessagesProj/src/main/java/org/telegram/messenger/BuildVars.java`
- Build the app, and see if it works.

### **Telegram WebK**

- Clone repo and install dependencies:
  - ```shell
    $ git clone https://github.com/morethanwords/tweb
    $ cd tweb
    $ npm i -g pnpm
    $ pnpm install
    ```
- Edit the values in this file:
  https://github.com/morethanwords/tweb/blob/f2827d9c19616a560346bd1662665ca30dc54668/src/lib/mtproto/dcConfigurator.ts#L50
  - Change `` const chosenServer = `wss://...` `` to:
  - ```typescript
    const chosenServer = `ws://127.0.0.1:3000/proxy`;
    ```
  - Change every datacenter ip and port below, respectively to `127.0.0.1`
    (localhost) and `3000` (websocket proxy port)
    https://github.com/morethanwords/tweb/blob/f2827d9c19616a560346bd1662665ca30dc54668/src/lib/mtproto/dcConfigurator.ts#L58-L70
- Edit the values in this file:
  https://github.com/morethanwords/tweb/blob/f2827d9c19616a560346bd1662665ca30dc54668/src/lib/mtproto/rsaKeysManager.ts#L69-L78
  - Change the `modulus` to the **lowercase** string of `prime` obtained previously
- Run the websocket proxy from piltover
  - ```shell
    $ poetry run python tools/websocket_proxy.py
    ```
- Run with `npm start`
- Wait some time for the app to compile
- Open the app in your browser (usually `https://0.0.0.0:8080/`)

### **Telegram WebZ**

- #TODO: WebZ instructions

### **Nimgram**

- #TODO: the client is currently under active development and refactoring, so I
  will wait until a working version is released

### Telegram X/TDLib

- #TODO: add instructions. I haven't figured out how it should be done yet.

#### _Make a pull request if you want to add instructions for your own client._

## How it works

- The client connects with TCP sockets to the server (websockets for web
  clients)
- The first bytes sent within a new connection determine the used
  [transport](https://core.telegram.org/mtproto/mtproto-transports)
  - `0xef`: Abridged
  - `0xeeeeeeee`: Intermediate
  - `0xdddddddd`: Padded Intermediate
  - `[length: 4 bytes][0x00000000]`: TCP Full, distinguishable by the empty
    `seq_no` (`0x00000000`)
  - `[presumably random bytes]`: _Usually_ and
    [Obfuscated](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation)
    transport
  - To distinguish between `TCP Full` and `Obfuscated` transports, a buffered
    reader is needed, to allow for peeking the stream without consuming it.
- **Type Language** (TL) Data Serialization
  - In piltover, the TL de/serialization is JIT (Just In Time), allowing for an
    easy json-like interface at the cost of slow type checking at runtime
    (#TODO: do something about this) without complex code-generation parsers
  - The TL parser (`tools/gen_tl.py`) utility uses **`jinja2`** to generate the
    `api_tl.py` / `mtproto_tl.py` files from the official TDesktop repo. (#TODO
    retrieve as much old schema layers for multi-layer support)
- [**Authorization Key**](https://core.telegram.org/mtproto/auth_key) generation
  - An authorization process starts, done by the `authorize()` method of the
    piltover's `Server` class.
  - Generate random prime numbers for `pq` decomposition, a proof of work to
    avoid clients' DoS to the server
  - Either use an old algorithm or `RSA_PAD` to encrypt the inner data payload
  - The server checks the stuff it needs to check, the client too
  - If everything went correctly, we are authorized
  - It is worth noting that every auth key has its own id (the 8 lower order
    bytes of `SHA1(auth_key)`)
  - Apart from the auth key id, every session has its own arbitrary (client
    provided) session_id, bound to the auth key. #TODO: Piltover doesn't
    currently check this value
- **Sign in / sign up process**
  - Client sends `invokeWithLayer(initConnection(getConfig(...)))`
  - Client signs in with number / sms
  - Run the server and see the logs to find out more...

## Why

One day, my Telegram account stopped working properly due to an internal server
error originating from a supposedly corrupted message I forwarded. Every time
the client tried to fetch new messages from private chats, it would face a
`[500 STORE_INVALID_OBJECT_TYPE]` error. Hopefully, the bug was fixed in ~1/2
days after being reported, but the fact that it happened at all motivated me
enough to try building my own server. In several days, I managed to make it
_kinda_ work :)

## Miscellaneous

List of other server implementations I found:

- https://github.com/teamgram/teamgram-server
- https://github.com/aykutalparslan/Telegram-Server, moved to
  https://github.com/aykutalparslan/Ferrite
- https://github.com/loyldg/mytelegram
- https://github.com/nebula-chat/telegramd (now gone, probably moved to
  teamgram: https://github.com/nebula-chat/chatengine)

Various applications similar to Telegram (probably using a custom MTProto
backend):

- https://nebula.chat/
- https://potato.im/
- https://icq.com/ (not sure about this one, but the clients are a copycat of
  Telegram's)
