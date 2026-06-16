"""Align each flat-body skill's frontmatter `name:` to its folder-name.
Idempotent, deterministic, touches only the `name:` line. Read source: the DARE
flat-body skills/ dir (passed as --flat-body, no default — privacy red-line).
"""
from __future__ import annotations
import argparse
from pathlib import Path


def name_field(text: str) -> str | None:
    """The de-quoted `name:` value inside the first --- frontmatter block, else None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    fm = text[:end] if end != -1 else text
    for ln in fm.splitlines():
        s = ln.strip()
        if s.startswith("name:"):
            return s.split(":", 1)[1].strip().strip('"').strip("'")
    return None


def needs_fix(folder_name: str, text: str) -> bool:
    """True when a frontmatter name exists and differs from the folder name."""
    nm = name_field(text)
    return nm is not None and nm != folder_name


def fix_name_line(text: str, folder_name: str) -> str:
    """Rewrite the frontmatter name: line to name: <folder_name>, else unchanged."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    fm_len = end if end != -1 else len(text)
    out_lines: list[str] = []
    replaced = False
    offset = 0  # running byte offset of the current line within text
    for ln in text.splitlines(keepends=True):
        within_frontmatter = offset < fm_len
        if not replaced and within_frontmatter and ln.lstrip().startswith("name:"):
            indent = ln[:len(ln) - len(ln.lstrip())]
            newline = "\n" if ln.endswith("\n") else ""
            out_lines.append(f"{indent}name: {folder_name}{newline}")
            replaced = True
        else:
            out_lines.append(ln)
        offset += len(ln)
    return "".join(out_lines)


def scan(flat_body: Path) -> list[tuple[str, str]]:
    """[(folder, current_name)] for every skill whose name != folder-name."""
    out: list[tuple[str, str]] = []
    for d in sorted(Path(flat_body).iterdir()):
        sk = d / "SKILL.md"
        if not (d.is_dir() and sk.exists()):
            continue
        text = sk.read_text(encoding="utf-8")
        if needs_fix(d.name, text):
            out.append((d.name, name_field(text)))
    return out


def apply_fixes(flat_body: Path) -> list[str]:
    """Rewrite SKILL.md in place for each mismatched skill; return changed folders."""
    changed: list[str] = []
    for folder, _old in scan(flat_body):
        sk = Path(flat_body) / folder / "SKILL.md"
        text = sk.read_text(encoding="utf-8")
        sk.write_text(fix_name_line(text, folder), encoding="utf-8")
        changed.append(folder)
    return changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Align frontmatter name to folder-name")
    ap.add_argument("--flat-body", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    flat = Path(a.flat_body)
    if a.dry_run:
        rows = scan(flat)
        for folder, old in rows:
            print(f"{folder}  <-  name: {old}")
        print(f"{len(rows)} would change")
        return 0
    changed = apply_fixes(flat)
    print(f"{len(changed)} name fields aligned to folder-name")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
