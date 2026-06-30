# ladder-foundry STAGE 2 — Persona Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn STAGE 1's seed-prose data-core into a real persona core (D1 PolicyCard contract + validator, D2 two endpoint personas + frozen `coord_table`, L7 deterministic config pipeline) and run the first real sim-cc persona-injection smoke test in a local Windows sandbox.

**Architecture:** Two milestones with a hard gate. PART 2A (Tasks 1–4) is pure local Python reading STAGE 1's `weights.py` — no key, no token, no CC runtime; acceptance = pytest + human-eye read of 6 generated configs. PART 2B (Tasks 5–7) is the first real sim-cc: a sandbox-confined `claude` REPL, persona-injection smoke test, session-jsonl read. The gate forbids 2B from starting until 2A passes pytest AND the human-eye read.

**Tech Stack:** Python 3.12.7, pytest 9.0.3 (base anaconda env). No new deps. STAGE 1 modules `generator/{weights,axes,interpolator,assembler,cards,leak_audit}.py` are consumed, not rewritten. 2B uses `claude` 2.1.196 (native Windows MINGW64) started directly in the Bash tool.

## Global Constraints

- **Branch `self-iteration/ladder-foundry`** — continue on it, do NOT branch off, do NOT push to main. Commit trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Commit only when steps say so.
- **NO `-p` / `--resume` / `--session-id` / `--allowedTools`** anywhere. All CC layers are normal interactive REPLs.
- **W5 leak boundary:** all authored prose (F0–F9, axis_prose bodies, F6/F7/F9 directives) must pass `generator.leak_audit.leak_audit` — no 32-check / 6-primitive / detection-signature vocabulary, no bare `R1`–`R18` / `P1`–`P14` tokens, no `primitive` / `pseudo-good` / `novel-good` / `PG engine` / `NG engine`. `leak_audit.py` is the ONLY file allowed to name denied terms.
- **Privacy red line:** the CC log path (`C:\Users\...\.claude\projects\...`) and any path derived from it (cwd-slug) MUST NEVER appear in a committed artifact. The jsonl reader takes `--logs-dir` as a REQUIRED arg, no default. Committed pilot output is de-identified / aggregate only. Sandbox outputs live under a gitignored path.
- **Two API-key groups (Claude / Codex) isolated;** key VALUES never enter a committed artifact (2B touches only the Claude key, by env var name only).
- **Data-oriented invariant:** training edits JSON DATA segments only; `.py` sources never move. `frozen_label` (rank_order + coord_table) is LOCKED — `revise` rejects it.
- **AS-3 structural lock:** `interp_params` key-set = exactly `{collision_offset_axis, endpoint_spread, granularity_map}`; `collision_offset_axis ∈ {B1, expression}` only, NEVER an A1–A5 label axis.
- **A4/A5 overlay convention (Option A, fixed, lives in D1):** `axis_prose` stays L0..L4-indexed for all 5 axes (STAGE 1 schema lock untouched). Tag map: A4 `{L0:C-, L2:C0, L4:C+}`, A5 `{L0:G0, L4:G+}`. A4/A5 are off-spine — NOT in `primary_sort {A1,A3,A2}`.
- **Prose selection reads `coord[axis]` ONLY.** `level_idx` (= `granularity_map(t)`) NEVER selects a prose body. If `coord is None` → FAIL LOUD, never fall back to `level_idx`.
- **Write/Edit calls stay under 13000 chars;** build large files in parts.
- **5-dim DARE standard only** (D1–D5). Academic standards (novelty/baseline/rigor/citations/publishability) are FORBIDDEN as judging criteria.

## File Structure

- `generator/contract.py` (CREATE, Task 1) — D1 semantic contract: field→axis docstring, A4/A5 tag-convention constants, `validate_card(card)`.
- `generator/weights.py` (MODIFY, Tasks 2+3) — `dump_initial` gains real authored `axis_prose` (Task 2) and a frozen 6-rung `coord_table` (Task 3). Schema/load/revise logic unchanged.
- `generator/gen_configs.py` (CREATE, Task 4) — L7 deterministic pipeline → 6 config JSONs.
- `sandbox/` (CREATE, Task 5) — `.claude/settings.local.json` (bypass + 1 deny rule), `.gitignore`, deny-probe procedure.
- `sandbox/read_session.py` (CREATE, Task 6) — session-jsonl reader, `--logs-dir` required.
- `sandbox/smoke_test.py` (CREATE, Task 7) — persona-injection smoke-test runner (real sim-cc).
- Tests: `tests/test_contract.py`, `tests/test_gen_configs.py`, `tests/test_read_session.py` (CREATE); `tests/test_weights.py`, `tests/test_interpolator.py` (MODIFY — two assertions D2 deliberately changes).

**Run all commands from `ladder-foundry/`** (the package root; `from generator import ...` resolves there). pytest invoked as `python -m pytest`.

## Two structural decisions locked from reading STAGE 1 source (reviewer: confirm)

1. **`coord` is a dict keyed by axis.** STAGE 1's `test_interpolator.py` / `test_stage1_handoff.py` fed `coord_table` opaque lists (`[0.0, 1.0]`) but NEVER passed them to `level_text`. The spec mandates `level_text(w, axis, coord[axis])`, so STAGE 2 defines the real `coord` shape as `{"A1":"L4","A2":"L4","A3":"L4","A4":"C+","A5":"G+","B1":"neu"}`. This is additive — `interpolator.ladder_levels` just does `coord_table.get(str(i))` and returns whatever shape is stored; no STAGE 1 logic changes.
2. **`B1` lives inside each `coord_table` rung.** The two endpoints differ in B1 (id0=neu, id5=buz) → B1 is per-rung data, and spec#3 calls B1 an off-spine *labeled overlay*, so it belongs in `frozen_label`. The STAGE 1 codex CONFORMS audit only locked the *empty* `coord_table` (`{}`); its value-shape was never asserted, so STAGE 2 is free to define it. B1 is NOT added to `axis_prose` (`weights.AXES` stays `{A1..A5}`); F9 composes B1's framing inline, not via `level_text`.

## STAGE 1 tests that change (spec-driven, NOT regressions)

D2 deliberately fills state two STAGE 1 tests assert is empty. Both are rewritten in Task 3:
- `tests/test_weights.py::test_coord_table_empty_in_batch0` — asserted `coord_table == {}`. After D2, `dump_initial` ships a populated 6-rung table. Rewrite to assert the 6 keys + endpoint values.
- `tests/test_interpolator.py::test_coord_read_from_table_not_computed` — asserted `all(r["coord"] is None ...)` for the empty batch-0. Rewrite to assert rung 0/5 carry the endpoint dicts and the read-not-computed property still holds (coord comes verbatim from the table).

