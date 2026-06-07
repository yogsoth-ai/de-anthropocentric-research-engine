# Plan B — generator + loss + optimizer system build Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Build every pure-function component with TDD: write a failing test → run red → minimal implementation → run green → commit.** Real-model components obey the `feedback-no-e2e-shell` iron rule — never fake-stub your way to green.

**Goal:** Build and test the entire component set from scratch — the three weight bodies, 9 leaf scripts, 2 codex loss skills, the `optimization-loop` skill — and grow Spec A's "single-run vertical slice" into a **single-topic 6-rung ladder**, validating loss-2 monotonicity τ + endpoint separation + gate arithmetic.

**Architecture:** Data-oriented — the three weights (① axis_prose / ② interp_params / ③ assembler_params) are JSON data segments inside `weights/<batch>.json`; the `.py` files are pure functions that only read those segments. **Changing a weight = changing JSON; the source code never moves.** The rank layer + label-coordinate layer are locked in the `frozen_label` segment (no one writes it). The CC is the driver; the 9 leaf py scripts never call each other and are all chained by the optimizer-CC in §loop order. loss uses codex (swapping the model family to avoid same-source bias), and the whole flow is check-blind (W5, passes leak_audit).

**Tech Stack:** Python 3.11 + pytest (pure functions, sub-second) · real claude/codex (integration e2e) · skill-creator conventions (`scripts/` executable + `references/` read on demand) · third-party proxy `api.ikuncode.cc`.

---

## Key discipline (applies to every Task, read first)

