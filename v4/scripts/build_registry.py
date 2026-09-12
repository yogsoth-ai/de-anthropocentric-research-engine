"""Derive v4 registry artifacts from the read-only architecture source."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCH = Path(r"D:\YOGSOTH-AI\file-transfer\2026-08-23-22-16-dare-v4-architecture.json")
REG = ROOT / "v4" / "registry"


def main() -> None:
    source = json.loads(ARCH.read_text(encoding="utf-8"))
    nodes = []
    for kind in ("tactics", "sops"):
        for node in source[kind]:
            item = dict(node)
            item["type"] = "tactic" if kind == "tactics" else "sop"
            item["provenance"] = item.get("old", [])
            nodes.append(item)
    calls = [
        {"type": "calls", "source": src, "target": target}
        for src, targets in source["calls"].items()
        for target in targets
    ]
    jumps = [
        {"type": "jump", "source": edge[0], "target": edge[1]}
        for edge in source["jumps"]
    ]
    graph = {
        "schema": "dare-v4-graph-1",
        "source": str(ARCH),
        "node_model": source["node_model"],
        "edge_semantics": source["edge_semantics"],
        "stats": source["stats"],
        "nodes": nodes,
        "edges": calls + jumps,
        "calls": calls,
        "jumps": jumps,
        "counts": {
            "nodes": len(nodes),
            "tactics": len(source["tactics"]),
            "sops": len(source["sops"]),
            "calls": len(calls),
            "jumps": len(jumps),
            "edges": len(calls) + len(jumps),
            "capability_contracts": len(source["capability_audit"]),
        },
    }
    capabilities = {
        "schema": "dare-v4-capabilities-1",
        "source": str(ARCH),
        "count": len(source["capability_audit"]),
        "contracts": source["capability_audit"],
    }
    REG.mkdir(parents=True, exist_ok=True)
    (REG / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REG / "capabilities.json").write_text(json.dumps(capabilities, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