---

# PART 2A — Persona Data Core (Tasks 1–4)

Pure local Python. No key, no token, no CC runtime. The last clean local milestone.

### Task 1: D1 — PolicyCard semantic contract + validator

**Files:**
- Create: `generator/contract.py`
- Test: `tests/test_contract.py`

**Interfaces:**
- Consumes: `generator.cards.PolicyCard` (dataclass, fields F0..F9 + `axis_levels: dict`); `generator.weights.AXES` (`{"A1".."A5"}`).
- Produces: `A4_TAGS = {"L0":"C-","L2":"C0","L4":"C+"}`, `A5_TAGS = {"L0":"G0","L4":"G+"}` (module constants — the A4/A5 level↔tag convention, read by L7 as a fixed structural constant); `validate_card(card) -> None` (raises `ValueError` on any contract violation, returns `None` on pass). `AXIS_LEVEL_KEYS = {"A1","A2","A3","A4","A5","B1"}`.

The field→axis contract (documented in the module docstring, enforced by `validate_card`):

| Field | Semantics | Source |
| --- | --- | --- |
| F0 | persona identity / role header | composite rung + B1 tone |
| F1 | substance demand | ← A1 |
| F2 | request legitimacy / coherence | ← A2 |
| F3 | operationalization insistence | ← A3 |
| F4 | premise corrigibility | ← A4 |
| F5 | generativity | ← A5 |
| F6 | acceptance rule, derived from F1/F3/F2 | `assembler_params.f6_derivation` |
| F7 | prerequisite facts | topic + A4 overlay |
| F8 | turn budget (constant per batch) | `assembler_params.turn_budget` |
| F9 | framing / tone directive | ← B1 |

`validate_card` checks: (1) `set(card.axis_levels.keys()) == AXIS_LEVEL_KEYS`; (2) A1/A2/A3 values ∈ `{"L0".."L4"}`; (3) A4 value ∈ `{"C-","C0","C+"}`; (4) A5 value ∈ `{"G0","G+"}`; (5) B1 value is a non-empty str; (6) every F0..F9 is a non-empty str. NOTE: `leak_audit` is NOT called inside `validate_card` — L7 runs `leak_audit` separately on each card (Task 4); keeping them separate matches STAGE 1's "backstop is its own pass" design.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_contract.py
import pytest
from generator.cards import PolicyCard
from generator.contract import validate_card, A4_TAGS, A5_TAGS, AXIS_LEVEL_KEYS


def _good_card(**over):
    base = dict(
        F0="role header", F1="f1", F2="f2", F3="f3", F4="f4",
        F5="f5", F6="f6", F7="f7", F8="12 turns", F9="f9",
        axis_levels={"A1": "L4", "A2": "L4", "A3": "L4",
                     "A4": "C+", "A5": "G+", "B1": "neu"},
    )
    base.update(over)
    return PolicyCard(**base)


def test_tag_conventions_are_fixed():
    assert A4_TAGS == {"L0": "C-", "L2": "C0", "L4": "C+"}
    assert A5_TAGS == {"L0": "G0", "L4": "G+"}
    assert AXIS_LEVEL_KEYS == {"A1", "A2", "A3", "A4", "A5", "B1"}


def test_good_card_passes():
    assert validate_card(_good_card()) is None


def test_missing_axis_key_rejected():
    c = _good_card()
    del c.axis_levels["B1"]
    with pytest.raises(ValueError):
        validate_card(c)


def test_a1_level_out_of_enum_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(axis_levels={"A1": "L9", "A2": "L4",
            "A3": "L4", "A4": "C+", "A5": "G+", "B1": "neu"}))


def test_a4_tag_out_of_enum_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(axis_levels={"A1": "L4", "A2": "L4",
            "A3": "L4", "A4": "C5", "A5": "G+", "B1": "neu"}))


def test_a5_tag_out_of_enum_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(axis_levels={"A1": "L4", "A2": "L4",
            "A3": "L4", "A4": "C+", "A5": "GG", "B1": "neu"}))


def test_empty_field_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(F3=""))
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_contract.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.contract'`.

- [ ] **Step 3: Write `generator/contract.py`**

```python
"""D1 — PolicyCard semantic contract + validator.

Field -> axis map (one-to-one for the label axes A1-A5; F0/F6/F7/F8/F9 are
composed or off-axis):

  F0  persona identity / role header   composite rung + B1 tone
  F1  substance demand                 <- A1
  F2  request legitimacy / coherence   <- A2
  F3  operationalization insistence    <- A3
  F4  premise corrigibility            <- A4
  F5  generativity                     <- A5
  F6  acceptance rule (from F1/F3/F2)   assembler_params.f6_derivation
  F7  prerequisite facts                topic + A4 overlay
  F8  turn budget (constant per batch)  assembler_params.turn_budget
  F9  framing / tone directive         <- B1

A4/A5 are OFF-SPINE overlays: NOT part of primary_sort {A1,A3,A2}, they do not
participate in the composite ladder ordering. axis_prose stays L0..L4-indexed
for ALL 5 axes (STAGE 1 schema lock); the human-meaningful A4/A5 tag is a FIXED
level<->tag convention recorded in axis_levels, defined here as a constant:

  A4: L0<->C-, L2<->C0, L4<->C+   (L1/L3 unused seed slots, accepted)
  A5: L0<->G0, L4<->G+            (L1/L2/L3 unused seed slots, accepted)

B1 has ONE source of truth: axis_levels["B1"]. F9 carries the B1 framing
directive; F0's role header is merely written in a tone CONSISTENT with B1 (F0
does not encode a second, independent B1 value).
"""

A4_TAGS = {"L0": "C-", "L2": "C0", "L4": "C+"}
A5_TAGS = {"L0": "G0", "L4": "G+"}
AXIS_LEVEL_KEYS = {"A1", "A2", "A3", "A4", "A5", "B1"}

_LABEL_LEVELS = {"L0", "L1", "L2", "L3", "L4"}
_A4_VALUES = set(A4_TAGS.values())   # {"C-","C0","C+"}
_A5_VALUES = set(A5_TAGS.values())   # {"G0","G+"}
_F_FIELDS = ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]


def validate_card(card):
    al = card.axis_levels
    if set(al.keys()) != AXIS_LEVEL_KEYS:
        raise ValueError(f"axis_levels keys must be {AXIS_LEVEL_KEYS}, got {set(al.keys())}")
    for ax in ("A1", "A2", "A3"):
        if al[ax] not in _LABEL_LEVELS:
            raise ValueError(f"{ax} level out of enum: {al[ax]!r}")
    if al["A4"] not in _A4_VALUES:
        raise ValueError(f"A4 tag out of enum: {al['A4']!r}")
    if al["A5"] not in _A5_VALUES:
        raise ValueError(f"A5 tag out of enum: {al['A5']!r}")
    if not isinstance(al["B1"], str) or not al["B1"]:
        raise ValueError(f"B1 must be a non-empty str, got {al['B1']!r}")
    for f in _F_FIELDS:
        v = getattr(card, f)
        if not isinstance(v, str) or not v:
            raise ValueError(f"{f} must be a non-empty str, got {v!r}")
    return None
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_contract.py -v`
Expected: PASS — 7 passed.

