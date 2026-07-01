#!/usr/bin/env python3
"""Assemble a loss payload -> call codex (isolated codex_fn) -> validate against
the co-located schema -> land loss/*.json. loss1 per-run, loss2 per-topic.
The codex edge is the ONLY non-local part; it is isolated behind codex_fn and
NEVER fake-stubbed to green (feedback-no-e2e-shell). Local tests inject a fake
codex_fn at the network boundary only, to verify plumbing.

No jsonschema dependency: a minimal required-keys + top-level-type validator is
the lazier correct choice (ladder-foundry is dep-free through STAGE 3); full
JSON-Schema validation is a STAGE-5 optional."""
import argparse
import json
import os
import random
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
TAU_MIN = 0.7
ENDPOINT_K = 5
ENDPOINT_ALLOWANCE = 1
RIGOR_FLOOR_EPS = 1

RANK_SCHEMA = {"type": "object", "required": ["pairwise"]}      # codex-facing, tmp only
# endpoint call is a 2-way compare labelled A/B (NOT positions); winner ∈ {"A","B"}.
ENDPOINT_SCHEMA = {"type": "object", "required": ["winner"],
                   "properties": {"winner": {"enum": ["A", "B"]}}}  # codex-facing, tmp only


class CodexOutputError(Exception):
    """Raised when codex output is missing required keys or has a wrong type."""


_JSON_TYPE = {"boolean": bool, "number": (int, float), "integer": int,
              "string": str, "object": dict, "array": list}


def validate(obj, schema):
    """Minimal validator: top-level type + required keys + one-level property
    types. NOT full JSON-Schema; enough to catch a malformed codex return."""
    if schema.get("type") == "object" and not isinstance(obj, dict):
        raise CodexOutputError(f"expected object, got {type(obj).__name__}")
    for k in schema.get("required", []):
        if k not in obj:
            raise CodexOutputError(f"missing required key {k!r}")
    for k, spec in schema.get("properties", {}).items():
        if k in obj and "type" in spec:
            t = spec["type"]
            py = _JSON_TYPE.get(t)
            if py and not isinstance(obj[k], py):
                raise CodexOutputError(f"key {k!r} expected {t}, got {type(obj[k]).__name__}")
            if t == "number" and isinstance(obj[k], bool):
                raise CodexOutputError(f"key {k!r} expected number, got bool")
    return obj


def shuffle_perm(n, seed):
    """Return a permutation list: position p -> original index perm[p]."""
    perm = list(range(n))
    random.Random(seed).shuffle(perm)
    return perm


def unshuffle(induced_positions, perm):
    """Map induced positions back to original indices via perm."""
    return [perm[p] for p in induced_positions]


def copeland_order(pairs, n):
    """Copeland aggregate: order positions by win count, descending."""
    wins = {i: 0 for i in range(n)}
    for pr in pairs:
        wins[pr["winner"]] += 1
    return sorted(range(n), key=lambda i: (-wins[i], i))


def kendall_tau(intended, induced):
    """Kendall tau between two orderings given as lists of the same items."""
    rank = {v: i for i, v in enumerate(induced)}
    seq = [rank[v] for v in intended]
    n = len(seq)
    c = d = 0
    for i in range(n):
        for j in range(i + 1, n):
            if seq[i] < seq[j]:
                c += 1
            elif seq[i] > seq[j]:
                d += 1
    return (c - d) / (c + d) if (c + d) else 0.0


def count_endpoint_wins(judgments, high_pos):
    return sum(1 for j in judgments if j["winner"] == high_pos)


def endpoint_pass(w0):
    return w0 >= ENDPOINT_K - ENDPOINT_ALLOWANCE


def rigor_floor(w0):
    half = ENDPOINT_K / 2
    return (not endpoint_pass(w0)) and (half - RIGOR_FLOOR_EPS <= w0 <= half + RIGOR_FLOOR_EPS)


def _default_codex_call(payload, schema_path):
    """REAL codex edge. Never runs in local tests. STAGE-5-verified."""
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     encoding="utf-8") as tf:
        out_path = tf.name
    subprocess.run(
        ["codex", "exec", "--output-schema", schema_path, "-o", out_path, payload],
        cwd="/workspace/work/loss",
        env={**os.environ, "CODEX_HOME": "/workspace/home/loss/.codex"},
        check=True)
    return Path(out_path).read_text(encoding="utf-8")


def _parse_or_degrade(raw, out, schema):
    """Parse + validate; on failure write a loud degraded artifact + exit 2."""
    try:
        obj = json.loads(raw)
        validate(obj, schema)
        return obj
    except (json.JSONDecodeError, CodexOutputError) as e:
        Path(out).write_text(json.dumps(
            {"pass": False, "parse_error": str(e), "raw": raw[:2000]},
            ensure_ascii=False, indent=2), encoding="utf-8")
        sys.exit(2)