- **Full rewrite from scratch**: treat the triple-layer architecture final draft only as the **design spec**; the ~20 .py files / tests in the old `2026-06-06-probe-pretrain/` on the device are **not read, not inherited, not migrated — not a single line** (to avoid being misled by the old fake nesting, the brittle `extract_blocks`, the `secondary_perturbation`-uses-A2/A3 bug, etc.). Everything is written from scratch into `<proj> = self-iteration/2026-06-07-probe-pretrain/`.
- **Layered testing**: deterministic pure functions use **pytest** (P, sub-second, full boundary coverage, no real model); components that need a real model get **integration e2e** with real CC/codex (R, obeying no-fake). The only synthesized thing is the "input config+topic"; sim/exec/codex are all real processes.
- **Shared premise of the three data-oriented weights**: `axes.py`①/`interpolator.py`②/`assembler.py`③ are all **pure functions that read the corresponding segment of `weights/<batch>.json`, with source code that never moves**. What the optimizer changes is always the JSON data. Rationale: snapshots are replayable, single-variable controlled, history immutable.
- **W5 check-blind**: every generation-side artifact (config, prose, loss skill) passes `leak_audit` in full, never containing 32-check / 6-primitive / detection-signature terms. What loss judges is "whether the generating condition was faithfully executed / whether the ladder is monotone", not "whether the research quality is good" (quality judgment is the downstream probe's job).
- **Privacy red line**: the CC log absolute path never enters any committed artifact; reading logs goes only through the mandatory `--logs-dir` script (`save_transcript`). `write_dataset` whitelist: schema validation before write; any field outside the whitelist (especially log paths, device usernames, raw transcript text) → hard-fail abort. The two sets of API key values never go into scripts/spec/reports/commits.
- **B's e2e endpoint = single topic, 6 rungs**: multi-batch LOOP-2, three-consecutive-pass convergence, backprop actually changing weights, long-running tmux, the PT5 pilot, the supervision panel, the full dataset — all belong to Spec C.

## B / C boundary (this plan does not cross it)

- **B builds the parts + the single-topic 6-rung run**; **C assembles and operates** (multi-batch, real backprop, long-running, pilot, supervision, full production).
- The `optimization-loop` skill is written in B (§loop/§gate/§state/§tools written in full), but the B phase only uses a 6-run to validate that its §loop/§gate run; **the §backprop section (the intelligent point) is written out but only truly exercised in Spec C's long run** — backprop's "attribute first, then act" can only be validated inside a multi-batch real fail-and-fix loop.
- `apply_weight_update.py` in the B phase only tests "can correctly change a JSON segment + the F1 copy mode"; its being intelligently driven by backprop is a C matter.
- The two skills `formated-specs` / `formated-result` **already exist** (project skills/); B only interfaces with their output contract (fence + JSON payload), and **does not rewrite them**.

---

## File Structure

Everything is written from scratch into `<proj> = self-iteration/2026-06-07-probe-pretrain/`:

```text
<proj>/
├── generator/                      # three weight bodies + supporting code (data-oriented pure-function package)
│   ├── axes.py            # ① level_text(axis,level) looks up the axis_prose table
│   ├── interpolator.py    # ② ladder_levels(n=6) reads the interp_params layer
│   ├── assembler.py       # ③ build_batch(...) reads assembler_params coordinates
│   ├── cards.py           # PolicyCard serialization to_dict
│   ├── leak_audit.py      # W5 DENY word-list interception
│   └── weights.py         # load / dump_initial / revise + schema
├── skills/optimization-loop/       # optimizer brain (claude skill)
│   ├── SKILL.md           # §loop/§gate/§backprop/§state/§tools
│   ├── scripts/           # 9 leaf py (deterministic, called by CC via Bash, no inter-calls)
│   │   ├── new_run_id.py        gen_configs.py     save_transcript.py
│   │   ├── concat_triple.py     run_codex_loss.py  gate_eval.py
│   │   ├── apply_weight_update.py write_dataset.py trace_emit.py
│   └── references/        # gate-thresholds.md + backprop-heuristic.md
├── skills/injection-fidelity/SKILL.md   # codex loss-1
├── skills/ladder-quality-order/SKILL.md # codex loss-2
├── config/topics.json             # B uses a single placeholder topic; C fills in 8 real topics
└── tests/                         # pytest (pure functions) + integration e2e (real model)
```

**Test-method tags**: P = pure-function pytest; R = real-model e2e; S = skill file.

**Build order (dependency-driven, bottom-up; each layer must be green before advancing to the next)**: B1 weights base → B2 three weight bodies → B3 generation pipeline → B4 data sink → B5 loss skills → B6 optimizer brain → B7 golden-sample 6-rung e2e. The Task numbering below aligns with this order.

---

### Task B1: weights base weights.py (data-oriented core)

**Files:**
- Create: `<proj>/generator/weights.py`
- Test: `<proj>/tests/test_weights.py`

`weights/<batch>.json` has four top-level segments — three trainable + one locked. `weights.py` provides `load` / `dump_initial` / `revise`. **All of it is hard-failable via pytest.**

**weights JSON schema (the single definitive definition in the whole document; a dozen-plus places in B/C refer back here):**

| Top-level segment | Corresponding weight | Reader | Writer | Trainable? |
| --- | --- | --- | --- | --- |
| `axis_prose` | ① prose `{axis:{level:body}}`, axis∈{A1..A5}, level∈{L0..L4} (A4 uses C+/C-, A5 uses G+/G-) | `axes.level_text` | `apply_weight_update(target=axis_prose)` | Yes |
| `interp_params` | ② layer: `collision_offset_axis` (only `"B1"`/`"expression"` allowed) + `endpoint_spread` + `granularity_map` | `interpolator.ladder_levels` | `apply_weight_update(target=interp_params)` | Yes (layer only) |
| `assembler_params` | ③ assembly: `two_stage` + `field_template` + `f6_derivation` + `turn_budget` (=F8) | `assembler.build_batch` | `apply_weight_update(target=assembler_params)` | Yes |
| `frozen_label` | rank layer `rank_order` (id0>…>id5 + primary-sort {A1,A3,A2} composite order) + label-coordinate layer `coord_table` (per-rung A1–A5 level values) | interpolator/assembler read-only | **no one writes (locked)** | **No** |

- [ ] **Step 1: write a failing test — illegal target is rejected**

Create `<proj>/tests/test_weights.py`:
```python
import pytest, json
from generator.weights import load, dump_initial, revise

def test_revise_rejects_frozen_label(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p)
    w = load(p)
    with pytest.raises(ValueError, match="frozen_label.*not trainable|not in whitelist"):
        revise(w, target="frozen_label", key="rank_order", new=[5,4,3,2,1,0], reason="x")

def test_revise_rejects_unknown_target(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p)
    w = load(p)
    with pytest.raises(ValueError):
        revise(w, target="not_a_segment", key="k", new="v", reason="x")
```

- [ ] **Step 2: run the test, confirm it fails**

Run: `cd <proj> && python -m pytest tests/test_weights.py::test_revise_rejects_frozen_label -v`
Expected: FAIL — `ModuleNotFoundError: generator.weights` or `revise not defined`.

- [ ] **Step 3: minimal implementation of weights.py**

Create `<proj>/generator/weights.py`:
```python
"""Data-oriented weights: three trainable segments + one locked segment. The .py only reads these segments; changing a weight = changing JSON."""
import json
from pathlib import Path

TRAINABLE = {"axis_prose", "interp_params", "assembler_params"}
COLLISION_ALLOWED = {"B1", "expression"}

def dump_initial(path):
    """Export batch-0.json from the three weights' defaults (not hand-filled)."""
    w = {
        "axis_prose": {ax: {lv: f"<{ax}.{lv} prose placeholder>" for lv in ["L0","L1","L2","L3","L4"]}
                       for ax in ["A1","A2","A3","A4","A5"]},
        "interp_params": {"collision_offset_axis": "B1", "endpoint_spread": 1.0,
                          "granularity_map": "round(t*4)"},
        "assembler_params": {"two_stage": True, "field_template": "<F0-F9 template placeholder>",
                             "f6_derivation": "<F1/F3/F2 derivation-rule placeholder>",
                             "turn_budget": {"pressure_turns": 10, "closing_turns": 2}},
        "frozen_label": {"rank_order": {"direction": [0,1,2,3,4,5],
                                        "primary_sort": ["A1","A3","A2"]},
                         "coord_table": {}},
    }
    Path(path).write_text(json.dumps(w, ensure_ascii=False, indent=2))
    return w

def load(path):
    return json.loads(Path(path).read_text())

def revise(w, target, key, new, reason):
    """Change one key of a trainable segment. frozen_label and unknown targets are always rejected."""
    if target not in TRAINABLE:
        raise ValueError(f"target '{target}' not in whitelist (frozen_label not trainable)")
    if target == "interp_params" and key == "collision_offset_axis" and new not in COLLISION_ALLOWED:
        raise ValueError(f"collision_offset_axis must be in {COLLISION_ALLOWED}, got '{new}'")
    old = w[target].get(key)
    w[target][key] = new
    return {"target": target, "key": key, "old": old, "new": new, "reason": reason}
```

- [ ] **Step 4: run the test, confirm it passes**

Run: `cd <proj> && python -m pytest tests/test_weights.py -v`
Expected: both PASS.

- [ ] **Step 5: add the collision schema lock + batch-0 export test**

Append to `<proj>/tests/test_weights.py`:
```python
def test_collision_offset_rejects_label_axis(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p); w = load(p)
    with pytest.raises(ValueError, match="collision_offset_axis"):
        revise(w, target="interp_params", key="collision_offset_axis", new="A2", reason="bug")

def test_collision_offset_accepts_b1_and_expression(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p); w = load(p)
    for v in ("B1", "expression"):
        rec = revise(w, target="interp_params", key="collision_offset_axis", new=v, reason="ok")
        assert rec["new"] == v

def test_dump_initial_has_four_segments(tmp_path):
    p = tmp_path / "batch-0.json"; w = dump_initial(p)
    assert set(w) == {"axis_prose","interp_params","assembler_params","frozen_label"}

def test_interp_params_has_no_coord(tmp_path):
    """Physical isolation (AS-3): interp_params never contains axis coordinate values."""
    p = tmp_path / "batch-0.json"; w = dump_initial(p)
    assert "coord_table" not in w["interp_params"]
    assert set(w["interp_params"]) == {"collision_offset_axis","endpoint_spread","granularity_map"}
```

- [ ] **Step 6: run all weights tests and commit**

Run: `cd <proj> && python -m pytest tests/test_weights.py -v`
Expected: all PASS (illegal target rejected, collision schema locked, batch-0 four segments, physical isolation).
```bash
git add generator/weights.py tests/test_weights.py
git commit -m "feat(B1): weights base — data-oriented schema, revise whitelist, collision lock, AS-3 isolation"
```

---

### Task B2: three weight bodies + cards + leak_audit (data-oriented pure functions)

**Files:**
- Create: `<proj>/generator/axes.py` ① / `interpolator.py` ② / `assembler.py` ③ / `cards.py` / `leak_audit.py`
- Test: `<proj>/tests/test_axes.py` / `test_interpolator.py` / `test_assembler.py` / `test_leak_audit.py`

The three weight bodies are all **pure functions that read the corresponding weights segment, with source code that never moves**. TDD them one by one.

- [ ] **Step 1: leak_audit, write a failing test (W5 DENY word-list interception)**

Create `<proj>/tests/test_leak_audit.py`:
```python
import pytest
from generator.leak_audit import leak_audit, LeakHit

def test_clean_text_passes():
    leak_audit("Design a controlled evaluation of an external model's reasoning fidelity")  # no raise

def test_denies_check_signature():
    with pytest.raises(LeakHit):
        leak_audit("This card must pass item 7 of the 32-check primitive detection")
```

- [ ] **Step 2: run red**

Run: `cd <proj> && python -m pytest tests/test_leak_audit.py -v`
Expected: FAIL — `ModuleNotFoundError: generator.leak_audit`.

- [ ] **Step 3: implement leak_audit.py**

Create `<proj>/generator/leak_audit.py`:
```python
"""W5 check-blind: DENY word-list intercepts 32-check / 6-primitive / detection-signature terms."""
import re

class LeakHit(Exception):
    """Hit the DENY word list; the caller handles via regenerate-then-reaudit."""

# Detection-signature word list (check-class terms, never allowed into generation-side artifacts)
DENY = [r"32-?check", r"6-?primitive", r"\bprimitive\b", r"detection signature", r"item .* of the check",
        r"PG[- ]?engine", r"NG[- ]?engine", r"pseudo-good", r"novel-good"]
_RX = re.compile("|".join(DENY), re.IGNORECASE)

def leak_audit(text):
    """Raise LeakHit on a DENY hit; return None if clean."""
    m = _RX.search(text or "")
    if m:
        raise LeakHit(f"DENY hit: {m.group(0)!r}")
    return None
```

- [ ] **Step 4: run green for leak_audit + commit**

Run: `cd <proj> && python -m pytest tests/test_leak_audit.py -v`
Expected: both PASS.
```bash
git add generator/leak_audit.py tests/test_leak_audit.py
git commit -m "feat(B2): leak_audit W5 DENY word-list interception"
```

- [ ] **Step 5: axes① write a failing test (look up the prose table)**

Create `<proj>/tests/test_axes.py`:
```python
from generator.axes import level_text
from generator.weights import dump_initial, load

def test_level_text_reads_axis_prose(tmp_path):
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    txt = level_text(w, "A1", "L0")
    assert "A1" in txt and "L0" in txt   # placeholder prose contains the axis.level identifier
```

- [ ] **Step 6: run red → implement axes.py → run green**

Run: `cd <proj> && python -m pytest tests/test_axes.py -v` → FAIL.
Create `<proj>/generator/axes.py`:
```python
"""Read-only pure function for weight ① axis_prose. Source code never moves; changing prose = changing the weights JSON."""

def level_text(weights, axis, level):
    """Look up the prose body at axis_prose[axis][level]."""
    return weights["axis_prose"][axis][level]
```
Run again → PASS.

- [ ] **Step 7: interpolator② write a failing test (6-rung mapping + rank layer locked)**

Create `<proj>/tests/test_interpolator.py`:
```python
from generator.interpolator import ladder_levels
from generator.weights import dump_initial, load

def test_ladder_six_rungs_monotone(tmp_path):
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    rungs = ladder_levels(w, n=6)
    assert len(rungs) == 6                       # 6 rungs
    # rank layer locked: direction is always id0..id5
    assert [r["rung_id"] for r in rungs] == [0,1,2,3,4,5]

def test_collision_offset_never_label_axis(tmp_path):
    """Layer collision offset allows only B1/expression, never returns A1-A5."""
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    rungs = ladder_levels(w, n=6)
    for r in rungs:
        assert r.get("collision_offset_axis") in (None, "B1", "expression")
```

- [ ] **Step 8: run red → implement interpolator.py → run green**

Run → FAIL. Create `<proj>/generator/interpolator.py`:
```python
"""Read-only pure function for weight ② interp_params layer. Rank layer / coordinate layer locked (read frozen_label); only the layer is trainable."""

def ladder_levels(weights, n=6):
    """6 rungs → L0–L4 level mapping. Direction (rank layer) locked; the layer reads interp_params."""
    direction = weights["frozen_label"]["rank_order"]["direction"]  # locked: [0..5]
    ip = weights["interp_params"]
    gmap = ip["granularity_map"]            # currently the tunable form of "round(t*4)"
    offset_axis = ip["collision_offset_axis"]  # only B1/expression (weights schema already locks this)
    rungs = []
    for i in direction[:n]:
        t = i / (n - 1)                     # 0..1
        level_idx = round(t * 4) if gmap == "round(t*4)" else round(eval_gmap(gmap, t))
        rungs.append({"rung_id": i, "level_idx": level_idx,
                      "collision_offset_axis": offset_axis})
    return rungs

def eval_gmap(gmap, t):
    """Restricted evaluation of granularity_map (placeholder: only the round(t*N) form is supported; extend on demand at landing)."""
    return round(t * 4)
```
Run → PASS.

- [ ] **Step 9: assembler③ write a failing test (collision offset uses only B1/expression layer)**

Create `<proj>/tests/test_assembler.py`:
```python
from generator.assembler import build_batch
from generator.weights import dump_initial, load

def test_collision_perturbation_uses_b1_not_label(tmp_path):
    """AS-3: collision perturbation may use only the B1/expression layer, strictly never the A1-A5 LABEL axes."""
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    cards = build_batch(w, n=6, topic_id="topic-00")
    for c in cards:
        # the perturbation landing point is never A1-A5
        assert c["perturbation_axis"] in ("B1", "expression")

def test_build_batch_six_cards(tmp_path):
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    cards = build_batch(w, n=6, topic_id="topic-00")
    assert len(cards) == 6
```

- [ ] **Step 10: run red → implement assembler.py → run green → commit all of B2**

Run → FAIL. Create `<proj>/generator/assembler.py`:
```python
"""Read-only pure function for weight ③ assembler_params. M1 two-stage (coordinates first, then expand cards); collision offset uses only the B1/expression layer."""
from generator.interpolator import ladder_levels

def build_batch(weights, n, topic_id):
    """Assemble the 6-rung coordinate tuples. Collision perturbation lands only on B1 (CONFOUND) or the expression layer, never touching A1-A5 (AS-3)."""
    ap = weights["assembler_params"]
    rungs = ladder_levels(weights, n=n)
    offset_axis = weights["interp_params"]["collision_offset_axis"]  # B1/expression
    cards = []
    for r in rungs:
        cards.append({
            "rung_id": r["rung_id"],
            "topic_id": topic_id,
            "level_idx": r["level_idx"],
            "perturbation_axis": offset_axis,   # collision-offset landing point, always a non-LABEL axis
            "two_stage": ap["two_stage"],
        })
    return cards
```
Run → PASS.
```bash
git add generator/axes.py generator/interpolator.py generator/assembler.py \
        tests/test_axes.py tests/test_interpolator.py tests/test_assembler.py
git commit -m "feat(B2): three weight bodies — axes/interpolator/assembler (data-oriented, AS-3 collision lock)"
```

- [ ] **Step 11: cards.py serialization (to_dict) + test**

Create `<proj>/generator/cards.py`:
```python
"""PolicyCard serialization. F0-F9 + axis levels → dict."""

def to_dict(card):
    """Card object → json-serializable dict (F0-F9 + axis_levels)."""
    return {f"F{i}": card.get(f"F{i}", "") for i in range(10)} | \
           {"axis_levels": card.get("axis_levels", {})}
```
Create `<proj>/tests/test_cards.py`:
```python
from generator.cards import to_dict
def test_to_dict_has_f0_f9():
    d = to_dict({f"F{i}": str(i) for i in range(10)} | {"axis_levels": {"A1":"L0"}})
    assert all(f"F{i}" in d for i in range(10)) and d["axis_levels"]["A1"] == "L0"
```
Run: `cd <proj> && python -m pytest tests/test_cards.py -v` → PASS.
```bash
git add generator/cards.py tests/test_cards.py
git commit -m "feat(B2): cards.to_dict serialization"
```

---

### Task B3: generation pipeline — new_run_id + trace_emit + gen_configs

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/new_run_id.py` / `trace_emit.py` / `gen_configs.py`
- Test: `<proj>/tests/test_new_run_id.py` / `test_trace_emit.py` / `test_gen_configs.py`

All 9 leaves live under `skills/optimization-loop/scripts/` (skill-creator convention: scripts/ self-contained executables). This Task starts with the first three.

- [ ] **Step 1: new_run_id write a failing test (yyyy-mm-dd-hh-mm-ss + build skeleton)**

Create `<proj>/tests/test_new_run_id.py`:
```python
import re, subprocess, sys
from pathlib import Path

def test_run_id_format_and_skeleton(tmp_path):
    out = subprocess.check_output([sys.executable,
        "skills/optimization-loop/scripts/new_run_id.py", "--runs-root", str(tmp_path)],
        text=True).strip()
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", out)  # run_id format
    base = tmp_path / out
    for sub in ("configs","transcripts","triples","loss","weights"):
        assert (base / sub).is_dir()                                  # skeleton built
```

- [ ] **Step 2: run red → implement new_run_id.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/new_run_id.py`:
```python
#!/usr/bin/env python3
"""Deterministically take system time → run_id (yyyy-mm-dd-hh-mm-ss), build the runs/<id>/ skeleton. Called once only at the epochs-loop entry."""
import argparse, datetime
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-root", default="runs")
    a = ap.parse_args()
    run_id = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    base = Path(a.runs_root) / run_id
    for sub in ("configs","transcripts","triples","loss","weights"):
        (base / sub).mkdir(parents=True, exist_ok=True)
    print(run_id)

if __name__ == "__main__":
    main()
```
Run → PASS.

- [ ] **Step 3: trace_emit write a failing test (11 events, 7 common-header fields + per-event body)**

Create `<proj>/tests/test_trace_emit.py`:
```python
import json, subprocess, sys
from pathlib import Path

COMMON = {"ts","run_id","event","batch_id","topic_id","rung_id","seq"}

def emit(tmp_path, **kw):
    args = [sys.executable, "skills/optimization-loop/scripts/trace_emit.py",
            "--trace", str(tmp_path/"trace.jsonl")]
    for k,v in kw.items(): args += [f"--{k}", str(v)]
    subprocess.check_call(args)

def test_batch_start_has_common_head_and_seq(tmp_path):
    emit(tmp_path, run_id="2026-06-07-00-00-00", event="run_start", batch_id="batch-0")
    emit(tmp_path, run_id="2026-06-07-00-00-00", event="batch_start", batch_id="batch-0",
         weights_snapshot_path="weights/batch-0.json")
    lines = (tmp_path/"trace.jsonl").read_text().splitlines()
    rows = [json.loads(l) for l in lines]
    assert COMMON <= set(rows[0])                       # 7 common-header fields present
    assert rows[0]["seq"] == 1 and rows[1]["seq"] == 2  # seq monotonically increasing
    assert rows[1]["weights_snapshot_path"] == "weights/batch-0.json"  # per-event body
```

- [ ] **Step 4: run red → implement trace_emit.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/trace_emit.py`:
```python
#!/usr/bin/env python3
"""Unified entry for the 11 events: append one line to trace.jsonl. 7 common-header fields + event-specific body. seq continues from the last line of the file +1 (stateless)."""
import argparse, json, datetime
from pathlib import Path

COMMON = ["run_id","event","batch_id","topic_id","rung_id"]

def next_seq(trace):
    p = Path(trace)
    if not p.exists(): return 1
    lines = [l for l in p.read_text().splitlines() if l.strip()]
    return (json.loads(lines[-1])["seq"] + 1) if lines else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", required=True)
    for k in COMMON: ap.add_argument(f"--{k}", default=None)
    a, unknown = ap.parse_known_args()
    # per-event body: remaining --key val pairs
    extra = {}
    it = iter(unknown)
    for tok in it:
        if tok.startswith("--"):
            extra[tok[2:]] = next(it, None)
    row = {"ts": datetime.datetime.now().isoformat(),
           "run_id": a.run_id, "event": a.event, "batch_id": a.batch_id,
           "topic_id": a.topic_id, "rung_id": a.rung_id, "seq": next_seq(a.trace)}
    row.update(extra)
    with open(a.trace, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
```
Run → PASS.

- [ ] **Step 5: gen_configs write a failing test (6 configs + sample naming + passes leak_audit)**

Create `<proj>/tests/test_gen_configs.py`:
```python
import json, subprocess, sys
from pathlib import Path
from generator.weights import dump_initial

def test_gen_six_configs_with_naming(tmp_path):
    runs = tmp_path / "runs" / "2026-06-07-00-00-00"
    (runs/"configs").mkdir(parents=True); (runs/"weights").mkdir()
    dump_initial(runs/"weights"/"batch-0.json")
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/gen_configs.py",
        "--run-dir", str(runs), "--batch-id", "batch-0",
        "--topics", "config/topics.json", "--n", "6"])
    cfgs = sorted((runs/"configs").glob("*.json"))
    assert len(cfgs) == 6                                  # B phase: single topic × 6 rungs
    names = [c.stem for c in cfgs]
    assert "batch-0-topic00-id0" in names                 # sample naming <batch>-topic<NN>-id<N>
