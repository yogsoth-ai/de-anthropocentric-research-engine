"""Derive the 29 cross-package name-collision groups from data/*.json.
A collision = a bare skill id that appears in >1 package, EXCLUDING the 5
import wrappers (already renamed last round) and the 4 REF nodes (graph-internal
ref structure, handled separately). Output drives the stage-1 rename."""
import json, glob
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
WRAP = {"web-search", "web-research", "paper-overview", "paper-search", "paper-research"}

def main():
    pkg_of = defaultdict(list)
    for f in sorted(glob.glob(str(HERE / "data" / "*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for n in d["nodes"]:
            pkg_of[n["id"]].append(d["name"])
    dups = {k: sorted(v) for k, v in pkg_of.items() if len(v) > 1 and k not in WRAP}
    groups = [{"pkg": pkg, "old": name} for name in sorted(dups) for pkg in dups[name]]
    out = {"note": "29 cross-package collision groups; <pkg>/<old> -> <pkg>/<pkg>-<old>",
           "groups": groups}
    (HERE / "collision-links.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"collision groups: {len(dups)} names, {len(groups)} nodes")

if __name__ == "__main__":
    main()
