# STAGE 1 Data-Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the data-oriented core of ladder-foundry — the 4-segment weights schema (3 trainable + 1 locked), the three read-only weight bodies, the W5 leak interceptor, and three-layer verification proving the output is correct for the whole system.

**Architecture:** Optimizer trains by editing JSON DATA segments; the `.py` files are PURE READ-ONLY functions whose source never moves. `weights.py` owns the schema + `load`/`dump_initial`/`revise` with all locks. `axes.py`/`interpolator.py`/`assembler.py` each read ONE segment. `frozen_label` (rank_order + coord_table) is locked from `revise`. Verified at three layers: per-component pytest, a cross-step handoff test, and an independent codex audit.

**Tech Stack:** Python 3.12 (stdlib only: `json`, `pathlib`, `dataclasses`, `re`), pytest 9.0.3. No third-party deps.

## Global Constraints

- Build from scratch; inherit NO line of old `probe-pretrain` code.
- Trainable = JSON data only; `.py` source never changes during training (proven by `test_revise_changes_data_not_source`).
- `frozen_label` is NOT trainable: `dump_initial` is its SOLE writer; `revise` rejects it.
- `interp_params` key-set is LOCKED to EXACTLY `{collision_offset_axis, endpoint_spread, granularity_map}` (AS-3 structural lock), validated on `load` AND `revise`.
- `collision_offset_axis ∈ {"B1","expression"}` only — NEVER an A1–A5 label axis.
- `coord_table` is EMPTY `{}` in batch-0; L4/L5 READ coords from it, never compute them; tests use a fixture coord_table and never assert a ladder from an empty table.
- `granularity_map` stores a STRATEGY NAME (string); dict-dispatch in code, NO `eval()`.
- Monotonicity is NONDECREASING not strict: `round(i*4/5)` over rungs `[0..5]` → level indices `[0,1,2,2,3,4]` (collision at level 2).
- STAGE 1 schema scoping decision: all five axes use levels `L0..L4` uniformly; the A4 C+/C- and A5 G+/G- overlay semantics are deferred to STAGE 2 prose authoring.
- Privacy red line: no CC log path in any artifact; no API key values; reference by name only.
- Every commit appends the trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- Run pytest from the `ladder-foundry/` directory.

## File Structure

| File | Responsibility |
| --- | --- |
| `generator/__init__.py` | empty — makes `generator` an importable package |
| `generator/weights.py` | L1: 4-segment schema, defaults, `load`/`dump_initial`/`revise`, all locks |
| `generator/leak_audit.py` | L2: `LeakHit` + `leak_audit(text)` regex DENY backstop |
| `generator/axes.py` | L3 ①: `level_text(w, axis, level)` pure read of `axis_prose` |
| `generator/interpolator.py` | L4 ②: `ladder_levels(w, n=6)` pure read of `interp_params` + `coord_table` |
| `generator/assembler.py` | L5 ③: `build_batch(w, n, topic_id)` pure read of `assembler_params` |
| `generator/cards.py` | L6: `PolicyCard` dataclass + `to_dict(card)` serialization |
| `demo.py` | human-readable health report (deliverable 2) |
| `tests/test_weights.py` | L1 unit tests |
| `tests/test_leak_audit.py` | L2 unit tests |
| `tests/test_axes.py` | L3 unit tests (incl. source-immutability test) |
| `tests/test_interpolator.py` | L4 unit tests |
| `tests/test_assembler.py` | L5 unit tests |
| `tests/test_cards.py` | L6 unit tests |
| `tests/test_stage1_handoff.py` | Layer-2 cross-step consumption test |

---

### Task 1: L1 weights.py — schema + load/dump_initial/revise + locks

**Files:**
- Create: `ladder-foundry/generator/__init__.py` (empty)
- Create: `ladder-foundry/generator/weights.py`
- Test: `ladder-foundry/tests/test_weights.py`

**Interfaces:**
- Consumes: nothing (root of the data core).
- Produces:
  - `dump_initial(path: str) -> dict` — writes batch-0 JSON, returns the dict.
  - `load(path: str) -> dict` — reads + validates a weights JSON.
  - `revise(w: dict, target: str, key: str, new, reason: str) -> dict` — mutates `w` in place, returns `{"target","key","old","new","reason"}`.
  - Module constants `TRAINABLE`, `AXES`, `LEVELS`, `INTERP_KEYS`, `COLLISION_ENUM`.
  - batch-0 shape: top-level keys `{axis_prose, interp_params, assembler_params, frozen_label}`; `interp_params` keys exactly `{collision_offset_axis, endpoint_spread, granularity_map}`; `frozen_label = {rank_order:{direction:[0,1,2,3,4,5], primary_sort:["A1","A3","A2"]}, coord_table:{}}`.

