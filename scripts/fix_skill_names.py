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
