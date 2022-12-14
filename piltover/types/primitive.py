from dataclasses import dataclass


@dataclass(init=True, repr=True, frozen=True, kw_only=True)
class Message:
    session_id: int
    msg_id: int
    data: bytes
