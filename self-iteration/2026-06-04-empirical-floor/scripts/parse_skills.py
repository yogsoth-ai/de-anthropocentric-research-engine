"""Parse all SKILL.md frontmatter into one intermediate model. Shared by N1 + 1a."""
import argparse, json, sys
from pathlib import Path
import yaml

LIST_FIELDS = ("used_by", "tactics", "sops", "dependencies")

def _norm_list(v):
    if v is None: return []
    if isinstance(v, list): return [str(x) for x in v]
    # Real body: ~145 files write a list field as a comma-joined scalar
    # (e.g. `used-by: a, b, c`). No skill name contains a comma, so splitting
    # the scalar form is safe. List items are already discrete and never split.
    return [p.strip() for p in str(v).split(",") if p.strip()]

def parse_skill_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    name = path.parent.name
    # 24 files in the real body open with a UTF-8 BOM before the '---' fence.
    if text and text[0] == "﻿":
        text = text[1:]
    if not text.startswith("---"):
        return {"name": name, "parse_error": "no-frontmatter"}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {"name": name, "parse_error": "no-frontmatter"}
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {"name": name, "parse_error": "yaml-error"}
    if not isinstance(fm, dict):
        return {"name": name, "parse_error": "yaml-error"}
    # 65 files write `dependencies` as a mapping {skills: [...], mcp: {...}}.
    # Only skills: entries are skill-graph edges; mcp: names external servers.
    raw_deps = fm.get("dependencies")
    if isinstance(raw_deps, dict):
        dep_value = raw_deps.get("skills")
    else:
        dep_value = raw_deps
    rec = {
        "name": fm.get("name", name),
        "execution": fm.get("execution"),
        "type": fm.get("type"),
        "category": fm.get("category"),
        "campaign": fm.get("campaign"),
        "used_by": _norm_list(fm.get("used-by")),
        "dependencies": _norm_list(dep_value),
        "tactics": _norm_list(fm.get("tactics")),
        "sops": _norm_list(fm.get("sops")),
        "parse_error": None,
    }
    return rec

def parse_skills_dir(skills_dir: Path) -> dict:
    skills, errors = [], []
    for sk in sorted(p for p in skills_dir.iterdir() if (p / "SKILL.md").exists()):
        rec = parse_skill_file(sk / "SKILL.md")
        skills.append(rec)
        if rec.get("parse_error"):
            errors.append(rec["name"])
    return {"skills": skills, "parse_errors": errors}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-dir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    model = parse_skills_dir(Path(a.skills_dir))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(model, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"parsed {len(model['skills'])} skills, {len(model['parse_errors'])} errors", file=sys.stderr)

if __name__ == "__main__":
    main()
