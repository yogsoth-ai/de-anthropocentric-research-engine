"""Read a sim-cc's own session jsonl. PRIVACY: --logs-dir is REQUIRED (no
default) so the CC-log path is never baked into committed source. We locate the
session by globbing projects/<cwd-slug>/ — NEVER by --session-id (banned)."""
import argparse
import json
from pathlib import Path


def cwd_to_slug(cwd):
    # CC's slug rule: non-alnum path chars -> '-'. Good enough to locate the dir.
    out = []
    for ch in cwd:
        out.append(ch if ch.isalnum() or ch == "-" else "-")
    return "".join(out)


def find_latest_session(logs_dir, cwd_slug):
    proj = Path(logs_dir) / "projects" / cwd_slug
    sessions = sorted(proj.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not sessions:
        raise FileNotFoundError(f"no .jsonl under projects/{cwd_slug}/")
    return sessions[-1]


def read_turns(session_path):
    turns = []
    for line in Path(session_path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        msg = rec.get("message") or {}
        role = msg.get("role") or rec.get("type")
        content = msg.get("content")
        if isinstance(content, list):
            text = " ".join(b.get("text", "") for b in content if isinstance(b, dict))
        else:
            text = content if isinstance(content, str) else ""
        if role and text:
            turns.append({"role": role, "text": text})
    return turns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True,
                    help="CC projects logs dir (REQUIRED, no default — privacy)")
    ap.add_argument("--cwd", required=True, help="the sim cwd to slug + locate")
    args = ap.parse_args()
    session = find_latest_session(args.logs_dir, cwd_to_slug(args.cwd))
    for t in read_turns(session):
        print(f"[{t['role']}] {t['text'][:200]}")


if __name__ == "__main__":
    main()
