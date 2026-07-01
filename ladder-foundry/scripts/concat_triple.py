#!/usr/bin/env python3
"""config + transcript fence blocks -> (research_config, research_graph,
research_result) triple. Cut by info-string fence, take the LAST block of each
kind (the accepted draft after pushback). Missing a required fence -> ValueError
(argparse/uncaught -> non-zero exit)."""
import argparse
import json
import re
from pathlib import Path


def last_block(md, info):
    """Return the JSON parsed from the LAST ```<info> ... ``` fence."""
    rx = re.compile(r"```" + re.escape(info) + r"\s*\n(.*?)\n```", re.DOTALL)
    blocks = rx.findall(md)
    if not blocks:
        raise ValueError(f"no '{info}' fenced block in transcript")
    return json.loads(blocks[-1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--sample", required=True)
    a = ap.parse_args()
    rd = Path(a.run_dir)
    cfg = json.loads((rd / "configs" / f"{a.sample}.json").read_text(encoding="utf-8"))
    md = (rd / "transcripts" / f"{a.sample}.md").read_text(encoding="utf-8")
    triple = {"research_config": cfg,
              "research_graph": last_block(md, "research-graph"),
              "research_result": last_block(md, "research-result")}
    (rd / "triples" / f"{a.sample}.json").write_text(
        json.dumps(triple, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
