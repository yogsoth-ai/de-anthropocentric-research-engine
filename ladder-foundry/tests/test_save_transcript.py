import json, subprocess, sys


def test_logs_dir_required(tmp_path):
    r = subprocess.run([sys.executable, "scripts/save_transcript.py",
        "--cwd", str(tmp_path), "--sample", "s1", "--out", str(tmp_path / "t.md")])
    assert r.returncode != 0      # missing --logs-dir must hard-fail (privacy red line)


def test_extracts_user_assistant_only(tmp_path):
    # synthetic logs dir laid out as CC does: projects/<cwd-slug>/<session>.jsonl
    cwd = tmp_path / "execwd"
    slug = "".join(c if c.isalnum() or c == "-" else "-" for c in str(cwd))
    proj = tmp_path / "logs" / "projects" / slug
    proj.mkdir(parents=True)
    (proj / "sess.jsonl").write_text("\n".join([
        json.dumps({"type": "user", "message": {"role": "user", "content": "question A"}}),
        json.dumps({"type": "assistant", "message": {"role": "assistant",
                    "content": [{"type": "text", "text": "reply B"}]}}),  # list-of-blocks
        json.dumps({"type": "system", "message": {"role": "system", "content": "internal noise"}}),
    ]), encoding="utf-8")
    out = tmp_path / "t.md"
    subprocess.check_call([sys.executable, "scripts/save_transcript.py",
        "--logs-dir", str(tmp_path / "logs"), "--cwd", str(cwd),
        "--sample", "batch-0-topic00-id0", "--out", str(out)])
    txt = out.read_text(encoding="utf-8")
    assert "question A" in txt and "reply B" in txt   # user + assistant (list-of-blocks) reach .md
    assert "internal noise" not in txt                # system filtered out
    assert "batch-0-topic00-id0" in txt               # sample header present
    assert slug not in txt and str(tmp_path) not in txt  # privacy: no slug / abs log path in body
