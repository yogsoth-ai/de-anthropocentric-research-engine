#!/usr/bin/env python3
"""Repair cp936-mojibake in v4 pilot bodies.

Corruption: UTF-8 3-byte sequences were decoded as cp936. The first two bytes
formed a CJK char; the third byte either (a) merged with the following ASCII
char -- losslessly recoverable by re-encoding to cp936 -- or (b) became U+FFFD
and was stored as '?' -- LOSSY, the byte is gone.

Because the lossy form collapses distinct symbols onto one CJK char
(>= <= ~= != all -> U+922E), character mapping is unsafe: it would silently
flip a >= threshold into !=. So lossy rows are repaired from the v3 source
using the ledger's own (source-node, source-line) coordinates.

Usage:
    python fix_mojibake.py --check      report only, exit 1 if corruption found
    python fix_mojibake.py --apply      rewrite files in place
"""
import argparse
import pathlib
import re
import sys

BASE = pathlib.Path(__file__).resolve().parents[3]
V4 = BASE / "v4" / "skills"
V3 = BASE / "skills"

# CJK + replacement char never legitimately appear in v4 English bodies.
MOJI = re.compile(r"[一-鿿　-〿＀-￯�]")

# Ledger row: | source-node | line | kind | quoted source text |
LEDGER_ROW = re.compile(r"^\|\s*([a-z0-9-]+)\s*\|\s*(\d+)\s*\|\s*([a-z-]+)\s*\|\s*(.*?)\s*\|\s*$")

# Prose fixes verified byte-for-byte against the corrupted bytes. Each entry is
# (exact corrupted substring, replacement). Kept explicit rather than derived so
# every substitution is reviewable.
PROSE_FIXES = [
    ("鈥渃ompeting鈥?", "“competing” "),
    ("鈥渧alid鈥?", "“valid” "),
    # 'criteria->core->aggregate': third byte consumed the following letter, so
    # re-encoding yields '->score'. Restore the semantically correct chain.
    ("criteria鈫抯core鈫抋ggregate",
     "criteria→core→aggregate"),
]


def ledger_escape(text: str) -> str:
    """Match how the ledger escapes pipes inside a table cell."""
    return text.replace("|", "\\\\|")


def repair_ledger_row(line: str) -> tuple[str, str | None]:
    """Re-fetch a corrupted ledger row's quoted text from the v3 source."""
    m = LEDGER_ROW.match(line)
    if not m:
        return line, "not-a-ledger-row"
    node, lineno, kind, _ = m.groups()
    src = V3 / node / "SKILL.md"
    if not src.is_file():
        return line, f"missing v3 source: {node}"
    lines = src.read_text(encoding="utf-8").splitlines()
    idx = int(lineno) - 1
    if not 0 <= idx < len(lines):
        return line, f"line {lineno} out of range in {node} ({len(lines)} lines)"
    truth = ledger_escape(lines[idx].strip())
    return f"| {node} | {lineno} | {kind} | {truth} |", None


def repair_text(text: str) -> tuple[str, list[str]]:
    problems: list[str] = []
    text = text.replace("﻿", "")
    for corrupt, fixed in PROSE_FIXES:
        text = text.replace(corrupt, fixed)
    out = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if not MOJI.search(line):
            out.append(line)
            continue
        fixed, err = repair_ledger_row(line)
        if err:
            problems.append(f"line {lineno}: {err}")
            out.append(line)
        else:
            out.append(fixed)
    return "\n".join(out) + "\n", problems


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    dirty: list[tuple[str, int]] = []
    failures: list[str] = []

    for node_dir in sorted(V4.iterdir()):
        path = node_dir / "SKILL.md"
        if not path.is_file():
            continue
        original = path.read_text(encoding="utf-8")
        hits = MOJI.findall(original)
        if not hits:
            continue
        dirty.append((node_dir.name, len(hits)))
        fixed, problems = repair_text(original)
        for p in problems:
            failures.append(f"{node_dir.name}: {p}")
        remaining = MOJI.findall(fixed)
        if args.apply:
            path.write_text(fixed, encoding="utf-8", newline="\n")
        status = "clean" if not remaining else f"{len(remaining)} LEFT"
        print(f"{node_dir.name}: {len(hits)} corrupt -> {status}")

    if not dirty:
        print("OK: no mojibake found in v4/skills")
        return 0
    for f in failures:
        print(f"  unresolved: {f}", file=sys.stderr)
    if args.check:
        print(f"\nFAIL: {len(dirty)} file(s) corrupted", file=sys.stderr)
        return 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
