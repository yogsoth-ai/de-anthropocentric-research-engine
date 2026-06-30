"""L2 — W5 leak interceptor (BACKSTOP, not the primary control).

Primary W5 control is structural role-blindness: generation/loss roles never
see the 32 checks. This regex DENY list is a second line of defence so a leak
that slips into generated text is caught loudly. Word-boundary regex, not
substring matching (the old code's anti-pattern: 'P3' would have hit 'MP3').
"""
import re

# DENY vocabulary: 32-check ids, 6 primitives, detection-signature phrases,
# PG/NG engine names. Extend here as new check vocabulary appears.
_DENY_TERMS = [
    r"R\d{1,2}",                 # R1..R18 precision checks
    r"P\d{1,2}",                 # P1..P14 recall checks
    r"primitive",
    r"detection signature",
    r"pseudo-good",
    r"novel-good",
    r"PG engine", r"NG engine",
    r"PG-engine", r"NG-engine",
]
_DENY = re.compile(r"\b(" + "|".join(_DENY_TERMS) + r")\b", re.IGNORECASE)


class LeakHit(Exception):
    """Raised when text contains a check/primitive/detection-signature term."""


def leak_audit(text):
    m = _DENY.search(text)
    if m:
        raise LeakHit(f"leak term matched: {m.group(0)!r}")
    return None