- [ ] **Step 5: Commit**

```bash
git add generator/contract.py tests/test_contract.py
git commit -m "feat(ladder-foundry): D1 PolicyCard semantic contract + validator

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: D2 part 1 — author real `axis_prose` bodies

**Files:**
- Modify: `generator/weights.py` (replace `_default_axis_prose`)
- Test: `tests/test_weights.py` (add 2 tests; existing tests stay green)

**Interfaces:**
- Consumes: `generator.weights.{AXES, LEVELS}`.
- Produces: `_default_axis_prose()` returning real authored bodies — same shape as before (`{axis: {level: str}}`, all 5 axes × all 5 levels), so `dump_initial`, `load`, `revise`, `level_text`, and every STAGE 1 test that reads structure stay green.

What changes: STAGE 1's `_default_axis_prose` returned `f"{axis}.{level} seed prose"`. D2 replaces every body with REAL persona prose. Author the FULL L0..L4 for A1/A2/A3 (the interpolator's intermediate rungs read these); A4 at L0/L2/L4 (= C-/C0/C+) and A5 at L0/L4 (= G0/G+) get real bodies, the unused slots (A4 L1/L3, A5 L1/L2/L3) keep a short placeholder string (non-empty, so structure holds — they are never selected because `coord[axis]` only ever names a used level).

Prose authoring rules (W5): each body is 1–3 plain sentences describing how a user at that axis level behaves toward a research-supervisor interaction. NO 32-check / 6-primitive / detection vocabulary, no bare `R1`–`R18`/`P1`–`P14`, no `primitive`/`pseudo-good`/`novel-good`/`PG engine`/`NG engine`. The endpoints anchor the ladder: A1.L4 = relentless substance demand; A1.L0 = no substance demand. A3.L4 = insists everything be operationalized; A3.L0 = never asks for operationalization. A2.L4 = fully coherent legitimate requests; A2.L0 = incoherent/illegitimate. A4.L4(C+) = readily corrects own premises; A4.L0(C-) = clings to premises. A5.L4(G+) = spawns new directions generatively; A5.L0(G0) = no generativity.

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_weights.py
def test_axis_prose_is_real_not_seed(tmp_path):
    w = _w(tmp_path)
    # every A1-A3 body across L0..L4 is authored, none is the STAGE-1 seed string
    for axis in ("A1", "A2", "A3"):
        for lvl in ("L0", "L1", "L2", "L3", "L4"):
            body = w["axis_prose"][axis][lvl]
            assert isinstance(body, str) and len(body) >= 15
            assert "seed prose" not in body


def test_axis_prose_passes_leak_audit(tmp_path):
    from generator.leak_audit import leak_audit
    w = _w(tmp_path)
    for axis, levels in w["axis_prose"].items():
        for lvl, body in levels.items():
            leak_audit(body)        # raises LeakHit if a denied term slipped in
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_weights.py::test_axis_prose_is_real_not_seed -v`
Expected: FAIL — body is `"A1.L0 seed prose"`, `"seed prose" in body` is True.

- [ ] **Step 3: Replace `_default_axis_prose` in `generator/weights.py`**

Replace the whole `_default_axis_prose` function body with explicit authored prose. Build the dict literally (do NOT loop a template). Example anchors below; the implementer authors all 25 bodies in this voice, keeping every string non-empty and leak-clean:

```python
def _default_axis_prose():
    # D2: real endpoint + intermediate persona prose. axis_prose stays
    # L0..L4-indexed for all 5 axes (STAGE 1 schema lock). A4/A5 unused slots
    # carry a short placeholder (never selected: coord[axis] only names a used
    # level). All bodies are leak-clean (W5) — no check/primitive vocabulary.
    return {
        "A1": {
            "L0": "Accepts whatever is offered and asks for nothing more; makes no demand on the substance of an answer.",
            "L1": "Occasionally nudges for a little more depth but is satisfied quickly.",
            "L2": "Expects a reasonable amount of substance and pushes back when an answer is thin.",
            "L3": "Demands well-supported substance and keeps pressing where an answer is underdeveloped.",
            "L4": "Relentlessly demands the deepest possible substance, never satisfied until every claim is fully grounded.",
        },
        "A2": {
            "L0": "Makes incoherent, self-contradictory requests with no legitimate through-line.",
            "L1": "Requests are mostly muddled, with only occasional coherence.",
            "L2": "Requests are workable though sometimes loosely framed.",
            "L3": "Requests are clear, coherent, and well-motivated.",
            "L4": "Every request is fully coherent, legitimate, and precisely scoped.",
        },
        "A3": {
            "L0": "Never asks for anything to be made concrete or operational; abstractions are fine as-is.",
            "L1": "Rarely asks how something would actually be done.",
            "L2": "Sometimes asks for a concrete procedure when it matters.",
            "L3": "Usually insists that proposals be turned into operational steps.",
            "L4": "Insists relentlessly that every idea be operationalized into concrete, executable steps.",
        },
        "A4": {
            "L0": "Clings to original premises and resists any correction even when shown to be wrong.",
            "L1": "(unused A4 slot)",
            "L2": "Will revise a premise when given a clear reason.",
            "L3": "(unused A4 slot)",
            "L4": "Readily corrects own premises the moment a better framing appears.",
        },
        "A5": {
            "L0": "Stays narrowly on the single given thread; spawns no new directions.",
            "L1": "(unused A5 slot)",
            "L2": "(unused A5 slot)",
            "L3": "(unused A5 slot)",
            "L4": "Generatively spawns new research directions and adjacent questions from any starting point.",
        },
    }
```

- [ ] **Step 4: Run the new tests AND the full STAGE 1 weights suite**

Run: `python -m pytest tests/test_weights.py tests/test_axes.py -v`
Expected: PASS — the 2 new tests pass; all pre-existing weights/axes tests still pass (structure unchanged). `test_revise_changes_data_not_source` still green (it edits A1.L0 and checks the .py is byte-identical — authoring the default does not break that).

- [ ] **Step 5: Commit**