- [ ] **Step 1: Write the failing tests**

```python
# ladder-foundry/tests/test_weights.py
import pytest
from generator import weights


def _w(tmp_path):
    return weights.dump_initial(str(tmp_path / "batch-0.json"))


def test_dump_initial_has_four_segments(tmp_path):
    w = _w(tmp_path)
    assert set(w.keys()) == {"axis_prose", "interp_params", "assembler_params", "frozen_label"}


def test_interp_params_key_set_locked(tmp_path):
    w = _w(tmp_path)
    assert set(w["interp_params"].keys()) == {"collision_offset_axis", "endpoint_spread", "granularity_map"}
    w["interp_params"]["sneaky_coord"] = [1, 2]      # smuggle a coord under a new key
    with pytest.raises(ValueError):
        weights.revise(w, "assembler_params", "turn_budget", 13, "trigger keyset check")


def test_coord_table_empty_in_batch0(tmp_path):
    w = _w(tmp_path)
    assert w["frozen_label"]["coord_table"] == {}


def test_rank_order_locked_values(tmp_path):
    w = _w(tmp_path)
    assert w["frozen_label"]["rank_order"]["direction"] == [0, 1, 2, 3, 4, 5]
    assert w["frozen_label"]["rank_order"]["primary_sort"] == ["A1", "A3", "A2"]


def test_revise_rejects_frozen_label(tmp_path):
    w = _w(tmp_path)
    with pytest.raises(ValueError):
        weights.revise(w, "frozen_label", "rank_order", {}, "must reject")


def test_revise_rejects_unknown_target(tmp_path):
    w = _w(tmp_path)
    with pytest.raises(ValueError):
        weights.revise(w, "bogus_segment", "k", "v", "must reject")


def test_collision_offset_rejects_label_axis(tmp_path):
    w = _w(tmp_path)
    with pytest.raises(ValueError):
        weights.revise(w, "interp_params", "collision_offset_axis", "A2", "must reject")


def test_collision_offset_accepts_b1_expression(tmp_path):
    w = _w(tmp_path)
    rec = weights.revise(w, "interp_params", "collision_offset_axis", "expression", "ok")
    assert rec["new"] == "expression"
    assert w["interp_params"]["collision_offset_axis"] == "expression"


def test_revise_axis_prose_dotted_key(tmp_path):
    w = _w(tmp_path)
    rec = weights.revise(w, "axis_prose", "A1.L0", "new body", "ok")
    assert rec == {"target": "axis_prose", "key": "A1.L0",
                   "old": rec["old"], "new": "new body", "reason": "ok"}
    assert w["axis_prose"]["A1"]["L0"] == "new body"


def test_revise_axis_prose_malformed_path(tmp_path):
    w = _w(tmp_path)
    for bad in ["A1", "A1.L0.x", "Z9.L0", "A1.L9"]:
        with pytest.raises(ValueError):
            weights.revise(w, "axis_prose", bad, "x", "must reject")


def test_load_roundtrip_and_keyset_validation(tmp_path):
    p = str(tmp_path / "batch-0.json")
    weights.dump_initial(p)
    w = weights.load(p)
    assert set(w.keys()) == {"axis_prose", "interp_params", "assembler_params", "frozen_label"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_weights.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator'` (or `AttributeError`).

- [ ] **Step 3: Create the package marker**

```python
# ladder-foundry/generator/__init__.py
```
(empty file)

- [ ] **Step 4: Write minimal implementation**

