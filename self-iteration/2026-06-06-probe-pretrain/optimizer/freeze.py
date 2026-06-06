import json
from collections import defaultdict
from pathlib import Path


def coverage_report(samples):
    """统计训练集里每个 overlay 轴坐标出现次数（RR-2 监控 monoculture）。"""
    rep = defaultdict(lambda: defaultdict(int))
    for s in samples:
        for ax in ("A1", "A2", "A3", "A4", "A5", "B1"):
            v = s.get("label", {}).get(ax)
            if v is not None:
                rep[ax][v] += 1
    return {k: dict(v) for k, v in rep.items()}


def freeze_weights(weights_dict, out_path):
    """冻结：打上 _frozen 标记，此后生成器不再改（spec §9）。"""
    d = dict(weights_dict)
    d["_frozen"] = True
    Path(out_path).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
