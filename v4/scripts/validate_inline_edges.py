#!/usr/bin/env python3
"""Validate inline call/jump edges against the v4 registry."""

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
    jumps = {node_id: set() for node_id in nodes}
    for edge in graph["calls"]:
        calls[edge["source"]].add(edge["target"])
    for edge in graph["jumps"]:
        jumps[edge["source"]].add(edge["target"])
    return nodes, calls, jumps


def capture_baseline(nodes: dict[str, dict]) -> int:
    if BASELINE.exists():
        print(f"ERROR: baseline already exists: {BASELINE}", file=sys.stderr)
        return 1
    protected: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    for node_id, node in nodes.items():
        path = SKILLS / node_id / "SKILL.md"
        data = path.read_bytes()
        protected[node_id] = {}
        for heading in PROTECTED:
            section = section_bytes(data, heading)
            protected[node_id][heading] = digest(section) if section is not None else None
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    payload = {
        "schema": "dare-v4-inline-edge-baseline-2",
        "hash": "sha256",
        "protected_sections": protected,
    }
    BASELINE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"OK: captured protected-section baselines for {len(protected)} nodes")
    return 0


def migrate_baseline(nodes: dict[str, dict]) -> int:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if baseline.get("schema") != "dare-v4-inline-edge-baseline-1":
        print("ERROR: migration requires the existing schema-1 baseline", file=sys.stderr)
        return 1
    errors: list[str] = []
    protected = baseline["protected_sections"]
    for node_id, expected_file in baseline["sop_files"].items():
        path = SKILLS / node_id / "SKILL.md"
        data = path.read_bytes()
        if digest(data) != expected_file:
            errors.append(f"{path}: SOP changed before baseline migration")
            continue
        protected[node_id] = {}
        for heading in PROTECTED:
            section = section_bytes(data, heading)
            protected[node_id][heading] = digest(section) if section is not None else None
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    payload = {
        "schema": "dare-v4-inline-edge-baseline-2",
        "hash": "sha256",
        "protected_sections": protected,
    }
    BASELINE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"OK: migrated protected-section baselines for {len(protected)} nodes")
    return 0


def check_body(
    node_id: str,
    text: str,
    expected_calls: set[str],
    expected_jumps: set[str],
    require_rule: bool,
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
    if require_rule and text.count(RULE) != 1:
        errors.append(f"{node_id}: inline rule count is {text.count(RULE)}, expected 1")
    return errors


def validate(selected: set[str] | None) -> int:
    nodes, calls, jumps = load_graph()
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    if not BASELINE.exists():
        print(f"ERROR: baseline missing; run {Path(__file__).name} --capture-baseline first", file=sys.stderr)
        return 1
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    node_ids = set(nodes)
    if selected:
        unknown = selected - node_ids
        if unknown:
            print(f"ERROR: unknown nodes: {sorted(unknown)}", file=sys.stderr)
            return 1
        node_ids &= selected
    errors: list[str] = []
    call_total = tactic_jump_total = sop_jump_total = 0
    for node_id in sorted(node_ids):
        path = SKILLS / node_id / "SKILL.md"
        data = path.read_bytes()
        text = data.decode("utf-8")
        is_tactic = nodes[node_id]["type"] == "tactic"
        expected_calls = calls[node_id] if is_tactic else set()
        errors.extend(
            f"{path}: {error}"
            for error in check_body(node_id, text, expected_calls, jumps[node_id], is_tactic)
        )
        call_total += len(expected_calls)
        if is_tactic:
            tactic_jump_total += len(jumps[node_id])
        else:
            sop_jump_total += len(jumps[node_id])
        for heading, expected in baseline["protected_sections"][node_id].items():
            section = section_bytes(data, heading)
            actual = digest(section) if section is not None else None
            if actual != expected:
                errors.append(f"{path}: protected section changed: ## {heading}")
    if selected is None:
        if len(graph["calls"]) != 317 or len(graph["jumps"]) != 157:
            errors.append(
                f"full registry totals differ: calls={len(graph['calls'])}/317, "
                f"jumps={len(graph['jumps'])}/157"
            )
        if call_total != 317 or tactic_jump_total != 82 or sop_jump_total != 75:
            errors.append(
                f"inline totals differ: calls={call_total}/317, tactic jumps={tactic_jump_total}/82, "
                f"SOP jumps={sop_jump_total}/75"
            )
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        print(f"FAIL: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        f"OK: inline edges validated for {len(node_ids)} node(s): "
        f"{call_total} calls, {tactic_jump_total} tactic jumps, {sop_jump_total} SOP jumps, "
        f"{call_total + tactic_jump_total + sop_jump_total} total"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture-baseline", action="store_true")
    parser.add_argument("--migrate-sop-baseline", action="store_true")
    parser.add_argument("--nodes", nargs="+", help="validate only named nodes")
    args = parser.parse_args()
    nodes, _, _ = load_graph()
    if args.capture_baseline:
        if args.nodes:
            parser.error("--nodes cannot be used with --capture-baseline")
        return capture_baseline(nodes)
    if args.migrate_sop_baseline:
        if args.nodes:
            parser.error("--nodes cannot be used with --migrate-sop-baseline")
        return migrate_baseline(nodes)
    return validate(set(args.nodes) if args.nodes else None)


if __name__ == "__main__":
    raise SystemExit(main())
