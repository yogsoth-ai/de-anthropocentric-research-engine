# ladder-foundry STAGE 3 — Run-Scripts Implementation Plan (L8–L14 + wrap)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Every script is built TDD: write the failing subprocess test → run red → transcribe the implementation → run green → commit.

**Goal:** Build the 7 deterministic, pure-function leaf scripts (blueprint L8–L14) that turn the STAGE 1/2 weights+persona core into the run skeleton + data-sink layer, each a standalone CLI with a subprocess pytest.

**Architecture:** Each script is a `scripts/<name>.py` argparse CLI; none import each other; all are locally pytest-verifiable with synthetic `tmp_path` inputs — NO remote CC, NO codex, NO key, NO token. Two scripts cross a package boundary: `apply_weight_update` imports `generator.weights`; `save_transcript` imports `sandbox/read_session.py`'s three functions (DRY reuse, no rewrite).

**Tech Stack:** Python 3.12 + pytest (subprocess-driven CLI tests, sub-second each) · stdlib only in the scripts (argparse/json/datetime/re/pathlib) · reuses existing `generator/` (STAGE 1/2) and `sandbox/read_session.py` (STAGE 2).

## Global Constraints

- All 7 scripts land in a NEW top-level `ladder-foundry/scripts/`; tests in `ladder-foundry/tests/`. pytest is run FROM `ladder-foundry/`, so every subprocess path prefix is `scripts/<name>.py`.
- `apply_weight_update.py` imports `generator` via `sys.path.insert(0, str(Path(__file__).resolve().parents[1]))` — **`parents[1]`**, NOT `parents[3]`. The script is 1 level below `ladder-foundry/`; `generator/` is its sibling. `parents[3]` walks above the repo → `ModuleNotFoundError`.
- `save_transcript.py` imports read_session via `sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))`.
- Privacy red line: `save_transcript --logs-dir` is REQUIRED with no default. No CC-log absolute path / cwd-slug ever written into a committed artifact. Every test uses `tmp_path` synthetic `--cwd`/`--logs-dir` values only — never a real device path.
- `gen_configs.py` (L7) stays in `generator/`, UNTOUCHED. The M1 naming-collision fix is a separate STAGE 2 patch, out of scope here.
- `runs/` is NOT pre-created. Scripts are parameter-driven (`--run-dir`/`--runs-root`); tests use `tmp_path`. No speculative empty directories committed.
- Data-oriented invariant: training edits JSON DATA only; `.py` sources never move. `frozen_label` locked; `collision_offset_axis ∈ {B1,expression}` — enforced by `weights.revise`, NOT re-implemented here.
- W5 check-blind: these scripts never name 32-check / 6-primitive / detection signatures.
- Branch `self-iteration/ladder-foundry` — do NOT branch off. Commit only the step's files. Commit trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

---

### Task 1: new_run_id.py (L8 — run skeleton)

**Files:**
- Create: `ladder-foundry/scripts/new_run_id.py`
- Test: `ladder-foundry/tests/test_new_run_id.py`

**Interfaces:**
- Consumes: nothing (pure stdlib).
- Produces: prints `run_id` = `now().strftime("%Y-%m-%d-%H-%M-%S")` to stdout; builds `<runs-root>/<run_id>/{configs,transcripts,triples,loss,weights}/`.

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_new_run_id.py`:
```python
import re, subprocess, sys


def test_run_id_format_and_skeleton(tmp_path):
    out = subprocess.check_output([sys.executable, "scripts/new_run_id.py",
        "--runs-root", str(tmp_path)], text=True).strip()
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", out)  # run_id format
    base = tmp_path / out
    for sub in ("configs", "transcripts", "triples", "loss", "weights"):
        assert (base / sub).is_dir()                                  # 5 subdirs built
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_new_run_id.py -v`
Expected: FAIL — `FileNotFoundError: scripts/new_run_id.py` (script not yet created → subprocess non-zero).

- [ ] **Step 3: Write minimal implementation**

Create `ladder-foundry/scripts/new_run_id.py`:
```python
#!/usr/bin/env python3
"""System time -> run_id (yyyy-mm-dd-hh-mm-ss) + build runs/<id>/ skeleton.
Pure stdlib (no generator import). Called once at the epoch-loop entry."""
import argparse
import datetime
from pathlib import Path

SUBDIRS = ("configs", "transcripts", "triples", "loss", "weights")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-root", default="runs")
    a = ap.parse_args()
    run_id = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    base = Path(a.runs_root) / run_id
    for sub in SUBDIRS:
        (base / sub).mkdir(parents=True, exist_ok=True)
    print(run_id)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_new_run_id.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/new_run_id.py ladder-foundry/tests/test_new_run_id.py
