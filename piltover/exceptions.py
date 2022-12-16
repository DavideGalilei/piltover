from piltover.utils import nameof


class Error(Exception):
    pass


class Disconnection(Error):
    pass


class InvalidConstructor(Error):
    def __init__(self, cid: int):
        super().__init__()
        self.cid = cid

    def __str__(self) -> str:
        return f"{nameof(self)}(cid=0x{self.cid:08x})"
