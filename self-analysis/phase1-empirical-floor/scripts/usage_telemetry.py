"""N6: aggregate skill-firing telemetry from CC .jsonl logs. De-identified output."""
import argparse, json, sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import networkx as nx

DISCLAIMER = ("Firing counts are a snapshot of the observed ecosystem. "
              "Low/zero frequency != redundant. This is NOT a pruning verdict.")

def _iter_skill_events(logs_dir: Path, scope_substr: str):
    for fp in sorted(Path(logs_dir).glob("*.jsonl")):
        for line in fp.open(encoding="utf-8"):
            line = line.strip()
            if not line: continue
            try: o = json.loads(line)
            except json.JSONDecodeError: continue
            if o.get("type") != "assistant": continue
            if scope_substr and scope_substr not in (o.get("cwd") or ""): continue
            sid = o.get("sessionId")
            msg = o.get("message", {})
            content = msg.get("content") if isinstance(msg, dict) else None
            if not isinstance(content, list): continue
            for b in content:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                    skill = (b.get("input") or {}).get("skill")
                    if skill: yield sid, skill

def collect_telemetry(logs_dir, graph, scope_substr="YOGSOTH-AI"):
    invocations = Counter()
    sessions_of = defaultdict(set)        # skill -> set(sessionId)  (in-memory only)
    per_session = defaultdict(set)        # sessionId -> set(skill)
    for sid, skill in _iter_skill_events(logs_dir, scope_substr):
        invocations[skill] += 1
        sessions_of[skill].add(sid)
        per_session[sid].add(skill)
    firing = {sk: {"invocations": invocations[sk], "sessions": len(sessions_of[sk])}
              for sk in invocations}
    co = Counter()
    for skills in per_session.values():
        for x, y in combinations(sorted(skills), 2):
            co[(x, y)] += 1
    cooccurrence = [[x, y, n] for (x, y), n in sorted(co.items())]
    G = nx.DiGraph(); G.add_nodes_from(graph["nodes"])
    for a, b, _ in graph["edges"]: G.add_edge(a, b)
    deg = nx.degree_centrality(G)
    btw = nx.betweenness_centrality(G) if G.number_of_nodes() > 2 else {n: 0.0 for n in G}
    centrality = {n: {"degree": round(deg.get(n, 0.0), 6),
                      "betweenness": round(btw.get(n, 0.0), 6)} for n in G.nodes()}
    return {"_disclaimer": DISCLAIMER, "firing_counts": firing,
            "cooccurrence": cooccurrence, "centrality": centrality}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True)
    ap.add_argument("--graph", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--scope-substr", default="YOGSOTH-AI")
    a = ap.parse_args()
    if not Path(a.logs_dir).is_dir():
        print(f"ERROR: --logs-dir not a directory", file=sys.stderr); sys.exit(2)
    graph = json.loads(Path(a.graph).read_text(encoding="utf-8"))
    t = collect_telemetry(a.logs_dir, graph, a.scope_substr)
    Path(a.out).write_text(json.dumps(t, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(t['firing_counts'])} skills fired; {len(t['cooccurrence'])} co-occ pairs")

if __name__ == "__main__":
    main()