git commit -m "feat(stage3): new_run_id (L8) — run_id + runs/ skeleton"
```

---

### Task 2: trace_emit.py (L9 — 11-event ledger, 2 micro-fixes)

**Files:**
- Create: `ladder-foundry/scripts/trace_emit.py`
- Test: `ladder-foundry/tests/test_trace_emit.py`

**Interfaces:**
- Consumes: nothing (pure stdlib).
- Produces: appends one jsonl line to `--trace`. Every line carries the 7 common-header fields `{ts, run_id, event, batch_id, topic_id, rung_id, seq}` + a per-event body from arbitrary `--key val` pairs. `ts` (ISO8601) and `seq` are generated inside (never caller-supplied); `seq` continues from the file's last valid line +1.

- [ ] **Step 1: Write the failing tests (header + seq + nested body; + 2 micro-fix coverage)**

Create `ladder-foundry/tests/test_trace_emit.py`:
```python
import json, subprocess, sys

COMMON = {"ts", "run_id", "event", "batch_id", "topic_id", "rung_id", "seq"}


def emit(trace, **kw):
    args = [sys.executable, "scripts/trace_emit.py", "--trace", str(trace)]
    for k, v in kw.items():
        args += [f"--{k}", str(v)]
    subprocess.check_call(args)


def test_header_seq_and_nested_body(tmp_path):
    tr = tmp_path / "trace.jsonl"
    emit(tr, run_id="2026-06-07-00-00-00", event="run_start", batch_id="batch-0",
         topic_id="topic-00", rung_id="0")
    emit(tr, run_id="2026-06-07-00-00-00", event="rung_start", batch_id="batch-0",
         topic_id="topic-00", rung_id="0", axis_levels='{"A1":"L4","A3":"L4"}')
    rows = [json.loads(l) for l in tr.read_text(encoding="utf-8").splitlines()]
    assert COMMON <= set(rows[0])                       # 7 header fields present
    assert all(rows[0][k] is not None for k in COMMON)  # test-hole: none slip through as None
    assert rows[0]["seq"] == 1 and rows[1]["seq"] == 2  # seq strictly increments
    assert rows[1]["axis_levels"] == {"A1": "L4", "A3": "L4"}  # micro-fix A: parsed object


def test_malformed_body_falls_back_to_raw_string(tmp_path):
    tr = tmp_path / "trace.jsonl"
    emit(tr, run_id="r", event="e", batch_id="b", topic_id="t", rung_id="0",
         note="{bad json not closed")
    row = json.loads(tr.read_text(encoding="utf-8").splitlines()[-1])
    assert row["note"] == "{bad json not closed"        # micro-fix A: graceful raw fallback


