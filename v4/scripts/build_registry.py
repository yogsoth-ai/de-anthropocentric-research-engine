"""Derive v4 registry artifacts from the read-only architecture source."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCH = Path(r"D:\YOGSOTH-AI\file-transfer\2026-08-23-22-16-dare-v4-architecture.json")
REG = ROOT / "v4" / "registry"
PROV_SUFFIX = re.compile(r"\s*(?:\([^)]*\)|\[[^]]*\])\s*$")
EXPLICIT_INTERMEDIATE = {
    "conceptual-blending [strategy]",
    "Pass3/merge-near-duplicate-concepts",
}
PROVENANCE_ALIASES = {
    "conceptual-blending/generic-space": "generic-space-extraction",
}
DESC_MODE_OVERRIDES = {
    "synthesize-meta-analytic-evidence": {
        "modes": ["pairwise", "network", "cumulative", "heterogeneity", "bias"],
        "modes_provenance": {
            "source": "architecture.desc",
            "reason": "The authoritative desc explicitly declares these modes while the architecture modes field is absent.",
        },
    },
}


def provenance_variants(value: str) -> set[str]:
    value = value.strip()
    stripped = value
    while True:
        next_value = PROV_SUFFIX.sub("", stripped).strip()
        if next_value == stripped:
            break
        stripped = next_value
    basename = stripped.rsplit("/", 1)[-1]
    variants = {value, stripped, basename}
    if "/" in stripped:
        package, name = stripped.rsplit("/", 1)
        variants.add(f"{package}-{name}")
    alias = PROVENANCE_ALIASES.get(stripped)
    if alias:
        variants |= {alias, alias.rsplit("/", 1)[-1]}
    return {x for x in variants if x}


def provenance_statuses(nodes: list[dict]) -> None:
    source = ROOT / "scripts" / "refactory_source.json"
    try:
        source_names = {n.get("name", "") for n in json.loads(source.read_text(encoding="utf-8")).get("nodes", [])}
        source_names |= {x.rsplit("/", 1)[-1] for x in source_names}
    except (OSError, json.JSONDecodeError):
        source_names = set()
    for node in nodes:
        statuses = {}
        for old in node.get("old", []):
            clean = PROV_SUFFIX.sub("", old).strip()
            variants = provenance_variants(old)
            if old in EXPLICIT_INTERMEDIATE:
                statuses[old] = "intermediate"
            elif any(candidate in source_names for candidate in variants):
                statuses[old] = "resolved"
            elif clean.startswith("Pass") or re.search(r"\[(?:campaign|strategy)(?:/tactic)?\]", old):
                statuses[old] = "intermediate"
            else:
                statuses[old] = "concept"
        node["provenance_status"] = statuses


def main() -> None:
    source = json.loads(ARCH.read_text(encoding="utf-8"))
    nodes = []
    for kind in ("tactics", "sops"):
        for node in source[kind]:
            item = dict(node)
            if node.get("id") in DESC_MODE_OVERRIDES:
                item.update(DESC_MODE_OVERRIDES[node["id"]])
            item["type"] = "tactic" if kind == "tactics" else "sop"
            item["provenance"] = item.get("old", [])
            nodes.append(item)
    provenance_statuses(nodes)
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
