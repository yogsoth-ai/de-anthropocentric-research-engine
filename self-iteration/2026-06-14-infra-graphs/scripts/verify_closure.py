"""Closure gate: scan the flat skills/ with a NEW-format parser (reads
dependencies.{strategies/tactics/sops/campaigns} sub-keys), reconstruct skill->skill
edges, and compare against the skill->skill target derived from refactory_source.json.
Missing edges -> non-zero exit. The target is COMPUTED (skill nodes only), never
hard-coded. Does NOT touch the old empirical scanner."""
import argparse, sys
from pathlib import Path
import lib_refactory as lib

SUBKEYS = ("strategies", "tactics", "sops", "campaigns")


def target_edges():
    """{(from, to)} of all skill->skill edges in refactory_source (missing+none)."""
    d = lib.load_source()
    nodes = {n["name"]: n for n in d["nodes"]}
    return {(e["from"], e["to"]) for e in d["edges"]
            if lib.is_real_skill_node(e["from"], nodes)
            and lib.is_real_skill_node(e["to"], nodes)}


def scan_dir(skills_dir):
    """{(from, to)} reconstructed from new-format dependencies sub-keys on disk."""
    edges = set()
    for sk in sorted(p for p in Path(skills_dir).iterdir() if (p / "SKILL.md").exists()):
        fm, _ = lib.read_frontmatter(sk / "SKILL.md")
        if not fm:
            continue
        deps = fm.get("dependencies") or {}
        if not isinstance(deps, dict):
            continue
        for k in SUBKEYS:
            for t in (deps.get(k) or []):
                edges.add((sk.name, t))
    return edges


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skills-dir", default=str(lib.SKILL_DIR))
    a = ap.parse_args()
    target = target_edges()
    found = scan_dir(a.skills_dir)
    missing = target - found
    print(f"target(skill->skill)={len(target)} found={len(found & target)} "
          f"missing={len(missing)}")
    if missing:
        for f, t in sorted(missing)[:30]:
            print(f"  MISSING {f} -> {t}", file=sys.stderr)
        print(f"... {len(missing)} total missing", file=sys.stderr)
        sys.exit(1)
    print("CLOSURE OK")


if __name__ == "__main__":
    main()
