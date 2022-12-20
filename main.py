import asyncio
import uvloop

from pathlib import Path

from loguru import logger
from piltover.server import Server, Client, Request
from piltover.utils import gen_keys, get_public_key_fingerprint
from piltover.types import Keys


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

    await pilt.serve()

try:
    uvloop.install()
    asyncio.run(main())
except KeyboardInterrupt:
    pass
