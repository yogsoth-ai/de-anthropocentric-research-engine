import re
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"
FORBIDDEN = [r"C:\\", r"/Users/", r"\.claude", r"sessionId", r"YOGSOTH-AI",
             r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"]

def test_no_identifiers_in_data_outputs():
    if not DATA.exists():
        return  # nothing generated yet
    offenders = []
    for f in DATA.rglob("*"):
        if not f.is_file(): continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for pat in FORBIDDEN:
            if re.search(pat, text):
                offenders.append(f"{f.name}: matched /{pat}/")
    assert not offenders, "Privacy leak in data/: " + "; ".join(offenders)
