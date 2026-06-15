"""Generate research-catalog/references/<package>.md — one skill table per
package, sorted by (layer-rank, name). Description text comes from the existing
skill-index.md listing; layer + membership come from the package graph json."""
import json, re, argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CATALOG = HERE.parent.parent / "skills" / "research-catalog"
SKILL_INDEX = CATALOG / "skill-index.md"
REF_DIR = CATALOG / "references"

NINE = ["north-star-crystallization","knowledge-acquisition","deep-insight",
        "hypothesis-formation","creative-ideation","convergence","stress-test",
        "experiment-execution","knowledge-structuring"]
LAYER_RANK = {"campaign":0,"strategy":1,"tactic":2,"sop":3,"references":4}


def parse_descriptions(path=SKILL_INDEX):
    """Parse '| skill | description |' rows from a markdown table file.
    The original source (skill-index.md) was split into the 9 ref files and
    removed; if the path is gone, return  and rely on the json `desc` field."""
    path = Path(path)
    if not path.exists():
        return {}
    desc = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([a-z0-9][a-z0-9-]*\.?[a-z]*)\s*\|\s*(.+?)\s*\|\s*$", line)
        if m and m.group(1) not in ("Skill", "-------"):
            desc[m.group(1)] = m.group(2)
    return desc


def rows_for_package(pkg):
    nodes = json.loads((DATA / f"{pkg}.json").read_text(encoding="utf-8"))["nodes"]
    desc = parse_descriptions()
    rows = [{"layer": n["layer"], "name": n["id"],
             "desc": desc.get(n["id"], n.get("desc", "").replace("|","\\|"))} for n in nodes]
    rows.sort(key=lambda r: (LAYER_RANK.get(r["layer"], 9), r["name"]))
    return rows


def render_table(pkg):
    rows = rows_for_package(pkg)
    out = [f"# {pkg} — skill table", "",
           f"{len(rows)} skills. Sorted by layer (campaign→strategy→tactic→sop), then name.",
           "", "| Layer | Skill | Description |", "| --- | --- | --- |"]
    for r in rows:
        d = (r["desc"] or "").replace("\n", " ").strip()
        out.append(f"| {r['layer']} | {r['name']} | {d} |")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(REF_DIR))
    ap.add_argument("--allow-degraded", action="store_true",
                    help="run even though skill-index.md is gone (descriptions "
                         "fall back to the sparser graph json desc field)")
    a = ap.parse_args()
    if not SKILL_INDEX.exists() and not a.allow_degraded:
        raise SystemExit(
            f"refusing to run: {SKILL_INDEX.name} is gone, so descriptions would "
            "degrade to the json desc field and OVERWRITE the committed ref files. "
            "The 9 ref files were already generated from skill-index.md and committed; "
            "regeneration is a one-time migration step, not idempotent. "
            "Pass --allow-degraded only if you intend the sparser output.")
    od = Path(a.out_dir); od.mkdir(parents=True, exist_ok=True)
    for pkg in NINE:
        (od / f"{pkg}.md").write_text(render_table(pkg), encoding="utf-8")
        print(f"{pkg}.md: {len(rows_for_package(pkg))} rows")


if __name__ == "__main__":
    main()
