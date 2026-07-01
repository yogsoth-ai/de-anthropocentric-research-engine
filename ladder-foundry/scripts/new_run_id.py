#!/usr/bin/env python3
"""System time -> run_id (yyyy-mm-dd-hh-mm-ss) + build runs/<id>/ skeleton.
Pure stdlib (no generator import). Called once at the epoch-loop entry."""
import argparse
import datetime
from pathlib import Path

SUBDIRS = ("configs", "transcripts", "triples", "loss", "weights")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-root", default="runs")
    a = ap.parse_args()
    run_id = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    base = Path(a.runs_root) / run_id
    for sub in SUBDIRS:
        (base / sub).mkdir(parents=True, exist_ok=True)
    print(run_id)


if __name__ == "__main__":
    main()
