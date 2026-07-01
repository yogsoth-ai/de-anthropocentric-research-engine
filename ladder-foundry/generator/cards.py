"""L6 — PolicyCard serialization. F0..F9 + axis_levels → JSON-serializable dict."""
from dataclasses import dataclass, asdict


@dataclass
class PolicyCard:
    F0: str
    F1: str
    F2: str
    F3: str
    F4: str
    F5: str
    F6: str
    F7: str
    F8: str
    F9: str
    axis_levels: dict


def to_dict(card):
    return asdict(card)
