#!/usr/bin/env python3
"""F2: revise one weights JSON segment (via generator.weights.revise) + append
revision_log.jsonl + write weights/<batch+1>.json. F1: --copy byte-for-byte
copy forward, no log. Data-oriented: edits JSON data only; this source never
moves. Invariants (frozen_label locked, collision_offset_axis enum) are enforced
by weights.revise, NOT re-implemented here."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1]: generator/ is sibling
from generator import weights as W


def next_id(batch_id):
    return f"batch-{int(batch_id.split('-')[1]) + 1}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights-dir", required=True)
    ap.add_argument("--batch-id", required=True)
    ap.add_argument("--copy", action="store_true")   # F1 copy mode
    ap.add_argument("--target")
    ap.add_argument("--key")
    ap.add_argument("--new")
    ap.add_argument("--reason")
    a = ap.parse_args()
    wd = Path(a.weights_dir)
    cur = W.load(wd / f"{a.batch_id}.json")
    nxt_path = wd / f"{next_id(a.batch_id)}.json"
    if a.copy:
        # F1: byte-for-byte copy forward, no change, no log
        nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2), encoding="utf-8")
        return
    rec = W.revise(cur, target=a.target, key=a.key, new=a.new, reason=a.reason)
    nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(wd.parent / "revision_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))       # for CC to assemble the weight_revised trace event


if __name__ == "__main__":
    main()
