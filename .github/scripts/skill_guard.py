#!/usr/bin/env python3
"""Skill Guard — structural and safety checks for the DARE v4 skill library.

Replaces the v3-era AI-plugin scanner. This tree is pure markdown: the real
attack surface is what a skill body instructs an agent to do, and the graph
closure that no other artifact validates since the v4 staging tree was dropped.

Exits 1 on any finding.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"

# 1. Dangerous instruction shapes. A skill body is prose handed to an agent;
#    these turn prose into an execution or exfiltration request.
DANGEROUS: list[tuple[str, str]] = [
    (r"\brm\s+-[rRf]", "destructive delete"),
    (r"\bcurl\b[^\n]*\|\s*(ba)?sh\b", "pipe download into shell"),
    (r"\bwget\b[^\n]*\|\s*(ba)?sh\b", "pipe download into shell"),
    (r"\bsudo\b", "privilege escalation"),
    (r"\beval\s*\(", "dynamic evaluation"),
    (r"\bchmod\s+777\b", "world-writable permission"),
    (r"\bgit\s+(push|reset\s+--hard|clean\s+-f)\b", "destructive or outbound git"),
    (r"\bnpm\s+publish\b", "package publication"),
    (r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|password)\s*[:=]\s*\S",
     "inline credential"),
    (r"(?i)(^|[\s`\"'(/])\.env\b", "environment file access"),
    (r"(?i)\bid_rsa\b|\.ssh/", "private key access"),
]

# 2. Paths that must not ship. The library installs as `skills/`; nothing
#    references a tree above it, a removed directory, or an absolute location.
BAD_PATHS: list[tuple[str, str]] = [
    (r"\bv4/skills/", "stale staging path — use skills/"),
    (r"\bv4/(?:registry|scripts|docs)/", "removed staging subtree"),
    (r"\bv3/", "stale v3 path"),
    (r"\bdsh-plugin/", "removed directory"),
    (r"\bchannel/", "removed directory"),
    (r"\bgraph\.json\b", "not shipped — describe the boundary in prose"),
    (r"\brefactory_source\.json\b", "development residue, not shipped"),
]

# Absolute locations are wrong in prose but legitimate inside fenced examples,
# so these are checked against prose only.
BAD_PATHS_PROSE: list[tuple[str, str]] = [
    (r"[A-Za-z]:[\\/]", "absolute Windows path"),
    (r"(?<![\w.`-])/(?:home|Users|tmp|etc|var|mnt)/", "absolute POSIX path"),
]

CALL_RE = re.compile(r"MUST load skill `([a-z0-9-]+)`")
JUMP_RE = re.compile(r"consider `([a-z0-9-]+)`")
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.M)
DESC_RE = re.compile(r"^description:\s*\S", re.M)

# Fenced code blocks are illustrative payloads (yaml contracts, checkpoint
# templates), not instructions to the agent. Safety patterns apply to prose.
FENCE_RE = re.compile(r"^```.*?^```", re.M | re.S)


def prose_only(text: str) -> str:
    """Blank out fenced blocks, preserving line numbering."""
    return FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def main() -> int:
    if not SKILLS.is_dir():
        print(f"FATAL: {SKILLS} not found")
        return 1

    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    names = {p.name for p in dirs}
    findings: list[str] = []

    for d in dirs:
        skill = d / "SKILL.md"
        rel = skill.relative_to(ROOT).as_posix()
        if not skill.is_file():
            findings.append(f"{d.relative_to(ROOT).as_posix()}: missing SKILL.md")
            continue

        stray = [f.name for f in d.iterdir() if f.name != "SKILL.md"]
        if stray:
            findings.append(f"{rel}: unexpected files in skill dir: {stray}")

        text = skill.read_text(encoding="utf-8")
        prose = prose_only(text)

        # 3. Frontmatter integrity.
        if not text.startswith("---"):
            findings.append(f"{rel}:1: missing frontmatter")
        m = NAME_RE.search(text)
        if not m:
            findings.append(f"{rel}: no name field")
        elif m.group(1).strip("\"'") != d.name:
            findings.append(f"{rel}: name '{m.group(1)}' != dir '{d.name}'")
        if not DESC_RE.search(text):
            findings.append(f"{rel}: no description field")

        for pattern, label in DANGEROUS:
            for hit in re.finditer(pattern, prose):
                line = prose[: hit.start()].count("\n") + 1
                findings.append(f"{rel}:{line}: {label}: {hit.group(0)[:60]!r}")

        for pattern, label in BAD_PATHS:
            for hit in re.finditer(pattern, text):
                line = text[: hit.start()].count("\n") + 1
                findings.append(f"{rel}:{line}: {label}: {hit.group(0)[:60]!r}")

        for pattern, label in BAD_PATHS_PROSE:
            for hit in re.finditer(pattern, prose):
                line = prose[: hit.start()].count("\n") + 1
                findings.append(f"{rel}:{line}: {label}: {hit.group(0)[:60]!r}")

        # 4. Edge closure — every referenced target must exist.
        for regex, kind in ((CALL_RE, "call"), (JUMP_RE, "jump")):
            for target in set(regex.findall(text)):
                if target not in names:
                    findings.append(f"{rel}: dangling {kind} edge -> `{target}`")

    print(f"scanned {len(dirs)} skills")
    if findings:
        print(f"\n{len(findings)} finding(s):\n")
        for f in findings:
            print(f"  {f}")
        return 1
    print("clean: frontmatter valid, edges closed, no unsafe instruction or stale path")
    return 0


if __name__ == "__main__":
    sys.exit(main())
