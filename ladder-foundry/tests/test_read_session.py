import json
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))
from read_session import find_latest_session, read_turns, cwd_to_slug


def _write_session(dirpath, name, turns):
    dirpath.mkdir(parents=True, exist_ok=True)
    p = dirpath / name
    lines = []
    for role, text in turns:
        lines.append(json.dumps({"type": role, "message": {"role": role,
            "content": [{"type": "text", "text": text}]}}))
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def test_cwd_to_slug_replaces_separators():
    s = cwd_to_slug(r"D:\YOGSOTH-AI\ladder-foundry\sandbox")
    assert "\\" not in s and "/" not in s and ":" not in s
    assert s.startswith("D-")


def test_find_latest_session_picks_newest(tmp_path):
    slug = "D--proj-sandbox"
    d = tmp_path / "projects" / slug
    p1 = _write_session(d, "aaa.jsonl", [("user", "hi")])
    p2 = _write_session(d, "bbb.jsonl", [("user", "yo")])
    import os, time
    os.utime(p2, (time.time() + 10, time.time() + 10))   # make bbb newest
    assert find_latest_session(str(tmp_path), slug) == p2


def test_read_turns_extracts_role_and_text(tmp_path):
    d = tmp_path / "projects" / "slug1"
    p = _write_session(d, "s.jsonl", [("user", "play this persona"),
                                      ("assistant", "Understood, I am the supervisor.")])
    turns = read_turns(p)
    assert turns[0]["role"] == "user" and "persona" in turns[0]["text"]
    assert turns[1]["role"] == "assistant" and "supervisor" in turns[1]["text"]


def test_logs_dir_is_required(tmp_path, monkeypatch):
    import read_session
    monkeypatch.setattr(sys, "argv", ["read_session.py"])   # no --logs-dir
    with pytest.raises(SystemExit):                          # argparse exits 2
        read_session.main()