def run_loss1(transcript, config, skill_md, out, codex_fn=_default_codex_call):
    schema = json.loads((HERE / "loss1.schema.json").read_text(encoding="utf-8"))
    payload = "\n\n".join([
        Path(skill_md).read_text(encoding="utf-8"),
        "## PolicyCard\n" + Path(config).read_text(encoding="utf-8"),
        "## Transcript\n" + Path(transcript).read_text(encoding="utf-8")])
    raw = codex_fn(payload, str(HERE / "loss1.schema.json"))
    obj = _parse_or_degrade(raw, out, schema)
    Path(out).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def run_loss2(triples, intended_order, skill_md, out, seed, codex_fn=_default_codex_call):
    schema = json.loads((HERE / "loss2.schema.json").read_text(encoding="utf-8"))
    intended = [s.strip() for s in intended_order.split(",")]      # id0..id5 high->low
    n = len(triples)
    perm = shuffle_perm(n, seed)
    perm_path = Path(out).parent / (Path(out).stem + ".perm.json")
    perm_path.write_text(json.dumps(
        {str(p): Path(triples[perm[p]]).stem for p in range(n)}, indent=2),
        encoding="utf-8")
    blocks = [Path(triples[perm[p]]).read_text(encoding="utf-8") for p in range(n)]
    skill = Path(skill_md).read_text(encoding="utf-8")
    # one rank call (15 pairwise winners over positions) + K endpoint calls
    rank_payload = skill + "\n\n## Samples (shuffled)\n" + json.dumps(
        {str(p): blocks[p] for p in range(n)})
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     encoding="utf-8") as tf:
        json.dump(RANK_SCHEMA, tf)
        rank_schema_path = tf.name
    rank_raw = codex_fn(rank_payload, rank_schema_path)
    rank = _parse_or_degrade(rank_raw, out, RANK_SCHEMA)
    pairs_pos = rank["pairwise"]                  # [{i,j,winner} in positions]
    order_pos = copeland_order(pairs_pos, n)      # induced positions, best first
    order_ids_idx = unshuffle(order_pos, perm)    # original indices, best first
    # intended order as original indices (triples[k] is id k)
    intended_idx = [int(s.replace("id", "")) for s in intended]
    tau = kendall_tau(intended_idx, order_ids_idx)
    # endpoints: true-high = intended_idx[0], true-low = intended_idx[-1]
    hi_idx, lo_idx = intended_idx[0], intended_idx[-1]
    hi_pos = perm.index(hi_idx)
    ep_payload = skill + "\n\n## Compare two\n" + json.dumps(
        {"A": blocks[hi_pos], "B": blocks[perm.index(lo_idx)]})
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     encoding="utf-8") as tf:
        json.dump(ENDPOINT_SCHEMA, tf)
        ep_schema_path = tf.name
    judgments = []
    for _ in range(ENDPOINT_K):
        ep_raw = codex_fn(ep_payload, ep_schema_path)
        judgments.append(_parse_or_degrade(ep_raw, out, ENDPOINT_SCHEMA))
    # endpoint judgments report winner as "A"/"B"; map to position
    jmapped = [{"winner": hi_pos if j["winner"] == "A" else perm.index(lo_idx)}
               for j in judgments]
    w0 = count_endpoint_wins(jmapped, hi_pos)
    no_inversion = order_ids_idx[0] == hi_idx and order_ids_idx[-1] == lo_idx
    artifact = {
        "tau": tau,
        "monotonicity_pass": (tau >= TAU_MIN) and no_inversion,
        "endpoint_separation_pass": endpoint_pass(w0),
        "rigor_floor_flag": rigor_floor(w0),
        "pairwise_log": [{"i": unshuffle([p["i"]], perm)[0],
                          "j": unshuffle([p["j"]], perm)[0],
                          "winner": unshuffle([p["winner"]], perm)[0],
                          "reason": p.get("reason", "")} for p in pairs_pos],
    }
    validate(artifact, schema)
    Path(out).write_text(json.dumps(artifact, ensure_ascii=False, indent=2),
                         encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    p1 = sub.add_parser("loss1")
    p1.add_argument("--transcript", required=True)
    p1.add_argument("--config", required=True)
    p1.add_argument("--skill-md", required=True)
    p1.add_argument("--out", required=True)
    p1.add_argument("--_test-bad-json", action="store_true")   # test-only: junk edge
    p2 = sub.add_parser("loss2")
    p2.add_argument("--triples", nargs="+", required=True)
    p2.add_argument("--intended-order", required=True)
    p2.add_argument("--skill-md", required=True)
    p2.add_argument("--out", required=True)
    p2.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    if a.mode == "loss1":
        fn = (lambda p, s: "not json {{{") if a._test_bad_json else _default_codex_call
        run_loss1(a.transcript, a.config, a.skill_md, a.out, codex_fn=fn)
    elif a.mode == "loss2":
        run_loss2(a.triples, a.intended_order, a.skill_md, a.out, a.seed)


if __name__ == "__main__":
    main()

