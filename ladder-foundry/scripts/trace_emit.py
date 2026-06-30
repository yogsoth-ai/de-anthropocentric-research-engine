#!/usr/bin/env python3
"""Append one event line to trace.jsonl. 7 common-header fields (ts/run_id/
event/batch_id/topic_id/rung_id/seq) + a per-event body from extra --key val
pairs. ts + seq are generated here (never caller-supplied). Stateless: seq
continues from the file's last valid line +1."""
import argparse
import datetime
import json
from pathlib import Path

COMMON = ["run_id", "event", "batch_id", "topic_id", "rung_id"]


def next_seq(trace):
    p = Path(trace)
    if not p.exists():
        return 1
    lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    # micro-fix B: a truncated/corrupt final line (crash mid-write) must not
    # crash the emitter — scan upward to the last line that parses.
    for line in reversed(lines):
        try:
            return json.loads(line)["seq"] + 1
        except (json.JSONDecodeError, KeyError):
            continue
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", required=True)
    for k in COMMON:
        ap.add_argument(f"--{k}", default=None)
    a, unknown = ap.parse_known_args()
    # per-event body: remaining --key val pairs. micro-fix A: try json.loads so
    # nested objects/arrays (config_full, axis_levels, recent_ratios, ...)
    # round-trip as parsed structures, not stringified.
    extra = {}
    it = iter(unknown)
    for tok in it:
        if tok.startswith("--"):
            raw = next(it, None)
            try:
                extra[tok[2:]] = json.loads(raw) if raw is not None else None
            except (json.JSONDecodeError, TypeError):
                extra[tok[2:]] = raw
    row = {"ts": datetime.datetime.now().isoformat(),
           "run_id": a.run_id, "event": a.event, "batch_id": a.batch_id,
           "topic_id": a.topic_id, "rung_id": a.rung_id, "seq": next_seq(a.trace)}
    row.update(extra)
    p = Path(a.trace)
    # Ensure we're on a new line in case the file ends without a newline
    # (e.g., from a crash during a previous write).
    prefix = ""
    if p.exists() and p.stat().st_size > 0:
        content = p.read_text(encoding="utf-8")
        if content and not content.endswith("\n"):
            prefix = "\n"
    with open(a.trace, "a", encoding="utf-8") as f:
        f.write(prefix + json.dumps(row, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