```bash
git add generator/weights.py tests/test_weights.py
git commit -m "feat(ladder-foundry): D2 author real axis_prose persona bodies

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 3: D2 part 2 — frozen 6-rung `coord_table` (+ rewrite 2 STAGE 1 tests)

**Files:**
- Modify: `generator/weights.py` (`dump_initial`: `coord_table` `{}` → 6 frozen rungs)
- Modify: `tests/test_weights.py` (rewrite `test_coord_table_empty_in_batch0`)
- Modify: `tests/test_interpolator.py` (rewrite `test_coord_read_from_table_not_computed`)

**Interfaces:**
- Consumes: nothing new.
- Produces: `dump_initial` ships `frozen_label.coord_table` = 6 entries keyed `"0".."5"`, each a dict `{"A1","A2","A3","A4","A5","B1"}` → level/tag string. This is the LOCKED label coordinate. `interpolator.ladder_levels` reads it verbatim via `coord_table.get(str(i))` (no code change there).

**Endpoint coordinates (from spec):**
- rung "0" (id0 genius): `{"A1":"L4","A2":"L4","A3":"L4","A4":"C+","A5":"G+","B1":"neu"}`
- rung "5" (id5 contrarian): `{"A1":"L0","A2":"L0","A3":"L0","A4":"C-","A5":"G0","B1":"buz"}`

**Intermediate rungs 1–4 (computed ONCE at authoring time, then FROZEN):** the A1/A2/A3 spine descends monotonically L4→L0 across rungs 0→5; A4/A5/B1 (off-spine overlays) transition near the midpoint. These values were chosen once at authoring time and are now LOCKED — generation NEVER recomputes them. Use the EXACT frozen table below verbatim (it is the single source of truth; do not derive values from any formula):

```python
# rung -> locked label coordinate (authored once, never recomputed at gen time)
_COORD_TABLE = {
    "0": {"A1": "L4", "A2": "L4", "A3": "L4", "A4": "C+", "A5": "G+", "B1": "neu"},
    "1": {"A1": "L3", "A2": "L3", "A3": "L3", "A4": "C+", "A5": "G+", "B1": "neu"},
    "2": {"A1": "L2", "A2": "L2", "A3": "L2", "A4": "C0", "A5": "G+", "B1": "neu"},
    "3": {"A1": "L2", "A2": "L1", "A3": "L2", "A4": "C0", "A5": "G0", "B1": "buz"},
    "4": {"A1": "L1", "A2": "L1", "A3": "L1", "A4": "C-", "A5": "G0", "B1": "buz"},
    "5": {"A1": "L0", "A2": "L0", "A3": "L0", "A4": "C-", "A5": "G0", "B1": "buz"},
}
```

Monotone non-increasing on the spine {A1,A3,A2} (verified: A1 4,3,2,2,1,0; A3 4,3,2,2,1,0; A2 4,3,2,1,1,0 — all non-increasing). Endpoint spread is the full L4↔L0 / C+↔C- / G+↔G0 / neu↔buz range (AS-1 headroom: max by design).

- [ ] **Step 1: Write/rewrite the failing tests**

```python
# REPLACE tests/test_weights.py::test_coord_table_empty_in_batch0 with:
def test_coord_table_has_six_frozen_rungs(tmp_path):
    w = _w(tmp_path)
    ct = w["frozen_label"]["coord_table"]
    assert set(ct.keys()) == {"0", "1", "2", "3", "4", "5"}
    assert ct["0"] == {"A1": "L4", "A2": "L4", "A3": "L4",
                       "A4": "C+", "A5": "G+", "B1": "neu"}
    assert ct["5"] == {"A1": "L0", "A2": "L0", "A3": "L0",
                       "A4": "C-", "A5": "G0", "B1": "buz"}


def test_coord_table_spine_is_monotone_nonincreasing(tmp_path):
    w = _w(tmp_path)
    ct = w["frozen_label"]["coord_table"]
    for axis in ("A1", "A2", "A3"):
        idx = [int(ct[str(i)][axis][1:]) for i in range(6)]   # "L4"->4
        assert all(b <= a for a, b in zip(idx, idx[1:])), f"{axis} not monotone: {idx}"
