import asyncio

import uvloop

from pathlib import Path
from piltover.server import Server


root = Path(__file__).parent.resolve(strict=True)


if True:
    # Hot code reloading
    import jurigged

    def log(s: jurigged.live.WatchOperation):
        if hasattr(s, "filename") and "unknown" not in s.filename:
            file = Path(s.filename)
            print("Reloaded", file.relative_to(root))

    jurigged.watch("piltover/*.py", logger=log)


async def main():
    pilt = Server()
    await pilt.serve()

try:
    uvloop.install()
    asyncio.run(main())
except KeyboardInterrupt:
    pass
