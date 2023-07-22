from enum import Enum, auto


class Transport(Enum):
    Abridged = auto()
    Intermediate = auto()
    PaddedIntermediate = auto()
    Full = auto()
    Obfuscated = auto()