```

```python
# REPLACE tests/test_interpolator.py::test_coord_read_from_table_not_computed with:
def test_coord_read_from_frozen_table(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    rungs = ladder_levels(w, n=6)
    # coord comes verbatim from the frozen table (read, never computed)
    assert rungs[0]["coord"] == w["frozen_label"]["coord_table"]["0"]
    assert rungs[5]["coord"] == w["frozen_label"]["coord_table"]["5"]
    assert rungs[0]["coord"]["A1"] == "L4"
    assert rungs[5]["coord"]["A1"] == "L0"
    # mutating the returned coord must not alter a fresh read (table is source of truth)
    assert rungs[3]["coord"] == w["frozen_label"]["coord_table"]["3"]
```

(The interpolator test file imports `from generator.interpolator import ladder_levels` already; add `from generator import weights` is already present.)

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_weights.py::test_coord_table_has_six_frozen_rungs tests/test_interpolator.py::test_coord_read_from_frozen_table -v`
Expected: FAIL — `coord_table` is still `{}` (KeyError on `ct["0"]`).

- [ ] **Step 3: Set `coord_table` in `dump_initial`**

In `generator/weights.py`, define `_COORD_TABLE` (the dict above) at module level near the other constants, and change the `frozen_label` block in `dump_initial`:

```python
        "frozen_label": {
            "rank_order": {"direction": [0, 1, 2, 3, 4, 5], "primary_sort": ["A1", "A3", "A2"]},
            "coord_table": {k: dict(v) for k, v in _COORD_TABLE.items()},  # frozen copy
        },
```

(`dict(v)` gives each dumped batch its own copy so an in-memory edit can't mutate the module constant.)

- [ ] **Step 4: Run the full STAGE 1 + new suite**

Run: `python -m pytest tests/test_weights.py tests/test_interpolator.py tests/test_stage1_handoff.py -v`
Expected: PASS. Note: `test_stage1_handoff.py::test_L4_consumes_dump_initial` overwrites `coord_table` with its own fixture then asserts 6 rungs — still green (it sets the table itself). All other STAGE 1 tests untouched. `test_ladder_nondecreasing` still asserts `level_idx == [0,1,2,2,3,4]` (level_idx is unchanged — it reads `granularity_map`, not `coord_table`).

- [ ] **Step 5: Commit**

```bash
git add generator/weights.py tests/test_weights.py tests/test_interpolator.py
git commit -m "feat(ladder-foundry): D2 freeze 6-rung coord_table + rewrite 2 STAGE-1 state tests

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 4: L7 — `gen_configs.py` deterministic pipeline (HARD-GATE deliverable)

**Files:**
- Create: `generator/gen_configs.py`
- Test: `tests/test_gen_configs.py`
- Modify: `.gitignore` (add `ladder-foundry/configs/`)

**Interfaces:**
- Consumes: `weights.{dump_initial,load}`, `assembler.build_batch(w, n, topic_id) -> list[dict]` (each `{topic_id, rung_id, level_idx, perturb_axis, coord, params}`), `axes.level_text(w, axis, level)`, `cards.PolicyCard`, `contract.{validate_card, A4_TAGS, A5_TAGS}`, `leak_audit.leak_audit`.
- Produces: `build_one(w, card, topic) -> PolicyCard`; `gen_configs(w, topic=_PLACEHOLDER_TOPIC, n=6) -> list[PolicyCard]`; `_PLACEHOLDER_TOPIC` constant; `main(out_dir)` writing `<out_dir>/config_<rung_id>.json`.

**Key rules baked into the pipeline:**
- F1/F2/F3 select prose by `coord[axis]` directly (`coord["A1"]` is already `"L4"`). F4/F5 must map the A4/A5 TAG back to a LEVEL before calling `level_text` (`coord["A4"]="C+"` → level `"L4"`), via the inverse of `A4_TAGS`/`A5_TAGS`.
- `coord is None` → raise `ValueError` (landmine 1: NEVER fall back to `level_idx`).
- `leak_audit` runs on every assembled F-field. In 2A the prose is STATIC (no LLM), so a hit = a bug in authored prose → FAIL LOUD (re-raise). The spec's "regenerate-then-reaudit bounded-retry" path is for the LATER LLM-text wiring (STAGE 5); 2A has nothing to regenerate. `# ponytail:` comment names this.
- Deterministic: same weights → byte-identical configs (no clock, no randomness).

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_gen_configs.py
import json
import pytest
from generator import weights
from generator.axes import level_text
from generator.gen_configs import gen_configs, build_one, _PLACEHOLDER_TOPIC, main
from generator.cards import to_dict
from generator.contract import validate_card


def _w(tmp_path):
    return weights.dump_initial(str(tmp_path / "b0.json"))


def test_pipeline_yields_six_cards(tmp_path):
    cards = gen_configs(_w(tmp_path))
    assert len(cards) == 6


def test_every_card_validates(tmp_path):
    for card in gen_configs(_w(tmp_path)):
        assert validate_card(card) is None


def test_f1_selected_by_coord_not_level_idx(tmp_path):
    w = _w(tmp_path)
    cards = gen_configs(w)
    # rung 0 coord A1 = L4 -> F1 must be the A1.L4 body verbatim
    assert level_text(w, "A1", "L4") in cards[0].F1
    assert level_text(w, "A1", "L0") in cards[5].F1


def test_f4_f5_map_tag_to_level(tmp_path):
    w = _w(tmp_path)
    cards = gen_configs(w)
    # rung0 A4=C+ -> A4.L4 body; A5=G+ -> A5.L4 body
    assert level_text(w, "A4", "L4") in cards[0].F4
    assert level_text(w, "A5", "L4") in cards[0].F5
    # rung5 A4=C- -> A4.L0 body; A5=G0 -> A5.L0 body
    assert level_text(w, "A4", "L0") in cards[5].F4
    assert level_text(w, "A5", "L0") in cards[5].F5


def test_coord_none_fails_loud(tmp_path):
    w = _w(tmp_path)
    bad = {"topic_id": "t", "rung_id": 9, "level_idx": 0,
           "perturb_axis": "B1", "coord": None, "params": w["assembler_params"]}
    with pytest.raises(ValueError):
        build_one(w, bad, _PLACEHOLDER_TOPIC)


def test_endpoints_diverge(tmp_path):
    cards = gen_configs(_w(tmp_path))
    assert cards[0].F1 != cards[5].F1
    assert cards[0].axis_levels["A1"] == "L4"
    assert cards[5].axis_levels["A1"] == "L0"
    assert cards[0].axis_levels["B1"] != cards[5].axis_levels["B1"]


def test_pipeline_is_deterministic(tmp_path):
    a = [to_dict(c) for c in gen_configs(_w(tmp_path))]
    b = [to_dict(c) for c in gen_configs(_w(tmp_path))]
    assert a == b


def test_main_writes_six_config_files(tmp_path):
    w = _w(tmp_path)
    main(str(tmp_path / "configs"), w=w)
    files = sorted((tmp_path / "configs").glob("config_*.json"))
    assert len(files) == 6
    doc = json.loads(files[0].read_text(encoding="utf-8"))
    assert set(doc.keys()) >= {"F0", "F1", "axis_levels"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_gen_configs.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'generator.gen_configs'`.

- [ ] **Step 3: Write `generator/gen_configs.py`**

```python
"""L7 — deterministic config-generation pipeline.

Wires every STAGE 1/2 component: weights -> ladder_levels (via build_batch) ->
per-rung prose selected by the LOCKED coord (never level_idx) -> assemble
F0..F9 -> validate_card + leak_audit -> config JSON. One placeholder topic in
2A => 6 config personas (the full 48 = 6 rungs x 8 topics waits for D3).
"""
import json
from pathlib import Path

from generator import weights
from generator.axes import level_text
from generator.assembler import build_batch
from generator.cards import PolicyCard, to_dict
from generator.contract import validate_card, A4_TAGS, A5_TAGS
from generator.leak_audit import leak_audit

_PLACEHOLDER_TOPIC = {
    "topic_id": "topic00",
    "F7_prerequisite": "No special prerequisites for this placeholder research topic.",
}

# inverse of the fixed A4/A5 level<->tag convention (contract.py owns the forward map)
_A4_TAG_TO_LEVEL = {tag: lvl for lvl, tag in A4_TAGS.items()}   # "C+"->"L4"
_A5_TAG_TO_LEVEL = {tag: lvl for lvl, tag in A5_TAGS.items()}   # "G+"->"L4"

_B1_FRAMING = {
    "neu": "Frame every request in a neutral, businesslike tone.",
    "buz": "Frame every request in a buzzword-heavy, hype-driven tone.",
}


def _audit_all(card):
    for f in ("F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"):
        # ponytail: 2A prose is static — a hit is an authored-prose bug, so
        # fail loud. The regenerate-then-reaudit retry loop belongs to the
        # later LLM-text path (STAGE 5), which has something to regenerate.
        leak_audit(getattr(card, f))


def build_one(w, card, topic):
    coord = card["coord"]
    if coord is None:
        raise ValueError(
            f"rung {card['rung_id']} coord=None — coord_table not populated; "
            "refusing to fall back to level_idx (label-drift guard)")
    params = card["params"]
    pc = PolicyCard(
        F0=f"Research-supervisor persona at ladder rung {card['rung_id']} of 6.",
        F1=level_text(w, "A1", coord["A1"]),
        F2=level_text(w, "A2", coord["A2"]),
        F3=level_text(w, "A3", coord["A3"]),
        F4=level_text(w, "A4", _A4_TAG_TO_LEVEL[coord["A4"]]),
        F5=level_text(w, "A5", _A5_TAG_TO_LEVEL[coord["A5"]]),
        F6=(f"Accept a reply only when it meets the substance (A1={coord['A1']}), "
            f"operationalization (A3={coord['A3']}), and legitimacy (A2={coord['A2']}) bar."),
        F7=f"Prerequisites: {topic['F7_prerequisite']} Premise stance: {coord['A4']}.",
        F8=f"{params['turn_budget']} turns total for this interaction.",
        F9=_B1_FRAMING.get(coord["B1"], f"Framing tone directive: {coord['B1']}."),
        axis_levels={ax: coord[ax] for ax in ("A1", "A2", "A3", "A4", "A5", "B1")},
    )
    validate_card(pc)
    _audit_all(pc)
    return pc


def gen_configs(w, topic=_PLACEHOLDER_TOPIC, n=6):
    return [build_one(w, card, topic)
            for card in build_batch(w, n=n, topic_id=topic["topic_id"])]


def main(out_dir, w=None):
    if w is None:
        w = weights.dump_initial(str(Path(out_dir) / "_batch0.json"))
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    cards = gen_configs(w)
    for card in cards:
        rung = card.F0.split("rung ")[1].split(" ")[0]   # "0".."5" from F0 header
        p = Path(out_dir) / f"config_{rung}.json"
        p.write_text(json.dumps(to_dict(card), indent=2, ensure_ascii=False), encoding="utf-8")
    return cards


if __name__ == "__main__":   # ponytail: thin CLI for the human-eye gate
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "configs")
    print("wrote 6 configs to", sys.argv[1] if len(sys.argv) > 1 else "configs")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_gen_configs.py -v`
Expected: PASS — 8 passed.

- [ ] **Step 5: Add `ladder-foundry/configs/` to `.gitignore`, then run the FULL suite + generate for the human-eye read**

```bash
echo "ladder-foundry/configs/" >> .gitignore
python -m pytest tests/ -v          # FULL STAGE 1+2 suite, expect all green
python -m generator.gen_configs configs   # writes 6 configs locally (gitignored)
```
Expected: full suite green (STAGE 1's ~30 + STAGE 2's new). 6 files `configs/config_0.json`..`config_5.json` written.

- [ ] **Step 6: HARD-GATE — human-eye read of the 6 configs**

Read `configs/config_0.json` through `config_5.json`. Confirm: config_0 reads like a genius user (relentless substance, full operationalization, generative, corrigible, neutral tone); config_5 reads like an absurd-contrarian (no substance demand, no operationalization, incoherent, clings to premises, buzzword tone); configs 1–4 a monotone transition between them. **This human read + the green pytest are the gate; 2B (Tasks 5–7) MUST NOT start until both pass.**

- [ ] **Step 7: Commit**

```bash
git add generator/gen_configs.py tests/test_gen_configs.py .gitignore
git commit -m "feat(ladder-foundry): L7 deterministic gen_configs pipeline (2A hard-gate)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

# PART 2B — Persona-Injection Smoke Test (Tasks 5–7)

First real sim-cc. **DO NOT START until 2A's pytest is green AND the human-eye read of the 6 configs passed (Task 4 Step 6).** Introduces key / token / sandbox confinement. Explicitly NOT the AS-1 quality-separation gate.

### Task 5: Sandbox scaffold + the load-bearing deny-under-bypass empirical check

**Files:**
- Create: `sandbox/.claude/settings.local.json`
- Create: `sandbox/.gitignore`
- Create: `sandbox/README.md` (the deny-probe procedure + what 2B is/isn't)
- Modify: `.gitignore` (repo root — ignore the sandbox runtime dirs)

**Interfaces:**
- Produces: a confined working dir `ladder-foundry/sandbox/` with `CLAUDE_CONFIG_DIR=sandbox/.claude` and a settings file that grants `bypassPermissions` but denies reads outside the sandbox.

**Why this task is a gate, not just setup:** `--allowedTools` is banned and `bypassPermissions` auto-approves everything, so `permissions.deny` is the ONLY in-claude confinement lever. `deny` is documented to evaluate BEFORE `defaultMode` — but that MUST be verified empirically on THIS machine before 2B is trusted to run locally. If deny does NOT fire under bypass, that is decisive evidence 2B must move to the remote box (STAGE 5 env), and Tasks 6–7 do not run locally.

- [ ] **Step 1: Write `sandbox/.claude/settings.local.json`**

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "deny": ["Read(//**)"]
  }
}
```

(One deny rule — the ponytail narrowing: 2B's sim is a pure conversational responder, no exec spawn, ~no tool calls. `Read(//**)` denies absolute-path reads outside the sandbox; the relative cwd is naturally bounded by `cd`. The heavy Bash/Write/Edit/CC-log/other-key-dir deny-list is STAGE 5's threat model, not imported here. If the empirical probe in Step 4 shows `Read(//**)` doesn't match the way this build expresses "outside the tree", adjust the glob to the form that does — the gate is "a deny rule fires under bypass", not this exact glob.)

- [ ] **Step 2: Write `sandbox/.gitignore`**

```
# sandbox runtime is local-only — never commit CC config, logs, or transcripts
.claude/
runs/
transcripts/
*.jsonl
```

- [ ] **Step 3: Write `sandbox/README.md`**

Document: (a) 2B is a persona-injection smoke test, NOT the AS-1 gate; (b) the deny-probe procedure (Step 4); (c) the privacy rule — the CC-log path and cwd-slug never enter a committed file, `read_session.py` takes `--logs-dir` required; (d) the ceiling: Windows Bash tool has no OS sandbox, `deny` governs Read/Write/Edit only, OS-hard boundary deferred to STAGE 5.

- [ ] **Step 4: Run the empirical deny-under-bypass probe (THE GATE)**

This is a manual procedure, not pytest (it spawns a real `claude`). From `ladder-foundry/sandbox/`, start a child `claude` REPL directly in the Bash tool with the sandbox config dir, and ask it to read a file OUTSIDE the sandbox (e.g. the repo's top-level `README`). Procedure (run via the Bash tool, interactive):

```bash
cd ladder-foundry/sandbox
IS_SANDBOX=1 CLAUDE_CONFIG_DIR="$(pwd)/.claude" claude
# Then, in that REPL, ask: "Read the file D:/YOGSOTH-AI/README.md and show me line 1."
# PASS  = the read is DENIED (deny fired under bypassPermissions).
# FAIL  = the read SUCCEEDS (deny did NOT fire) -> 2B cannot run locally.
```

Record the verdict in `sandbox/README.md` (PASS/FAIL + date, de-identified — no log path). **If FAIL: stop. Tasks 6–7 move to the remote STAGE 5 env; report to the user.** If PASS: proceed.

- [ ] **Step 5: Commit** (sandbox scaffold only — NO runtime artifacts; `.claude/` is gitignored)

```bash
git add sandbox/settings.local.json.template 2>/dev/null; \
git add sandbox/.gitignore sandbox/README.md .gitignore
# NOTE: sandbox/.claude/settings.local.json is gitignored by sandbox/.gitignore.
# Commit a copy as sandbox/settings.local.json.template so the scaffold is reproducible.
cp sandbox/.claude/settings.local.json sandbox/settings.local.json.template
git add sandbox/settings.local.json.template
git commit -m "feat(ladder-foundry): 2B sandbox scaffold + deny-under-bypass probe

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

(Add `ladder-foundry/sandbox/.claude/` and `ladder-foundry/sandbox/runs/` to the repo-root `.gitignore` in Step 1 of this task if not already covered by `sandbox/.gitignore`. The committed scaffold = `.gitignore`, `README.md`, `settings.local.json.template`. Runtime `.claude/`, logs, transcripts NEVER committed.)

---

### Task 6: `read_session.py` — session-jsonl reader (`--logs-dir` REQUIRED)

**Files:**
- Create: `sandbox/read_session.py`
- Test: `tests/test_read_session.py`

**Interfaces:**
- Produces: `find_latest_session(logs_dir, cwd_slug) -> Path` (newest `.jsonl` under `logs_dir/projects/<cwd_slug>/`); `read_turns(session_path) -> list[dict]` (each `{role, text}` extracted from the jsonl lines); `cwd_to_slug(cwd) -> str` (CC's cwd→slug rule: replace path separators and `:`/`.` with `-`). `main()` via argparse with `--logs-dir` as a REQUIRED argument (no default).

**Privacy:** `--logs-dir` has NO default — the caller must pass it explicitly, so the CC-log path is never baked into committed source. The reader returns turn text; it does NOT print the logs-dir path. Tests use a synthetic jsonl under `tmp_path`, never a real CC log.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_read_session.py
import json
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))
from read_session import find_latest_session, read_turns, cwd_to_slug


def _write_session(dirpath, name, turns):
    dirpath.mkdir(parents=True, exist_ok=True)
    p = dirpath / name
    lines = []
    for role, text in turns:
        lines.append(json.dumps({"type": role, "message": {"role": role,
            "content": [{"type": "text", "text": text}]}}))
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def test_cwd_to_slug_replaces_separators():
    s = cwd_to_slug(r"D:\YOGSOTH-AI\ladder-foundry\sandbox")
    assert "\\" not in s and "/" not in s and ":" not in s
    assert s.startswith("D-")


def test_find_latest_session_picks_newest(tmp_path):
    slug = "D--proj-sandbox"
    d = tmp_path / "projects" / slug
    p1 = _write_session(d, "aaa.jsonl", [("user", "hi")])
    p2 = _write_session(d, "bbb.jsonl", [("user", "yo")])
    import os, time
    os.utime(p2, (time.time() + 10, time.time() + 10))   # make bbb newest
    assert find_latest_session(str(tmp_path), slug) == p2


def test_read_turns_extracts_role_and_text(tmp_path):
    d = tmp_path / "projects" / "slug1"
    p = _write_session(d, "s.jsonl", [("user", "play this persona"),
                                      ("assistant", "Understood, I am the supervisor.")])
    turns = read_turns(p)
    assert turns[0]["role"] == "user" and "persona" in turns[0]["text"]
    assert turns[1]["role"] == "assistant" and "supervisor" in turns[1]["text"]


def test_logs_dir_is_required(tmp_path, monkeypatch):
    import read_session
    monkeypatch.setattr(sys, "argv", ["read_session.py"])   # no --logs-dir
    with pytest.raises(SystemExit):                          # argparse exits 2
        read_session.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_read_session.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'read_session'` (until created).

- [ ] **Step 3: Write `sandbox/read_session.py`**

```python
"""Read a sim-cc's own session jsonl. PRIVACY: --logs-dir is REQUIRED (no
default) so the CC-log path is never baked into committed source. We locate the
session by globbing projects/<cwd-slug>/ — NEVER by --session-id (banned)."""
import argparse
import json
from pathlib import Path


def cwd_to_slug(cwd):
    # CC's slug rule: non-alnum path chars -> '-'. Good enough to locate the dir.
    out = []
    for ch in cwd:
        out.append(ch if ch.isalnum() or ch == "-" else "-")
    return "".join(out)


def find_latest_session(logs_dir, cwd_slug):
    proj = Path(logs_dir) / "projects" / cwd_slug
    sessions = sorted(proj.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not sessions:
        raise FileNotFoundError(f"no .jsonl under projects/{cwd_slug}/")
    return sessions[-1]


def read_turns(session_path):
    turns = []
    for line in Path(session_path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        msg = rec.get("message") or {}
        role = msg.get("role") or rec.get("type")
        content = msg.get("content")
        if isinstance(content, list):
            text = " ".join(b.get("text", "") for b in content if isinstance(b, dict))
        else:
            text = content if isinstance(content, str) else ""
        if role and text:
            turns.append({"role": role, "text": text})
    return turns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True,
                    help="CC projects logs dir (REQUIRED, no default — privacy)")
    ap.add_argument("--cwd", required=True, help="the sim cwd to slug + locate")
    args = ap.parse_args()
    session = find_latest_session(args.logs_dir, cwd_to_slug(args.cwd))
    for t in read_turns(session):
        print(f"[{t['role']}] {t['text'][:200]}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_read_session.py -v`
Expected: PASS — 4 passed. (`cwd_to_slug` produces `"D--YOGSOTH-AI-ladder-foundry-sandbox"` for the example; the slug must MATCH whatever CC actually writes — Task 7 Step 2 verifies the real slug empirically and adjusts `cwd_to_slug` if CC's rule differs.)

- [ ] **Step 5: Commit**

```bash
git add sandbox/read_session.py tests/test_read_session.py
git commit -m "feat(ladder-foundry): 2B session-jsonl reader (--logs-dir required, privacy)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 7: `smoke_test.py` — persona-injection smoke test (real sim-cc, manual gate)

**Files:**
- Create: `sandbox/smoke_test.py`
- Create: `sandbox/stimulus.md` (the FIXED written stimulus)
- Create: `sandbox/SMOKE_RESULT.md` (de-identified verdict, written by hand after the run)

**Interfaces:**
- Consumes: `gen_configs.main` output (`configs/config_0.json`, `config_5.json`); `read_session.{find_latest_session, read_turns, cwd_to_slug}`.
- Produces: `build_injection(config_path, stimulus_path) -> str` (the message text injected into the sim: full config + play-this-persona instruction + the fixed stimulus + a DONE convention); `diverged(turns0, turns5) -> bool` (cheap lexical check the two endpoints reacted differently). No new CC-spawning code is auto-run by pytest — the actual spawn is a manual Bash-tool procedure (Step 4) because it starts a real interactive `claude`.

**This is a smoke test, not pytest-automated end-to-end.** The pytest piece covers the pure helpers (`build_injection`, `diverged`). The real sim-cc spawn + injection + jsonl read is a documented manual procedure, run once per endpoint, verdict recorded by hand in `SMOKE_RESULT.md`. Privacy: `SMOKE_RESULT.md` is de-identified/aggregate (no log path, no cwd-slug, no transcript dump — only "persona worn: yes/no, diverged: yes/no").

- [ ] **Step 1: Write the failing tests + the fixed stimulus**

```python
# tests/test_smoke_test.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))
from smoke_test import build_injection, diverged


def test_injection_contains_config_and_stimulus(tmp_path):
    cfg = tmp_path / "config_0.json"
    cfg.write_text('{"F0":"role header X","F1":"demand substance"}', encoding="utf-8")
    stim = tmp_path / "stimulus.md"
    stim.write_text("A research proposal to react to.", encoding="utf-8")
    msg = build_injection(str(cfg), str(stim))
    assert "role header X" in msg
    assert "research proposal" in msg
    assert "DONE" in msg            # the reply convention is present


def test_diverged_true_when_reactions_differ():
    t0 = [{"role": "assistant", "text": "I demand far more rigorous substance here."}]
    t5 = [{"role": "assistant", "text": "Sounds great, no notes, ship it."}]
    assert diverged(t0, t5) is True


def test_diverged_false_when_identical():
    t = [{"role": "assistant", "text": "Same exact reaction text."}]
    assert diverged(t, t) is False
```

```markdown
<!-- sandbox/stimulus.md (the FIXED stimulus — sim has no exec to talk to) -->
# Research proposal (fixed stimulus)

Proposal: "We will improve model reasoning by adding a "think harder" instruction
to the prompt and measuring vibes on 5 hand-picked examples. No baseline, no
metric defined yet. We expect it to obviously work."

React to this proposal as the persona you have been given.
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_smoke_test.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'smoke_test'`.

- [ ] **Step 3: Write `sandbox/smoke_test.py`**

```python
"""2B persona-injection smoke test helpers. The real sim-cc spawn is a manual
Bash-tool procedure (see SMOKE_RESULT.md); these helpers build the injection
message and check endpoint divergence. NOT the AS-1 quality gate."""
import json
from pathlib import Path


def build_injection(config_path, stimulus_path):
    cfg = json.loads(Path(config_path).read_text(encoding="utf-8"))
    stimulus = Path(stimulus_path).read_text(encoding="utf-8")
    cfg_text = json.dumps(cfg, indent=2, ensure_ascii=False)
    return (
        "You are role-playing a research-supervisor USER persona defined by the "
        "PolicyCard below. Stay fully in character for the whole conversation.\n\n"
        f"=== PolicyCard ===\n{cfg_text}\n=== end PolicyCard ===\n\n"
        "React to the following fixed stimulus AS this persona would. When you "
        "have given your full in-character reaction, end your message with the "
        "single line: DONE\n\n"
        f"=== Stimulus ===\n{stimulus}\n=== end Stimulus ==="
    )


def diverged(turns0, turns5):
    def assistant_text(turns):
        return " ".join(t["text"] for t in turns if t["role"] == "assistant").lower()
    a, b = assistant_text(turns0), assistant_text(turns5)
    if not a or not b:
        return False
    return a != b


if __name__ == "__main__":   # ponytail: prints the id0 injection for a dry run
    import sys
    print(build_injection(sys.argv[1], sys.argv[2]))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_smoke_test.py -v`
Expected: PASS — 3 passed.

- [ ] **Step 5: Run the REAL smoke test (manual, gated on Task 5 deny-probe = PASS)**

Manual procedure, run from `ladder-foundry/sandbox/` via the Bash tool. For EACH endpoint (id0 then id5), spawn a FRESH sim-cc (between-run independence — no session reuse):

1. Build the injection: `python smoke_test.py ../configs/config_0.json stimulus.md` → copy the printed message.
2. Start a fresh sim: `IS_SANDBOX=1 CLAUDE_CONFIG_DIR="$(pwd)/.claude" claude` in the sandbox cwd.
3. Paste the injection as the first message; let the sim react and emit DONE.
4. Exit that REPL. Read its session jsonl: `python read_session.py --logs-dir "<the CC projects dir>" --cwd "$(pwd)"` (pass the real logs dir on the command line — it is NEVER written into any committed file).
5. Repeat 1–4 with `config_5.json` in a brand-new REPL.

Then verify by eye + `diverged()`: (1) each sim WORE its persona (id0 reaction demands substance/operationalization, id5 reaction is contrarian/low-demand); (2) the two reactions visibly DIVERGE on the same stimulus. This does NOT verify AS-1 quality separation.

- [ ] **Step 6: Write `sandbox/SMOKE_RESULT.md` (de-identified) + commit**

Record ONLY: date; deny-probe verdict (from Task 5); "id0 persona worn: yes/no"; "id5 persona worn: yes/no"; "endpoints diverged: yes/no"; one-sentence qualitative note. NO log path, NO cwd-slug, NO raw transcript.

```bash
git add sandbox/smoke_test.py sandbox/stimulus.md sandbox/SMOKE_RESULT.md tests/test_smoke_test.py
git commit -m "feat(ladder-foundry): 2B persona-injection smoke test + de-identified result

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Done criteria

- **2A:** full pytest suite green (STAGE 1 + STAGE 2: contract, weights, interpolator, gen_configs); human-eye read of the 6 configs confirms id0=genius / id5=contrarian / 1–4 monotone.
- **2B:** deny-under-bypass probe = PASS; both endpoints wear their persona; the two endpoints diverge on the fixed stimulus; `SMOKE_RESULT.md` de-identified.
- **Honest boundary:** STAGE 2 proves the persona core is structurally sound and a real sim-cc wears the persona (loss-1 precursor). It does NOT prove the eventual (graph, result) samples are quality-separated (AS-1) — that needs exec + loss-2 in STAGE 5/6.
