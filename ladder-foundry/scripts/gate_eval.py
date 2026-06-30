#!/usr/bin/env python3
"""Pure gate arithmetic: topic (3-way AND) / batch (pass_ratio) / converged
(last 3). No CC/codex call. Thresholds are module constants here; STAGE 4 may
externalize them to a references file."""
import argparse

FIDELITY_MIN = 0.90
BATCH_RATIO_MIN = 0.80


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    t = sub.add_parser("topic")
    t.add_argument("--fidelity-rate", type=float, required=True)
    t.add_argument("--mono", required=True)
    t.add_argument("--endpoint", required=True)
    b = sub.add_parser("batch")
    b.add_argument("--flags", required=True)
    c = sub.add_parser("converged")
    c.add_argument("--recent", required=True)
    a = ap.parse_args()
    if a.mode == "topic":
        ok = (a.fidelity_rate >= FIDELITY_MIN and a.mono == "true" and a.endpoint == "true")
        print("true" if ok else "false")
    elif a.mode == "batch":
        flags = [x == "true" for x in a.flags.split(",")]
        print("true" if sum(flags) / len(flags) >= BATCH_RATIO_MIN else "false")
    elif a.mode == "converged":
        rs = [float(x) for x in a.recent.split(",")]
        print("true" if len(rs) >= 3 and all(r >= BATCH_RATIO_MIN for r in rs[-3:]) else "false")


if __name__ == "__main__":
    main()
