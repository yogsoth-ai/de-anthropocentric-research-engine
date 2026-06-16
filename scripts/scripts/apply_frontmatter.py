"""Phase-1 (2): for every flat skill, delete used-by, and write dependencies sub-keys
(strategies/tactics/sops/campaigns) computed from refactory_source.json out-edges.
Only skill->skill edges are written (ref/<pkg>, timestamp.py excluded - references
layer, not skill nodes). Also fixes external <repo-path>/scripts/ body refs to an
internal relative path. --apply to write."""
import argparse, re
from pathlib import Path
import lib_refactory as lib


def build_dep_index():
    """node -> {subkey: sorted[skill names]} from ALL skill->skill out-edges
    (missing + none = the full correct dependency set)."""
    d = lib.load_source()
    nodes = {n["name"]: n for n in d["nodes"]}
    idx = {}
    for e in d["edges"]:
        f, t = e["from"], e["to"]
        if not lib.is_real_skill_node(f, nodes):
            continue
        if not lib.is_real_skill_node(t, nodes):
            continue
        sub = lib.subkey_for_layer(nodes[t]["layer"])
        idx.setdefault(f, {}).setdefault(sub, set()).add(t)
    return {n: {k: sorted(v) for k, v in subs.items()} for n, subs in idx.items()}


def apply(idx):
    written = 0
    for sk in sorted(p for p in lib.SKILL_DIR.iterdir() if (p / "SKILL.md").exists()):
        md = sk / "SKILL.md"
        fm, body = lib.read_frontmatter(md)
        if fm is None:
            continue
        fm.pop("used-by", None)                 # delete reverse sprawl
        if sk.name in idx:
            fm["dependencies"] = idx[sk.name]   # new sub-keyed forward deps
        body = re.sub(r'<[\w-]*repo-path>/scripts/', 'scripts/', body)  # self-contain
        lib.write_frontmatter(md, fm, body)
        written += 1
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    idx = build_dep_index()
    tot = sum(len(v) for subs in idx.values() for v in subs.values())
    print(f"nodes with deps={len(idx)}; total dep edges={tot}")
    print(f"wrote {apply(idx)} SKILL.md" if a.apply else "DRY-RUN")


if __name__ == "__main__":
    main()
