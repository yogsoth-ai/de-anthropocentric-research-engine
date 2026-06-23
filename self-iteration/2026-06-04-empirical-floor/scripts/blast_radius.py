"""N1: per-skill blast radius = set of transitive forward-callers."""
import argparse, json
from pathlib import Path
import networkx as nx

def compute_blast_radius(graph: dict) -> dict:
    G = nx.DiGraph()
    G.add_nodes_from(graph["nodes"])
    for a, b, _src in graph["edges"]:
        G.add_edge(a, b)
    out = {}
    for n in G.nodes():
        # ancestors() = all nodes with a directed path TO n = transitive callers
        callers = nx.ancestors(G, n)
        out[n] = {"impact_size": len(callers), "impacted": sorted(callers)}
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    graph = json.loads(Path(a.graph).read_text(encoding="utf-8"))
    br = compute_blast_radius(graph)
    Path(a.out).write_text(json.dumps(br, indent=2, ensure_ascii=False), encoding="utf-8")
    top = sorted(br.items(), key=lambda kv: kv[1]["impact_size"], reverse=True)[:5]
    print("top blast radius:", [(k, v["impact_size"]) for k, v in top])

if __name__ == "__main__":
    main()