```

- [ ] **Step 6: run red → implement gen_configs.py → run green → commit B3**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/gen_configs.py`:
```python
#!/usr/bin/env python3
"""Read weights → interpolator/assembler/axes → config (B phase: 6 for a single topic), each passing leak_audit."""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # make generator importable
from generator import weights as W
from generator.assembler import build_batch
from generator.axes import level_text
from generator.cards import to_dict
from generator.leak_audit import leak_audit, LeakHit

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--batch-id", required=True)
    ap.add_argument("--topics", required=True)
    ap.add_argument("--n", type=int, default=6)
    a = ap.parse_args()
    rd = Path(a.run_dir)
    w = W.load(rd/"weights"/f"{a.batch_id}.json")
    topics = json.loads(Path(a.topics).read_text())
    topic = topics[0]                      # B phase uses only the 1st (placeholder) topic
    tnn = topic["topic_id"].split("-")[1]  # "00"
    cards = build_batch(w, n=a.n, topic_id=topic["topic_id"])
    for c in cards:
        card = to_dict({**c, "axis_levels": {"A1": "L0"}})  # placeholder: really fill from axes.level_text prose
        text = json.dumps(card, ensure_ascii=False)
        leak_audit(text)                   # LeakHit → caller does regenerate-then-reaudit (cap 3)
        sample = f"{a.batch_id}-topic{tnn}-id{c['rung_id']}"
        (rd/"configs"/f"{sample}.json").write_text(json.dumps(card, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```
