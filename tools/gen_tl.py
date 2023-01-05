import re
import io
import sys
import asyncio

import httpx

from io import StringIO
from pathlib import Path
from string import whitespace
from collections import defaultdict

from loguru import logger


root = Path(__file__).parent.resolve(strict=True)
data = root / "resources"
data.mkdir(parents=True, exist_ok=True)
out = root / "output"
out.mkdir(parents=True, exist_ok=True)


api = data / "api.tl"
API_URL = "https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/Telegram/Resources/tl/api.tl"


class Parser(StringIO):
    def __init__(self, initial_value: str | None = ...) -> None:
        super().__init__(initial_value)
        self.line = 0
        self.pos = 0

    def peek(self, next: int = 1) -> str:
        pos = self.tell()
        result = super().read(next)
        self.seek(pos, io.SEEK_SET)
        return result

    def read(self, size: int) -> str:
        result = super().read(size)
        newlines = result.count("\n")
        self.line += newlines
        if newlines:
            self.pos = len(result[result.rindex("\n"):]) - 1
        else:
            self.pos += size
        if not result:
            raise EOFError("Reached EOF")
        return result

    def readuntil(self, char: str) -> str:
        result = ""
        while self.peek() not in char:
            result += self.read(1)
        self.read(1)  # skip char
        return result


def parse(file: Path, output: Path):
    stream = Parser(file.read_text())

    layer = -1
    switch = "types"
    # default: types

    tl: defaultdict[str, list[dict] | int] = defaultdict(list)

    try:
        while True:
            token = stream.peek(1)
            if not token:
                logger.success("Finished parsing (EOF)")
                break

            match token:
                case "\n" | "\r" | " ":
                    stream.read(1)
                case "/":
                    stream.read(1)
                    while stream.peek() in ["/", " "]:
                        stream.read(1)
                    
                    comment = stream.readuntil("\n")
                    if match := re.match(r"LAYER (?P<layer>[0-9]+)", comment, re.IGNORECASE):
                        layer = int(match.group("layer"))
                        logger.info("Found layer: {layer}", layer=layer)
                case "-":
                    line = stream.readuntil("\n")
                    match = re.match(r"-*\s*(?P<switch>\w+)\s*-*", line, re.IGNORECASE)
                    if not match:
                        continue
                    switch = match.group("switch")
                    assert switch in ["types", "functions"], f"Found invalid switch: {line!r}"
                case char:
                    type_name = stream.readuntil("#")
                    namespace, _, type_name = type_name.rpartition(".")
                    constructor = stream.readuntil(" ")

                    logger.debug(
                        "Parsing {name}#{cid}...",
                        name=f"{namespace}.{type_name}" if namespace else type_name,
                        cid=constructor,
                    )

                    fields = []
                    while True:
                        while (token := stream.peek()) in whitespace:
                            stream.read(1)  # discard whitespace
                        if token in ["=", ";"]:
                            stream.read(1)
                            break
                        elif token in ["#"]:
                            # vector case
                            stream.read(1)
                            continue
                        elif token in ["{", "["]:
                            matching = {
                                "{": "}",
                                "[": "]",
                            }
                            stream.readuntil(matching[token])
                            continue

                        name = stream.readuntil(":")
                        type = stream.readuntil(" =")
                        logger.debug(" -> {name}: {type}", name=name, type=type)

                        fields.append(
                            {
                                "name": name,
                                "type": type,
                            }
                        )
                    
                    while (token := stream.peek()) in whitespace:
                        stream.read(1)  # discard whitespace
                    return_type = stream.readuntil(";")

                    parsed = {
                        "_": type_name,
                        "cid": constructor,
                        "params": fields,
                        "ret": return_type,
                    }
                    tl[switch].append(parsed)

                    logger.debug("*** {ret}", ret=return_type)
                    continue

                    logger.error(
                        "Error: invalid character ({char}) at line ({line}, pos={pos})",
                        char=char,
                        line=stream.line + 1,
                        pos=stream.pos + 1,
                    )
                    logger.debug("Context: {context}", context=stream.readuntil("\n"))
                    return
    except EOFError:
        logger.warning("Reached EOF")

    tl["layer"] = layer

    with output.open("w+") as to:
        to.write(template.read_text())


async def main():
    if "update" in sys.argv[1:] or not api.exists():
        logger.info("Updating api.tl...")

        async with httpx.AsyncClient() as client:
            with api.open("wb") as file:
                async with client.stream("GET", url=API_URL) as stream:
                    async for chunk in stream.aiter_bytes(chunk_size=4096):
                        file.write(chunk)

    logger.info("Parsing {name}...", name=api.name)
    parse(api, out / "api_tl.py")


if __name__ == "__main__":
    asyncio.run(main())