```python
# ladder-foundry/generator/weights.py
"""L1 — the data-core: 4-segment weights schema + load/dump_initial/revise.

Data-oriented principle: training changes the JSON DATA segments only; this
source never moves. frozen_label is NOT trainable (dump_initial is its sole
writer). interp_params key-set is structurally locked (AS-3).
"""
import json
from pathlib import Path

TRAINABLE = {"axis_prose", "interp_params", "assembler_params"}
AXES = {"A1", "A2", "A3", "A4", "A5"}
LEVELS = {"L0", "L1", "L2", "L3", "L4"}
INTERP_KEYS = {"collision_offset_axis", "endpoint_spread", "granularity_map"}
COLLISION_ENUM = {"B1", "expression"}


def _default_axis_prose():
    # ponytail: seed prose only — STAGE 2 (D2 endpoint personas) authors the
    # real bodies. STAGE 1 just needs structure to prove read/write/lock.
    return {axis: {level: f"{axis}.{level} seed prose" for level in sorted(LEVELS)}
            for axis in sorted(AXES)}


def _check_interp_keyset(w):
    got = set(w["interp_params"].keys())
    if got != INTERP_KEYS:
        raise ValueError(f"interp_params key-set locked to {INTERP_KEYS}, got {got}")


def dump_initial(path):
    """Export batch-0 from the three weights' defaults. SOLE writer of frozen_label."""
    w = {
        "axis_prose": _default_axis_prose(),
        "interp_params": {
            "collision_offset_axis": "B1",
            "endpoint_spread": 1.0,
            "granularity_map": "round",
        },
        "assembler_params": {
            "two_stage": {"pressure_turns": 10, "closing_turns": 2},
            "field_template": {"F0": "research supervisor"},
            "f6_derivation": "derived_from:A1+A3+A2",
            "turn_budget": 12,
        },
        "frozen_label": {
            "rank_order": {"direction": [0, 1, 2, 3, 4, 5], "primary_sort": ["A1", "A3", "A2"]},
            "coord_table": {},
        },
    }
    Path(path).write_text(json.dumps(w, indent=2, ensure_ascii=False), encoding="utf-8")
    return w


def load(path):
    w = json.loads(Path(path).read_text(encoding="utf-8"))
    _check_interp_keyset(w)
    return w


def revise(w, target, key, new, reason):
    if target == "frozen_label":
        raise ValueError("frozen_label not trainable (lifeline of the label)")
    if target not in TRAINABLE:
        raise ValueError(f"unknown target {target!r}")
    _check_interp_keyset(w)
    if target == "axis_prose":
        parts = key.split(".")
        if len(parts) != 2:
            raise ValueError(f"axis_prose key must be 'AXIS.LEVEL', got {key!r}")
        axis, level = parts
        if axis not in AXES or level not in LEVELS:
            raise ValueError(f"unknown axis/level in {key!r}")
        old = w["axis_prose"][axis][level]
        w["axis_prose"][axis][level] = new
    else:
        if key not in w[target]:
            raise ValueError(f"unknown key {key!r} for {target}")
        if target == "interp_params" and key == "collision_offset_axis" and new not in COLLISION_ENUM:
            raise ValueError(f"collision_offset_axis must be B1/expression, got {new!r}")
        old = w[target][key]
        w[target][key] = new
    return {"target": target, "key": key, "old": old, "new": new, "reason": reason}
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_weights.py -v`
Expected: PASS — all 11 tests green.

- [ ] **Step 6: Commit**

```bash
git add ladder-foundry/generator/__init__.py ladder-foundry/generator/weights.py ladder-foundry/tests/test_weights.py
git commit -m "feat(ladder-foundry): L1 weights schema + load/dump_initial/revise with locks"
```

---

### Task 2: L2 leak_audit.py — W5 regex DENY backstop

**Files:**
- Create: `ladder-foundry/generator/leak_audit.py`
- Test: `ladder-foundry/tests/test_leak_audit.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `class LeakHit(Exception)` — carries the matched term.
  - `leak_audit(text: str) -> None` — raises `LeakHit` on a denied term, else returns `None`.

**Note:** leak_audit is a BACKSTOP, not the primary W5 control (the primary control is structural role-blindness: generation roles never see the checks). The DENY vocabulary is deliberately a regex word-boundary list, not fragile substring matching.

- [ ] **Step 1: Write the failing tests**

```python
# ladder-foundry/tests/test_leak_audit.py
import pytest
from generator.leak_audit import leak_audit, LeakHit


def test_clean_text_passes():
    assert leak_audit("The supervisor pushed for more operational substance.") is None


def test_denies_check_signature():
    for leak in [
        "this maps to the R7 precision check",
        "primitive P3 fires here",
        "looks like a pseudo-good sample",
        "the novel-good engine generated it",
        "detection signature matched",
    ]:
        with pytest.raises(LeakHit):
            leak_audit(leak)


