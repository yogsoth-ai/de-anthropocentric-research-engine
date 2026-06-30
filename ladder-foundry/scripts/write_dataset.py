#!/usr/bin/env python3
"""Privacy whitelist trim + schema -> dataset/<topic>/<sample>.json. Hard-fails
if the triple carries any field outside {research_config, research_graph,
research_result} (catches a leaked logs_dir), and again if the assembled output
has any non-whitelist key. loss1/topic_pass are CLI params (STAGE 4's loss fills
real values later)."""
import argparse
import json
import sys
from pathlib import Path

TRIPLE_KEYS = {"research_config", "research_graph", "research_result"}
WHITELIST = {"sample_id", "label", "research_config", "research_graph",
             "research_result", "loss1_fidelity", "topic_pass", "intended_rank"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--sample", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--rung", type=int, required=True)
    ap.add_argument("--out-root", required=True)
    ap.add_argument("--axis-levels", default="{}")
    ap.add_argument("--loss1", default="0.0")
    ap.add_argument("--topic-pass", default="false")
    a = ap.parse_args()
    tri = json.loads((Path(a.run_dir) / "triples" / f"{a.sample}.json").read_text(encoding="utf-8"))
    extra = set(tri) - TRIPLE_KEYS
    if extra:
        sys.exit(f"FATAL: triple has non-whitelist fields {extra} (privacy red line)")
    sample = {
        "sample_id": a.sample,
        "label": {"rung_id": a.rung, "axis_levels": json.loads(a.axis_levels)},
        "research_config": tri["research_config"],
        "research_graph": tri["research_graph"],
        "research_result": tri["research_result"],
        "loss1_fidelity": float(a.loss1),
        "topic_pass": a.topic_pass.lower() == "true",
        "intended_rank": a.rung,
    }
    leaked = set(sample) - WHITELIST
    if leaked:
        sys.exit(f"FATAL: output has non-whitelist fields {leaked}")
    out = Path(a.out_root) / a.topic
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{a.sample}.json").write_text(
        json.dumps(sample, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
