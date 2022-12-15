def read_int(data: bytes) -> int:
    return int.from_bytes(data, byteorder="little", signed=False)