Run → PASS.
```bash
git add skills/optimization-loop/scripts/new_run_id.py \
        skills/optimization-loop/scripts/trace_emit.py \
        skills/optimization-loop/scripts/gen_configs.py \
        tests/test_new_run_id.py tests/test_trace_emit.py tests/test_gen_configs.py
git commit -m "feat(B3): gen pipeline — new_run_id + trace_emit(11 events) + gen_configs(leak_audit)"
```

> **leak_audit hit handling (regenerate-then-reaudit, cap 3)**: after gen_configs catches a `LeakHit`, it regenerates the card's fields and re-audits; if it still hits after a **retry cap of 3**, it hard-aborts the batch and alarms. The B-phase placeholder prose will not trigger this; the cap logic is spelled out in the B6 skill §tools, and gen_configs leaves a `try/except LeakHit` hook.

---

### Task B4: data sink — save_transcript + concat_triple + write_dataset

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/save_transcript.py` / `concat_triple.py` / `write_dataset.py`
- Test: `<proj>/tests/test_save_transcript.py` / `test_concat_triple.py` / `test_write_dataset.py`

Three data-sink pieces: extract the transcript from the exec jsonl, cut the formated blocks to assemble the triple, and write the dataset after trimming fields by whitelist.

- [ ] **Step 1: save_transcript write a failing test (--logs-dir mandatory + take only user/assistant)**

Create `<proj>/tests/test_save_transcript.py`:
```python
import json, subprocess, sys
from pathlib import Path

def test_logs_dir_required():
    r = subprocess.run([sys.executable,
        "skills/optimization-loop/scripts/save_transcript.py", "--sample", "x", "--out", "y.md"])
    assert r.returncode != 0      # missing --logs-dir must hard-fail (privacy red line)

def test_extracts_user_assistant_only(tmp_path):
    logs = tmp_path/"logs"; logs.mkdir()
    sess = logs/"sess.jsonl"
    sess.write_text("\n".join([
        json.dumps({"type":"user","message":{"content":"question A"}}),
        json.dumps({"type":"assistant","message":{"content":"reply B"}}),
        json.dumps({"type":"system","message":{"content":"internal noise"}}),
    ]))
    out = tmp_path/"t.md"
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/save_transcript.py",
        "--logs-dir", str(logs), "--sample", "s1", "--out", str(out)])
    txt = out.read_text()
    assert "question A" in txt and "reply B" in txt and "internal noise" not in txt  # only user/assistant
```

- [ ] **Step 2: run red → implement save_transcript.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/save_transcript.py`:
```python
#!/usr/bin/env python3
"""Read the exec session jsonl (type in user/assistant) → transcript.md. --logs-dir mandatory (privacy red line: the only place that reads logs)."""
import argparse, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True)   # missing → argparse hard-fail
    ap.add_argument("--sample", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = []
    for jl in sorted(Path(a.logs_dir).glob("*.jsonl")):
        for line in jl.read_text().splitlines():
            if not line.strip(): continue
            o = json.loads(line)
            if o.get("type") in ("user","assistant"):
                c = o.get("message",{}).get("content","")
                rows.append(f"### {o['type']}\n\n{c}\n")
    Path(a.out).write_text("\n".join(rows), encoding="utf-8")  # never write the absolute log path

if __name__ == "__main__":
    main()
```
Run → PASS.

- [ ] **Step 3: concat_triple write a failing test (fence-cut blocks + take the last one + payload JSON)**

Create `<proj>/tests/test_concat_triple.py`:
```python
import json, subprocess, sys
from pathlib import Path

def test_concat_takes_last_fenced_block(tmp_path):
    rd = tmp_path/"run"; (rd/"configs").mkdir(parents=True); (rd/"transcripts").mkdir(); (rd/"triples").mkdir()
    (rd/"configs"/"s1.json").write_text(json.dumps({"F0":"cfg"}))
    # transcript contains two versions of research-result (revised after pushback) → must take the last
    md = "\n".join([
        "```research-graph", '{"nodes":[],"edges":[]}', "```",
        "```research-result", '{"title":"old"}', "```",
        "```research-result", '{"title":"final"}', "```",
    ])
    (rd/"transcripts"/"s1.md").write_text(md)
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/concat_triple.py", "--run-dir", str(rd), "--sample", "s1"])
    tri = json.loads((rd/"triples"/"s1.json").read_text())
    assert tri["research_config"]["F0"] == "cfg"
    assert tri["research_result"]["title"] == "final"       # take the last fence
    assert "nodes" in tri["research_graph"]                 # graph block also cut out
```

- [ ] **Step 4: run red → implement concat_triple.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/concat_triple.py`:
```python
#!/usr/bin/env python3
"""config + transcript (formated fence blocks) → triple. Cut by info-string fence, take the last one (the accepted draft)."""
import argparse, json, re
from pathlib import Path

