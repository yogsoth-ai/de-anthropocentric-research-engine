# deny-list: detection-layer vocabulary (32-check / 6-primitive / detection signatures). Cards must never contain these.
DENY = [
    "deletable", "won't invoke", "wont invoke", "manipulable metric",
    "pseudo-question", "novel-good", "pseudo-good", "decorative mechanism",
    "skill-stuffing", "orphan deliverable", "mirror benchmark",
    "check ", "primitive", "detection signature",
]


def leak_audit(card_text: str) -> bool:
    """True = clean (no deny term); False = a deny-list term was hit."""
    low = card_text.lower()
    return not any(term in low for term in DENY)