def test_substring_false_positive_avoided():
    # 'P3' as a check id must deny, but 'P3' inside an unrelated word must not.
    assert leak_audit("the MP3 file format") is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_leak_audit.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.leak_audit'`.

- [ ] **Step 3: Write minimal implementation**

```python
# ladder-foundry/generator/leak_audit.py
"""L2 — W5 leak interceptor (BACKSTOP, not the primary control).

Primary W5 control is structural role-blindness: generation/loss roles never
see the 32 checks. This regex DENY list is a second line of defence so a leak
that slips into generated text is caught loudly. Word-boundary regex, not
substring matching (the old code's anti-pattern: 'P3' would have hit 'MP3').
"""
import re

# DENY vocabulary: 32-check ids, 6 primitives, detection-signature phrases,
# PG/NG engine names. Extend here as new check vocabulary appears.
_DENY_TERMS = [
    r"R\d{1,2}",                 # R1..R18 precision checks
    r"P\d{1,2}",                 # P1..P14 recall checks
    r"primitive",
    r"detection signature",
    r"pseudo-good",
    r"novel-good",
    r"PG engine", r"NG engine",
    r"PG-engine", r"NG-engine",
]
_DENY = re.compile(r"\b(" + "|".join(_DENY_TERMS) + r")\b", re.IGNORECASE)


class LeakHit(Exception):
    """Raised when text contains a check/primitive/detection-signature term."""


def leak_audit(text):
    m = _DENY.search(text)
    if m:
        raise LeakHit(f"leak term matched: {m.group(0)!r}")
    return None
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_leak_audit.py -v`
Expected: PASS — all 3 tests green.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/generator/leak_audit.py ladder-foundry/tests/test_leak_audit.py
git commit -m "feat(ladder-foundry): L2 leak_audit W5 regex DENY backstop"
```

---

### Task 3: L3 axes.py — pure read of axis_prose (+ source-immutability proof)

**Files:**
- Create: `ladder-foundry/generator/axes.py`
- Test: `ladder-foundry/tests/test_axes.py`

**Interfaces:**
- Consumes: `weights.dump_initial(path) -> dict`, `weights.revise(...)`.
- Produces: `level_text(w: dict, axis: str, level: str) -> str` — returns `w["axis_prose"][axis][level]`.

**Note:** `test_revise_changes_data_not_source` is the data-oriented proof — it asserts `axes.py`'s bytes on disk are identical before and after a legal `revise`, proving training touches DATA not SOURCE.

- [ ] **Step 1: Write the failing tests**

```python
# ladder-foundry/tests/test_axes.py
from pathlib import Path
from generator import weights
from generator.axes import level_text

_AXES_PY = Path(__file__).resolve().parents[1] / "generator" / "axes.py"


