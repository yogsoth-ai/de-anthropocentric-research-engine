"""Align each flat-body skill's frontmatter `name:` to its folder-name.
Idempotent, deterministic, touches only the `name:` line. Read source: the DARE
flat-body skills/ dir (passed as --flat-body, no default — privacy red-line).
"""
from __future__ import annotations
import argparse
from pathlib import Path
