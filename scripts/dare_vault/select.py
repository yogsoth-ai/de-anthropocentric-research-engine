import json, re
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "refactory_source.json"

INFRA_PKGS = {"context-management","literature-engine","web-browsing",
    "subagent-spawning","research-catalog","engine-core","ara-from-context"}

UTIL_RE = re.compile(r"(paper|web-search|web-research|deep-web|-web-|-web$|"
    r"context-init|context-checkpoint|context-review|context-exploring|"
    r"cold-start|hot-start|warm-start|checkpoint-and-recover|explore-resume|"
    r"spawn-agent|subagent|implementer-dispatch|-specs$|^executing-specs|"
    r"^writing-specs|plan-writing|plan-formatting|implementation-planning|"
    r"research-catalog)")

def load():
    d = json.loads(SRC.read_text(encoding="utf-8"))
    return {n["name"]: n for n in d["nodes"]}, d["edges"]

def kept_names(nodes):
    out = set()
    for name, n in nodes.items():
        if n.get("layer") in ("references", "entry"): continue
        if n.get("package") in INFRA_PKGS: continue
        if UTIL_RE.search(name): continue
        out.add(name)
    return out

def kept_edges(edges, kept):
    return [e for e in edges if e["from"] in kept and e["to"] in kept]