def test_level_text_reads_prose(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert level_text(w, "A1", "L0") == w["axis_prose"]["A1"]["L0"]


def test_revise_changes_data_not_source(tmp_path):
    before = _AXES_PY.read_bytes()
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    weights.revise(w, "axis_prose", "A1.L0", "edited body", "training step")
    after = _AXES_PY.read_bytes()
    assert before == after                      # source byte-identical
    assert level_text(w, "A1", "L0") == "edited body"   # data changed
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_axes.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.axes'`.

- [ ] **Step 3: Write minimal implementation**

```python
# ladder-foundry/generator/axes.py
"""L3 ① — pure read of the axis_prose weight. Source never moves; training
edits w["axis_prose"] (DATA), proven by test_revise_changes_data_not_source.
"""


def level_text(w, axis, level):
    return w["axis_prose"][axis][level]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_axes.py -v`
Expected: PASS — both tests green.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/generator/axes.py ladder-foundry/tests/test_axes.py
git commit -m "feat(ladder-foundry): L3 axes.py pure read + source-immutability proof"
```

---

### Task 4: L4 interpolator.py — ladder_levels (rank locked, coords READ not computed)

**Files:**
- Create: `ladder-foundry/generator/interpolator.py`
- Test: `ladder-foundry/tests/test_interpolator.py`

**Interfaces:**
- Consumes: `weights.dump_initial(path) -> dict`.
- Produces:
  - `GRANULARITY: dict[str, callable]` — name→curve dispatch (NO eval).
  - `ladder_levels(w: dict, n: int = 6) -> list[dict]` — each rung dict is
    `{"rung_id": int, "level_idx": int, "collision_offset_axis": str, "coord": <value or None>}`.

**Key rules:** reads `direction` (LOCKED) from `frozen_label.rank_order`; `level_idx` via the named granularity strategy `round(t*(L-1))` with `t = i/(n-1)`, `L=5`; coordinates are READ from `frozen_label.coord_table` keyed by `str(rung_id)` (None if absent), NEVER computed by the spread layer. For `n=6`, level indices are `[0,1,2,2,3,4]` — NONDECREASING, not strict (collision at level 2).

- [ ] **Step 1: Write the failing tests**

```python
# ladder-foundry/tests/test_interpolator.py
from generator import weights
from generator.interpolator import ladder_levels


def test_rank_direction_locked(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    rungs = ladder_levels(w, n=6)
    assert [r["rung_id"] for r in rungs] == [0, 1, 2, 3, 4, 5]


def test_ladder_nondecreasing(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    levels = [r["level_idx"] for r in ladder_levels(w, n=6)]
    assert levels == [0, 1, 2, 2, 3, 4]                 # collision at level 2
    assert all(b >= a for a, b in zip(levels, levels[1:]))   # nondecreasing


def test_coord_read_from_table_not_computed(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert all(r["coord"] is None for r in ladder_levels(w, n=6))  # empty batch-0
    w["frozen_label"]["coord_table"] = {"0": [0.0, 1.0], "5": [9.0, 9.0]}  # fixture
    rungs = ladder_levels(w, n=6)
    assert rungs[0]["coord"] == [0.0, 1.0]
    assert rungs[5]["coord"] == [9.0, 9.0]
    assert rungs[1]["coord"] is None                    # not fabricated


def test_collision_offset_axis_carried(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert all(r["collision_offset_axis"] in {"B1", "expression"}
               for r in ladder_levels(w, n=6))
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_interpolator.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.interpolator'`.

- [ ] **Step 3: Write minimal implementation**

```python
# ladder-foundry/generator/interpolator.py
"""L4 ② — pure read of interp_params (spread layer). The rank direction and
the coordinate table are LOCKED (read-only); the spread layer NEVER computes a
coordinate, it only READS coord_table — the locked coordinate layer is
load-bearing by construction (audit requirement).
"""

_L = 5  # number of axis levels L0..L4


def _round_strategy(t):
    # round(t*(L-1)). Python round() is banker's-rounding on exact .5 ties; not
    # biting [0,1,2,2,3,4] for n=6/L=5, but a semantics trap if L/n change.
    return round(t * (_L - 1))


GRANULARITY = {"round": _round_strategy}   # name->curve dispatch, NO eval()


def ladder_levels(w, n=6):
    direction = w["frozen_label"]["rank_order"]["direction"]
    coord_table = w["frozen_label"]["coord_table"]
    offset_axis = w["interp_params"]["collision_offset_axis"]
    strat = GRANULARITY[w["interp_params"]["granularity_map"]]
    rungs = []
    for i in direction[:n]:
        t = i / (n - 1)
        rungs.append({
            "rung_id": i,
            "level_idx": strat(t),
            "collision_offset_axis": offset_axis,
            "coord": coord_table.get(str(i)),   # READ, never computed
        })
    return rungs
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_interpolator.py -v`
Expected: PASS — all 4 tests green.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/generator/interpolator.py ladder-foundry/tests/test_interpolator.py
git commit -m "feat(ladder-foundry): L4 interpolator ladder_levels (rank locked, coords read)"
```

---

### Task 5: L5 assembler.py — build_batch (perturbation never on A1–A5)

**Files:**
- Create: `ladder-foundry/generator/assembler.py`
- Test: `ladder-foundry/tests/test_assembler.py`

**Interfaces:**
- Consumes: `weights.dump_initial(path) -> dict`, `interpolator.ladder_levels(w, n) -> list[dict]`.
- Produces: `build_batch(w: dict, n: int, topic_id: str) -> list[dict]` — one card per rung:
  `{"topic_id": str, "rung_id": int, "level_idx": int, "perturb_axis": str, "coord": <value or None>, "params": dict}`.

**Key rule:** `perturb_axis` is copied straight from each rung's `collision_offset_axis` (∈{B1,expression}); the assembler has no other offset source, so perturbation can NEVER land on A1–A5.

- [ ] **Step 1: Write the failing tests**

```python
# ladder-foundry/tests/test_assembler.py
from generator import weights
from generator.assembler import build_batch


def test_build_batch_one_card_per_rung(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    assert len(cards) == 6
    assert [c["rung_id"] for c in cards] == [0, 1, 2, 3, 4, 5]
    assert all(c["topic_id"] == "topic00" for c in cards)


def test_collision_offset_never_label_axis(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    label_axes = {"A1", "A2", "A3", "A4", "A5"}
    assert all(c["perturb_axis"] not in label_axes for c in cards)
    assert all(c["perturb_axis"] in {"B1", "expression"} for c in cards)


def test_params_externalized_from_assembler_segment(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    assert cards[0]["params"]["turn_budget"] == w["assembler_params"]["turn_budget"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_assembler.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.assembler'`.

- [ ] **Step 3: Write minimal implementation**

```python
# ladder-foundry/generator/assembler.py
"""L5 ③ — pure read of assembler_params. Assembles one coordinate card per
rung. The ONLY perturbation source is each rung's collision_offset_axis
(∈{B1,expression}); there is no path to an A1–A5 label axis — the schema lock
guarantees it.
"""
from generator.interpolator import ladder_levels


def build_batch(w, n, topic_id):
    params = w["assembler_params"]
    cards = []
    for rung in ladder_levels(w, n=n):
        cards.append({
            "topic_id": topic_id,
            "rung_id": rung["rung_id"],
            "level_idx": rung["level_idx"],
            "perturb_axis": rung["collision_offset_axis"],
            "coord": rung["coord"],
            "params": params,
        })
    return cards
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_assembler.py -v`
Expected: PASS — all 3 tests green.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/generator/assembler.py ladder-foundry/tests/test_assembler.py
git commit -m "feat(ladder-foundry): L5 assembler build_batch (perturb never on A1-A5)"
```

---

### Task 6: L6 cards.py — PolicyCard + to_dict serialization

**Files:**
- Create: `ladder-foundry/generator/cards.py`
- Test: `ladder-foundry/tests/test_cards.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `@dataclass class PolicyCard` with fields `F0..F9` (str) and `axis_levels` (dict).
  - `to_dict(card: PolicyCard) -> dict` — JSON-serializable `{F0..F9, axis_levels}`.

- [ ] **Step 1: Write the failing tests**

```python
# ladder-foundry/tests/test_cards.py
import json
from generator.cards import PolicyCard, to_dict


def _card():
    return PolicyCard(
        F0="research supervisor", F1="topic", F2="persona", F3="pressure",
        F4="stance", F5="corrigibility", F6="acceptance", F7="controversy",
        F8="turn budget", F9="closing",
        axis_levels={"A1": "L0", "A2": "L0", "A3": "L0", "A4": "L0", "A5": "L0"},
    )


def test_to_dict_has_f0_f9():
    d = to_dict(_card())
    assert [f"F{i}" for i in range(10)] == [k for k in d if k.startswith("F")]
    assert d["axis_levels"]["A1"] == "L0"


def test_to_dict_is_json_serializable():
    json.dumps(to_dict(_card()))   # raises if not serializable
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ladder-foundry && python -m pytest tests/test_cards.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.cards'`.

- [ ] **Step 3: Write minimal implementation**

```python
# ladder-foundry/generator/cards.py
"""L6 — PolicyCard serialization. F0..F9 + axis_levels → JSON-serializable dict."""
from dataclasses import dataclass, asdict


@dataclass
class PolicyCard:
    F0: str
    F1: str
    F2: str
    F3: str
    F4: str
    F5: str
    F6: str
    F7: str
    F8: str
    F9: str
    axis_levels: dict


def to_dict(card):
    return asdict(card)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ladder-foundry && python -m pytest tests/test_cards.py -v`
Expected: PASS — both tests green.

- [ ] **Step 5: Commit**

```bash
git add ladder-foundry/generator/cards.py ladder-foundry/tests/test_cards.py
git commit -m "feat(ladder-foundry): L6 cards PolicyCard + to_dict"
```

---

### Task 7: Layer-2 cross-step handoff test (correct FOR THE SYSTEM)

**Files:**
- Create: `ladder-foundry/tests/test_stage1_handoff.py`

**Interfaces:**
- Consumes: `weights.dump_initial`, `axes.level_text`, `interpolator.ladder_levels`, `assembler.build_batch`.
- Produces: nothing (verification only).

**Why:** Layer-1 tests prove each component is self-consistent. This proves L1's `dump_initial` output is REALLY consumable by its downstream L3/L4/L5 in the shape the plan requires — the answer to "correct for the whole system, not just green."

- [ ] **Step 1: Write the failing test**

```python
# ladder-foundry/tests/test_stage1_handoff.py
"""Layer-2: downstream really ingests L1's dump_initial output."""
from generator import weights
from generator.axes import level_text
from generator.interpolator import ladder_levels
from generator.assembler import build_batch


def test_L3_consumes_dump_initial(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert isinstance(level_text(w, "A3", "L4"), str)


def test_L4_consumes_dump_initial(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    w["frozen_label"]["coord_table"] = {"0": [0.0], "5": [9.0]}   # fixture coords
    rungs = ladder_levels(w, n=6)
    assert len(rungs) == 6
    assert [r["rung_id"] for r in rungs] == [0, 1, 2, 3, 4, 5]


def test_L5_consumes_dump_initial(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    assert len(cards) == 6
    assert all(c["perturb_axis"] in {"B1", "expression"} for c in cards)
```

- [ ] **Step 2: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_stage1_handoff.py -v`
Expected: PASS (all three components already exist from Tasks 1–5, so this is green immediately — it is a *consumption contract*, not a red→green unit).

- [ ] **Step 3: Run the FULL suite**

Run: `cd ladder-foundry && python -m pytest tests/ -v`
Expected: PASS — every test from Tasks 1–7 green. This `pytest -v` green list is human-verifiable deliverable #1 (each test name = one invariant).

- [ ] **Step 4: Commit**

```bash
git add ladder-foundry/tests/test_stage1_handoff.py
git commit -m "test(ladder-foundry): Layer-2 cross-step handoff (L1 output consumable by L3/L4/L5)"
```

---

### Task 8: demo.py health report (human-verifiable deliverable #2 + #3)

**Files:**
- Create: `ladder-foundry/demo.py`

**Interfaces:**
- Consumes: `weights`, `axes`. Produces: a CLI script (no functions other code depends on).

**Why:** A human reads `demo.py`'s output and confirms STAGE 1 is correct WITHOUT reading code — prints batch-0 anatomy, the four attack tests (all rejected), one legal revise (accepted + source unchanged), and the contract reconciliation table (deliverable #3).

- [ ] **Step 1: Write demo.py**

```python
# ladder-foundry/demo.py
"""STAGE 1 health report. Run: python demo.py
Prints batch-0 anatomy + attack tests in plain language; a human verifies
STAGE 1 is correct without reading code.
"""
import tempfile
from pathlib import Path
from generator import weights
from generator.axes import level_text

_AXES_PY = Path(__file__).resolve().parent / "generator" / "axes.py"


def _expect_reject(label, fn):
    try:
        fn()
        print(f"  [FAIL] {label}: was ACCEPTED (should reject)")
    except ValueError:
        print(f"  [ok]   {label}: rejected")


def main():
    tmp = Path(tempfile.mkdtemp()) / "batch-0.json"
    w = weights.dump_initial(str(tmp))

    print("== batch-0 anatomy ==")
    print(f"  4 segments present: {set(w) == {'axis_prose','interp_params','assembler_params','frozen_label'}}")
    print(f"  interp_params 3-key-locked: {set(w['interp_params']) == weights.INTERP_KEYS}")
    print(f"  contains a coord under interp_params? {'coord' in str(w['interp_params'])}")
    print(f"  coord_table empty: {w['frozen_label']['coord_table'] == {}}")
    print(f"  rank direction locked: {w['frozen_label']['rank_order']['direction'] == [0,1,2,3,4,5]}")

    print("== attack tests (all must be rejected) ==")
    _expect_reject("revise frozen_label", lambda: weights.revise(w, "frozen_label", "x", 1, "atk"))
    _expect_reject("set collision=A2", lambda: weights.revise(w, "interp_params", "collision_offset_axis", "A2", "atk"))
    _expect_reject("unknown target", lambda: weights.revise(w, "bogus", "x", 1, "atk"))
    w["interp_params"]["sneaky"] = 1
    _expect_reject("inject extra interp_params key", lambda: weights.revise(w, "assembler_params", "turn_budget", 13, "atk"))
    del w["interp_params"]["sneaky"]

    print("== legal revise (must be accepted, source unchanged) ==")
    before = _AXES_PY.read_bytes()
    weights.revise(w, "axis_prose", "A1.L0", "edited", "legal training step")
    after = _AXES_PY.read_bytes()
    print(f"  revise axis_prose A1.L0: {'ok' if level_text(w,'A1','L0')=='edited' else 'FAIL'}")
    print(f"  axes.py source byte-identical: {before == after}")

    print("== contract reconciliation (field -> schema -> consumer) ==")
    rows = [
        ("axis_prose", "L1 schema seg ①", "L3 axes.level_text"),
        ("interp_params", "L1 schema seg ② (3-key lock)", "L4 interpolator.ladder_levels"),
        ("assembler_params", "L1 schema seg ③", "L5 assembler.build_batch"),
        ("frozen_label.rank_order", "L1 locked (dump_initial only)", "L4 reads direction"),
        ("frozen_label.coord_table", "L1 locked, empty in batch-0", "L4/L5 read coords"),
    ]
    for field, schema, consumer in rows:
        print(f"  {field:28} | {schema:32} | {consumer}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**

Run: `cd ladder-foundry && python demo.py`
Expected: every anatomy line `True`, all four attacks `[ok] ... rejected`, legal revise `ok` + source `True`, reconciliation table printed. No `[FAIL]` anywhere.

- [ ] **Step 3: Commit**

```bash
git add ladder-foundry/demo.py
git commit -m "feat(ladder-foundry): demo.py STAGE 1 health report (deliverables 2+3)"
```

---

### Task 9: Layer-3 codex independent audit (no self-confirmation)

**Files:** none created (verification gate).

**Why:** Tests + code are both authored by the same model → same-source error risk. Codex (different model family) audits the produced `batch-0.json` + the §3 authoritative schema table from the spec, WITHOUT seeing the pytest suite, and judges conformance to the design plan. Only if codex concurs is "marked my own homework" ruled out.

- [ ] **Step 1: Generate the artifact to audit**

Run: `cd ladder-foundry && python -c "from generator import weights; weights.dump_initial('weights/batch-0.json')"`
(Create `ladder-foundry/weights/` first if absent. Note: `weights/*.json` is gitignored — the artifact is for the audit, not committed.)

- [ ] **Step 2: Dispatch the codex audit**

Hand codex: (a) the generated `batch-0.json`, (b) spec §3 schema table + §11 locked decisions — but NOT `tests/`. Ask: "Does this batch-0.json conform to the schema? List any deviation." Capture the verdict.

- [ ] **Step 3: Record verdict + checkpoint**

Append the codex verdict to `ladder-foundry/context/2026-06-30-13-33-stage1-data-core.md` as a new checkpoint. If codex flags a real deviation, fix it (new red→green cycle) before declaring STAGE 1 done.

- [ ] **Step 4: Flip the progress mermaid**

In `ladder-foundry/context/2026-06-30-13-09-codes-reference.md`, move L1–L6 from `class ... tbd` to `class ... done`. Commit.

```bash
git add ladder-foundry/context/2026-06-30-13-33-stage1-data-core.md ladder-foundry/context/2026-06-30-13-09-codes-reference.md
git commit -m "docs(ladder-foundry): STAGE 1 codex audit verdict + mermaid L1-L6 done"
```

---

## Self-Review

**Spec coverage:** §3 schema → Task 1; §3.1 functions → Task 1; §3.2 AS-3 lock → Task 1 (`test_interp_params_key_set_locked`); §3.3 granularity dispatch → Task 4 (`GRANULARITY`, no eval); §4 leak_audit → Task 2; §5 L3/L4/L5 incl. nondecreasing `[0,1,2,2,3,4]` + coords-read-not-computed → Tasks 3/4/5; §6 cards → Task 6; §7 Layer-1 every named test → Tasks 1–6; Layer-2 handoff → Task 7; Layer-3 codex → Task 9; §8 deliverables → Task 8 (demo) + Task 7 (pytest list); §9 file structure → File Structure table; §11 decisions → Global Constraints. No gaps.

**Placeholder scan:** no TBD/TODO; every code step shows full code; no "similar to Task N".

**Type consistency:** `dump_initial`/`load`/`revise` signatures identical across Tasks 1/3/4/5/7/8. `ladder_levels` rung dict keys (`rung_id, level_idx, collision_offset_axis, coord`) consumed unchanged by Task 5. `build_batch` card keys (`perturb_axis` etc.) consistent across Tasks 5/7/8. `INTERP_KEYS` referenced in Task 8 demo matches Task 1 definition.