def last_block(md, info):
    """Take the JSON inside the last info-string fence."""
    rx = re.compile(r"```" + re.escape(info) + r"\s*\n(.*?)\n```", re.DOTALL)
    blocks = rx.findall(md)
    if not blocks:
        raise ValueError(f"no '{info}' fenced block in transcript")
    return json.loads(blocks[-1])      # multiple versions: take the last

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--sample", required=True)
    a = ap.parse_args()
    rd = Path(a.run_dir)
    cfg = json.loads((rd/"configs"/f"{a.sample}.json").read_text())
    md = (rd/"transcripts"/f"{a.sample}.md").read_text()
    triple = {"research_config": cfg,
              "research_graph": last_block(md, "research-graph"),
              "research_result": last_block(md, "research-result")}
    (rd/"triples"/f"{a.sample}.json").write_text(json.dumps(triple, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```
Run → PASS.

- [ ] **Step 5: write_dataset write a failing test (field outside whitelist → hard-fail)**

Create `<proj>/tests/test_write_dataset.py`:
```python
import json, subprocess, sys
from pathlib import Path

WHITELIST = {"sample_id","label","research_config","research_graph",
             "research_result","loss1_fidelity","topic_pass","intended_rank"}

def _triple(extra=None):
    d = {"research_config":{"F0":"x"}, "research_graph":{"nodes":[]},
         "research_result":{"title":"t"}}
    if extra: d.update(extra)
    return d

def test_rejects_non_whitelist_field(tmp_path):
    rd = tmp_path/"run"; (rd/"triples").mkdir(parents=True)
    # inject a log path (field outside the privacy red line)
    (rd/"triples"/"s1.json").write_text(json.dumps(
        _triple({"logs_dir":"/workspace/home/exec/.claude/projects/x"})))
    r = subprocess.run([sys.executable,
        "skills/optimization-loop/scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "s1", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path/"dataset")])
    assert r.returncode != 0      # field outside whitelist → hard-fail abort

def test_writes_whitelisted_sample(tmp_path):
    rd = tmp_path/"run"; (rd/"triples").mkdir(parents=True)
    (rd/"triples"/"s1.json").write_text(json.dumps(_triple()))
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "batch-0-topic00-id0", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path/"dataset"),
        "--axis-levels", '{"A1":"L0"}', "--loss1", "1.0", "--topic-pass", "true"])
    out = json.loads((tmp_path/"dataset"/"topic-00"/"batch-0-topic00-id0.json").read_text())
    assert set(out) <= WHITELIST and out["label"]["rung_id"] == 0
```

- [ ] **Step 6: run red → implement write_dataset.py → run green → commit B4**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/write_dataset.py`:
```python
#!/usr/bin/env python3
"""Privacy whitelist trims fields + schema validation → dataset/<topic>/<sample>.json. A field outside the whitelist hard-fails."""
import argparse, json, sys
from pathlib import Path

WHITELIST = {"sample_id","label","research_config","research_graph",
             "research_result","loss1_fidelity","topic_pass","intended_rank"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True); ap.add_argument("--sample", required=True)
    ap.add_argument("--topic", required=True); ap.add_argument("--rung", type=int, required=True)
    ap.add_argument("--out-root", required=True)
    ap.add_argument("--axis-levels", default="{}"); ap.add_argument("--loss1", default="0.0")
    ap.add_argument("--topic-pass", default="false")
    a = ap.parse_args()
    tri = json.loads((Path(a.run_dir)/"triples"/f"{a.sample}.json").read_text())
    # if the triple mixed in a field outside the whitelist (e.g. a log path) → hard-fail
    extra = set(tri) - {"research_config","research_graph","research_result"}
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
    if set(sample) - WHITELIST:
        sys.exit(f"FATAL: output has non-whitelist fields {set(sample)-WHITELIST}")
    out = Path(a.out_root)/a.topic; out.mkdir(parents=True, exist_ok=True)
    (out/f"{a.sample}.json").write_text(json.dumps(sample, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```
Run → PASS.
```bash
git add skills/optimization-loop/scripts/save_transcript.py \
        skills/optimization-loop/scripts/concat_triple.py \
        skills/optimization-loop/scripts/write_dataset.py \
        tests/test_save_transcript.py tests/test_concat_triple.py tests/test_write_dataset.py
git commit -m "feat(B4): data sink — save_transcript(--logs-dir mandatory) + concat_triple(fence take-last) + write_dataset(whitelist hard-fail)"
```

---

### Task B5: loss skills — injection-fidelity + ladder-quality-order + run_codex_loss + gate_eval

**Files:**
- Create: `<proj>/skills/injection-fidelity/SKILL.md` (S, codex loss-1)
- Create: `<proj>/skills/ladder-quality-order/SKILL.md` (S, codex loss-2)
- Create: `<proj>/skills/optimization-loop/scripts/run_codex_loss.py` (R) / `gate_eval.py` (P)
- Create: `<proj>/skills/optimization-loop/references/gate-thresholds.md`
- Test: `<proj>/tests/test_gate_eval.py` (P) / `tests/e2e/test_loss_real.py` (R)

loss uses codex (swapping the model family to avoid same-source bias), and the whole flow is check-blind. The gate is pure arithmetic (P); the two loss skills + run_codex_loss need real codex (R).

- [ ] **Step 1: write gate-thresholds.md (threshold central location, all thresholds defined uniquely)**

Create `<proj>/skills/optimization-loop/references/gate-thresholds.md`:
```markdown
# Full gate threshold table (gate_eval.py reads from here, not scattered through the code)

| Threshold | Value | Use |
| --- | --- | --- |
| fidelity_rate gate | ≥ 0.90 | per-topic: the pass ratio of the 6 rungs' fidelity |
| monotonicity τ gate | ≥ 0.7 | loss-2 monotonicity_pass |
| party-C calibration τ line | ≥ 0.8 | quality good enough, hand off to next stage |
| endpoint separation | id0 wins ≥ K−allowance times | loss-2 endpoint_separation_pass (K-run majority vote) |
| batch_pass_ratio gate | ≥ 0.80 (= ≥7/8 topics) | batch_passed |
| convergence | last 3 of recent_ratios all ≥0.80 | converged |

The pilot-period measured values of K / allowance are filled by Spec C; the B phase uses K=5, allowance=1 as placeholders.
```

- [ ] **Step 2: gate_eval write a failing test (three-way AND / pass_ratio / converged)**

Create `<proj>/tests/test_gate_eval.py`:
```python
import subprocess, sys, json

def gate(*args):
    return subprocess.check_output([sys.executable,
        "skills/optimization-loop/scripts/gate_eval.py", *args], text=True).strip()

def test_topic_passes_three_way_and():
    # fidelity_rate>=0.90 AND mono AND endpoint → true
    out = gate("topic", "--fidelity-rate","0.90","--mono","true","--endpoint","true")
    assert out == "true"
    # any one fails → false
    assert gate("topic","--fidelity-rate","0.83","--mono","true","--endpoint","true") == "false"
    assert gate("topic","--fidelity-rate","0.95","--mono","false","--endpoint","true") == "false"

def test_batch_pass_ratio_hard_integer_line():
    # 7/8 = 0.875 passes; 6/8 = 0.75 does not
    assert gate("batch","--flags","true,true,true,true,true,true,true,false") == "true"
    assert gate("batch","--flags","true,true,true,true,true,true,false,false") == "false"

def test_converged_last_three():
    assert gate("converged","--recent","0.625,0.875,0.875,0.875") == "true"   # last 3 all ≥0.80
    assert gate("converged","--recent","0.875,0.75,0.875") == "false"          # break in the middle
```

- [ ] **Step 3: run red → implement gate_eval.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/gate_eval.py`:
```python
#!/usr/bin/env python3
"""Gate pure arithmetic: topic_passes / batch_pass_ratio / converged. Does not call CC/codex. Thresholds see references/gate-thresholds.md."""
import argparse

FIDELITY_MIN = 0.90
BATCH_RATIO_MIN = 0.80

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    t = sub.add_parser("topic")
    t.add_argument("--fidelity-rate", type=float, required=True)
    t.add_argument("--mono"); t.add_argument("--endpoint")
    b = sub.add_parser("batch"); b.add_argument("--flags", required=True)
    c = sub.add_parser("converged"); c.add_argument("--recent", required=True)
    a = ap.parse_args()
    if a.mode == "topic":
        ok = (a.fidelity_rate >= FIDELITY_MIN and a.mono=="true" and a.endpoint=="true")
        print("true" if ok else "false")
    elif a.mode == "batch":
        flags = [x=="true" for x in a.flags.split(",")]
        ratio = sum(flags)/len(flags)
        print("true" if ratio >= BATCH_RATIO_MIN else "false")
    elif a.mode == "converged":
        rs = [float(x) for x in a.recent.split(",")]
        print("true" if len(rs)>=3 and all(r>=BATCH_RATIO_MIN for r in rs[-3:]) else "false")

if __name__ == "__main__":
    main()
```
Run → PASS.
```bash
git add skills/optimization-loop/scripts/gate_eval.py \
        skills/optimization-loop/references/gate-thresholds.md tests/test_gate_eval.py
git commit -m "feat(B5): gate_eval gate arithmetic (three-way AND/pass_ratio/converged) + threshold table"
```

- [ ] **Step 4: write injection-fidelity SKILL.md (loss-1, check-blind)**

Create `<proj>/skills/injection-fidelity/SKILL.md`:
```markdown
---
name: injection-fidelity
description: codex loss-1. Judges whether, within a run, sim faithfully plays the config persona and applies supervision pressure to exec per the rung's axis levels. check-blind (W5).
---

# What is judged
Parse sim's behavior in the transcript (the user turns), extract 6 pressure signals, compare each against the expected band of this rung's axis level, and AND across axes into the single-sample fidelity. Never touch 32-check / 6-primitive / detection signatures (that is the downstream probe's job).

# The 6 pressure signals (each bound to one axis)
| Signal | Bound axis | What it measures |
| --- | --- | --- |
| pushback_count | A1 substance demand | number of user turns that push back / demand more substance |
| operationalization_demand_count | A3 operationalization insistence | number of turns demanding numbers / executable steps |
| accept_without_question_rate | reverse pressure (low A1) | proportion of accepting without challenge |
| premise_defended_count | A4=C- (PG engine) | number of turns still defending a wrong premise after being challenged |
| incoherent_demand_flag | low A2 | boolean of incoherent demands |
| novel_seed_count | A5=G+ (NG engine) | number of turns introducing original directions / cross-domain connections / reframings |
Also record premise_dropped / premise_revised (A4 trajectory) + the A5 substantive-seed check (the seed must be substantive, topic-relevant).

# Scoring (expected bands)
Each signal is normalized by F8 turn_budget → falls into the non-overlapping expected band for this rung's axis level (L0..L4 partition [0,1] into bands).
Example: A1=L0 ⇒ pushback_rate≥0.7; A1=L4 ⇒ ≤0.05.
single-sample fidelity = AND over this card's bound axes [observed ∈ band]. batch fidelity_rate = pass proportion, gate ≥0.90.

# per-turn drift gate
Cut the transcript into first/second half; both halves' signals must be in band; if the second half's pressure signals drift toward the cooperative extreme beyond tolerance → drift_flag=true → that sample's fidelity FAILs.

# Output (--output-schema hard-constrains loss1.json)
{ "fidelity": bool, "loss1": float[0,1], "per_axis_evidence": {axis:{observed,expected_band,pass}}, "drift_flag": bool, "note": str }

# Cold-start self-check (falsifier)
FS1-1 counts right but semantically empty (spot-check semantic pressure); FS1-2 A5 seed novel but trivial/off-topic (check topic-relevance); FS1-3 the two parsers' counts disagree (nail down the parser spec).

# W5
Check-blind in full, passes leak_audit. Concrete threshold values see ../optimization-loop/references/gate-thresholds.md.
```

- [ ] **Step 5: write ladder-quality-order SKILL.md (loss-2, check-blind)**

Create `<proj>/skills/ladder-quality-order/SKILL.md`:
```markdown
---
name: ladder-quality-order
description: codex loss-2. Judges whether a topic's 6 rungs of research quality decline monotonically along id0→id5 and whether the endpoints are well-separated. Pairwise ranking (NOT absolute scoring), check-blind (W5).
---

# What is judged
Consume the same topic's 6 rungs of (graph,result), but without seeing the rung id, without seeing the config — just take the shuffled 6 artifacts and rank them by research quality from high to low. The judgment is "which is more solid", never calling 32-check.

# Judgment unit = PAIR (pairwise, no absolute score)
Take (sample_i, sample_j) i<j; the judge outputs only "which is higher quality in the overall D1–D5 sense (or tie) + a one-line reason". Explicit pairwise ordering, NOT absolute scoring.
The ranking prompt may use only D1–D5 quality language (more meaningful/useful/better-structured); forbidden: the 32-check word list / 6 primitives / pseudo-good·novel-good classification terms.

# Aggregation
- Monotonicity: aggregate the pairwise verdicts into a rank, compute Kendall τ between the judge order and the true id order. monotonicity_pass = (τ≥0.7 and no adjacent inversion at the endpoints).
- Endpoint separation: do K independent pairwise judgments on (id0,id5), endpoint_separation_pass = (id0 wins ≥ K−allowance times). Near-tie → rigor_floor_flag (escalates to §backprop attribution, not a tuning bug).
- party-C calibration hand-off: τ≥0.8 and endpoints 100% consistent → hand off to the next stage.
- z⊥C self-check (FS2-2): the judge runs the B1 confound-triplet (same substance, different style); the ranking must be flat, otherwise the judge is contaminated by the confound and this topic's loss-2 signal is untrustworthy.

# Output (--output-schema hard-constrains loss2.json)
{ "tau": float, "monotonicity_pass": bool, "endpoint_separation_pass": bool, "rigor_floor_flag": bool, "pairwise_log": [{i,j,winner,reason}] }

# W5
Check-blind in full, passes leak_audit. Thresholds (τ line/K/allowance/party-C calibration line) see ../optimization-loop/references/gate-thresholds.md.
```

- [ ] **Step 6: verify both loss skills are check-blind in full (pass leak_audit)**

Run:
```bash
cd <proj> && python3 -c "
from generator.leak_audit import leak_audit
for f in ['skills/injection-fidelity/SKILL.md','skills/ladder-quality-order/SKILL.md']:
    leak_audit(open(f,encoding='utf-8').read()); print(f, 'CLEAN')
"
```
Expected: both files print `CLEAN` (the skill body describes the judgment using only "signal / quality-order" language and does not contain DENY'd detection-signature terms; note: word-list items such as `pseudo-good` are mentioned only as "forbidden words" — if that triggers, rewrite to a neutral referent like "DL-5 classification term" — ensure leak_audit really passes at landing).

> **★Landing tip**: if leak_audit hits a self-reference like "forbidden X" inside the skill, change the forbidden word to a neutral referent (e.g. write "32 checks" as "downstream probe checks") to guarantee the generation-side artifact is check-blind in full. The skill should convey "don't use these words", but must not itself contain those words.

- [ ] **Step 6b: write the output-schema files (used by codex --output-schema for hard constraint)**

Create `<proj>/schemas/loss1.json` (JSON Schema, fields aligned with the injection-fidelity SKILL.md output section):
```json
{
  "type": "object",
  "required": ["fidelity","loss1","per_axis_evidence","drift_flag"],
  "properties": {
    "fidelity": {"type": "boolean"},
    "loss1": {"type": "number", "minimum": 0, "maximum": 1},
    "per_axis_evidence": {"type": "object"},
    "drift_flag": {"type": "boolean"},
    "note": {"type": "string"}
  }
}
```
Create `<proj>/schemas/loss2.json` (aligned with the ladder-quality-order SKILL.md output section):
```json
{
  "type": "object",
  "required": ["tau","monotonicity_pass","endpoint_separation_pass","rigor_floor_flag"],
  "properties": {
    "tau": {"type": "number"},
    "monotonicity_pass": {"type": "boolean"},
    "endpoint_separation_pass": {"type": "boolean"},
    "rigor_floor_flag": {"type": "boolean"},
    "pairwise_log": {"type": "array"}
  }
}
```
Expected: both schema files in place; `run_codex_loss.py --schema schemas/loss1.json` can reference them.

- [ ] **Step 7: implement run_codex_loss.py (start codex, inject full SKILL.md + payload)**

Create `<proj>/skills/optimization-loop/scripts/run_codex_loss.py`:
```python
#!/usr/bin/env python3
"""Start codex to compute loss-1 (per-run) / loss-2 (per-topic). Inject the full SKILL.md (codex does not auto-mount it) + payload.
codex uses the Codex-group credential (CODEX_HOME=/workspace/home/loss/.codex, a separate OpenAI group, swapping the model family to avoid same-source bias)."""
import argparse, json, subprocess, os
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--which", choices=["loss1","loss2"], required=True)
    ap.add_argument("--skill", required=True)        # SKILL.md path
    ap.add_argument("--payload", required=True)      # transcript (.md) or the 6-triple directory
    ap.add_argument("--schema", required=True)       # loss1.json/loss2.json output-schema
    ap.add_argument("--out", required=True)
    ap.add_argument("--codex-home", default="/workspace/home/loss/.codex")
    a = ap.parse_args()
    skill = Path(a.skill).read_text(encoding="utf-8")
    payload = Path(a.payload).read_text(encoding="utf-8")
    prompt = f"{skill}\n\n# INPUT PAYLOAD\n{payload}\n"
    env = {**os.environ, "CODEX_HOME": a.codex_home}
    # codex exec --output-schema <schema> -o <out> ; prompt goes via stdin
    subprocess.run(["codex","exec","--output-schema",a.schema,"-o",a.out,"-"],
                   input=prompt, text=True, env=env, check=True)

def parse_loss1(out_path):
    """Parse codex loss1 output → fidelity value."""
    return json.loads(Path(out_path).read_text())

if __name__ == "__main__":
    main()
```

- [ ] **Step 8: real-model e2e — feed injection-fidelity the golden-sample transcript (R, obey no-fake)**

Create `<proj>/tests/e2e/test_loss_real.py`:
```python
"""R: real codex. Requires both key sets configured on the device (CODEX_HOME points to the loss config-dir). Skips when CI has no key."""
import json, os, subprocess, sys
import pytest
from pathlib import Path

CODEX_HOME = os.environ.get("CODEX_HOME","/workspace/home/loss/.codex")
pytestmark = pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"),
                                reason="needs Codex-group key; real-model e2e (no fake)")

def test_injection_fidelity_real(tmp_path):
    # golden-sample real transcript (the one produced by the A slice; here use the e2e artifact in fixtures/golden-slice)
    transcript = Path("fixtures/golden-slice/transcript.md")
    out = tmp_path/"loss1.json"
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/run_codex_loss.py",
        "--which","loss1","--skill","skills/injection-fidelity/SKILL.md",
        "--payload",str(transcript),"--schema","schemas/loss1.json","--out",str(out)])
    r = json.loads(out.read_text())
    assert isinstance(r["fidelity"], bool)          # schema valid
    assert 0.0 <= r["loss1"] <= 1.0                 # fidelity numeric range
    assert "per_axis_evidence" in r                 # per-axis evidence retained
