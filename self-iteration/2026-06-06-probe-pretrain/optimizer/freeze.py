import json
from collections import defaultdict
from pathlib import Path


def coverage_report(samples):
    """Count occurrences of each overlay axis coordinate in the training set (RR-2 monoculture monitor)."""
    rep = defaultdict(lambda: defaultdict(int))
    for s in samples:
        for ax in ("A1", "A2", "A3", "A4", "A5", "B1"):
            v = s.get("label", {}).get(ax)
            if v is not None:
                rep[ax][v] += 1
    return {k: dict(v) for k, v in rep.items()}


def freeze_weights(weights_dict, out_path):
    """Freeze: stamp _frozen; the generator does not change after this (spec sec 9)."""
    d = dict(weights_dict)
    d["_frozen"] = True
    Path(out_path).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
