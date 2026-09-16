#!/usr/bin/env python3
"""Validate inline tactic call/jump edges against the v4 registry."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "v4" / "registry" / "graph.json"
SKILLS = ROOT / "v4" / "skills"
BASELINE = ROOT / "v4" / "registry" / "inline-edge-baseline.json"
RULE = "Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds."
PROTECTED = (
    "Input contract",
    "Output contract",
    "Thresholds and quality gates",
    "Preserved source criteria ledger",
    "Provenance map",
)
MUST_RE = re.compile(r"You MUST load skill `([a-z][a-z0-9-]+)`")
CONSIDER_RE = re.compile(r"\bconsider(?: jumping to)? `([a-z][a-z0-9-]+)`", re.I)
MAY_RE = re.compile(r"`([a-z][a-z0-9-]+)` may be the better next tactic", re.I)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section_bytes(data: bytes, heading: str) -> bytes | None:
    match = re.search(
        rb"^## " + re.escape(heading.encode()) + rb"\r?\n.*?(?=^## |\Z)",
        data,
        re.M | re.S,
    )
    return match.group(0) if match else None


def load_graph() -> tuple[dict[str, dict], dict[str, set[str]], dict[str, set[str]]]:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in graph["nodes"]}
    calls = {node_id: set() for node_id, node in nodes.items() if node["type"] == "tactic"}
    jumps = {node_id: set() for node_id, node in nodes.items() if node["type"] == "tactic"}
    for edge in graph["calls"]:
        calls[edge["source"]].add(edge["target"])
    for edge in graph["jumps"]:
        if edge["source"] in jumps:
            jumps[edge["source"]].add(edge["target"])
    return nodes, calls, jumps


def capture_baseline(nodes: dict[str, dict]) -> int:
    if BASELINE.exists():
        print(f"ERROR: baseline already exists: {BASELINE}", file=sys.stderr)
        return 1
    protected: dict[str, dict[str, str]] = {}
    sop_files: dict[str, str] = {}
    errors: list[str] = []
    for node_id, node in nodes.items():
        path = SKILLS / node_id / "SKILL.md"
        data = path.read_bytes()
        if node["type"] == "sop":
            sop_files[node_id] = digest(data)
            continue
        protected[node_id] = {}
        for heading in PROTECTED:
            section = section_bytes(data, heading)
            if section is None:
                errors.append(f"{path}: missing protected section ## {heading}")
            else:
                protected[node_id][heading] = digest(section)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    payload = {
        "schema": "dare-v4-inline-edge-baseline-1",
        "hash": "sha256",
        "protected_sections": protected,
        "sop_files": sop_files,
    }
    BASELINE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"OK: captured {len(protected)} tactic baselines and {len(sop_files)} SOP file baselines")
    return 0


def check_body(
    node_id: str,
    text: str,
    expected_calls: set[str],
    expected_jumps: set[str],
) -> list[str]:
    errors: list[str] = []
    actual_calls = set(MUST_RE.findall(text))
    actual_jumps = set(CONSIDER_RE.findall(text)) | set(MAY_RE.findall(text))
    if actual_calls != expected_calls:
        errors.append(
            f"{node_id}: MUST targets differ: missing={sorted(expected_calls - actual_calls)}, "
            f"extra={sorted(actual_calls - expected_calls)}"
        )
    if actual_jumps != expected_jumps:
        errors.append(
            f"{node_id}: jump targets differ: missing={sorted(expected_jumps - actual_jumps)}, "
            f"extra={sorted(actual_jumps - expected_jumps)}"
        )
    forced_jumps = expected_jumps & actual_calls
    if forced_jumps:
        errors.append(f"{node_id}: jump targets appear in MUST calls: {sorted(forced_jumps)}")
    if text.count(RULE) != 1:
        errors.append(f"{node_id}: inline rule count is {text.count(RULE)}, expected 1")
    return errors


def validate(selected: set[str] | None) -> int:
    nodes, calls, jumps = load_graph()
    if not BASELINE.exists():
        print(f"ERROR: baseline missing; run {Path(__file__).name} --capture-baseline first", file=sys.stderr)
        return 1
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    tactic_ids = set(calls)
    if selected:
        unknown = selected - tactic_ids
        if unknown:
            print(f"ERROR: unknown or non-tactic nodes: {sorted(unknown)}", file=sys.stderr)
            return 1
        tactic_ids &= selected
    errors: list[str] = []
    call_total = jump_total = 0
    for node_id in sorted(tactic_ids):
        path = SKILLS / node_id / "SKILL.md"
        data = path.read_bytes()
        text = data.decode("utf-8")
        errors.extend(f"{path}: {error}" for error in check_body(node_id, text, calls[node_id], jumps[node_id]))
        call_total += len(calls[node_id])
        jump_total += len(jumps[node_id])
        for heading, expected in baseline["protected_sections"][node_id].items():
            section = section_bytes(data, heading)
            if section is None or digest(section) != expected:
                errors.append(f"{path}: protected section changed: ## {heading}")
    if selected is None:
        for node_id, expected in baseline["sop_files"].items():
            path = SKILLS / node_id / "SKILL.md"
            if digest(path.read_bytes()) != expected:
                errors.append(f"{path}: SOP file changed")
        if call_total != 317 or jump_total != 157:
            errors.append(f"registry totals differ: calls={call_total}/317, jumps={jump_total}/157")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        print(f"FAIL: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        f"OK: inline edges validated for {len(tactic_ids)} tactic(s), "
        f"{call_total} calls, {jump_total} jumps"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture-baseline", action="store_true")
    parser.add_argument("--nodes", nargs="+", help="validate only named tactic nodes")
    args = parser.parse_args()
    nodes, _, _ = load_graph()
    if args.capture_baseline:
        if args.nodes:
            parser.error("--nodes cannot be used with --capture-baseline")
        return capture_baseline(nodes)
    return validate(set(args.nodes) if args.nodes else None)


if __name__ == "__main__":
    raise SystemExit(main())
