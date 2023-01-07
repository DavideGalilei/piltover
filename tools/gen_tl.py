import re
import io
import sys
import asyncio

import httpx

from io import StringIO
from pathlib import Path
from string import whitespace
from collections import defaultdict
from typing import Any

from loguru import logger
from black import format_str, FileMode
from jinja2 import Environment, FileSystemLoader, select_autoescape


root = Path(__file__).parent.resolve(strict=True)
templates = (root / "templates").resolve(strict=True)
data = root / "resources"
data.mkdir(parents=True, exist_ok=True)
piltover = root.parent
out = piltover / "piltover" / "tl" / "generated"
# out = root / "output"
out.mkdir(parents=True, exist_ok=True)


FILES = [
    {
        "path": data / "api.tl",
        "url": "https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/Telegram/Resources/tl/api.tl",
        "bytes_str": False,
    },
    {
        "path": data / "mtproto.tl",
        "url": "https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/Telegram/Resources/tl/mtproto.tl",
        "bytes_str": True,
    },
]


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
            self.pos = len(result[result.rindex("\n") :]) - 1
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


TYPES_MAP = {
    "#": "Int32",
    "int": "Int32",
    "long": "Int64",
    "double": "float",
    "int128": "Int128",
    "int256": "Int256",
    "bool": "bool",
    "true": "Bit",
    "string": "str",
    "bytes": "bytes",
}


def typeinfo(typ: str, bytes_str: bool = False) -> dict:
    if typ.lower() in TYPES_MAP:
        # hardcode exception for res_pq etc... (generally, mtproto.tl)
        if typ == "string" and bytes_str:
            typ = "bytes"
        else:
            typ = TYPES_MAP[typ.lower()]

        return {
            "optional": False,
            "typ": typ,
        }
    elif typ == "X" or typ.startswith("!"):
        typ = "TLType"
        return {
            "optional": False,
            "typ": typ,
        }
    elif typ.lower().startswith("vector"):
        inner = re.match(r"vector\s*<?(?P<typ>[\w\.]+)>?", typ, re.IGNORECASE)
        if not inner:
            raise TypeError(f"Invalid vector type: {typ!r}")

        typ = inner.group("typ")
        info = typeinfo(typ, bytes_str=bytes_str)
        if info["optional"]:
            raise TypeError(f"Vector elements cannot be optional: {typ!r}")

        typ = repr(info["original"]) if "original" in info else info["typ"]

        return {
            "optional": False,
            "typ": f"list[{typ}]",
        }
    elif "?" in typ:
        field_bit, typ = typ.split("?", 1)
        field, bit = field_bit.split(".", 1)
        bit = int(bit)

        info = typeinfo(typ, bytes_str=bytes_str)

        return {
            "optional": True,
            "field": field,
            "bit": bit,
            "typ": info["typ"],
        }
    else:
        # return {
        #     "optional": False,
        #     "typ": repr(typ),
        # }
        return {
            "optional": False,
            "typ": "TLType",
            "original": typ,
        }


def parse(file: Path, output: Path, bytes_str: bool = False):
    stream = Parser(file.read_text())

    layer = -1
    switch = "types"
    # default: types

    tl: defaultdict[str, list[dict]] = defaultdict(list)

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
                    if match := re.match(
                        r"LAYER (?P<layer>[0-9]+)", comment, re.IGNORECASE
                    ):
                        layer = int(match.group("layer"))
                        logger.info("Found layer: {layer}", layer=layer)
                case "-":
                    line = stream.readuntil("\n")
                    match = re.match(r"-*\s*(?P<switch>\w+)\s*-*", line, re.IGNORECASE)
                    if not match:
                        continue
                    switch = match.group("switch")
                    assert switch in [
                        "types",
                        "functions",
                    ], f"Found invalid switch: {line!r}"
                case _:
                    type_info = stream.readuntil(" ")
                    if "#" not in type_info:
                        logger.debug(
                            "Skipping {name}, no constructor found", name=type_info
                        )
                        stream.readuntil(";")
                        continue

                    type_name, constructor = type_info.split("#")
                    namespace, _, type_name = type_name.rpartition(".")
                    formatted = f"{namespace}.{type_name}" if namespace else type_name

                    if not constructor:
                        logger.debug(
                            "Skipping {name}, no constructor found", name=formatted
                        )
                        stream.readuntil(";")
                        continue

                    logger.debug(
                        "Parsing {name}#{cid}...",
                        name=formatted,
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
                        "_": formatted,
                        "namespace": namespace,
                        "name": type_name,
                        "cid": constructor,
                        "params": fields,
                        "ret": return_type,
                        "switch": switch,
                    }
                    tl[switch].append(parsed)

                    logger.debug("*** {ret}", ret=return_type)
    except EOFError:
        logger.warning("Reached EOF")
    except Exception:
        logger.exception("An error occurred")
        logger.error(
            "Error at line ({line}, pos={pos})",
            line=stream.line + 1,
            pos=stream.pos + 1,
        )
        logger.debug("Context: {context}", context=stream.readuntil("\n"))

    result: dict[str, Any] = dict(tl)
    result["layer"] = layer

    VECTOR_CID = 0x1CB5C415
    BOOL_FALSE = 0xBC799737
    BOOL_TRUE = 0x997275B5
    MSG_CONTAINER_CID = 0x73F1F8DC
    RPC_ERROR_CID = 0x2144CA19

    to_skip = list(
        map(
            lambda cid: hex(cid)[2:],
            [VECTOR_CID, BOOL_FALSE, BOOL_TRUE, MSG_CONTAINER_CID, RPC_ERROR_CID],
        )
    )

    # clean result
    clean = []

    for typ in result.get("types", []) + result.get("functions", []):
        push = {}
        if typ["cid"] in to_skip:
            continue

        push["_"] = typ["_"]
        push["cid"] = typ["cid"]
        push["switch"] = typ["switch"]

        push["params"] = []
        for field in typ.get("params", []):
            push["params"].append(
                {
                    "name": field["name"],
                    "info": typeinfo(field["type"], bytes_str=bytes_str),
                }
            )

        push["ret"] = typeinfo(typ["ret"], bytes_str=bytes_str)
        clean.append(push)

    env = Environment(
        loader=FileSystemLoader(templates),
        autoescape=select_autoescape(),
    )

    template = env.get_template("template.jinja2")

    with output.open("w+") as to:
        logger.info("Rendering template...")
        rendered = template.render(
            types=clean,
            layer=layer,
        )
        # TODO: uncomment
        logger.info("Formatting file with black...")
        rendered = format_str(rendered, mode=FileMode())

        logger.info(
            "Writing file to {path}",
            path=output.relative_to(Path.cwd()).as_posix(),
        )
        to.write(rendered)


async def main():
    if "update" in sys.argv[1:] or not all(file["path"].exists() for file in FILES):
        for file in FILES:
            path: Path = file["path"]
            logger.info("Updating {name}...", name=path.name)

            async with httpx.AsyncClient() as client:
                with path.open("wb") as to:
                    async with client.stream("GET", url=file["url"]) as stream:
                        async for chunk in stream.aiter_bytes(chunk_size=4096):
                            to.write(chunk)

    logger.remove()
    logger.add(sys.stderr, level="INFO")

    for file in FILES:
        path = file["path"]
        logger.info("Parsing {name}...", name=path.name)
        out_name = out / f"{path.stem}_tl.py"
        parse(path, out_name, bytes_str=file["bytes_str"])


if __name__ == "__main__":
    asyncio.run(main())
