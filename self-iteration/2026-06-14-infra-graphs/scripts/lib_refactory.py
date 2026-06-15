"""Shared helpers for the skills/ dependency refactory. Single source of truth
for: reading refactory_source.json, the 101-entry rename map (collision+wrapper),
edge-target-layer -> dependencies sub-key mapping, wrapper->internal-body source
pointers, and the new-format frontmatter read/write."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../scripts
INFRA = HERE.parent                              # .../2026-06-14-infra-graphs
SKILL_DIR = INFRA.parent.parent / "skills"       # .../de-anthropocentric-research-engine/skills
SRC_ROOT = Path("D:/YOGSOTH-AI")                 # 13 package source repos


def load_source():
    return json.loads((INFRA / "refactory_source.json").read_text(encoding="utf-8"))


def rename_map():
    """(package, old_bare) -> new_bare. 64 collision + 37 wrapper = 101."""
    out = {}
    col = json.loads((HERE / "collision-links.json").read_text(encoding="utf-8"))["groups"]
    for c in col:
        out[(c["pkg"], c["old"])] = f'{c["pkg"]}-{c["old"]}'
    links = json.loads((HERE / "infra-links.json").read_text(encoding="utf-8"))["collapse"]
    for c in links:
        out[(c["pkg"], c["wrapper"])] = f'{c["pkg"]}-{c["wrapper"]}'
    return out


def subkey_for_layer(layer):
    return {"campaign": "campaigns", "strategy": "strategies",
            "tactic": "tactics", "sop": "sops"}[layer]


def wrapper_source_map():
    """new wrapper node name -> internal body source path (self-contained)."""
    links = json.loads((HERE / "infra-links.json").read_text(encoding="utf-8"))["collapse"]
    return {f'{c["pkg"]}-{c["wrapper"]}': f'skills/{c["skill"]}/SKILL.md' for c in links}


def is_real_skill_node(name, nodes):
    """True iff this endpoint is a real skill folder (not a references-layer node:
    ref/<pkg> or timestamp.py). Used to filter the closure target to skill->skill."""
    n = nodes.get(name)
    return bool(n) and n["layer"] != "references"


def read_frontmatter(skill_md_path):
    """Return (frontmatter_dict_or_None, body_str). Tolerates UTF-8 BOM."""
    import yaml
    text = Path(skill_md_path).read_text(encoding="utf-8")
    if text and text[0] == "﻿":
        text = text[1:]
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None, text
    return (fm if isinstance(fm, dict) else None), parts[2]


def write_frontmatter(skill_md_path, fm, body):
    """Re-serialize frontmatter (block style, unicode preserved) + body."""
    import yaml
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
    Path(skill_md_path).write_text(f"---\n{y}---{body}", encoding="utf-8")
