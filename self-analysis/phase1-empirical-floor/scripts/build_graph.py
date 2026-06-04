"""N1: reconstruct the forward call graph from frontmatter declarations."""
import argparse, json
from pathlib import Path

def build_graph(model: dict) -> dict:
    nodes = {s["name"] for s in model["skills"] if not s.get("parse_error")}
    edges = []
    for s in model["skills"]:
        if s.get("parse_error"): continue
        a = s["name"]
        for parent in s.get("used_by", []):
            edges.append([parent, a, "used-by"])
        for dep in s.get("dependencies", []):
            edges.append([a, dep, "dependencies"])
        for tac in s.get("tactics", []):
            edges.append([a, tac, "tactics"])
        for sop in s.get("sops", []):
            edges.append([a, sop, "sops"])
        if s.get("campaign"):
            edges.append([s["campaign"], a, "campaign"])
    referenced = {e[0] for e in edges} | {e[1] for e in edges}
    dangling = sorted(referenced - nodes)
    return {"nodes": sorted(nodes), "edges": edges, "dangling_targets": dangling}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    model = json.loads(Path(a.model).read_text(encoding="utf-8"))
    g = build_graph(model)
    Path(a.out).write_text(json.dumps(g, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(g['nodes'])} nodes, {len(g['edges'])} edges, {len(g['dangling_targets'])} dangling")

if __name__ == "__main__":
    main()
