# STAGE 1 Design Spec — Data-Core (L1–L6)

> Date: 2026-06-30 · Project: ladder-foundry · Phase: STAGE 1
> Scope: the data-oriented core — three trainable weights, their JSON schema, W5 leak interceptor. All Windows-local pure functions verified by pytest. No remote, no token, no key.
> Source authority: `D:\YOGSOTH-AI\context\self-iteration\2026-06-07-triple-cc-system\2026-06-06-triple-cc-architecture-design.md` (weights schema L533–556) + Plan B (B1/B2).

## 1. What STAGE 1 is and why it exists

ladder-foundry forges a labeled, monotone good→bad ladder of research samples whose label = the known generating condition (the PolicyCard). The system trains three weights to produce that ladder. STAGE 1 builds the DATA-CORE those weights live in: the JSON schema, the read-only accessor functions, and the W5 leak interceptor. Verified-anti-pattern note: the old `2026-06-06-probe-pretrain/` had NO weights.py at all (no schema, no lock, no revise guard), hard-coded constants in assembler.py, prose baked into axes.py, and a fragile substring leak check. STAGE 1 builds the foundation the old code never had; it does not inherit a single line of old code.

The data-oriented principle (the spine of the whole system): the optimizer trains by changing JSON DATA segments; the `.py` files are PURE READ-ONLY functions whose source never moves. This makes snapshots replayable, training single-variable-controlled, and history immutable.

## 2. Components (6)

| # | File | Role | Trainable weight |
| --- | --- | --- | --- |
| L1 | `generator/weights.py` | 4-segment schema + load / dump_initial / revise | — (the container) |
| L2 | `generator/leak_audit.py` | W5 regex DENY interceptor | — |
| L3 | `generator/axes.py` | pure read of axis_prose | ① 档位话术 |
| L4 | `generator/interpolator.py` | pure read of interp_params + coord_table | ② 插值铺陈层 |
| L5 | `generator/assembler.py` | pure read of assembler_params + coord_table | ③ 组装逻辑 |
| L6 | `generator/cards.py` | PolicyCard → dict serialization | — |

## 3. L1 weights.py — the schema (single authoritative definition)

`weights/<batch>.json` has FOUR top-level segments: three trainable + one locked.

| Top-level key | Weight | Reader | Writer | Trainable? |
| --- | --- | --- | --- | --- |
| `axis_prose` | ① `{axis:{level:body}}`, axis∈{A1..A5}, level∈{L0..L4} (A4 uses C+/C-, A5 uses G+/G-) | `axes.level_text` | `revise(target=axis_prose)` | Yes |
| `interp_params` | ② spread layer: EXACTLY `{collision_offset_axis, endpoint_spread, granularity_map}` | `interpolator.ladder_levels` | `revise(target=interp_params)` | Yes (spread only) |
| `assembler_params` | ③ `{two_stage, field_template, f6_derivation, turn_budget}` | `assembler.build_batch` | `revise(target=assembler_params)` | Yes |
| `frozen_label` | `rank_order{direction,primary_sort}` + `coord_table{}` | interpolator/assembler read-only | **dump_initial ONLY (locked from revise)** | No |

### 3.1 Functions

- `dump_initial(path) -> dict` — export batch-0 from the three weights' defaults (NOT hand-filled). It is the **SOLE writer of `frozen_label`** (decision locked). In STAGE 1 it writes `coord_table: {}` (EMPTY — STAGE 1 does not fabricate placeholder coordinates; real coords come from D2 endpoint personas in STAGE 2, at which point dump_initial re-exports batch-0 with the real coord_table). `rank_order.direction = [0,1,2,3,4,5]` and `primary_sort = ["A1","A3","A2"]` are written here and locked.
- `load(path) -> dict` — read a weights JSON.
- `revise(w, target, key, new, reason) -> dict` — change ONE key of ONE trainable segment, return a revision record `{target,key,old,new,reason}`. **`key` is a dotted path only for `axis_prose`** (e.g. `"A1.L0"` → split into [axis, level]); for `interp_params`/`assembler_params` it is a flat key. When target==axis_prose, validate EXACTLY two segments AND whitelist axis∈{A1..A5} / level∈{L0..L4} (codex footgun: a flat-split would silently accept `A1`, `A1.L0.x`, or unknown labels). Hard rejections (raise ValueError):
  1. `target == "frozen_label"` → reject ("frozen_label not trainable / lifeline of the label").
  2. `target ∉ {axis_prose, interp_params, assembler_params}` → reject (whitelist).
  3. `target=="interp_params" and key=="collision_offset_axis" and new ∉ {"B1","expression"}` → reject (AS-3 enum lock).
  4. malformed axis_prose path (≠2 segments / unknown axis / unknown level) → reject.

`load` AND `revise` both validate the interp_params key-set (§3.2). Not redundant (codex): load-validation catches hand-edited/corrupted JSON before any reader touches it; revise-validation protects the in-memory mutation path and callers that build `w` without going through load.

