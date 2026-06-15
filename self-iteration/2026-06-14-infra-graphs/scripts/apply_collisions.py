"""Phase-1 (1): rebuild collision + wrapper skill folders in the flat skills/ from
their package source repos, delete the old merged folders + stale flat-merge orphan
wrapper folders, fix wrapper source: pointers to internal bodies, replace the two
external-import web bodies (web-search / web-research) with the REAL bodies from the
source repo (self-containment), and copy timestamp.py into the two context skills as
a bundled script. --apply to write; default is dry-run."""
import argparse, json, shutil
from pathlib import Path
import lib_refactory as lib

# 5 stale flat-merge orphan wrapper folders: NOT graph nodes; 3 carry external source.
# Safe to delete (the real wrappers become <pkg>-<wrapper>, real bodies stay bare).
ORPHANS = ("broad-paper-search", "broad-web-search",
           "paper-overview", "paper-research", "paper-search")

# the two flat folders that are external-import wrappers on disk but MUST become
# real self-contained bodies (kept bare-named, copied from web-browsing source repo).
WEB_BODIES = {"web-search": "web-browsing", "web-research": "web-browsing"}


def build_plan():
    """Compute (copies, deletes, scripts, wrapper_source_fixes, body_fixes) w/o writing."""
    col = json.loads((lib.HERE / "collision-links.json").read_text(encoding="utf-8"))["groups"]
    links = json.loads((lib.HERE / "infra-links.json").read_text(encoding="utf-8"))["collapse"]
    copies, deletes = [], set()
    # collisions: copy each pkg version from source repo -> <pkg>-<old>; delete old merged
    for c in col:
        pkg, old = c["pkg"], c["old"]
        src = lib.SRC_ROOT / pkg / "skills" / old
        copies.append({"src": str(src), "dst": str(lib.SKILL_DIR / f"{pkg}-{old}")})
        deletes.add(str(lib.SKILL_DIR / old))
    # wrappers: copy pkg wrapper folder from source repo -> <pkg>-<wrapper>
    wrapper_source_fixes = []
    for c in links:
        pkg, wr = c["pkg"], c["wrapper"]
        src = lib.SRC_ROOT / pkg / "skills" / wr
        copies.append({"src": str(src), "dst": str(lib.SKILL_DIR / f"{pkg}-{wr}")})
        wrapper_source_fixes.append({"node": f"{pkg}-{wr}",
                                     "source": f"skills/{c['skill']}/SKILL.md"})
    # stale orphan wrapper folders -> delete (flat-merge leftovers, not graph nodes)
    for o in ORPHANS:
        deletes.add(str(lib.SKILL_DIR / o))
    # web-search / web-research: replace external-import wrapper with the REAL body
    body_fixes = [{"name": n, "src": str(lib.SRC_ROOT / pkg / "skills" / n),
                   "dst": str(lib.SKILL_DIR / n)} for n, pkg in WEB_BODIES.items()]
    # timestamp.py -> bundled script in both context skills
    ts_src = lib.SRC_ROOT / "context-management" / "scripts" / "timestamp.py"
    scripts = [{"src": str(ts_src), "dst": str(lib.SKILL_DIR / s / "scripts" / "timestamp.py")}
               for s in ("context-init", "context-checkpoint")]
    return {"copies": copies, "deletes": sorted(deletes),
            "scripts": [s["dst"] for s in scripts], "_scripts": scripts,
            "wrapper_source_fixes": wrapper_source_fixes, "body_fixes": body_fixes}


def apply(plan):
    for c in plan["copies"]:
        dst = Path(c["dst"])
        if dst.exists(): shutil.rmtree(dst)
        shutil.copytree(c["src"], dst)
    # replace external-import web bodies with the real source-repo bodies
    for b in plan["body_fixes"]:
        dst = Path(b["dst"])
        if dst.exists(): shutil.rmtree(dst)
        shutil.copytree(b["src"], dst)
    for s in plan["_scripts"]:
        Path(s["dst"]).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(s["src"], s["dst"])
    # fix wrapper source: pointers (in the freshly-copied wrapper SKILL.md)
    for w in plan["wrapper_source_fixes"]:
        md = lib.SKILL_DIR / w["node"] / "SKILL.md"
        fm, body = lib.read_frontmatter(md)
        if fm is not None:
            fm["execution"] = "import"
            fm["source"] = w["source"]
            lib.write_frontmatter(md, fm, body)
    # delete old merged collision folders + stale orphans (AFTER copies read clean)
    for d in plan["deletes"]:
        p = Path(d)
        if p.exists(): shutil.rmtree(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write to disk (default dry-run)")
    a = ap.parse_args()
    plan = build_plan()
    print(f"copies={len(plan['copies'])} deletes={len(plan['deletes'])} "
          f"scripts={len(plan['scripts'])} body_fixes={len(plan['body_fixes'])} "
          f"wrapper_source_fixes={len(plan['wrapper_source_fixes'])}")
    if a.apply:
        apply(plan); print("APPLIED")
    else:
        print("DRY-RUN (pass --apply to write)")


if __name__ == "__main__":
    main()