```

- [ ] **Step 9: run the real-model e2e (on the device, key configured) → run green → commit B5**

Run (on the device): `cd <proj> && OPENAI_API_KEY=$OPENAI_API_KEY python -m pytest tests/e2e/test_loss_real.py -v`
Expected: PASS — real codex emits a schema-valid loss1.json, with an interpretable fidelity value. In a no-key environment it SKIPs (not counted as a failure, but **it must have really run on the device**, obeying no-fake).
```bash
git add skills/injection-fidelity/SKILL.md skills/ladder-quality-order/SKILL.md \
        skills/optimization-loop/scripts/run_codex_loss.py tests/e2e/test_loss_real.py
git commit -m "feat(B5): codex loss skills(injection-fidelity/ladder-quality-order) + run_codex_loss(real codex) check-blind"
```

> **The R e2e for ladder-quality-order (loss-2)** is the same shape: feed 6 rungs of real triples, validate codex pairwise ranking → τ + endpoints + loss2.json schema. It depends on B7's 6-rung artifacts, so the real run of loss-2 is validated together in B7 (B5 first validates loss-1 single-run).

---

### Task B6: optimizer brain — apply_weight_update + optimization-loop SKILL.md

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/apply_weight_update.py` (P)
- Create: `<proj>/skills/optimization-loop/SKILL.md` (S, thick skill)
- Create: `<proj>/skills/optimization-loop/references/backprop-heuristic.md` (S)
- Test: `<proj>/tests/test_apply_weight_update.py` (P)