def test_truncated_last_line_recovery(tmp_path):
    tr = tmp_path / "trace.jsonl"
    emit(tr, run_id="r", event="e", batch_id="b", topic_id="t", rung_id="0")  # seq 1
    with open(tr, "a", encoding="utf-8") as f:          # simulate a crash mid-write
        f.write('{"seq": 2, "event": "rung_done", trunc')
    emit(tr, run_id="r", event="e2", batch_id="b", topic_id="t", rung_id="0")
    rows = [l for l in tr.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert json.loads(rows[-1])["seq"] == 2             # micro-fix B: scan past corrupt line
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_trace_emit.py -v`
Expected: FAIL — `FileNotFoundError: scripts/trace_emit.py`.

- [ ] **Step 3: Write minimal implementation**

Create `ladder-foundry/scripts/trace_emit.py`:
```python
#!/usr/bin/env python3
"""Append one event line to trace.jsonl. 7 common-header fields (ts/run_id/
event/batch_id/topic_id/rung_id/seq) + a per-event body from extra --key val
pairs. ts + seq are generated here (never caller-supplied). Stateless: seq
continues from the file's last valid line +1."""
import argparse
import datetime
import json
from pathlib import Path

COMMON = ["run_id", "event", "batch_id", "topic_id", "rung_id"]


def next_seq(trace):
    p = Path(trace)
    if not p.exists():
        return 1
    lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    # micro-fix B: a truncated/corrupt final line (crash mid-write) must not
    # crash the emitter — scan upward to the last line that parses.
    for line in reversed(lines):
        try:
            return json.loads(line)["seq"] + 1
        except (json.JSONDecodeError, KeyError):
            continue
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", required=True)
    for k in COMMON:
        ap.add_argument(f"--{k}", default=None)
    a, unknown = ap.parse_known_args()
    # per-event body: remaining --key val pairs. micro-fix A: try json.loads so
    # nested objects/arrays (config_full, axis_levels, recent_ratios, ...)
    # round-trip as parsed structures, not stringified.
    extra = {}
    it = iter(unknown)
    for tok in it:
        if tok.startswith("--"):
            raw = next(it, None)
            try:
                extra[tok[2:]] = json.loads(raw) if raw is not None else None
            except (json.JSONDecodeError, TypeError):
                extra[tok[2:]] = raw
    row = {"ts": datetime.datetime.now().isoformat(),
           "run_id": a.run_id, "event": a.event, "batch_id": a.batch_id,
           "topic_id": a.topic_id, "rung_id": a.rung_id, "seq": next_seq(a.trace)}
    row.update(extra)
    with open(a.trace, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_trace_emit.py -v`
Expected: all 3 PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/trace_emit.py ladder-foundry/tests/test_trace_emit.py
git commit -m "feat(stage3): trace_emit (L9) — 7-header jsonl + seq self-increment, nested-body + truncated-line micro-fixes"
```

---

### Task 3: save_transcript.py (L10 — exec transcript → .md, DRY reuse read_session)

**Files:**
- Create: `ladder-foundry/scripts/save_transcript.py`
- Test: `ladder-foundry/tests/test_save_transcript.py`
- Reuse (do NOT modify): `ladder-foundry/sandbox/read_session.py`

**Interfaces:**
- Consumes from `sandbox/read_session.py`: `cwd_to_slug(cwd)` → str; `find_latest_session(logs_dir, cwd_slug)` → Path (newest `.jsonl` under `projects/<slug>/`, raises `FileNotFoundError` if none); `read_turns(session_path)` → `list[{"role":str,"text":str}]` (handles `content` as str OR list-of-blocks).
- Produces: writes a markdown `--out` file with a `--sample` header + one `### {role}` block per user/assistant turn. `--logs-dir` is REQUIRED (no default).

**Reuse precondition (re-confirm before transcribing):** `sandbox/read_session.py` exposes exactly those three functions with the signatures above. Verified present. If a signature differs at implementation time, STOP and report — do not silently re-implement.

- [ ] **Step 1: Write the failing tests (--logs-dir required + only user/assistant + no path leak)**

Create `ladder-foundry/tests/test_save_transcript.py`:
```python
import json, subprocess, sys


def test_logs_dir_required(tmp_path):
    r = subprocess.run([sys.executable, "scripts/save_transcript.py",
        "--cwd", str(tmp_path), "--sample", "s1", "--out", str(tmp_path / "t.md")])
    assert r.returncode != 0      # missing --logs-dir must hard-fail (privacy red line)


def test_extracts_user_assistant_only(tmp_path):
    # synthetic logs dir laid out as CC does: projects/<cwd-slug>/<session>.jsonl
    cwd = tmp_path / "execwd"
    slug = "".join(c if c.isalnum() or c == "-" else "-" for c in str(cwd))
    proj = tmp_path / "logs" / "projects" / slug
    proj.mkdir(parents=True)
    (proj / "sess.jsonl").write_text("\n".join([
        json.dumps({"type": "user", "message": {"role": "user", "content": "question A"}}),
        json.dumps({"type": "assistant", "message": {"role": "assistant",
                    "content": [{"type": "text", "text": "reply B"}]}}),  # list-of-blocks
        json.dumps({"type": "system", "message": {"role": "system", "content": "internal noise"}}),
    ]), encoding="utf-8")
    out = tmp_path / "t.md"
    subprocess.check_call([sys.executable, "scripts/save_transcript.py",
        "--logs-dir", str(tmp_path / "logs"), "--cwd", str(cwd),
        "--sample", "batch-0-topic00-id0", "--out", str(out)])
    txt = out.read_text(encoding="utf-8")
    assert "question A" in txt and "reply B" in txt   # user + assistant (list-of-blocks) reach .md
    assert "internal noise" not in txt                # system filtered out
    assert "batch-0-topic00-id0" in txt               # sample header present
    assert slug not in txt and str(tmp_path) not in txt  # privacy: no slug / abs log path in body
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_save_transcript.py -v`
Expected: FAIL — `FileNotFoundError: scripts/save_transcript.py`.

- [ ] **Step 3: Write minimal implementation (thin shell over read_session)**

Create `ladder-foundry/scripts/save_transcript.py`:
```python
#!/usr/bin/env python3
"""Read THIS run's exec session jsonl (located by cwd-slug) -> transcript.md,
user/assistant turns only. --logs-dir is REQUIRED (privacy red line: the only
place that reads CC logs). DRY: reuses sandbox/read_session.py's three
functions; adds only the .md formatting shell."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))
from read_session import cwd_to_slug, find_latest_session, read_turns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True,
                    help="CC projects logs dir (REQUIRED, no default — privacy)")
    ap.add_argument("--cwd", required=True, help="the exec cwd to slug + locate")
    ap.add_argument("--sample", required=True, help="sample id for the .md header")
    ap.add_argument("--out", required=True, help="output .md path")
    a = ap.parse_args()
    session = find_latest_session(a.logs_dir, cwd_to_slug(a.cwd))
    blocks = [f"# transcript: {a.sample}\n"]
    for t in read_turns(session):
        if t["role"] in ("user", "assistant"):
            blocks.append(f"### {t['role']}\n\n{t['text']}\n")
    Path(a.out).write_text("\n".join(blocks), encoding="utf-8")  # never write slug / abs log path


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_save_transcript.py -v`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/save_transcript.py ladder-foundry/tests/test_save_transcript.py
git commit -m "feat(stage3): save_transcript (L10) — exec jsonl to .md, DRY reuse read_session, --logs-dir required"
```

---

### Task 4: concat_triple.py (L11 — fence blocks → triple)

**Files:**
- Create: `ladder-foundry/scripts/concat_triple.py`
- Test: `ladder-foundry/tests/test_concat_triple.py`

**Interfaces:**
- Consumes: `<run-dir>/configs/<sample>.json` + `<run-dir>/transcripts/<sample>.md`.
- Produces: `<run-dir>/triples/<sample>.json` = `{"research_config":..., "research_graph":..., "research_result":...}`. Cuts by info-string fence (` ```research-graph ` / ` ```research-result `), takes the LAST block of each kind, raises `ValueError` if a required fence is absent.

- [ ] **Step 1: Write the failing tests (take-last + missing-fence ValueError)**

Create `ladder-foundry/tests/test_concat_triple.py`:
```python
import json, subprocess, sys


def _setup(tmp_path, md):
    rd = tmp_path / "run"
    for sub in ("configs", "transcripts", "triples"):
        (rd / sub).mkdir(parents=True)
    (rd / "configs" / "s1.json").write_text(json.dumps({"F0": "cfg"}), encoding="utf-8")
    (rd / "transcripts" / "s1.md").write_text(md, encoding="utf-8")
    return rd


def test_concat_takes_last_fenced_block(tmp_path):
    md = "\n".join([
        "```research-graph", '{"nodes": [], "edges": []}', "```",
        "```research-result", '{"title": "old"}', "```",
        "```research-result", '{"title": "final"}', "```",   # accepted draft after pushback
    ])
    rd = _setup(tmp_path, md)
    subprocess.check_call([sys.executable, "scripts/concat_triple.py",
        "--run-dir", str(rd), "--sample", "s1"])
    tri = json.loads((rd / "triples" / "s1.json").read_text(encoding="utf-8"))
    assert tri["research_config"]["F0"] == "cfg"
    assert tri["research_result"]["title"] == "final"     # LAST research-result block
    assert "nodes" in tri["research_graph"]               # graph block also cut


def test_missing_fence_raises(tmp_path):
    rd = _setup(tmp_path, "```research-graph\n{\"nodes\": []}\n```\n")  # no research-result
    r = subprocess.run([sys.executable, "scripts/concat_triple.py",
        "--run-dir", str(rd), "--sample", "s1"])
    assert r.returncode != 0                              # missing required fence -> non-zero
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_concat_triple.py -v`
Expected: FAIL — `FileNotFoundError: scripts/concat_triple.py`.

- [ ] **Step 3: Write minimal implementation**

Create `ladder-foundry/scripts/concat_triple.py`:
```python
#!/usr/bin/env python3
"""config + transcript fence blocks -> (research_config, research_graph,
research_result) triple. Cut by info-string fence, take the LAST block of each
kind (the accepted draft after pushback). Missing a required fence -> ValueError
(argparse/uncaught -> non-zero exit)."""
import argparse
import json
import re
from pathlib import Path


def last_block(md, info):
    """Return the JSON parsed from the LAST ```<info> ... ``` fence."""
    rx = re.compile(r"```" + re.escape(info) + r"\s*\n(.*?)\n```", re.DOTALL)
    blocks = rx.findall(md)
    if not blocks:
        raise ValueError(f"no '{info}' fenced block in transcript")
    return json.loads(blocks[-1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--sample", required=True)
    a = ap.parse_args()
    rd = Path(a.run_dir)
    cfg = json.loads((rd / "configs" / f"{a.sample}.json").read_text(encoding="utf-8"))
    md = (rd / "transcripts" / f"{a.sample}.md").read_text(encoding="utf-8")
    triple = {"research_config": cfg,
              "research_graph": last_block(md, "research-graph"),
              "research_result": last_block(md, "research-result")}
    (rd / "triples" / f"{a.sample}.json").write_text(
        json.dumps(triple, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_concat_triple.py -v`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/concat_triple.py ladder-foundry/tests/test_concat_triple.py
git commit -m "feat(stage3): concat_triple (L11) — fence blocks to triple, take-last, missing-fence ValueError"
```

---

### Task 5: gate_eval.py (L12 — pure gate arithmetic)

**Files:**
- Create: `ladder-foundry/scripts/gate_eval.py`
- Test: `ladder-foundry/tests/test_gate_eval.py`

**Interfaces:**
- Consumes: nothing (pure stdlib, no CC/codex).
- Produces: prints `"true"`/`"false"` for one of three subcommands — `topic` (`--fidelity-rate/--mono/--endpoint` → 3-way AND), `batch` (`--flags` comma list → pass_ratio ≥0.80), `converged` (`--recent` comma list → last 3 all ≥0.80). Thresholds are module constants `FIDELITY_MIN=0.90`, `BATCH_RATIO_MIN=0.80`.

- [ ] **Step 1: Write the failing tests (3-way AND / 7-8 integer line / converged last-3)**

Create `ladder-foundry/tests/test_gate_eval.py`:
```python
import subprocess, sys


def gate(*args):
    return subprocess.check_output([sys.executable, "scripts/gate_eval.py", *args],
        text=True).strip()


def test_topic_three_way_and():
    assert gate("topic", "--fidelity-rate", "0.90", "--mono", "true", "--endpoint", "true") == "true"
    assert gate("topic", "--fidelity-rate", "0.83", "--mono", "true", "--endpoint", "true") == "false"
    assert gate("topic", "--fidelity-rate", "0.95", "--mono", "false", "--endpoint", "true") == "false"
    assert gate("topic", "--fidelity-rate", "0.95", "--mono", "true", "--endpoint", "false") == "false"


def test_batch_hard_integer_line():
    assert gate("batch", "--flags", "true,true,true,true,true,true,true,false") == "true"   # 7/8
    assert gate("batch", "--flags", "true,true,true,true,true,true,false,false") == "false"  # 6/8


def test_converged_last_three():
    assert gate("converged", "--recent", "0.625,0.875,0.875,0.875") == "true"   # last 3 >= 0.80
    assert gate("converged", "--recent", "0.875,0.75,0.875") == "false"          # break in middle
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_gate_eval.py -v`
Expected: FAIL — `FileNotFoundError: scripts/gate_eval.py`.

- [ ] **Step 3: Write minimal implementation**

Create `ladder-foundry/scripts/gate_eval.py`:
```python
#!/usr/bin/env python3
"""Pure gate arithmetic: topic (3-way AND) / batch (pass_ratio) / converged
(last 3). No CC/codex call. Thresholds are module constants here; STAGE 4 may
externalize them to a references file."""
import argparse

FIDELITY_MIN = 0.90
BATCH_RATIO_MIN = 0.80


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    t = sub.add_parser("topic")
    t.add_argument("--fidelity-rate", type=float, required=True)
    t.add_argument("--mono", required=True)
    t.add_argument("--endpoint", required=True)
    b = sub.add_parser("batch")
    b.add_argument("--flags", required=True)
    c = sub.add_parser("converged")
    c.add_argument("--recent", required=True)
    a = ap.parse_args()
    if a.mode == "topic":
        ok = (a.fidelity_rate >= FIDELITY_MIN and a.mono == "true" and a.endpoint == "true")
        print("true" if ok else "false")
    elif a.mode == "batch":
        flags = [x == "true" for x in a.flags.split(",")]
        print("true" if sum(flags) / len(flags) >= BATCH_RATIO_MIN else "false")
    elif a.mode == "converged":
        rs = [float(x) for x in a.recent.split(",")]
        print("true" if len(rs) >= 3 and all(r >= BATCH_RATIO_MIN for r in rs[-3:]) else "false")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_gate_eval.py -v`
Expected: all 3 PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/gate_eval.py ladder-foundry/tests/test_gate_eval.py
git commit -m "feat(stage3): gate_eval (L12) — 3-way AND / pass_ratio / converged, thresholds as constants"
```

---

### Task 6: apply_weight_update.py (L13 — change weights JSON, parents[1] fix)

**Files:**
- Create: `ladder-foundry/scripts/apply_weight_update.py`
- Test: `ladder-foundry/tests/test_apply_weight_update.py`
- Imports (do NOT modify): `ladder-foundry/generator/weights.py`

**Interfaces:**
- Consumes from `generator.weights`: `load(path)` → dict; `revise(w, target, key, new, reason)` → `{"target","key","old","new","reason"}` (signature byte-identical to the real `weights.py`; rejects `frozen_label`, unknown targets, and `collision_offset_axis` not in `{B1,expression}`).
- Produces: F2 mode (`--target/--key/--new/--reason`) writes `<weights-dir>/<batch+1>.json` + appends one line to `<weights-dir>/../revision_log.jsonl`, prints the revise record. F1 mode (`--copy`) byte-for-byte copies forward, writes NO log.

**Path fix (load-bearing):** `sys.path.insert(0, str(Path(__file__).resolve().parents[1]))` — **`parents[1]`** (the script's grandparent-via-1-level is `ladder-foundry/`, `generator/` is its sibling). `parents[3]` was Plan B's value for a deeper `skills/.../scripts/` layout and is WRONG here → `ModuleNotFoundError`.

- [ ] **Step 1: Write the failing tests (F2 revise+log / F1 copy byte-identical+no log+size>0)**

Create `ladder-foundry/tests/test_apply_weight_update.py`:
```python
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from generator.weights import dump_initial


def test_f2_revise_writes_next_batch_and_log(tmp_path):
    wd = tmp_path / "weights"; wd.mkdir()
    dump_initial(wd / "batch-0.json")
    subprocess.check_call([sys.executable, "scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0",
        "--target", "axis_prose", "--key", "A1.L0", "--new", "stronger pressure prose",
        "--reason", "loss-1 failed"])
    nxt = json.loads((wd / "batch-1.json").read_text(encoding="utf-8"))
    assert nxt["axis_prose"]["A1"]["L0"] == "stronger pressure prose"   # exactly one cell changed
    rec = json.loads((wd.parent / "revision_log.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert rec["target"] == "axis_prose" and rec["key"] == "A1.L0"      # logged


def test_f1_copy_byte_identical_no_log(tmp_path):
    wd = tmp_path / "weights"; wd.mkdir()
    dump_initial(wd / "batch-0.json")
    subprocess.check_call([sys.executable, "scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0", "--copy"])
    nxt_path = wd / "batch-1.json"
    assert nxt_path.stat().st_size > 0                                  # test-hole: not empty
    assert json.loads(nxt_path.read_text(encoding="utf-8")) == \
           json.loads((wd / "batch-0.json").read_text(encoding="utf-8"))  # byte-equal content
    assert not (wd.parent / "revision_log.jsonl").exists()              # copy writes NO log
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_apply_weight_update.py -v`
Expected: FAIL — `FileNotFoundError: scripts/apply_weight_update.py`.

- [ ] **Step 3: Write minimal implementation**

Create `ladder-foundry/scripts/apply_weight_update.py`:
```python
#!/usr/bin/env python3
"""F2: revise one weights JSON segment (via generator.weights.revise) + append
revision_log.jsonl + write weights/<batch+1>.json. F1: --copy byte-for-byte
copy forward, no log. Data-oriented: edits JSON data only; this source never
moves. Invariants (frozen_label locked, collision_offset_axis enum) are enforced
by weights.revise, NOT re-implemented here."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1]: generator/ is sibling
from generator import weights as W


def next_id(batch_id):
    return f"batch-{int(batch_id.split('-')[1]) + 1}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights-dir", required=True)
    ap.add_argument("--batch-id", required=True)
    ap.add_argument("--copy", action="store_true")   # F1 copy mode
    ap.add_argument("--target")
    ap.add_argument("--key")
    ap.add_argument("--new")
    ap.add_argument("--reason")
    a = ap.parse_args()
    wd = Path(a.weights_dir)
    cur = W.load(wd / f"{a.batch_id}.json")
    nxt_path = wd / f"{next_id(a.batch_id)}.json"
    if a.copy:
        # F1: byte-for-byte copy forward, no change, no log
        nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2), encoding="utf-8")
        return
    rec = W.revise(cur, target=a.target, key=a.key, new=a.new, reason=a.reason)
    nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(wd.parent / "revision_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))       # for CC to assemble the weight_revised trace event


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_apply_weight_update.py -v`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/apply_weight_update.py ladder-foundry/tests/test_apply_weight_update.py
git commit -m "feat(stage3): apply_weight_update (L13) — F2 revise+log / F1 byte-copy, parents[1] generator import"
```

---

### Task 7: write_dataset.py (L14 — privacy whitelist → dataset)

**Files:**
- Create: `ladder-foundry/scripts/write_dataset.py`
- Test: `ladder-foundry/tests/test_write_dataset.py`

**Interfaces:**
- Consumes: `<run-dir>/triples/<sample>.json` (must contain exactly `{research_config, research_graph, research_result}`).
- Produces: `<out-root>/<topic>/<sample>.json` = a whitelisted sample `{sample_id, label:{rung_id,axis_levels}, research_config, research_graph, research_result, loss1_fidelity, topic_pass, intended_rank}`. Hard-fails (`sys.exit`) if the triple carries any field outside `{research_config, research_graph, research_result}` (catches a leaked `logs_dir`), and again if the output has any non-whitelist key. `--loss1`/`--topic-pass` are CLI params (filled by STAGE 4's loss later; fake values fully exercise the privacy logic).

- [ ] **Step 1: Write the failing tests (non-whitelist field → non-zero exit; output keys ⊆ whitelist)**

Create `ladder-foundry/tests/test_write_dataset.py`:
```python
import json, subprocess, sys

WHITELIST = {"sample_id", "label", "research_config", "research_graph",
             "research_result", "loss1_fidelity", "topic_pass", "intended_rank"}


def _triple(extra=None):
    d = {"research_config": {"F0": "x"}, "research_graph": {"nodes": []},
         "research_result": {"title": "t"}}
    if extra:
        d.update(extra)
    return d


def test_rejects_non_whitelist_field(tmp_path):
    rd = tmp_path / "run"; (rd / "triples").mkdir(parents=True)
    # inject a leaked field (e.g. a logs_dir). The VALUE is a synthetic sentinel,
    # NOT a real device path — committed tests must never carry a real CC-log path.
    (rd / "triples" / "s1.json").write_text(json.dumps(
        _triple({"logs_dir": "REDACTED-synthetic-sentinel-not-a-real-path"})), encoding="utf-8")
    r = subprocess.run([sys.executable, "scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "s1", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path / "dataset")])
    assert r.returncode != 0      # non-whitelist field in triple -> hard-fail abort


def test_writes_whitelisted_sample(tmp_path):
    rd = tmp_path / "run"; (rd / "triples").mkdir(parents=True)
    (rd / "triples" / "batch-0-topic00-id0.json").write_text(
        json.dumps(_triple()), encoding="utf-8")
    subprocess.check_call([sys.executable, "scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "batch-0-topic00-id0", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path / "dataset"),
        "--axis-levels", '{"A1":"L0"}', "--loss1", "1.0", "--topic-pass", "true"])
    out = json.loads((tmp_path / "dataset" / "topic-00" /
                      "batch-0-topic00-id0.json").read_text(encoding="utf-8"))
    assert set(out) <= WHITELIST            # output keys subset of whitelist
    assert out["label"]["rung_id"] == 0     # label.rung_id correct
    assert out["topic_pass"] is True
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_write_dataset.py -v`
Expected: FAIL — `FileNotFoundError: scripts/write_dataset.py`.

- [ ] **Step 3: Write minimal implementation**

Create `ladder-foundry/scripts/write_dataset.py`:
```python
#!/usr/bin/env python3
"""Privacy whitelist trim + schema -> dataset/<topic>/<sample>.json. Hard-fails
if the triple carries any field outside {research_config, research_graph,
research_result} (catches a leaked logs_dir), and again if the assembled output
has any non-whitelist key. loss1/topic_pass are CLI params (STAGE 4's loss fills
real values later)."""
import argparse
import json
import sys
from pathlib import Path

TRIPLE_KEYS = {"research_config", "research_graph", "research_result"}
WHITELIST = {"sample_id", "label", "research_config", "research_graph",
             "research_result", "loss1_fidelity", "topic_pass", "intended_rank"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--sample", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--rung", type=int, required=True)
    ap.add_argument("--out-root", required=True)
    ap.add_argument("--axis-levels", default="{}")
    ap.add_argument("--loss1", default="0.0")
    ap.add_argument("--topic-pass", default="false")
    a = ap.parse_args()
    tri = json.loads((Path(a.run_dir) / "triples" / f"{a.sample}.json").read_text(encoding="utf-8"))
    extra = set(tri) - TRIPLE_KEYS
    if extra:
        sys.exit(f"FATAL: triple has non-whitelist fields {extra} (privacy red line)")
    sample = {
        "sample_id": a.sample,
        "label": {"rung_id": a.rung, "axis_levels": json.loads(a.axis_levels)},
        "research_config": tri["research_config"],
        "research_graph": tri["research_graph"],
        "research_result": tri["research_result"],
        "loss1_fidelity": float(a.loss1),
        "topic_pass": a.topic_pass.lower() == "true",
        "intended_rank": a.rung,
    }
    leaked = set(sample) - WHITELIST
    if leaked:
        sys.exit(f"FATAL: output has non-whitelist fields {leaked}")
    out = Path(a.out_root) / a.topic
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{a.sample}.json").write_text(
        json.dumps(sample, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_write_dataset.py -v`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/scripts/write_dataset.py ladder-foundry/tests/test_write_dataset.py
git commit -m "feat(stage3): write_dataset (L14) — privacy whitelist trim + schema, double hard-fail"
```

---

### Task 8: wrap — full-suite regression + privacy grep + ledger

**Files:**
- Modify: `.superpowers/sdd/progress.md` (append STAGE 3 completion lines)
- No new source; this task is verification + bookkeeping.

**Interfaces:**
- Consumes: all 7 scripts + tests from Tasks 1–7, plus the existing STAGE 1/2 suite.
- Produces: a green full-suite run, a clean privacy grep, an updated ledger.

- [ ] **Step 1: Full-suite regression (STAGE 1+2+3 all green)**

Run: `cd ladder-foundry && python -m pytest tests/ -v`
Expected: all STAGE 1/2/3 tests PASS (STAGE 2 final was 55 passed; STAGE 3 adds 7 test files → count rises). No failures, no errors.

- [ ] **Step 2: Privacy grep over scripts/ + tests/ (three log-path signatures, all must be clean)**

Run (from `ladder-foundry/`):
```bash
grep -rnE 'C:\\Users\\[^\\]+\\\.claude\\projects|/workspace/home/[^/]+/\.claude/projects|-claude-projects' scripts/ tests/ \
  && echo "LEAK FOUND — FIX BEFORE COMMIT" || echo "NO LEAK"
```
Expected: prints `NO LEAK`. The three alternatives cover: Windows CC-log path (`C:\Users\<user>\.claude\projects`), POSIX role config-dir log path (`/workspace/home/<role>/.claude/projects`), and a bare cwd-slug. Note the slug form: `read_session.cwd_to_slug` maps both `:` and `\` to `-`, so a leaked path slugifies to `...-claude-projects` (NO colon) — hence the third signature is `-claude-projects`, not `projects/<drive>:-`. Any hit = a committed artifact leaked a real device path → fix the offending test to use only `tmp_path` synthetic values.

- [ ] **Step 3: Update the progress ledger**

Append to `.superpowers/sdd/progress.md` (after the STAGE 2 section), recording each task's commit range and the wrap result. Use the actual 7-char commit SHAs from `git log --oneline`:
```markdown

## STAGE 3 run-scripts (L8–L14) — progress

- Task 1 (L8 new_run_id): complete (<base7>..<head7>, review clean)
- Task 2 (L9 trace_emit + 2 micro-fixes): complete (..<head7>, review clean)
- Task 3 (L10 save_transcript, DRY read_session): complete (..<head7>, review clean)
- Task 4 (L11 concat_triple): complete (..<head7>, review clean)
- Task 5 (L12 gate_eval): complete (..<head7>, review clean)
- Task 6 (L13 apply_weight_update, parents[1]): complete (..<head7>, review clean)
- Task 7 (L14 write_dataset): complete (..<head7>, review clean)
- Task 8 wrap: full suite green (N passed); privacy grep NO LEAK (3 signatures clean).

## ALL STAGE 3 TASKS COMPLETE
```

- [ ] **Step 4: Commit the ledger**

```bash
git add .superpowers/sdd/progress.md
git commit -m "chore(stage3): wrap — full-suite green, privacy grep clean, ledger updated"
```

---

## Self-Review (checked against the STAGE 3 design spec)

**1. Spec coverage** — every spec section maps to a task:
- 7 scripts L8–L14 (spec §3) → Tasks 1–7, one each. ✅
- parents[1] fix (spec §2 P1) → Task 6 path-fix block + inline comment. ✅
- test path prefix `scripts/<name>.py` (spec §2 P2) → every test's subprocess call. ✅
- trace_emit 2 micro-fixes (spec §3 L9) → Task 2 `next_seq` reversed-scan (B) + `json.loads` body parse (A), each with a red-going test. ✅
- save_transcript DRY reuse + reuse precondition (spec §3 L10) → Task 3 imports the 3 read_session functions + precondition note + list-of-blocks test. ✅
- gate_eval thresholds as constants (spec §5) → Task 5 module constants. ✅
- two test-hole fixes (spec §4) → Task 2 `all(... is not None)`, Task 6 `st_size > 0`. ✅
- write_dataset privacy gate (spec §3 L14) → Task 7. The INPUT check (`set(tri) - TRIPLE_KEYS`, catching an upstream-leaked `logs_dir`) is the real dynamically-fed gate and has a red-going test. The OUTPUT check (`set(sample) - WHITELIST`) is a cheap static invariant over a hard-coded dict literal — it can only fire if someone edits the literal without updating WHITELIST, so it is a compile-time guard, not a live-tested branch. Kept (2 lines guarding the #1 constraint); not oversold as tested. ✅
- T8 wrap: full-suite + 3-signature privacy grep + ledger (spec §6 T8) → Task 8. ✅
- M1 left untouched, runs/ not pre-created, gen_configs in generator/ (spec §1) → Global Constraints + no task touches them. ✅

**2. Placeholder scan** — no "TBD/TODO/implement later"; every code step carries complete runnable code; commands have expected output. The ledger's `<base7>..<head7>` are explicit fill-from-`git log` instructions, not plan placeholders. ✅

**3. Type consistency** — `revise(w, target, key, new, reason)` (Task 6) matches the real `generator/weights.py` exactly; the three read_session signatures (Task 3) match `sandbox/read_session.py` exactly; sample naming `<batch>-topic<NN>-id<N>` consistent across Tasks 3/4/7; the 7-field common header `{ts,run_id,event,batch_id,topic_id,rung_id,seq}` consistent in Task 2; WHITELIST set identical between Task 7 test and implementation. ✅

No gaps found.



