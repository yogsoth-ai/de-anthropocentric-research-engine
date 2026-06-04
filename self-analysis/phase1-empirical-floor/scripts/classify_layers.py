"""Assign each skill a 4-layer level (campaign/strategy/tactic/sop) by fusing
multiple signals, with a hand-curated override map for meta/reference/special
nodes. Consumed by render_graph.py to lay out the body strictly by layer.

Signal priority (highest first):
  1. override map  — hand-pinned meta/reference/known-special nodes
  2. declared `type` frontmatter
  3. skill-index description keyword (Campaign/strategy/tactic/SOP)
  4. graph role (target of a tactics:/sops: edge, source of a campaign edge)
  5. leaf-default — has a phase but none of the above => bottom-layer SOP
  6. unresolved — nothing known
"""
import argparse, json, re
from collections import Counter, defaultdict
from pathlib import Path

LAYERS = ["campaign", "strategy", "tactic", "sop"]

# 9 nodes not assignable from the 8 research phases (engine + spec toolchain).
# Layers confirmed from docs/superpowers spec + user direction.
OVERRIDES = {
    "de-anthropocentric-research-engine": "meta",   # the engine orchestrator
    "research-catalog": "reference",                # "Strategy Book TOC", not sop-layer
    "writing-specs": "sop",
    "executing-specs": "sop",
    "skill-index": "sop",
    "spec-self-review": "sop",                      # spec: "SOP (mandatory)"
    "scope-clarification": "sop",                   # writing-specs questioning SOP
    "campaign-selection": "sop",
    "constraint-elicitation": "sop",
}

def _desc_lvl(name, desc_of):
    d = (desc_of.get(name) or "").lower()
    if re.search(r"\bcampaign\b", d): return "campaign"
    if re.search(r"\bstrateg", d): return "strategy"
    if re.search(r"\btactic\b", d): return "tactic"
    if re.search(r"\bsop\b", d): return "sop"
    return None

def classify_node(name, typ_of, desc_of, role_of, phase_of, overrides):
    if name in overrides:
        return overrides[name], "override"
    t = typ_of.get(name)
    if t in LAYERS:
        return t, "declared-type"
    dl = _desc_lvl(name, desc_of)
    if dl:
        return dl, "index-desc"
    roles = role_of.get(name, set())
    for lvl in LAYERS:
        if lvl in roles:
            return lvl, "graph-role"
    if phase_of.get(name):
        return "sop", "leaf-default"
    return None, "unresolved"

def build_roles(graph):
    role = defaultdict(set)
    for a, b, src in graph["edges"]:
        if src == "tactics": role[b].add("tactic"); role[a].add("strategy")
        elif src == "sops":  role[b].add("sop");    role[a].add("strategy")
        elif src == "campaign": role[a].add("campaign")
    return role

def parse_index(index_path):
    """Parse skill-index.md -> {name: phase}, {name: description}."""
    text = Path(index_path).read_text(encoding="utf-8").lstrip("﻿")
    phase = None
    phase_of, desc_of = {}, {}
    for line in text.splitlines():
        h = re.match(r"^##\s+([a-z0-9-]+)\s+\(\d+\s+skills?\)", line)
        if h:
            phase = h.group(1); continue
        row = re.match(r"^\|\s*([a-z0-9-]+)\s*\|\s*(.+?)\s*\|$", line)
        if row and phase and row.group(1).lower() != "skill":
            phase_of[row.group(1)] = phase
            desc_of[row.group(1)] = row.group(2)
    return phase_of, desc_of

def classify_all(graph, model, index_path, overrides=OVERRIDES):
    typ_of = {s["name"]: s.get("type") for s in model["skills"] if not s.get("parse_error")}
    phase_of, desc_of = parse_index(index_path)
    role_of = build_roles(graph)
    out = {}
    for n in graph["nodes"]:
        lvl, src = classify_node(n, typ_of, desc_of, role_of, phase_of, overrides)
        out[n] = {"layer": lvl, "source": src, "phase": phase_of.get(n)}
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--index", required=True, help="path to skill-index.md")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    graph = json.loads(Path(a.graph).read_text(encoding="utf-8"))
    model = json.loads(Path(a.model).read_text(encoding="utf-8"))
    layered = classify_all(graph, model, a.index)
    Path(a.out).write_text(json.dumps(layered, indent=2, ensure_ascii=False), encoding="utf-8")
    print("layers:", dict(Counter(v["layer"] for v in layered.values())))
    print("sources:", dict(Counter(v["source"] for v in layered.values())))

if __name__ == "__main__":
    main()