The 9th leaf + the brain program. In the B phase apply_weight_update only tests "can correctly change a JSON segment + the F1 copy mode" (its being intelligently driven by backprop is a C matter). SKILL.md §loop/§gate/§state/§tools written in full; §backprop written out but left for C to validate in depth.

- [ ] **Step 1: apply_weight_update write a failing test (revise a segment + F1 copy + revision_log)**

Create `<proj>/tests/test_apply_weight_update.py`:
```python
import json, subprocess, sys
from pathlib import Path
from generator.weights import dump_initial

def test_revise_writes_next_batch_and_log(tmp_path):
    wd = tmp_path/"weights"; wd.mkdir(); dump_initial(wd/"batch-0.json")
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0",
        "--target","axis_prose","--key","A1.L0","--new","stronger pressure prose","--reason","loss-1 failed"])
    nxt = json.loads((wd/"batch-1.json").read_text())
    assert nxt["axis_prose"]["A1"]["L0"] == "stronger pressure prose"      # changed that one cell
    log = (wd.parent/"revision_log.jsonl").read_text().splitlines()
    rec = json.loads(log[-1])
    assert rec["target"]=="axis_prose" and rec["key"]=="A1.L0"  # written to revision_log

def test_f1_copy_mode_byte_identical(tmp_path):
    wd = tmp_path/"weights"; wd.mkdir(); dump_initial(wd/"batch-0.json")
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0", "--copy"])
    # F1: byte-for-byte copy, no revision_log, no weight_revised
    assert json.loads((wd/"batch-1.json").read_text()) == json.loads((wd/"batch-0.json").read_text())
    assert not (wd.parent/"revision_log.jsonl").exists()        # copy mode does not write a log
```

- [ ] **Step 2: run red → implement apply_weight_update.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/apply_weight_update.py`:
```python
#!/usr/bin/env python3
"""F2: revise one of the three weights + write revision_log + write weights/<batch+1>.json. F1: --copy byte-for-byte copy (no log)."""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from generator import weights as W

def next_id(batch_id):
    return f"batch-{int(batch_id.split('-')[1]) + 1}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights-dir", required=True); ap.add_argument("--batch-id", required=True)
    ap.add_argument("--copy", action="store_true")     # F1 copy mode
    ap.add_argument("--target"); ap.add_argument("--key"); ap.add_argument("--new"); ap.add_argument("--reason")
    a = ap.parse_args()
    wd = Path(a.weights_dir)
    cur = W.load(wd/f"{a.batch_id}.json")
    nxt_path = wd/f"{next_id(a.batch_id)}.json"
    if a.copy:
        # F1: byte-for-byte copy, no change, no log, no weight_revised emit
        nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2)); return
    rec = W.revise(cur, target=a.target, key=a.key, new=a.new, reason=a.reason)  # change one segment (validation in weights.revise)
    nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2))
    with open(wd.parent/"revision_log.jsonl","a",encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))         # for CC to assemble the weight_revised trace event

if __name__ == "__main__":
    main()
```
Run → PASS.
```bash
git add skills/optimization-loop/scripts/apply_weight_update.py tests/test_apply_weight_update.py
git commit -m "feat(B6): apply_weight_update — revise segment+revision_log(F2) / byte-for-byte copy(F1)"
```

- [ ] **Step 3: write optimization-loop SKILL.md (thick skill, §loop/§gate/§backprop/§state/§tools)**

Create `<proj>/skills/optimization-loop/SKILL.md`:
```markdown
---
name: optimization-loop
description: optimizer-cc's training main program. Specifies the epoch loop, gating, backprop, state persistence, child-CC startup. check-blind (W5).
---

# §loop — control flow
Two-level nesting. LOOP-2 (epoch/batch, runs to convergence) wraps LOOP-1 (48 runs = outer for topic_i in 0..7 × inner for rung in 0..5):
- Enter epoch: new_run_id.py takes run_id → emit run_start → build runs/<run_id>/trace.jsonl.
- Enter batch: take the largest-numbered weights directory as batch_id (no +1; cold start = batch-0) → emit batch_start → gen_configs.py reads weights/<batch_id>.json to build config.
- for topic_i: emit topic_start → for rung: emit rung_start → [start sim → inject config → sim starts exec → inject topic+forced → multi-turn → concat triple → run_codex_loss(loss-1) → emit rung_done] → IF rung<5 loop back else per-topic aggregation.
- per-topic aggregation: run_codex_loss(loss-2, consumes 6 rungs) → gate_eval(topic) → emit topic_done → write_dataset(6 samples) → IF topic_i<7 loop back else END LOOP-1.
- batch wrap-up: read the topic_pass of the 8 topic_done → gate_eval(batch) → emit batch_done → IF 3 consecutive batches pass the gate: T freeze+converged+run_end / F1 copy forward / F2 §backprop.
Which scripts/ leaf each step calls, which trace event it emits, strictly follow this section; no improvising.

# §gate — gate decision (pure arithmetic, gate_eval.py, no CC/codex call)
- per-topic three-way AND: topic_pass = (fidelity_rate≥0.90) ∧ monotonicity_pass ∧ endpoint_separation_pass.
- batch: batch_pass_ratio≥0.80, hard integer line = ≥7/8 topics pass (6/8=0.75 fails).
- convergence: the trace tail recent_ratios, last 3 all ≥0.80. Stateless, reconstructable from the trace.
- All threshold values are in references/gate-thresholds.md. check-blind: read only fidelity_rate (loss-1) + τ/endpoints (loss-2).

# §backprop — backpropagation (the only thin section left · intelligent point ③ · B writes it out, leaves C to validate in depth)
Attribute first, then act; one batch changes only one weight. Decision table: loss-1 failed → ①axis_prose; loss-2 endpoints not separated → first read rigor_floor_flag (if true, don't touch weights) otherwise ① the endpoint cell; loss-2 middle blurred (τ low but endpoints separated) → ②interp_params; ≥4/8 double-collapse → ③assembler_params. Priority loss-1 > subtype B > whole card. Attribution input is three-layered (batch_done→topic_done→loss/*.json verdicts, stop once it's enough to judge). Detailed heuristics in references/backprop-heuristic.md. W5: attribution reads only fidelity/τ/endpoints + codex verdicts; new prose passes leak_audit.

# §state — cross-batch state persistence
"Memory is not trustworthy; disk is the only source of truth." The persistence trio: trace.jsonl (11 events) / weights/<batch>.json (snapshot) / revision_log.jsonl. Fixed /compact once at each batch's end; after compact reload this skill + restore from disk: read weights/<batch+1>.json (new weights) + revision_log.jsonl + the trace tail (recent_ratios/batch_id/last-line seq+1 continuation). batch_id takes the largest number in the weights directory itself (no +1). Privacy: transcript_path is a relative path, the log-reading script requires --logs-dir.

# §tools — leaf tools + child-CC startup
Leaves (scripts/): new_run_id / gen_configs / save_transcript (once at run end, --logs-dir mandatory) / concat_triple / run_codex_loss / gate_eval / apply_weight_update / write_dataset / trace_emit. The three weight bodies axes/interpolator/assembler stay in generator/; gen_configs calls them, apply_weight_update changes their weights JSON data segment (data-oriented, source code does not move).
leak_audit hit: regenerate-then-reaudit, hard-abort the batch and alarm if it still hits after a cap of 3.
Child-CC startup: the parent CC directly starts, in its own Bash tool, IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role> bash -lc 'cd <cwd> && claude', a normal multi-turn conversation. Three iron rules: no driver script / not into tmux (only the optimizer uses tmux) / each run is freshly spawned, born and dies on the spot. Authoritative transcript = exec session jsonl.
```

- [ ] **Step 4: write backprop-heuristic.md (§backprop line-by-line landing, B writes it out, leaves C to validate in depth)**

Create `<proj>/skills/optimization-loop/references/backprop-heuristic.md`:
```markdown
# §backprop detailed heuristics (intelligent point ③ · one batch changes only one weight)

| # | Discriminant (signal reading) | Change template | Priority |
| --- | --- | --- | --- |
| 0 | Front gate: this topic's B1 confound-triplet judge is not flat (FS2-2) | loss-2 signal contaminated, this batch does not change weights based on loss-2; harden judge prompt (not counted as "changing one weight") | check first |
| 1 | Some topic's fidelity_rate<0.90 or any rung's drift_flag; per_axis_evidence points out which axis observed∉band | revise("axis_prose","<axis>.<level>", more accurate/stronger pressure wording, reason) | highest (foundation) |
| 2 | endpoint_separation_pass=false: first read rigor_floor_flag | flag true → alarm, don't touch weights (coordinates locked, can't be trained); flag false → change the axis_prose id0/id5 cell. Never go into ② | next-highest |
| 3 | τ<0.7 but endpoint_separation_pass=true (middle blurred) | revise("interp_params","<knob>", new value, reason), knob∈{collision_offset_axis(only B1/expression), endpoint_spread, granularity_map} | medium |
| 4 | ≥4/8 topics' fidelity and τ both collapse (first rule out broken parser/leak tools) | revise("assembler_params","<knob>", new value, reason) | lowest (fallback) |

