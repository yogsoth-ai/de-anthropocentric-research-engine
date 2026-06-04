"""N1 headline: confidence-graded map. NOT a pruning verdict."""
import argparse, json
from collections import Counter
from pathlib import Path

DISCLAIMER = ("Confidence-graded map of skill usage. 'unknown' is the honest "
              "default under thin coverage. This is NOT a pruning verdict.")

def build_completeness(model, graph, telemetry):
    names = [s["name"] for s in model["skills"] if not s.get("parse_error")]
    has_incoming = {e[1] for e in graph["edges"]}
    fired = set((telemetry or {}).get("firing_counts", {}).keys())
    telemetry_present = telemetry is not None
    labels = {}
    for n in names:
        if n in has_incoming or n in fired:
            labels[n] = "in-use"
        elif telemetry_present:
            labels[n] = "suspect-redundant"
        else:
            labels[n] = "unknown"
    return {
        "_disclaimer": DISCLAIMER,
        "labels": labels,
        "summary": dict(Counter(labels.values())),
        "coverage": {"telemetry_present": telemetry_present,
                     "skills_fired": len(fired)},
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--graph", required=True)
    ap.add_argument("--telemetry", default=None)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    model = json.loads(Path(a.model).read_text(encoding="utf-8"))
    graph = json.loads(Path(a.graph).read_text(encoding="utf-8"))
    telemetry = json.loads(Path(a.telemetry).read_text(encoding="utf-8")) if a.telemetry else None
    cm = build_completeness(model, graph, telemetry)
    Path(a.out).write_text(json.dumps(cm, indent=2, ensure_ascii=False), encoding="utf-8")
    print("labels:", cm["summary"])

if __name__ == "__main__":
    main()
