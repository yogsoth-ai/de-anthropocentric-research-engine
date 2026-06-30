#!/usr/bin/env python3
"""Read THIS run's exec session jsonl (located by cwd-slug) -> transcript.md,
user/assistant turns only. --logs-dir is REQUIRED (privacy red line: the only
place that reads CC logs). DRY: reuses sandbox/read_session.py's three
functions; adds only the .md formatting shell."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))
from read_session import cwd_to_slug, find_latest_session, read_turns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True,
                    help="CC projects logs dir (REQUIRED, no default — privacy)")
    ap.add_argument("--cwd", required=True, help="the exec cwd to slug + locate")
    ap.add_argument("--sample", required=True, help="sample id for the .md header")
    ap.add_argument("--out", required=True, help="output .md path")
    a = ap.parse_args()
    session = find_latest_session(a.logs_dir, cwd_to_slug(a.cwd))
    blocks = [f"# transcript: {a.sample}\n"]
    for t in read_turns(session):
        if t["role"] in ("user", "assistant"):
            blocks.append(f"### {t['role']}\n\n{t['text']}\n")
    Path(a.out).write_text("\n".join(blocks), encoding="utf-8")  # never write slug / abs log path


if __name__ == "__main__":
    main()