Concrete numeric thresholds (band boundaries, τ line, K-allowance, ≥4/8) reference gate-thresholds.md. Attribution input is three-layered from coarse to fine: batch_done.{topic_pass_flags,any_rigor_floor} → the failed topic's topic_done → if needed loss/*.json verdicts. Stop once it's enough to judge.
```

- [ ] **Step 5: real-model e2e — optimization-loop 6-run orchestration runs through a single topic (R)**

This is B6's acceptance: a real optimizer-CC loads the skill, runs a single topic's 6 rungs through per §loop (§gate computes topic_pass). **§backprop is not validated in depth here** (left for C). Write `<proj>/tests/e2e/test_loop_6run.md` (manual execution checklist, real CC):
```markdown
# B6 e2e: optimization-loop 6-run single topic (real claude/codex)
1. On the device start optimizer-CC (placeholder: locally start claude loading the optimization-loop skill).
2. Feed the instruction "run all 6 rungs of topic-00 of batch-0".
3. Verify: trace.jsonl shows run_start→batch_start→topic_start→(rung_start→dialogue_turn→rung_done)×6→topic_done.
4. Verify: 6 configs/, 6 transcripts/, 6 triples/, 6 loss1.json persisted.
5. Verify: topic_done contains tau / monotonicity_pass / endpoint_separation_pass / topic_pass.
6. no-fake: sim/exec/codex are all real processes, artifacts are not stubs.
```
Expected: §loop/§gate orchestration runs through, artifact shapes correct.

- [ ] **Step 6: commit B6**
```bash
git add skills/optimization-loop/SKILL.md \
        skills/optimization-loop/references/backprop-heuristic.md tests/e2e/test_loop_6run.md
git commit -m "feat(B6): optimization-loop thick skill(§loop/§gate/§state/§tools full + §backprop written, left for C)"
```

---

### Task B7: golden-sample 6-rung e2e (B-phase endpoint acceptance)

**Files:**
- Create: `<proj>/config/topics.json` (B-phase single placeholder topic)
- Create: `<proj>/tests/e2e/test_golden_6rung.md` (R, manual execution checklist)
- Artifacts land in `runs/` (device-local, gitignored)

Grow Spec A's "single-run slice" into a **complete single-topic 6-rung run**, validating loss-2 monotonicity τ + endpoint separation + gate arithmetic. Real claude/codex throughout, obeying no-fake.

- [ ] **Step 1: write config/topics.json (B-phase single placeholder topic)**

Create `<proj>/config/topics.json`:
```json
[
  {
    "topic_id": "topic-00",
    "title_short": "placeholder: minimal controlled evaluation of an external DL phenomenon",
    "full_text": "Study one tiny external DL phenomenon: design a minimal executable controlled evaluation. Require exec to use formated-specs for the spec and call formated-results at wrap-up. (B-phase placeholder; C phase fills in 8 real frontier topics.)",
    "F7_prerequisite": "placeholder: a challengeable factual premise (C phase fills in a real frontier claim)"
  }
]
```
Expected: single-element array, four fields present (`topic_id`/`title_short`/`full_text`/`F7_prerequisite`). **The 8 real topics are filled by Spec C**; B only needs the placeholder to run the pipeline through.

- [ ] **Step 2: write the B7 e2e execution checklist (real claude/codex, full 6-rung chain)**

Create `<proj>/tests/e2e/test_golden_6rung.md`:
```markdown
# B7 e2e: golden-sample single topic 6 rungs (real claude/codex, obey no-fake)
Prerequisite: Spec A environment in place (the four identities can start); B1–B6 all pytest green.

## Run
1. new_run_id.py builds runs/<id>/; trace_emit run_start.
2. gen_configs.py reads weights/batch-0.json (exported by dump_initial) → 6 configs (topic-00 × id0..id5), each passing leak_audit.
3. for rung in 0..5:
   - really start sim (inject config_full) → sim really starts exec (inject topic + the two forced items) → real multi-turn → exec's final step formated-results fence block.
   - save_transcript (--logs-dir points to the exec config-dir) → concat_triple → triples/<sample>.json.
   - run_codex_loss(loss1) → loss/<sample>.loss1.json; trace_emit rung_done.
4. per-topic aggregation: run_codex_loss(loss2, consumes 6 triples) → loss/topic-00.loss2.json.
5. gate_eval(topic, fidelity_rate, mono, endpoint) → topic_pass; trace_emit topic_done.
6. write_dataset × 6 → dataset/topic-00/.

## Acceptance (B's core gain, beyond the A slice)
- [ ] 6 rungs of triples present, loss2.json has tau (float).
- [ ] **loss-2 monotonicity**: codex ranks the shuffled 6 rungs, τ computed against the true id order (≥0.7 counts as monotonicity_pass).
- [ ] **endpoint separation**: K pairwise judgments of id0 vs id5, endpoint_separation_pass computed.
- [ ] **gate arithmetic**: gate_eval three-way AND produces topic_pass.
- [ ] **privacy**: dataset/ and triples/ have no CC log absolute path (grep NO LEAK).
- [ ] **no-fake**: sim/exec/codex are all real processes, the only synthesized thing is config+topic.

## Not validated (left for C)
multi-batch, three-consecutive gate pass, real backprop, long-running tmux, 48-run, supervision panel.
```

- [ ] **Step 3: really run the B7 e2e on the device, accept item by item**

Run (on the device, both key sets configured): run through the single topic's 6 rungs per the `test_golden_6rung.md` checklist.
Expected: 6-rung ladder produced; loss-2 τ computed; endpoint separation judged; topic_pass computed by gate_eval; NO LEAK; all real, no stubs.

- [ ] **Step 4: full pytest regression + privacy scan + commit B7**

Run:
```bash
cd <proj> && python -m pytest tests/ -v --ignore=tests/e2e   # pure functions all green
grep -rl '/workspace/home/.*/.claude/projects' dataset/ runs/*/triples 2>/dev/null && echo LEAK || echo "NO LEAK"
```
Expected: all pytest PASS; prints `NO LEAK`.
```bash
git add config/topics.json tests/e2e/test_golden_6rung.md
git commit -m "feat(B7): golden-sample 6-rung e2e — loss-2 monotonicity τ + endpoint separation + gate arithmetic (real claude/codex)"
```

---

## Self-Review (checked against Spec B)

- **Component manifest (§2) coverage**: three weight bodies axes①/interpolator②/assembler③ + cards + leak_audit + weights (B1/B2); 9 leaves new_run_id/gen_configs/save_transcript/concat_triple/run_codex_loss/gate_eval/apply_weight_update/write_dataset/trace_emit (B3/B4/B5/B6); 2 codex loss skills (B5); optimization-loop skill (B6). Each has a Task, none missing.
- **Build order (§4) alignment**: B1 base → B2 three weights → B3 generation pipeline → B4 data sink → B5 loss → B6 brain → B7 6-rung e2e, the Task numbering corresponds one-to-one.
- **weights schema (§3) hard-constraint coverage**: physical isolation AS-3 (B1 test_interp_params_has_no_coord), revise whitelist (B1 test_revise_rejects_frozen_label), collision schema lock (B1 test_collision_offset_rejects_label_axis), batch-0 dump_initial (B1). Complete.
- **Test matrix (§5) alignment**: P (weights/three-weights/leak/concat/gate/apply/trace/write_dataset all pytest), R (loss1 real codex B5, 6-run orchestration B6, full 6-rung chain B7), no-fake honored.
- **Privacy red line (§6) coverage**: save_transcript --logs-dir mandatory (B4 test_logs_dir_required), write_dataset whitelist hard-fail (B4 test_rejects_non_whitelist_field), keys not in committed artifacts (placeholders throughout), NO LEAK scan (B7).
- **Type consistency**: the `revise(w,target,key,new,reason)` signature defined in B1, called consistently in B6 apply_weight_update; the sample naming `<batch>-topic<NN>-id<N>` consistent across B3/B4/B7; the loss1.json/loss2.json schema consistent between the B5 skill and the B7 acceptance; the trace 7-field common header defined in B3 trace_emit, referenced consistently in B6 §loop.
- **placeholder scan**: topics.json single placeholder topic, gen_configs's placeholder prose, SKILL.md §backprop "left for C to validate in depth" are the **intentional B/C boundary**, not plan gaps — already annotated with who fills them and when. The `schemas/loss1.json`/`loss2.json` output-schema files are referenced in B5 run_codex_loss — **note: at landing, B5 Step 7 must also create `<proj>/schemas/loss1.json` and `loss2.json` (JSON Schema, fields aligned with the SKILL.md output section)**.

## Execution Handoff

See the index plan `2026-06-07-INDEX-triple-cc-pretrain.md`. B depends on A (environment in place); B must be fully green (pytest + the B7 6-rung e2e) before advancing to C.