### 3.2 AS-3 structural isolation (decision locked: schema-level, not just enum)

`interp_params`'s key set is LOCKED to EXACTLY `{collision_offset_axis, endpoint_spread, granularity_map}`. On `load` and on `revise`, validate `set(interp_params.keys()) == {those three}`; ANY extra key → raise ValueError. This is the STRUCTURAL guarantee that no axis-coordinate value can ride inside interp_params under some other key — coordinates physically live only in `frozen_label.coord_table`, a separate top-level segment. The `collision_offset_axis ∈ {B1,expression}` enum is an ADDITIONAL lock on top. Rationale: the fidelity auditor flagged that a one-field enum is necessary but not sufficient — a coord could hide under a different key. The key-set lock closes that.

### 3.3 granularity_map — named-strategy selector (decision locked: eval killed)

`granularity_map` stores a STRATEGY NAME (string), currently only `"round"` = `round(t*(L-1))` where t = rung_id/(n-1), L = number of levels (5). The read-only `.py` does dict-dispatch on the name; there is NO `eval()` of a stored formula (the old plan's eval-of-string is killed — it was arbitrary code execution sitting on a trainable JSON surface). New named strategies are added to the dispatch dict ONLY when STAGE-7 backprop demonstrably needs a new curve. The optimizer "trains" granularity by editing the strategy NAME (data); the curve math lives in read-only code (mechanism) — faithful to data-oriented weights.

## 4. L2 leak_audit.py — W5 interceptor

`leak_audit(text)` raises `LeakHit` if `text` contains any 32-check / 6-primitive / detection-signature term, else returns None. Implementation: a regex DENY list (not fragile substring matching — the old code's anti-pattern). Caller (L7 in STAGE 2) handles a hit via regenerate-then-reaudit (cap 3). NOTE (per the fidelity audit): leak_audit is a BACKSTOP, not the primary W5 control — the primary control is structural role-blindness (generation roles never see the checks). The DENY vocabulary must be reasonably complete (32-check names, 6 primitives, detection-signature phrases, PG/NG-engine, pseudo-good/novel-good); documented as a backstop.

## 5. L3/L4/L5 — three weight bodies (pure read-only)

All three read their segment from a loaded weights dict; source never moves; training = changing the JSON.

- **L3 `axes.py` ①**: `level_text(w, axis, level) -> str` — returns `w["axis_prose"][axis][level]`. That is all.
- **L4 `interpolator.py` ②**: `ladder_levels(w, n=6) -> list[dict]`. Reads `direction` (LOCKED) from `frozen_label.rank_order`, `interp_params` (spread layer), and `coord_table` from `frozen_label`. For each rung i in direction[:n]: t = i/(n-1); level_idx via the named granularity strategy; **coordinates are READ FROM `coord_table`, never computed by the spread layer** (the structural guard the audit demanded — the locked coordinate layer is load-bearing by construction). Each rung dict carries `{rung_id, level_idx, collision_offset_axis, coord}`. When coord_table is empty (STAGE 1 batch-0), there are no coords to read — this is CORRECT, because STAGE 1 never runs a real batch; pytest feeds a small fixture coord_table to exercise the read path, and NEVER asserts a real ladder out of an empty table.
  - **★Monotonicity is NONDECREASING, not strict (codex finding, write into the test)**: for n=6, L=5, `round(t*(L-1)) = round(i*4/5)` maps rung ids [0,1,2,3,4,5] → level indices **[0,1,2,2,3,4]** — one COLLISION at level 2, no gaps. So `test_ladder_nondecreasing` asserts level_idx is nondecreasing along direction (NOT strictly increasing). This collision is EXACTLY why `collision_offset_axis` exists: STAGE-2+ uses B1/expression to stagger the two rungs that land on level 2, never an A1–A5 axis. (Also: Python `round()` is banker's-rounding on exact .5 ties — not biting [0,1,2,2,3,4] but a future semantics trap if L/n change; note it in code.) `detect_collapse` is CUT from STAGE 1 (codex + ponytail): it is neither load-bearing for the schema/lock/handoff invariants nor needed to prove the read-only contract; add it in STAGE 6 if loss-2 needs collision-point detection.
- **L5 `assembler.py` ③**: `build_batch(w, n, topic_id) -> list[dict]`. Reads `assembler_params` (the externalized constants the old code hard-coded: two_stage, field_template, f6_derivation, turn_budget=F8). Calls ladder_levels, assembles per-rung coordinate cards. Collision perturbation lands ONLY on `collision_offset_axis` (∈{B1,expression}), NEVER on A1–A5 — guaranteed because the only offset source is interp_params.collision_offset_axis which the schema locks.

## 6. L6 cards.py — serialization

`to_dict(card) -> dict` — PolicyCard → `{F0..F9, axis_levels}`, JSON-serializable. Trivial.

## 7. Three-layer verification (the "is it CORRECT, not just green" answer)

Green tests prove "the code does what I asserted"; they do NOT prove my assertions match the project plan. So STAGE 1 verifies correctness at three independent layers:

### Layer 1 — per-component pytest (L1 self-correct)
TDD red→green. Each test NAME is a human-readable invariant. Required tests:
- L1: `test_dump_initial_has_four_segments`, `test_revise_rejects_frozen_label`, `test_revise_rejects_unknown_target`, `test_collision_offset_rejects_label_axis`, `test_collision_offset_accepts_b1_expression`, `test_interp_params_key_set_locked` (extra key → ValueError, the AS-3 structural lock), `test_coord_table_empty_in_batch0`, `test_revise_changes_data_not_source` (axes.py source byte-identical before/after).
- L2: `test_clean_text_passes`, `test_denies_check_signature`.
- L3/L4/L5: read-from-fixture-coord_table tests; L4 `test_rank_direction_locked` (direction [0..5]) + `test_ladder_nondecreasing` (level_idx [0,1,2,2,3,4], nondecreasing not strict); L5 `test_collision_offset_never_label_axis`.
- L6: `test_to_dict_has_f0_f9`.

### Layer 2 — cross-step consumption test (correct FOR THE SYSTEM)
This answers "what this step produces, the next step can actually use, in the shape the plan requires." A `tests/test_stage1_handoff.py` proves L1's output is really consumable by its downstream:
- `test_L3_consumes_dump_initial`: dump_initial → axes.level_text reads prose back.
- `test_L4_consumes_dump_initial`: same batch-0 (+ fixture coords) → ladder_levels yields 6 rungs, direction [0..5].
- `test_L5_consumes_dump_initial`: → build_batch yields 6 cards, perturbation axis ∈ {B1,expression}.
Downstream really ingests L1's output → proves L1 is correct for the system, not just self-consistent.

### Layer 3 — codex independent audit (different model family, no self-confirmation)
Tests and code are both mine → same-source error risk. So codex (different model family, the same instrument the whole system uses for loss) audits the finished L1 output + the authoritative schema table (§3), WITHOUT seeing my tests, and judges whether the produced batch-0.json conforms to the design plan. Only if codex concurs is "I marked my own homework" ruled out.

### Honest boundary — what STAGE 1 CANNOT verify
STAGE 1 verifies the STRUCTURAL and INTERFACE layers (schema conforms, downstream connects, locks hold). It CANNOT verify the SEMANTIC layer ("does the prose actually force a quality ladder") — that needs loss-2 to run in STAGE 6. The spec does not pretend L1's green tests prove whole-system semantic correctness.

## 8. Human-verifiable deliverables

1. **`pytest -v` green list** — each test name = one invariant, human-readable.
2. **`demo.py` health report** — prints batch-0 anatomy + attack tests in plain language (4 segments present, interp_params 3-key-locked, contains-coord? no, coord_table empty, rank locked; then: revise frozen_label → rejected, set collision=A2 → rejected, inject extra interp_params key → rejected, legal revise axis_prose → ok + axes.py source unchanged). Human reads it without reading code.
3. **Contract reconciliation table** — maps each batch-0 field to the design-doc authoritative schema (§3) and to its downstream consumer (L3/L4/L5/L13), proving L1's output IS the structure the system agreed on.

## 9. File structure

```text
ladder-foundry/                       # <proj> root (code lives directly here, no probe-pretrain subdir)
├── generator/
│   ├── weights.py        # L1
│   ├── leak_audit.py     # L2
│   ├── axes.py           # L3 ①
│   ├── interpolator.py   # L4 ②
│   ├── assembler.py      # L5 ③
│   └── cards.py          # L6
├── demo.py               # human-readable health report (deliverable 2)
└── tests/
    ├── test_weights.py test_leak_audit.py test_axes.py
    ├── test_interpolator.py test_assembler.py test_cards.py
    └── test_stage1_handoff.py   # Layer-2 cross-step consumption
```

## 10. Build order (TDD, each green before next)
L1 → L2 → L3 → L4 → L5 → L6 → handoff test → demo.py → codex audit. Each: failing test → red → minimal impl → green → commit.

## 11. Decisions locked this round
1. coord_table EMPTY in batch-0 (no placeholder); L4/L5 READ coords from it (locked layer load-bearing by construction); pytest uses fixture coords, never asserts a ladder from empty.
2. dump_initial is the SOLE writer of frozen_label (STAGE 1 writes empty coords, STAGE 2 writes real); revise never touches frozen_label.
3. AS-3 isolation = structural key-set lock on interp_params (+ collision enum), not just the enum.
4. granularity_map = named-strategy selector (eval killed).
5. Three-layer verification (pytest + handoff + codex audit); semantic layer explicitly deferred to STAGE 6.
