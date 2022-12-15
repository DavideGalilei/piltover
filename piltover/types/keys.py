from dataclasses import dataclass


@dataclass(init=True)
class Keys:
    public_key: str
    private_key: str
