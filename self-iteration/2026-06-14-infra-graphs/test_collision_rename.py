import subprocess, re, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _collision():
    return json.loads((HERE / "collision-links.json").read_text(encoding="utf-8"))["groups"]

def test_collision_links_shape():
    g = _collision()
    assert len(g) == 64, f"collision nodes={len(g)} (want 64)"
    names = {c["old"] for c in g}
    assert len(names) == 29, f"collision names={len(names)} (want 29)"
    # no wrapper / no REF leaked in
    WRAP = {"web-search","web-research","paper-overview","paper-search","paper-research"}
    assert not (names & WRAP), f"wrapper leaked into collision set: {names & WRAP}"
    for c in g:
        assert "/" not in c["old"], f"old name should be bare: {c['old']}"
