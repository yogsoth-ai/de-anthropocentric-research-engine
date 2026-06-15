"""Phase-3 helper: generate the three-level `## Available Strategies/Tactics/SOPs/
Campaigns` body tables from each skill's frontmatter dependencies sub-keys. The
"when to use" column is filled from each TARGET skill's on-disk description (the
refactory_source descriptions are mojibake; on-disk SKILL.md is clean). Sections are
clipped by which sub-keys the node actually has, and are rewritten idempotently
(an existing managed block between the markers is replaced, never duplicated).
Does NOT touch frontmatter, so closure is unaffected. --apply [--package PKG]."""
import argparse, re
from pathlib import Path
import lib_refactory as lib

SUBKEY_HEADING = {
    "campaigns": "Available Campaigns",
    "strategies": "Available Strategies",
    "tactics": "Available Tactics",
    "sops": "Available SOPs",
}
COL_LABEL = {"campaigns": "Campaign", "strategies": "Strategy",
             "tactics": "Tactic", "sops": "SOP"}
ORDER = ["strategies", "tactics", "sops", "campaigns"]
BEGIN = "<!-- BEGIN available-tables (generated) -->"
END = "<!-- END available-tables (generated) -->"
NOTE = "可选,无固定顺序;最终叶子终为 sop。"


def one_line(text):
    text = (text or "").replace("\n", " ").replace("|", "/")
    return re.sub(r"\s+", " ", text).strip()


def collect_descriptions(skills_dir):
    """name -> one-line description from each on-disk SKILL.md frontmatter."""
    out = {}
    for sk in Path(skills_dir).iterdir():
        md = sk / "SKILL.md"
        if not md.exists():
            continue
        fm, _ = lib.read_frontmatter(md)
        if fm:
            out[sk.name] = one_line(fm.get("description", ""))
    return out


def render_section(subkey, names, descs):
    label = COL_LABEL[subkey]
    head = f"## {SUBKEY_HEADING[subkey]}\n\n{NOTE}\n\n| {label} | 何时用 |\n| --- | --- |\n"
    rows = "".join(f"| {n} | {descs.get(n, '')} |\n" for n in sorted(names))
    return head + rows


def build_block(name, skills_dir, descs):
    """The full managed block (between markers) for one node, or '' if no deps."""
    fm, _ = lib.read_frontmatter(Path(skills_dir) / name / "SKILL.md")
    deps = (fm or {}).get("dependencies") or {}
    if not isinstance(deps, dict):
        return ""
    sections = [render_section(k, deps[k], descs)
                for k in ORDER if deps.get(k)]
    if not sections:
        return ""
    return BEGIN + "\n\n" + "\n".join(sections) + "\n" + END


def upsert_block(body, block):
    """Replace an existing managed block, else append before trailing whitespace."""
    pat = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
    if pat.search(body):
        return pat.sub(block, body)
    return body.rstrip() + "\n\n" + block + "\n"


def apply(skills_dir, package=None):
    d = lib.load_source()
    nodes = {n["name"]: n for n in d["nodes"]}
    descs = collect_descriptions(skills_dir)
    written = 0
    for sk in sorted(p for p in Path(skills_dir).iterdir() if (p / "SKILL.md").exists()):
        node = nodes.get(sk.name)
        if package and (not node or node.get("package") != package):
            continue
        block = build_block(sk.name, skills_dir, descs)
        if not block:
            continue
        fm, body = lib.read_frontmatter(sk / "SKILL.md")
        new_body = upsert_block(body, block)
        if new_body != body:
            lib.write_frontmatter(sk / "SKILL.md", fm, new_body)
            written += 1
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--package", default=None, help="limit to one package")
    a = ap.parse_args()
    if a.apply:
        print(f"wrote available-tables into {apply(str(lib.SKILL_DIR), a.package)} SKILL.md")
    else:
        print("DRY-RUN (pass --apply to write)")


if __name__ == "__main__":
    main()
