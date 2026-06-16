"""Refresh the Description column of research-catalog/references/<pkg>.md from
each skill's CURRENT on-disk SKILL.md frontmatter description. The ref tables
were first generated when descriptions were still Chinese; after the i18n pass
the on-disk descriptions are English and are the single source of truth. Layer,
Skill, ordering, and the header are preserved; only the third column changes.
Idempotent. Skills absent on disk keep their existing cell."""
import re
from pathlib import Path
import lib_refactory as lib

REF_DIR = Path(lib.SKILL_DIR).parent / "skills" / "research-catalog" / "references"
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([a-z0-9][a-z0-9.\-]*)\s*\|\s*(.*?)\s*\|\s*$")


def one_line(text):
    text = (text or "").replace("\n", " ").replace("|", "/")
    return re.sub(r"\s+", " ", text).strip()


def load_descs():
    out = {}
    for md in Path(lib.SKILL_DIR).glob("*/SKILL.md"):
        fm, _ = lib.read_frontmatter(md)
        if fm:
            out[md.parent.name] = one_line(fm.get("description", ""))
    return out


def refresh(descs):
    changed = 0
    for f in sorted(REF_DIR.glob("*.md")):
        lines = f.read_text(encoding="utf-8").splitlines()
        out = []
        for ln in lines:
            m = ROW.match(ln)
            if m and m.group(1) not in ("Layer",) and m.group(2) != "---":
                layer, name, old = m.group(1), m.group(2), m.group(3)
                new = descs.get(name, old)
                out.append(f"| {layer} | {name} | {new} |")
            else:
                out.append(ln)
        new_txt = "\n".join(out) + "\n"
        if new_txt != f.read_text(encoding="utf-8"):
            f.write_text(new_txt, encoding="utf-8")
            changed += 1
            print(f"refreshed {f.name}")
    return changed


if __name__ == "__main__":
    n = refresh(load_descs())
    print(f"refreshed {n} ref files")
