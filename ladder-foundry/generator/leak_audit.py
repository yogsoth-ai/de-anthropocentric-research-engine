"""L2 — W5 leak interceptor (BACKSTOP, not the primary control).

Primary W5 control is structural role-blindness: generation/loss roles never
see the 32 checks. This regex DENY list is a second line of defence so a leak
that slips into generated text is caught loudly. Word-boundary regex, not
substring matching (the old code's anti-pattern: 'P3' would have hit 'MP3').
"""
import re

# DENY vocabulary: 32-check ids, 6 primitives, detection-signature phrases,
# PG/NG engine names. Extend here as new check vocabulary appears.
# ponytail: bare ids R1-R18/P1-P14 also occur as figure/table labels ("Table P1") — this backstop will over-match those. Acceptable: primary W5 control is role-blindness; a hit only forces regenerate-reaudit. Upgrade to context-anchored matching (require an adjacent "check"/"precision"/"recall" token) when leak_audit is wired into L7 in STAGE 2 and real exec text exists to tune against.
_DENY_TERMS = [
    r"R(?:1[0-8]|[1-9])",        # R1..R18 precision checks
    r"P(?:1[0-4]|[1-9])",        # P1..P14 recall checks
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
