# deny-list：检测层词汇（32-check/6-primitive/检测特征）。卡片绝不能含。
DENY = [
    "deletable", "won't invoke", "wont invoke", "manipulable metric",
    "pseudo-question", "novel-good", "pseudo-good", "decorative mechanism",
    "skill-stuffing", "orphan deliverable", "mirror benchmark",
    "check ", "primitive", "detection signature",
]


def leak_audit(card_text: str) -> bool:
    """True = 干净（无 deny 词）；False = 命中 deny-list。"""
    low = card_text.lower()
    return not any(term in low for term in DENY)
