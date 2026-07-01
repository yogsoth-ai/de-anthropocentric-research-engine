# ladder-foundry STAGE 4 — Loss Skills + Optimizer Brain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Author the 7 STAGE-4 artifacts (2 exec contracts, 2 codex loss judges, 1 leaf script, 1 thick optimizer skill, 1 references pair) that turn the STAGE 1–3 core into the loss layer + optimizer brain a real three-layer-nested CC run (STAGE 5) will execute.

**Architecture:** Five artifacts are prompt files (CC/codex scripts, not runnable Python); one (`run_codex_loss.py`) is the last leaf script with its codex edge isolated behind an injectable `codex_fn`; one (`optimization-loop`) is the thick SKILL that plays the whole training loop. STAGE 4 crosses the all-local line: what CAN be checked locally (leak-audit, fence-contract-vs-`concat_triple`, schema validation, `run_codex_loss` payload/parse/τ/landing plumbing, `§tools` leaf-name/threshold introspection) is verified now; codex semantics and the end-to-end nested run are honestly marked STAGE-5-deferred, never faked green.

**Tech Stack:** Python 3.12 stdlib only (NO new deps — ladder-foundry is dep-free through STAGE 3; `pytest` for tests, `subprocess` for CLI checks); Markdown SKILL.md (skill-creator frontmatter); JSON Schema files validated by a minimal in-house validator (no `jsonschema` dep).

## Global Constraints

(Every task's requirements implicitly include this section. Values are verbatim from the spec.)

- **W5 leak boundary:** generation + loss skills are check-blind — never name the 32 checks / 6 primitives / detection signatures / PG·NG engine. Every SKILL.md + reference + schema passes `generator.leak_audit.leak_audit(text)` (raises `LeakHit`). The probe is the ONLY check-seeing session.
- **D1–D5 standard ONLY** for loss-2 quality judging (D1 meaningfulness / D2 skill-research value / D3 use-to-DARE / D4 respects 4-layer / D5 prerequisites). Academic standards (novelty / baseline / rigor / citations / publishability) are FORBIDDEN as judging criteria.
- **Privacy red line:** `save_transcript.py --logs-dir` is REQUIRED with no default; no CC-log absolute path / cwd-slug in any committed artifact; trace `transcript_path` is relative; committed outputs are de-identified; API-key VALUES never committed. `run_codex_loss.py` never reads CC logs (its transcript input is already de-identified by `save_transcript`).
- **NO `-p` / `--resume` / `--session-id` / `--allowedTools` anywhere** — not even in design text. All three CC layers are normal interactive REPLs. (These are `claude` flags; `codex exec` flags are unaffected.)
- **Child-CC launch:** a parent CC directly runs `claude` in its own Bash tool (`IS_SANDBOX=1` + child `CLAUDE_CONFIG_DIR` + `cd`); NO driver script / NO PTY/pexpect / NO tmux for children (tmux only for the optimizer host); NO `drive_cc.py`. Fresh sim/exec each run (between-run independence); only the optimizer is continuous. Authoritative transcript = exec session jsonl.
- **Data-oriented invariant:** training edits weights JSON DATA segments only; `.py` sources never move; `frozen_label` is LOCKED (enforced by `weights.revise`, which raises on it); `collision_offset_axis ∈ {B1, expression}` only. ONE weight changed per batch (先归因再动手 / attribute-first).
- **no-fake-stub:** `run_codex_loss`'s codex edge is NEVER fake-stubbed to go green. Local tests inject a fake `codex_fn` at the network boundary ONLY, to verify plumbing; no local test asserts a gate outcome (`fidelity_rate≥0.90`, `monotonicity_pass`, `endpoint_separation_pass`) from canned codex output (the pinned forbidden line).
- **Threshold single-source:** `0.90`/`0.80` live in `gate_eval.py` module constants (STAGE 3); numbers a STAGE-4 script computes with (`TAU_MIN`, `ENDPOINT_K`, `ENDPOINT_ALLOWANCE`, `RIGOR_FLOOR_EPS`) live as that script's module constants; `references/gate-thresholds.md` is the human index that POINTS BACK to those owners and is the home only for CC/codex-read numbers that no script owns (丙 line `0.80`, drift ε). No number is copied into a second code/doc location.
- **Skill structure:** 1 thick (`optimization-loop`: SKILL.md + scripts/ + references/) + 4 light (single SKILL.md, +co-located schema for the 2 loss judges; no scripts/ or references/).
- **Naming:** `formated-specs` and `formated-results` are BOTH PLURAL (the prototype's singular `formated-result` is a typo).
- **Branch:** `self-iteration/ladder-foundry` — do NOT branch off, do NOT push main, do NOT merge/finish. Commit only at each task's final step. Write/Edit calls stay under 13000 chars (build large files in parts). Commit trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- **Declared deviations (not defects):** D1 — leaves NOT moved into `optimization-loop/scripts/`; `§tools` references them by relative anchor `../../scripts/<name>.py` + `../../generator/gen_configs.py` (moving them would break STAGE-3's verified `parents[1]` import). M1 — `gen_configs` `config_{rung}.json` naming collision is annotated, NOT fixed here (a standalone STAGE-2 patch for before STAGE 5).

---

## File Structure (decomposition lock)

All new files land under `ladder-foundry/`. Tests run with pytest from the `ladder-foundry/` directory (so subprocess paths are `scripts/...`). Existing files (`generator/`, `scripts/`, `sandbox/`) are UNTOUCHED.

| File | Responsibility | Task |
| --- | --- | --- |
| `skills/formated-specs/SKILL.md` | exec spec-slot skill → emits one `research-graph` JSON fenced block into the dialogue | T1 |
| `skills/formated-results/SKILL.md` | exec closing skill → emits one `research-result` JSON fenced block, same-source paired | T1 |
| `tests/test_formated_contract.py` | leak-audit both SKILL.md + fence red/green against `concat_triple.py` | T1 |
| `skills/injection-fidelity/SKILL.md` | loss-1 codex judge prompt (6 signals, bands, drift gate, falsifiers) | T2 |
| `skills/injection-fidelity/loss1.schema.json` | authoritative loss-1 output schema | T2 |
| `tests/test_injection_fidelity.py` | leak-audit + schema validity + band arithmetic + coord cross-check | T2 |
| `skills/ladder-quality-order/SKILL.md` | loss-2 codex judge prompt (pairwise, endpoint K-vote, z⊥C, D1–D5 only) | T3 |
| `skills/ladder-quality-order/loss2.schema.json` | authoritative loss-2 output schema | T3 |
| `tests/test_ladder_quality_order.py` | leak-audit + schema validity + downstream gate_eval alignment | T3 |
| `skills/optimization-loop/scripts/run_codex_loss.py` | assemble payload → call `codex_fn` → validate → land `loss/*.json` | T4 |
| `skills/optimization-loop/scripts/loss1.schema.json` | byte-identical copy of the authoritative loss-1 schema (the one the script reads) | T4 |
| `skills/optimization-loop/scripts/loss2.schema.json` | byte-identical copy of the authoritative loss-2 schema | T4 |
| `tests/test_run_codex_loss.py` | subprocess plumbing (payload, shuffle reversibility, τ, K-vote, landing, bad-JSON exit 2) | T4 |
| `skills/optimization-loop/SKILL.md` | optimizer brain: §loop/§gate/§backprop/§state/§tools | T5 |
| `tests/test_optimization_loop.py` | §tools leaf-name/CLI introspection + §backprop target/key ⊆ weights, leak-audit | T5 |
| `skills/optimization-loop/references/gate-thresholds.md` | threshold index (points back, new numbers only) | T6 |
| `skills/optimization-loop/references/backprop-heuristic.md` | attribution heuristic expanded | T6 |
| `tests/test_references_audit.py` | leak-audit both references + threshold point-back grep | T6 |
| `tests/test_stage4_audit.py` | global W5 sweep + banned-flag word audit + privacy grep over `skills/` | T7 |

**Codex-edge interface (locked, used by T4 + referenced by T5):**
`codex_fn(payload: str, schema_path: str) -> str` returns a raw JSON string. The real default `_default_codex_call` shells out to `codex exec --output-schema <schema_path> -o <tmp> <payload>` (cwd `/workspace/work/loss`, config `/workspace/home/loss/.codex`); it NEVER runs in local tests. Tests inject a fake `codex_fn` at this boundary only.
- **loss-1:** ONE `codex_fn` call; its return IS the final artifact (validated against `loss1.schema.json`, written to `--out`). codex fills the whole schema.
- **loss-2:** codex does NOT compute τ/Copeland (harness-side). ONE "rank" call returns `{"pairwise":[{"i":int,"j":int,"winner":int,"reason":str}]}` (positions, 15 entries); then `ENDPOINT_K` independent "endpoint" calls each return `{"winner":int,"reason":str}` for the (id0,id5) pair. `run_codex_loss` un-shuffles, Copeland-aggregates, computes Kendall τ, counts endpoint wins `w0`, assembles the final artifact, validates it against `loss2.schema.json`, writes it. The rank/endpoint codex-facing schemas are small inline dicts (`RANK_SCHEMA` / `ENDPOINT_SCHEMA`) written to a tmp file for the real call — NOT committed schema files.

---

## Task 1: formated-specs + formated-results (exec contracts, paired)

**Files:**
- Create: `ladder-foundry/skills/formated-specs/SKILL.md`
- Create: `ladder-foundry/skills/formated-results/SKILL.md`
- Test: `ladder-foundry/tests/test_formated_contract.py`

**Interfaces:**
- Consumes: STAGE-3 `scripts/concat_triple.py` (`last_block(md, info)` cuts the LAST ` ```<info> ` fenced JSON block; `info` ∈ {`research-graph`, `research-result`}; missing → `ValueError` → non-zero exit). `generator/leak_audit.py::leak_audit(text)` (raises `LeakHit`).
- Produces: two SKILL.md prompt files. No Python symbols. Downstream (T5 §loop) names these two skills as exec's two mandatory steps.

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_formated_contract.py`:

```python
import json
import subprocess
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]          # ladder-foundry/
SPECS = LF / "skills" / "formated-specs" / "SKILL.md"
RESULTS = LF / "skills" / "formated-results" / "SKILL.md"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit, LeakHit


def test_both_skill_md_exist():
    assert SPECS.exists() and RESULTS.exists()


def test_skill_md_are_leak_clean():
    leak_audit(SPECS.read_text(encoding="utf-8"))      # raises LeakHit on any check vocab
    leak_audit(RESULTS.read_text(encoding="utf-8"))


def test_frontmatter_names_are_plural():
    assert "name: formated-specs" in SPECS.read_text(encoding="utf-8")
    assert "name: formated-results" in RESULTS.read_text(encoding="utf-8")


def _make_run(tmp_path, graph_blocks, result_blocks):
    rd = tmp_path / "runs" / "r0"
    for sub in ("configs", "transcripts", "triples"):
        (rd / sub).mkdir(parents=True)
    (rd / "configs" / "s.json").write_text('{"rung_id": 0}', encoding="utf-8")
    md = "# transcript\n\n"
    for g in graph_blocks:
        md += "```research-graph\n" + json.dumps(g) + "\n```\n\n"
    for r in result_blocks:
        md += "```research-result\n" + json.dumps(r) + "\n```\n\n"
    (rd / "transcripts" / "s.md").write_text(md, encoding="utf-8")
    return rd


def _run_concat(rd):
    return subprocess.run([sys.executable, "scripts/concat_triple.py",
                           "--run-dir", str(rd), "--sample", "s"],
                          cwd=str(LF), capture_output=True, text=True)


def test_fence_contract_green(tmp_path):
    rd = _make_run(tmp_path, [{"nodes": []}], [{"title": "only"}])
    r = _run_concat(rd)
    assert r.returncode == 0, r.stderr
    tri = json.loads((rd / "triples" / "s.json").read_text(encoding="utf-8"))
    assert set(tri) == {"research_config", "research_graph", "research_result"}
    assert tri["research_result"]["title"] == "only"


def test_takes_last_result_block(tmp_path):
    rd = _make_run(tmp_path, [{"nodes": []}],
                   [{"title": "draft"}, {"title": "final"}])
    assert _run_concat(rd).returncode == 0
    tri = json.loads((rd / "triples" / "s.json").read_text(encoding="utf-8"))
    assert tri["research_result"]["title"] == "final"


def test_missing_result_fence_nonzero(tmp_path):
    rd = _make_run(tmp_path, [{"nodes": []}], [])     # no research-result fence
    assert _run_concat(rd).returncode != 0


def test_wrong_info_string_drift_nonzero(tmp_path):
    rd = tmp_path / "runs" / "r0"
    for sub in ("configs", "transcripts", "triples"):
        (rd / sub).mkdir(parents=True)
    (rd / "configs" / "s.json").write_text("{}", encoding="utf-8")
    # ```json drift instead of ```research-graph -> concat findall empties -> ValueError
    (rd / "transcripts" / "s.md").write_text(
        '```json\n{"nodes": []}\n```\n\n```research-result\n{"title":"x"}\n```\n',
        encoding="utf-8")
    assert _run_concat(rd).returncode != 0
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_formated_contract.py -v`
Expected: FAIL — `test_both_skill_md_exist` / leak / frontmatter fail because the SKILL.md files do not exist yet. (Fence tests may pass already since they exercise the delivered `concat_triple.py` — that is fine; they are the contract pin.)

- [ ] **Step 3: Author `skills/formated-specs/SKILL.md`**

Create `ladder-foundry/skills/formated-specs/SKILL.md` (W5-clean — no check/primitive vocabulary; only field names F0–F9, axes A1–A5, and the D1–D5 standard):

````markdown
---
name: formated-specs
description: Spec-slot skill for the research-executor. Emit the 4-layer DARE orchestration of the assigned topic as one research-graph JSON fenced block in your reply. Replaces the generic spec-writing step.
---

# formated-specs

You occupy the spec step of the research executor. Instead of writing a spec
file, you emit the orchestration you are about to (notionally) run as a single
JSON object inside one fenced block, directly in your reply.

## Hard contract

1. Emit exactly one fenced block opened with ` ```research-graph ` (that exact
   info-string, hyphen, NOT ` ```json `) and closed with ` ``` `.
2. The block body is a single valid JSON object, the schema below.
3. Emit it **into your reply (the dialogue)** — do NOT write it to a file. The
   block lands in this session's transcript; the harness cuts it from there.
4. Atomicity: produce the whole block within one assistant turn.
5. If you revise after pushback, emit a new full `research-graph` block; the
   harness keeps the LAST one. Never emit a half block.
6. Mandatory final step: after the graph block, load and run `formated-results`.

## research-graph schema

```json
{
  "nodes":        [ {"id": "n1", "skill": "<skill-name>", "layer": "campaign|strategy|tactic|sop"} ],
  "edges":        [ {"from": "n1", "to": "n2", "kind": "calls|sequences"} ],
  "layer_labels": { "n1": "campaign|strategy|tactic|sop" },
  "manifest":     [ "<skill actually orchestrated>" ],
  "prereq_dag":   [ {"node": "n2", "requires": ["n1"]} ]
}
```

Populate `manifest` only with skills you actually orchestrated; do not
fabricate. `layer` and `layer_labels` must respect the 4-layer architecture
(campaign → strategy → tactic → sop). Judge nothing against academic
standards; this is a structural record of orchestration only.
````

- [ ] **Step 4: Author `skills/formated-results/SKILL.md`**

Create `ladder-foundry/skills/formated-results/SKILL.md`:

````markdown
---
name: formated-results
description: Closing skill for the research-executor, loaded as the last step of formated-specs. Summarize the design just produced into one research-result JSON fenced block in your reply. Do not execute the research.
---

# formated-results

You are the closing step, loaded by `formated-specs`. Summarize the design you
just produced into one fenced block, in the same dialogue. Add no new
research — only summarize what `formated-specs` already orchestrated.

## Hard contract

1. Emit exactly one fenced block opened with ` ```research-result ` (that exact
   info-string) and closed with ` ``` `.
2. Body is a single valid JSON object, the schema below.
3. Emit it **into your reply (the dialogue)**, not to a file.
4. Atomicity: one assistant turn.
5. On revision, emit a new full block; the harness keeps the LAST one.
6. Same-source: only summarize the design `formated-specs` produced. The depth
   is document-level (hypothesis + design body); do not run experiments.

## research-result schema

```json
{
  "title":     "<one-line title of the design>",
  "sections":  [ {"heading": "<section heading>", "body": "<design prose>"} ],
  "artifacts": [ "<spec filename or figure reference>" ]
}
```

Sections carry the design body. Judge nothing against academic standards.
````

- [ ] **Step 5: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_formated_contract.py -v`
Expected: PASS (all 7 tests green).

- [ ] **Step 6: Commit**

```bash
cd ladder-foundry
git add skills/formated-specs/SKILL.md skills/formated-results/SKILL.md tests/test_formated_contract.py
git commit -m "feat(stage4): formated-specs + formated-results exec contracts (T1)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 2: injection-fidelity (loss-1 codex judge)

**Files:**
- Create: `ladder-foundry/skills/injection-fidelity/SKILL.md`
- Create: `ladder-foundry/skills/injection-fidelity/loss1.schema.json`
- Test: `ladder-foundry/tests/test_injection_fidelity.py`

**Interfaces:**
- Consumes: `generator/leak_audit.py::leak_audit`. `generator/weights.py::_COORD_TABLE` (the locked rung→coord map: rung 0 = `A1:L4,A3:L4,A2:L4,A4:C+,A5:G+`; rung 5 = all `L0`,`A4:C-`,`A5:G0`) for the band cross-check.
- Produces: `loss1.schema.json` (the authoritative loss-1 output schema; T4 copies it byte-identical beside `run_codex_loss.py`). The schema's required keys are the contract T4's minimal validator enforces.

**Band definition (locked, used by SKILL.md prose AND the test):**
Continuous axes A1/A3 map a rate in [0,1] to 5 non-overlapping bands, monotone increasing with level: `L0=[0,.10]`, `L1=(.10,.30]`, `L2=(.30,.55]`, `L3=(.55,.80]`, `L4=(.80,1]`. Direction: HIGHER level → HIGHER rate (more pushback / more operationalization-demand). The A1 mirror signal `accept_without_question_rate` uses the `1−x`-flipped band (HIGHER level → LOWER acceptance). Overlay axes: A2 flag = `card.A2 ∈ {L0,L1}` → demand-incoherence expected; A4 by C-/C0/C+ event-bit combos; A5: `G+` → `novel_seed_count ≥ 1`, `G0` → `novel_seed_count ≤ 1`.

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_injection_fidelity.py`:

```python
import json
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILL = LF / "skills" / "injection-fidelity" / "SKILL.md"
SCHEMA = LF / "skills" / "injection-fidelity" / "loss1.schema.json"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit
from generator.weights import _COORD_TABLE


def test_files_exist():
    assert SKILL.exists() and SCHEMA.exists()


def test_skill_and_schema_leak_clean():
    leak_audit(SKILL.read_text(encoding="utf-8"))
    leak_audit(SCHEMA.read_text(encoding="utf-8"))


def test_schema_is_valid_json_with_required_keys():
    s = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert s.get("additionalProperties") is False
    req = set(s["required"])
    assert {"fidelity", "loss1", "per_axis_evidence", "drift_flag"} <= req
    props = s["properties"]
    assert props["fidelity"]["type"] == "boolean"
    assert props["loss1"]["type"] == "number"
    assert props["drift_flag"]["type"] == "boolean"


def test_six_rung_expected_matrix_matches_coord_table():
    # A1 increases with rung quality: rung 0 -> L4 band, rung 5 -> L0 band
    assert _COORD_TABLE["0"]["A1"] == "L4"
    assert _COORD_TABLE["5"]["A1"] == "L0"
    # the SKILL.md must state the same monotone direction; assert it names A1 + pushback
    txt = SKILL.read_text(encoding="utf-8")
    assert "A1" in txt and "pushback" in txt.lower()


def test_consistency_rule_documented():
    # loss1 == count(pass)/5 and fidelity == all(pass) and not drift -- must be in prose
    txt = SKILL.read_text(encoding="utf-8")
    assert "/5" in txt or "/ 5" in txt
    assert "drift" in txt.lower()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_injection_fidelity.py -v`
Expected: FAIL — `test_files_exist` and the schema/leak tests fail (files absent).

- [ ] **Step 3: Author `skills/injection-fidelity/loss1.schema.json`**

Create `ladder-foundry/skills/injection-fidelity/loss1.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "additionalProperties": false,
  "required": ["fidelity", "loss1", "per_axis_evidence", "drift_flag"],
  "properties": {
    "fidelity": {"type": "boolean"},
    "loss1": {"type": "number", "minimum": 0, "maximum": 1},
    "drift_flag": {"type": "boolean"},
    "note": {"type": "string"},
    "per_axis_evidence": {
      "type": "object",
      "additionalProperties": false,
      "required": ["A1", "A2", "A3", "A4", "A5"],
      "properties": {
        "A1": {"$ref": "#/definitions/axis"},
        "A2": {"$ref": "#/definitions/axis"},
        "A3": {"$ref": "#/definitions/axis"},
        "A4": {"$ref": "#/definitions/axis"},
        "A5": {"$ref": "#/definitions/axis"}
      }
    }
  },
  "definitions": {
    "axis": {
      "type": "object",
      "additionalProperties": false,
      "required": ["observed", "expected_band", "pass", "quote"],
      "properties": {
        "observed": {"type": ["number", "string", "boolean"]},
        "expected_band": {"type": "string"},
        "pass": {"type": "boolean"},
        "quote": {"type": "string", "minLength": 1}
      }
    }
  }
}
```

- [ ] **Step 4: Author `skills/injection-fidelity/SKILL.md`**

Create `ladder-foundry/skills/injection-fidelity/SKILL.md` (W5-clean; the codex judge prompt). Build it in two Write/Edit parts if it approaches 13000 chars. Content (verbatim structure):

````markdown
---
name: injection-fidelity
description: Loss-1 judge (codex role). Given one sample's de-identified dialogue and its PolicyCard, decide axis-by-axis whether the user-simulator enacted the card's per-axis pressure. Judge enactment of the card, never whether the research is good.
---

# injection-fidelity (loss-1)

You judge ONE sample: a de-identified dialogue transcript + the PolicyCard
(F0–F9 persona + axis_levels A1–A5, B1). Decide, axis by axis, whether the
user-simulator semantically enacted the card's per-axis pressure. You judge
"was the card enacted", never "is the research good". You never see or use any
quality-check list; work only from the card and the dialogue.

## Pressure window

Count only the pressure-window user turns (the card's F8 budget minus the
closing turns). Normalize every rate by that count (`pressure_turns`).

## The 6 signals → axes

| Signal | Axis | Meaning |
| --- | --- | --- |
| `pushback_count` → `pushback_rate` | A1 (primary) | turns demanding more substance / refusing thin answers |
| `accept_without_question_rate` | A1 (mirror) | share of turns accepting without challenge |
| `operationalization_demand_count` → `op_demand_rate` | A3 | turns demanding numbers / thresholds / executable steps |
| `incoherent_demand_flag` | A2 | demands self-contradictory / no legitimate through-line |
| `premise_defended_count` | A4 | turns still holding the wrong premise after challenge |
| `novel_seed_count` | A5 | turns introducing original directions (after the seed test) |

Event bits: `premise_dropped` / `premise_revised` (A4 trajectory).

**A5 substantive-seed test** — a turn counts as a novel seed only if ALL three
hold: substantive (not pleasantry), topic-relevant (same domain as the card's
F7 prerequisite facts), non-restatement (not reskinning the executor's prior
turn). Each counted seed carries a `quote` + the 3 judgments in
`per_axis_evidence.A5`.

## Expected bands (continuous axes A1, A3)

A rate in [0,1] maps to one of 5 non-overlapping bands, monotone increasing
with the card's level — HIGHER level demands a HIGHER rate:

- L0 = [0, .10], L1 = (.10, .30], L2 = (.30, .55], L3 = (.55, .80], L4 = (.80, 1]

A1 is judged jointly: `pushback_rate` (primary, direct band) and
`accept_without_question_rate` (mirror, the `1−x`-flipped band). The two
directions must agree; if they contradict, A1 fails.

Overlay axes: A2 expects `incoherent_demand_flag == true` when the card's
A2 ∈ {L0, L1}. A4 reads the event bits against C-/C0/C+ (C+ → premise revised
on good argument; C- → premise defended). A5: `G+` → `novel_seed_count ≥ 1`;
`G0` → `novel_seed_count ≤ 1`.

## Drift gate

Split the pressure window into halves. Both halves' rates must stay in-band.
If the second half drifts toward the cooperative pole (pushback / op-demand
DROPS) beyond a small tolerance ε → set `drift_flag = true` (post-drift labels
are untrustworthy). Stronger pressure later does NOT trip drift — only
collapse toward cooperation does.

## Verdict

- `per_axis_evidence[ax].pass = (observed band == expected band)` for ax ∈ A1–A5.
- `fidelity = all(pass for A1..A5) AND (not drift_flag)`.
- `loss1 = count(pass for A1..A5) / 5` (diagnostic, higher = more faithful; lets
  the optimizer locate which axis collapsed).
- B1 is a confound, off-spine, NOT in the fidelity AND.

Emit exactly the JSON of `loss1.schema.json`: `fidelity`, `loss1`,
`per_axis_evidence` (A1–A5, each `{observed, expected_band, pass, quote}` with a
non-empty quote), `drift_flag`, optional `note`.

## Three things you must not get wrong

1. Counts match but the pressure is surface-only — a "why?" with no substance
   is NOT A1 pushback. Require a non-empty quote proving substantive pressure.
2. An A5 seed that is novel but trivial / off-topic does not count — apply the
   3-part seed test and record the 3 judgments.
3. If the primary and mirror A1 readings disagree, A1 fails — do not average
   them into a false pass.
````

- [ ] **Step 5: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_injection_fidelity.py -v`
Expected: PASS (all tests green).

- [ ] **Step 6: Commit**

```bash
cd ladder-foundry
git add skills/injection-fidelity/ tests/test_injection_fidelity.py
git commit -m "feat(stage4): injection-fidelity loss-1 codex judge + schema (T2)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 3: ladder-quality-order (loss-2 codex judge)

**Files:**
- Create: `ladder-foundry/skills/ladder-quality-order/SKILL.md`
- Create: `ladder-foundry/skills/ladder-quality-order/loss2.schema.json`
- Test: `ladder-foundry/tests/test_ladder_quality_order.py`

**Interfaces:**
- Consumes: `generator/leak_audit.py::leak_audit`. STAGE-3 `scripts/gate_eval.py topic` (`--mono` / `--endpoint` take the string `"true"`/`"false"`; `--fidelity-rate` is a float). The bool fields here feed those two flags downstream.
- Produces: `loss2.schema.json` (authoritative; T4 copies it byte-identical beside `run_codex_loss.py`). Fields `monotonicity_pass` → `gate_eval --mono`, `endpoint_separation_pass` → `gate_eval --endpoint` (lower-cased to `"true"`/`"false"` by the optimizer).

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_ladder_quality_order.py`:

```python
import json
import sys
import subprocess
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILL = LF / "skills" / "ladder-quality-order" / "SKILL.md"
SCHEMA = LF / "skills" / "ladder-quality-order" / "loss2.schema.json"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit


def test_files_exist():
    assert SKILL.exists() and SCHEMA.exists()


def test_skill_and_schema_leak_clean():
    leak_audit(SKILL.read_text(encoding="utf-8"))
    leak_audit(SCHEMA.read_text(encoding="utf-8"))


def test_schema_required_keys_and_optional_fields_omitted():
    s = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert s.get("additionalProperties") is False
    req = set(s["required"])
    assert req == {"tau", "monotonicity_pass", "endpoint_separation_pass",
                   "rigor_floor_flag", "pairwise_log"}
    props = set(s["properties"])
    # ponytail must-fix: STAGE-5 optional fields are NOT in the schema
    assert "calibration_handoff" not in props
    assert "confound_flat_pass" not in props
    assert s["properties"]["tau"]["type"] == "number"
    for b in ("monotonicity_pass", "endpoint_separation_pass", "rigor_floor_flag"):
        assert s["properties"][b]["type"] == "boolean"


def test_pairwise_log_item_shape():
    s = json.loads(SCHEMA.read_text(encoding="utf-8"))
    item = s["properties"]["pairwise_log"]["items"]
    assert set(item["required"]) == {"i", "j", "winner", "reason"}
    assert item["properties"]["reason"]["minLength"] == 1


def test_downstream_gate_alignment():
    # the two bools, lower-cased, must be the exact strings gate_eval topic accepts
    r = subprocess.run([sys.executable, "scripts/gate_eval.py", "topic",
                        "--fidelity-rate", "0.95", "--mono", "true",
                        "--endpoint", "true"],
                       cwd=str(LF), capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout.strip() == "true"
    r2 = subprocess.run([sys.executable, "scripts/gate_eval.py", "topic",
                         "--fidelity-rate", "0.95", "--mono", "false",
                         "--endpoint", "true"],
                        cwd=str(LF), capture_output=True, text=True)
    assert r2.stdout.strip() == "false"


def test_d1_d5_only_no_academic_criteria():
    txt = SKILL.read_text(encoding="utf-8").lower()
    for forbidden in ("novelty", "baseline", "citation", "publishab", "peer review"):
        assert forbidden not in txt, forbidden
    assert "d1" in txt and "d5" in txt
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_ladder_quality_order.py -v`
Expected: FAIL — `test_files_exist` + schema/leak tests fail (files absent). `test_downstream_gate_alignment` passes already (exercises the delivered `gate_eval.py`).

- [ ] **Step 3: Author `skills/ladder-quality-order/loss2.schema.json`**

Create `ladder-foundry/skills/ladder-quality-order/loss2.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "additionalProperties": false,
  "required": ["tau", "monotonicity_pass", "endpoint_separation_pass",
               "rigor_floor_flag", "pairwise_log"],
  "properties": {
    "tau": {"type": "number", "minimum": -1, "maximum": 1},
    "monotonicity_pass": {"type": "boolean"},
    "endpoint_separation_pass": {"type": "boolean"},
    "rigor_floor_flag": {"type": "boolean"},
    "pairwise_log": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["i", "j", "winner", "reason"],
        "properties": {
          "i": {"type": "integer"},
          "j": {"type": "integer"},
          "winner": {"type": "integer"},
          "reason": {"type": "string", "minLength": 1}
        }
      }
    }
  }
}
```

- [ ] **Step 4: Author `skills/ladder-quality-order/SKILL.md`**

Create `ladder-foundry/skills/ladder-quality-order/SKILL.md` (W5-clean; D1–D5 only):

````markdown
---
name: ladder-quality-order
description: Loss-2 judge (codex role). Over one topic's 6 shuffled research-design samples, pairwise-rank by quality using the D1–D5 standard. Emit the pairwise log; the harness computes the order and the ladder verdicts. Judge quality difference, never against academic standards.
---

# ladder-quality-order (loss-2)

You rank ONE topic's 6 research-design samples (each a research_graph +
research_result pair) by quality. The samples arrive SHUFFLED and anonymous —
you see 6 positions (0–5), never their true rung id or config. You judge only
on the D1–D5 standard:

- D1 meaningfulness — is the research question real and worth asking?
- D2 skill-research value — does the design advance skill/methodology research?
- D3 use-to-DARE — is it usable by the DARE engine?
- D4 respects the 4-layer architecture (campaign → strategy → tactic → sop)?
- D5 prerequisites — are the stated prerequisites sound and met?

Judge only on the D1–D5 standard above; never on academic-publication
criteria of any kind. You never see any quality-check list.

## Pairwise mechanism

You will be asked to compare two positions at a time. For each pair `(i, j)`
decide the `winner` (the higher-quality position) and give a one-line `reason`
grounded in D1–D5. Do not assign absolute scores — only pick a winner per pair.
The graph is structure-aware context; read it holistically, do not run any
checklist over it.

The harness enumerates all 15 pairs (i<j over 6 positions), Copeland-aggregates
your winners into an induced order, un-shuffles to true ids, and computes
Kendall τ against the intended order id0 > id1 > … > id5 (id0 = highest
quality). You only emit `{winner, reason}` per pair.

## Endpoint separation

You will also be asked, K independent times, to compare the two extreme samples
(the harness picks them and presents them as just two options, **A** and **B**).
Return `{"winner": "A" | "B"}` — exactly the label of the higher-quality one.
Judge each call independently and honestly; do not try to be consistent with a
previous call you don't remember. (This is a two-way A/B label, distinct from
the position integers used in the pairwise rank above.)

## Confound flat-check (when present)

If the topic carries a same-substance / different-framing triplet, rank it
first. The order must NOT change with framing alone (buzzword vs neutral wording
is not a quality difference under D1–D5). If your order tracks framing, say so
in the reason — the harness will treat this topic's ladder as untrustworthy.

## What the harness writes (you do not compute these)

The harness assembles `loss2.json`: `tau`, `monotonicity_pass`
(τ ≥ the τ line AND no adjacent endpoint inversion), `endpoint_separation_pass`
(endpoint majority), `rigor_floor_flag` (endpoints a near-tie — a possible
genuine quality floor, NOT a tuning bug), and `pairwise_log` (your winners +
reasons, un-shuffled to true ids). Your only job: honest per-pair winners and
D1–D5 reasons.
````

- [ ] **Step 5: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_ladder_quality_order.py -v`
Expected: PASS (all tests green).

- [ ] **Step 6: Commit**

```bash
cd ladder-foundry
git add skills/ladder-quality-order/ tests/test_ladder_quality_order.py
git commit -m "feat(stage4): ladder-quality-order loss-2 codex judge + schema (T3)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 4: run_codex_loss.py (the last leaf script)

**Files:**
- Create: `ladder-foundry/skills/optimization-loop/scripts/run_codex_loss.py`
- Create: `ladder-foundry/skills/optimization-loop/scripts/loss1.schema.json` (byte-identical copy of T2's)
- Create: `ladder-foundry/skills/optimization-loop/scripts/loss2.schema.json` (byte-identical copy of T3's)
- Test: `ladder-foundry/tests/test_run_codex_loss.py`

**Interfaces:**
- Consumes: `injection-fidelity/SKILL.md` + `ladder-quality-order/SKILL.md` (full text, into the payload); `loss1.schema.json` / `loss2.schema.json` (read from `Path(__file__).parent`, NOT from `--skill-md`); the de-identified transcript `.md` from `save_transcript.py`; `configs/<sample>.json`; the 6 `triples/<sample>.json` from `concat_triple.py`.
- Produces: `runs/<id>/loss/<sample>.loss1.json` (validated against `loss1.schema.json`), `runs/<id>/loss/<topic>.loss2.json` (validated against `loss2.schema.json`), `runs/<id>/loss/<topic>.perm.json` (the `pos→sample_id` permutation). The `loss2.json` bools feed `gate_eval.py topic`.
- **codex_fn(payload: str, schema_path: str) -> str** — the isolated edge. Default `_default_codex_call`; tests inject a fake returning fixture JSON.

**Module constants (this script OWNS these — gate_eval owns 0.90/0.80):**

```python
TAU_MIN = 0.7              # loss-2 monotonicity τ line
ENDPOINT_K = 5             # independent endpoint comparisons
ENDPOINT_ALLOWANCE = 1     # endpoint_separation_pass iff w0 >= K - allowance
RIGOR_FLOOR_EPS = 1        # near-tie half-window: w0 in [K/2 - eps, K/2 + eps]
```

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_run_codex_loss.py`:

```python
import json
import subprocess
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SCRIPT = LF / "skills" / "optimization-loop" / "scripts" / "run_codex_loss.py"
sys.path.insert(0, str(SCRIPT.parent))


def test_script_and_schemas_exist():
    assert SCRIPT.exists()
    assert (SCRIPT.parent / "loss1.schema.json").exists()
    assert (SCRIPT.parent / "loss2.schema.json").exists()


def test_schemas_are_byte_identical_copies():
    import run_codex_loss  # noqa
    s1a = (SCRIPT.parent / "loss1.schema.json").read_bytes()
    s1b = (LF / "skills" / "injection-fidelity" / "loss1.schema.json").read_bytes()
    assert s1a == s1b
    s2a = (SCRIPT.parent / "loss2.schema.json").read_bytes()
    s2b = (LF / "skills" / "ladder-quality-order" / "loss2.schema.json").read_bytes()
    assert s2a == s2b


def test_validate_minimal_ok():
    import run_codex_loss as M
    schema = json.loads((SCRIPT.parent / "loss1.schema.json").read_text(encoding="utf-8"))
    good = {"fidelity": True, "loss1": 1.0, "drift_flag": False,
            "per_axis_evidence": {ax: {"observed": 0.9, "expected_band": "L4",
                                       "pass": True, "quote": "q"}
                                  for ax in ("A1", "A2", "A3", "A4", "A5")}}
    M.validate(good, schema)  # no raise


def test_validate_missing_key_raises():
    import run_codex_loss as M
    schema = json.loads((SCRIPT.parent / "loss1.schema.json").read_text(encoding="utf-8"))
    bad = {"fidelity": True}  # missing loss1/per_axis_evidence/drift_flag
    try:
        M.validate(bad, schema)
        assert False, "should have raised"
    except M.CodexOutputError:
        pass


def test_validate_wrong_type_raises():
    import run_codex_loss as M
    schema = json.loads((SCRIPT.parent / "loss1.schema.json").read_text(encoding="utf-8"))
    bad = {"fidelity": "yes", "loss1": 1.0, "drift_flag": False,
           "per_axis_evidence": {}}
    try:
        M.validate(bad, schema)
        assert False
    except M.CodexOutputError:
        pass


def test_shuffle_unshuffle_reversible():
    import run_codex_loss as M
    ids = ["id0", "id1", "id2", "id3", "id4", "id5"]
    perm = M.shuffle_perm(len(ids), seed=42)        # list pos -> original index
    shuffled = [ids[perm[p]] for p in range(len(ids))]
    back = M.unshuffle(list(range(len(ids))), perm)  # induced positions -> orig idx
    assert sorted(back) == list(range(len(ids)))
    assert {shuffled[p] for p in range(6)} == set(ids)


def test_kendall_tau_perfect_and_reversed():
    import run_codex_loss as M
    # induced order identical to intended -> tau == 1
    assert M.kendall_tau([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]) == 1.0
    # fully reversed -> tau == -1
    assert M.kendall_tau([0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]) == -1.0


def test_copeland_from_pairwise():
    import run_codex_loss as M
    # 0 beats everyone, 5 loses to everyone -> induced order 0..5
    pairs = []
    for i in range(6):
        for j in range(i + 1, 6):
            pairs.append({"i": i, "j": j, "winner": i})  # lower index always wins
    order = M.copeland_order(pairs, n=6)
    assert order == [0, 1, 2, 3, 4, 5]


def test_endpoint_vote_count():
    import run_codex_loss as M
    # w0 = number of times the true-high endpoint (mapped winner) wins
    judgments = [{"winner": 0}, {"winner": 0}, {"winner": 5},
                 {"winner": 0}, {"winner": 0}]
    w0 = M.count_endpoint_wins(judgments, high_pos=0)
    assert w0 == 4
    assert M.endpoint_pass(w0) is True       # 4 >= 5 - 1
    assert M.endpoint_pass(2) is False


def _fake_loss1(payload, schema_path):
    return json.dumps({
        "fidelity": True, "loss1": 1.0, "drift_flag": False,
        "per_axis_evidence": {ax: {"observed": 0.9, "expected_band": "L4",
                                   "pass": True, "quote": "q"}
                              for ax in ("A1", "A2", "A3", "A4", "A5")}})


def test_loss1_landing(tmp_path, monkeypatch):
    import run_codex_loss as M
    rd = tmp_path / "runs" / "r0"
    (rd / "configs").mkdir(parents=True)
    (rd / "loss").mkdir(parents=True)
    (rd / "transcripts").mkdir(parents=True)
    (rd / "configs" / "s.json").write_text('{"rung_id": 0}', encoding="utf-8")
    (rd / "transcripts" / "s.md").write_text("### user\n\nhi\n", encoding="utf-8")
    out = rd / "loss" / "s.loss1.json"
    M.run_loss1(transcript=str(rd / "transcripts" / "s.md"),
                config=str(rd / "configs" / "s.json"),
                skill_md=str(LF / "skills" / "injection-fidelity" / "SKILL.md"),
                out=str(out), codex_fn=_fake_loss1)
    got = json.loads(out.read_text(encoding="utf-8"))
    assert got["fidelity"] is True and got["loss1"] == 1.0


def test_loss2_plumbing_lands_and_validates(tmp_path):
    # Structure-only: fake rank + endpoint codex_fns exercise the run_loss2
    # composition (A/B->position map, perm.index, copeland->unshuffle, perm.json
    # + loss2.json write + schema validate). Asserts NOTHING about the verdict
    # values (no gate outcome from canned output -> stays clear of the no-fake-
    # stub forbidden line); only that the artifact lands well-formed.
    import run_codex_loss as M
    rd = tmp_path / "runs" / "r0"
    (rd / "triples").mkdir(parents=True)
    (rd / "loss").mkdir(parents=True)
    triples = []
    for k in range(6):
        p = rd / "triples" / f"id{k}.json"
        p.write_text(json.dumps({"research_config": {}, "research_graph": {},
                                 "research_result": {"title": f"id{k}"}}),
                     encoding="utf-8")
        triples.append(str(p))

    def fake_codex(payload, schema_path):
        if "pairwise" in Path(schema_path).read_text(encoding="utf-8"):
            pairs = [{"i": i, "j": j, "winner": i}
                     for i in range(6) for j in range(i + 1, 6)]
            return json.dumps({"pairwise": pairs})
        return json.dumps({"winner": "A"})        # endpoint A/B label

    out = rd / "loss" / "topic00.loss2.json"
    M.run_loss2(triples=triples, intended_order="id0,id1,id2,id3,id4,id5",
                skill_md=str(LF / "skills" / "ladder-quality-order" / "SKILL.md"),
                out=str(out), seed=7, codex_fn=fake_codex)
    art = json.loads(out.read_text(encoding="utf-8"))
    schema = json.loads((SCRIPT.parent / "loss2.schema.json").read_text(encoding="utf-8"))
    M.validate(art, schema)                       # lands schema-valid
    assert set(art) >= {"tau", "monotonicity_pass", "endpoint_separation_pass",
                        "rigor_floor_flag", "pairwise_log"}
    assert (out.with_suffix(".perm.json")).exists()      # permutation recorded
    assert len(art["pairwise_log"]) == 15                # all i<j pairs, unshuffled


def test_bad_json_degrades_and_exits_2(tmp_path):
    # subprocess: a codex edge returning junk -> degrade-to-disk + exit 2
    rd = tmp_path / "runs" / "r0"
    (rd / "configs").mkdir(parents=True)
    (rd / "loss").mkdir(parents=True)
    (rd / "transcripts").mkdir(parents=True)
    (rd / "configs" / "s.json").write_text('{"rung_id": 0}', encoding="utf-8")
    (rd / "transcripts" / "s.md").write_text("### user\n\nhi\n", encoding="utf-8")
    out = rd / "loss" / "s.loss1.json"
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "loss1",
         "--transcript", str(rd / "transcripts" / "s.md"),
         "--config", str(rd / "configs" / "s.json"),
         "--skill-md", str(LF / "skills" / "injection-fidelity" / "SKILL.md"),
         "--out", str(out), "--_test-bad-json"],
        capture_output=True, text=True)
    assert r.returncode == 2
    got = json.loads(out.read_text(encoding="utf-8"))
    assert got["pass"] is False and "parse_error" in got
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_run_codex_loss.py -v`
Expected: FAIL — `ModuleNotFoundError` / `test_script_and_schemas_exist` fails (script absent).

- [ ] **Step 3: Copy the two schemas beside the script**

Create the script dir and copy both authoritative schemas byte-identical:

```bash
cd ladder-foundry
mkdir -p skills/optimization-loop/scripts
cp skills/injection-fidelity/loss1.schema.json skills/optimization-loop/scripts/loss1.schema.json
cp skills/ladder-quality-order/loss2.schema.json skills/optimization-loop/scripts/loss2.schema.json
```

- [ ] **Step 4: Write the harness helpers (no codex edge yet)**

Create `ladder-foundry/skills/optimization-loop/scripts/run_codex_loss.py` — part 1 (helpers + minimal validator + math). Keep each Write under 13000 chars; this is part 1 of 2:

```python
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
```

- [ ] **Step 5: Append the codex edge + CLI (part 2)**

Append to `run_codex_loss.py` (part 2 of 2):

```python
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
    perm_path = Path(out).with_suffix(".perm.json")
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
```

- [ ] **Step 6: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_run_codex_loss.py -v`
Expected: PASS (all tests green). `test_bad_json_degrades_and_exits_2` uses the `--_test-bad-json` flag (a fake junk edge at the boundary — NOT a fake-stub of a gate verdict).

- [ ] **Step 7: Commit**

```bash
cd ladder-foundry
git add skills/optimization-loop/scripts/ tests/test_run_codex_loss.py
git commit -m "feat(stage4): run_codex_loss leaf — payload/validate/shuffle/tau plumbing, codex_fn isolated (T4)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 5: optimization-loop SKILL.md (the optimizer brain)

**Files:**
- Create: `ladder-foundry/skills/optimization-loop/SKILL.md`
- Test: `ladder-foundry/tests/test_optimization_loop.py`

**Interfaces:**
- Consumes: every STAGE-3 leaf CLI by name (`new_run_id.py`, `trace_emit.py`, `save_transcript.py`, `concat_triple.py`, `gate_eval.py`, `apply_weight_update.py`, `write_dataset.py`) + `generator/gen_configs.py::main(out_dir, w)` + its own `scripts/run_codex_loss.py`. `generator/weights.py::{TRAINABLE, INTERP_KEYS, COLLISION_ENUM}` (the §backprop target/key vocabulary). `gate_eval.py::{FIDELITY_MIN, BATCH_RATIO_MIN}` (threshold point-back). `generator/leak_audit.py`.
- Produces: the SKILL.md prose. No Python symbols. T6 references expand §backprop / thresholds.

**The test asserts the brain names REAL things (the ponytail must-fix: a real assertion, not a prose read):** it greps SKILL.md for each leaf's relative anchor + introspects each script's argparse to confirm the flags the skill names actually exist, and confirms §backprop's target/key vocabulary ⊆ `weights.TRAINABLE` ∪ `INTERP_KEYS`.

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_optimization_loop.py`:

```python
import subprocess
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILL = LF / "skills" / "optimization-loop" / "SKILL.md"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit
from generator.weights import TRAINABLE, INTERP_KEYS


def txt():
    return SKILL.read_text(encoding="utf-8")


def test_skill_exists_and_leak_clean():
    assert SKILL.exists()
    leak_audit(txt())


def test_names_all_seven_leaves_by_relative_anchor():
    t = txt()
    for leaf in ("new_run_id.py", "trace_emit.py", "save_transcript.py",
                 "concat_triple.py", "gate_eval.py", "apply_weight_update.py",
                 "write_dataset.py"):
        assert f"../../scripts/{leaf}" in t, leaf
    assert "../../generator/gen_configs.py" in t
    assert "scripts/run_codex_loss.py" in t          # own leaf, local anchor


def test_named_leaf_flags_actually_exist():
    # introspect a couple of leaves: the flags the skill names must be real
    t = txt()
    help_save = subprocess.run([sys.executable, "scripts/save_transcript.py", "-h"],
                               cwd=str(LF), capture_output=True, text=True).stdout
    assert "--logs-dir" in help_save and "--logs-dir" in t
    help_gate = subprocess.run([sys.executable, "scripts/gate_eval.py", "topic", "-h"],
                               cwd=str(LF), capture_output=True, text=True).stdout
    for flag in ("--fidelity-rate", "--mono", "--endpoint"):
        assert flag in help_gate and flag in t


def test_backprop_targets_subset_of_weights_vocab():
    t = txt()
    # every target the skill says it can change must be a real trainable segment
    assert "axis_prose" in t and "interp_params" in t and "assembler_params" in t
    assert TRAINABLE == {"axis_prose", "interp_params", "assembler_params"}
    # interp knobs named must be the locked key-set
    for k in INTERP_KEYS:
        assert k in t, k


def test_threshold_point_back_not_copied():
    t = txt()
    # the skill points back to the module constants, does not re-state the digits
    assert "FIDELITY_MIN" in t and "BATCH_RATIO_MIN" in t


def test_banned_flags_and_driver_absent():
    t = txt()
    for banned in ("-p ", "--resume", "--session-id", "--allowedTools",
                   "drive_cc", "pexpect", "PTY"):
        assert banned not in t, banned


def test_logs_dir_required_privacy_line_present():
    t = txt()
    assert "--logs-dir" in t and "required" in t.lower()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_optimization_loop.py -v`
Expected: FAIL — `test_skill_exists_and_leak_clean` fails (file absent).

- [ ] **Step 3: Author `skills/optimization-loop/SKILL.md` — part 1 (frontmatter + §loop)**

Create the file with frontmatter + §loop. Keep each Write under 13000 chars (part 1 of 3):

````markdown
---
name: optimization-loop
description: The optimizer brain for the ladder-foundry pretraining loop. Runs the two-level nested batch loop, delegates gating to gate_eval, attributes a failing batch to one weight (attribute-first), and recovers from disk after compaction. Control flow is fully scripted; only the backprop attribution is a judgment call.
---

# optimization-loop

You are the optimizer. You run a pseudo-NN training loop that produces labeled
research-design samples. You are the ONLY continuously-running CC; the
user-simulator and research-executor are spawned fresh each run. Disk is the
only source of truth — your memory is not.

## §loop — the two-level nested batch loop

LOOP-2 (epochs/batches, runs to convergence) wraps LOOP-1 (one batch = 48 runs
= 8 topics × 6 rungs).

**Epoch start (once):**
1. `python ../../scripts/new_run_id.py --runs-root runs` → capture `run_id`.
   Emit trace `run_start`.

**Batch start (each batch):**
2. `batch_id` = the highest `batch-N` in `runs/<run_id>/weights/` (cold start =
   `batch-0`; do NOT pre-increment). Emit `batch_start`.
3. Generate configs from the current weights: call
   `../../generator/gen_configs.py` `main(out_dir, w)` (it is `main(out_dir, w)`,
   NOT an argparse CLI — invoke via a one-line `python -c` that imports it and
   passes the loaded `weights/<batch_id>.json`). M1 note: gen_configs names
   configs `config_{rung}.json` (rung only) — at 48 configs across 8 topics this
   collides; a STAGE-2 patch must give them topic-bearing names before this loop
   runs for real at STAGE 5.

**Per run (8 topics × 6 rungs = 48):**
4. Spawn the user-simulator CC (see §tools). Inject its `research_config`.
5. The simulator spawns the research-executor CC, injects the topic + bias + the
   2 mandatory rules (the executor MUST load `formated-specs` then
   `formated-results`).
6. Simulator ↔ executor talk for the card's turn budget. Emit `dialogue_turn`
   per exchange.
7. `python ../../scripts/save_transcript.py --logs-dir <REQUIRED> --cwd <exec-cwd>
   --sample <sample> --out runs/<run_id>/transcripts/<sample>.md`. `--logs-dir`
   is REQUIRED, no default (privacy red line).
8. `python ../../scripts/concat_triple.py --run-dir runs/<run_id> --sample <sample>`.
9. `python scripts/run_codex_loss.py loss1 --transcript … --config … --skill-md
   ../injection-fidelity/SKILL.md --out runs/<run_id>/loss/<sample>.loss1.json`.
   Emit `rung_done`.

**Per topic (after its 6 rungs):**
10. `python scripts/run_codex_loss.py loss2 --triples <6 triples id0..id5>
    --intended-order id0,id1,id2,id3,id4,id5 --skill-md ../ladder-quality-order/SKILL.md
    --out runs/<run_id>/loss/<topic>.loss2.json --seed <fixed>`.
11. `python ../../scripts/gate_eval.py topic --fidelity-rate <topic fidelity_rate>
    --mono <loss2.monotonicity_pass> --endpoint <loss2.endpoint_separation_pass>`.
    Emit `topic_done`.
12. `python ../../scripts/write_dataset.py --run-dir … --sample … --topic … --rung …
    --out-root dataset --loss1 … --topic-pass …` ×6 (one per rung).

**Batch close:**
13. `python ../../scripts/gate_eval.py batch --flags <8 topic-pass bools>`. Emit
    `batch_done` (include `recent_ratios`).
14. `python ../../scripts/gate_eval.py converged --recent <last-3 batch ratios>`.
    - TRUE → freeze weights, emit `converged` + `run_end`. Done.
    - FALSE → go to §backprop, then a new batch.

Follow this section exactly; no improvisation in the control flow.
````

- [ ] **Step 4: Author SKILL.md — part 2 (§gate + §backprop)**

Append (part 2 of 3):

````markdown
## §gate

Delegate ALL gate arithmetic to `../../scripts/gate_eval.py` (pure, no CC/codex):

- per-topic: 3-way AND (`fidelity_rate ≥ FIDELITY_MIN` ∧ `monotonicity_pass` ∧
  `endpoint_separation_pass`).
- batch: `pass_ratio ≥ BATCH_RATIO_MIN`, hard integer line ≥ 7/8 topics.
- converged: the trace-tail `recent_ratios`, last 3 all ≥ `BATCH_RATIO_MIN`.

Thresholds are NOT restated here. `FIDELITY_MIN` and `BATCH_RATIO_MIN` are the
module constants in `../../scripts/gate_eval.py` — the single source of truth.
New numbers the judges use (τ line, 丙 line, K, endpoint allowance, drift ε)
live in `references/gate-thresholds.md`, which also points back, never copies.

check-blind: you read only `fidelity_rate`, `tau`, `monotonicity_pass`,
`endpoint_separation_pass`, and codex verdicts. You never see or reason about
any quality-check list. `rigor_floor_flag` is an orthogonal alarm — it is NOT
in the AND.

## §backprop — attribute first, then act (the one judgment point)

One batch changes ONE weight. First attribute the failure, then act. Read the
trace coarse→fine (`batch_done` → `topic_done` → `loss/*.json`) and stop when
decided.

Decision table:

| Signal read | Target weight | Key |
| --- | --- | --- |
| loss-1 fidelity fails (an axis collapsed) | `axis_prose` | the collapsed `AXIS.LEVEL` cell |
| loss-2 endpoints NOT separated, `rigor_floor_flag == true` | NONE | alarm only — do NOT train ② (coords are frozen_label-locked; training ② is a no-op). Record and move on. |
| loss-2 endpoints NOT separated, `rigor_floor_flag == false` | `axis_prose` | the id0 or id5 endpoint cell |
| loss-2 middle collision (τ < TAU_MIN but endpoints separated) | `interp_params` | one of `collision_offset_axis` (B1/expression only), `endpoint_spread`, `granularity_map` |
| ≥ 4/8 topics double-collapse (both losses fail) | `assembler_params` | the structural knob implicated |

Priority: loss-1 > loss-2 middle-collision > whole-card. Pre-gate: if a topic's
z⊥C confound check is NOT flat, that topic's loss-2 is void — do NOT change any
weight on it this batch.

Execution: the attribution is YOUR decision (no script). Then EITHER
`python ../../scripts/apply_weight_update.py --weights-dir runs/<run_id>/weights
--batch-id <batch_id> --target <target> --key <key> --new <new-text> --reason <why>`
(F2: writes `weights/<batch+1>.json` + appends `revision_log.jsonl`), OR the
same with `--copy` (F1: byte-copy forward, no log — when you decide NOT to
change a weight this batch).

Before committing new `axis_prose` text, run it through `generator/leak_audit.py`
(it must not name any check vocabulary). W5: your attribution inputs are only
fidelity / τ / endpoint / codex verdicts — never a check list. Detail in
`references/backprop-heuristic.md`.
````

- [ ] **Step 5: Author SKILL.md — part 3 (§state + §tools)**

Append (part 3 of 3):

````markdown
## §state — disk is the only truth

Memory is not trustworthy across a `/compact`. Three persisted artifacts:
`runs/<run_id>/trace.jsonl`, `runs/<run_id>/weights/<batch>.json`,
`runs/<run_id>/revision_log.jsonl`.

At each batch end: run `/compact`, reload THIS skill, and recover from disk:
- read `weights/<batch+1>.json` (the new weights for the next gen_configs),
- read `revision_log.jsonl` (the change history),
- read the `trace.jsonl` tail (`recent_ratios` + `batch_id` + last `seq` → +1 to
  continue numbering).

Privacy: the trace's `transcript_path` is always relative;
`save_transcript.py --logs-dir` is required with no default. After recovery,
verify the `frozen_label` lock is intact — `weights.revise("frozen_label", …)`
must still raise.

## §tools — the leaf registry + child-CC launch

Leaves are NOT moved into this skill (D1). Reference them by relative anchor
from this skill dir:
- `../../scripts/new_run_id.py`, `../../scripts/trace_emit.py`,
  `../../scripts/save_transcript.py`, `../../scripts/concat_triple.py`,
  `../../scripts/gate_eval.py`, `../../scripts/apply_weight_update.py`,
  `../../scripts/write_dataset.py`
- `../../generator/gen_configs.py` (`main(out_dir, w)`, non-argparse; M1
  collision annotated — a STAGE-2 patch is a STAGE-5 prerequisite)
- this skill's own leaf: `scripts/run_codex_loss.py`

**Child-CC launch (3 iron rules):**
1. A parent CC starts its child by running `claude` DIRECTLY in its own Bash
   tool: `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role-dir> bash -lc 'cd <child-cwd> &&
   claude'`. No driver script. No pseudo-terminal. No tmux for children (tmux
   hosts only the optimizer itself).
2. Fresh sim/exec each run (between-run independence — a different persona is
   injected, so no context may carry over). Only the optimizer is continuous.
3. Authoritative transcript = the exec session jsonl (read by save_transcript
   via `--logs-dir`).

All three CC layers are normal interactive REPLs. Never pass the print, resume,
session-id, or allowed-tools flags to any `claude` invocation — those modes are
forbidden in this loop and must not appear even in this skill's text.

Four role config-dirs:
- optimizer `/workspace/home/optim/.claude` (this skill + superpowers)
- simulator `/workspace/home/sim/.claude` (superpowers only; persona injected)
- executor `/workspace/home/exec/.claude` (the DARE skill library +
  formated-specs / formated-results + superpowers)
- codex `/workspace/home/loss/.codex` (the 2 loss skills only)
````

- [ ] **Step 6: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_optimization_loop.py -v`
Expected: PASS (all tests green).

- [ ] **Step 7: Commit**

```bash
cd ladder-foundry
git add skills/optimization-loop/SKILL.md tests/test_optimization_loop.py
git commit -m "feat(stage4): optimization-loop brain — loop/gate/backprop/state/tools (T5)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 6: references (gate-thresholds.md + backprop-heuristic.md)

**Files:**
- Create: `ladder-foundry/skills/optimization-loop/references/gate-thresholds.md`
- Create: `ladder-foundry/skills/optimization-loop/references/backprop-heuristic.md`
- Test: `ladder-foundry/tests/test_references_audit.py`

**Interfaces:**
- Consumes: `generator/leak_audit.py`. Names `gate_eval.FIDELITY_MIN` / `BATCH_RATIO_MIN` (point-back) and `run_codex_loss.TAU_MIN` / `ENDPOINT_K` / `ENDPOINT_ALLOWANCE` / `RIGOR_FLOOR_EPS` (point-back); is the SOLE home only for numbers no script owns (丙 line `0.80`, drift ε).
- Produces: two reference docs. No symbols. Referenced by §gate and §backprop.

**Threshold ownership (locked — prevents a second truth source):** `0.90`/`0.80` gate lines are owned by `gate_eval.py`. `TAU_MIN`/`ENDPOINT_K`/`ENDPOINT_ALLOWANCE`/`RIGOR_FLOOR_EPS` are owned by `run_codex_loss.py`. `gate-thresholds.md` POINTS BACK to both owners and only states outright the numbers no script computes with: the 丙-calibration τ line (`0.80`) and the drift tolerance ε (a judge-read number).

- [ ] **Step 1: Write the failing test**

Create `ladder-foundry/tests/test_references_audit.py`:

```python
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
REF = LF / "skills" / "optimization-loop" / "references"
GATE = REF / "gate-thresholds.md"
BP = REF / "backprop-heuristic.md"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit


def test_both_exist_and_leak_clean():
    assert GATE.exists() and BP.exists()
    leak_audit(GATE.read_text(encoding="utf-8"))
    leak_audit(BP.read_text(encoding="utf-8"))


def test_gate_points_back_not_copies():
    t = GATE.read_text(encoding="utf-8")
    # names the owning constants
    assert "FIDELITY_MIN" in t and "BATCH_RATIO_MIN" in t
    assert "TAU_MIN" in t
    # explicit point-back language present
    assert "gate_eval" in t and "run_codex_loss" in t
    assert "source of truth" in t.lower() or "points back" in t.lower()


def test_gate_owns_only_unowned_numbers():
    t = GATE.read_text(encoding="utf-8")
    # 0.90 / 0.80 gate lines must NOT be re-stated as literals here
    assert "0.90" not in t
    # the 丙 calibration line 0.80 IS owned here (a judge number no script holds)
    assert "0.80" in t


def test_backprop_three_disciplines_and_subset():
    t = BP.read_text(encoding="utf-8")
    assert "attribute" in t.lower()
    assert "one weight" in t.lower() or "single-variable" in t.lower()
    # the loss-2 subtype split discipline
    assert "frozen_label" in t
    for tgt in ("axis_prose", "interp_params", "assembler_params"):
        assert tgt in t, tgt


def test_backprop_no_academic_criteria():
    t = BP.read_text(encoding="utf-8").lower()
    for forbidden in ("novelty", "baseline", "citation", "publishab"):
        assert forbidden not in t
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd ladder-foundry && python -m pytest tests/test_references_audit.py -v`
Expected: FAIL — `test_both_exist_and_leak_clean` fails (files absent).

- [ ] **Step 3: Author `references/gate-thresholds.md`**

Create `ladder-foundry/skills/optimization-loop/references/gate-thresholds.md`:

```markdown
# gate-thresholds

This file is a human index of the loop's numeric lines. It is NOT the source of
truth for the gate numbers — it points back to the code that owns each one, so
no number lives in two places.

## Owned by code (DO NOT copy the digits here)

| Number | Owner | Meaning |
| --- | --- | --- |
| `FIDELITY_MIN` | `../../scripts/gate_eval.py` | per-topic batch fidelity_rate floor |
| `BATCH_RATIO_MIN` | `../../scripts/gate_eval.py` | batch pass_ratio floor + converged line |
| `TAU_MIN` | `scripts/run_codex_loss.py` | loss-2 monotonicity Kendall τ line |
| `ENDPOINT_K` | `scripts/run_codex_loss.py` | independent endpoint comparisons |
| `ENDPOINT_ALLOWANCE` | `scripts/run_codex_loss.py` | endpoint majority slack |
| `RIGOR_FLOOR_EPS` | `scripts/run_codex_loss.py` | near-tie half-window for the rigor-floor alarm |

To change any of these, edit the owning module constant — never this table.

## Owned here (no script computes with them)

These are judge-/operator-read numbers with no code owner; this doc is their
sole home:

- 丙-calibration hand-off τ line: **0.80** (τ ≥ 0.80 AND endpoints 100%
  consistent → quality good enough to hand to the next stage). Derived by the
  optimizer from the loss-2 artifact; not a persisted schema field.
- drift tolerance ε: the second-half rate may fall at most ε toward the
  cooperative pole before `drift_flag` trips. Calibrated to real dialogue at
  STAGE 5; start conservative (one band-width).

check-blind: this file names no quality-check list, only the loop's own
thresholds.
```

- [ ] **Step 4: Author `references/backprop-heuristic.md`**

Create `ladder-foundry/skills/optimization-loop/references/backprop-heuristic.md`:

```markdown
# backprop-heuristic

The §backprop section expanded line by line: `discriminant (signal reading) →
fix template (data-oriented wording) → priority`. Numeric limits reference
`gate-thresholds.md`, never repeated here.

## Three disciplines (non-negotiable)

1. **Attribute first, then act** (先归因再动手). Read the trace coarse→fine
   (`batch_done` → `topic_done` → `loss/*.json`) and decide WHICH weight before
   touching anything.
2. **Single-variable.** One batch changes exactly ONE weight. Everything else is
   carried forward byte-identical (`apply_weight_update.py --copy`).
3. **Loss-2 must split subtype first.** "Endpoints not separated" and "middle
   collision" have different roots. Endpoints-not-separated must NOT train the
   interpolator — the label coordinates are `frozen_label`-locked, so training ②
   on them is a no-op. Split before acting.

## The five discriminant lines

1. loss-1 fidelity fails → the collapsed axis's prose is too weak/strong →
   `axis_prose` at `AXIS.LEVEL` → priority 1.
2. loss-2 endpoints not separated AND `rigor_floor_flag == true` → suspected
   genuine quality floor (endpoints can't be pulled apart) → ALARM, change
   nothing → record, skip.
3. loss-2 endpoints not separated AND `rigor_floor_flag == false` → an endpoint
   persona is mis-pitched → `axis_prose` id0 or id5 endpoint cell → priority 2.
4. loss-2 middle collision (τ below the line, endpoints separated) → the
   interpolation between rungs is muddy → `interp_params`
   (`collision_offset_axis` [B1/expression only], `endpoint_spread`,
   `granularity_map`) → priority 3.
5. ≥ 4/8 topics double-collapse → a structural assembly problem →
   `assembler_params` → priority 4 (whole-card).

Priority order: 1 > 4 > {2/3} per their rows; loss-1 always before loss-2.

## Pre-gate

z⊥C not flat (the confound check varies with framing) → that topic's loss-2 is
void → do NOT change any weight on it this batch.

## check-blind

Attribution inputs are ONLY: fidelity, τ, endpoint separation, rigor_floor_flag,
and the codex verdict text. Never a quality-check list. New `axis_prose` text
must pass `generator/leak_audit.py` before commit.
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `cd ladder-foundry && python -m pytest tests/test_references_audit.py -v`
Expected: PASS (all tests green).

- [ ] **Step 6: Commit**

```bash
cd ladder-foundry
git add skills/optimization-loop/references/ tests/test_references_audit.py
git commit -m "feat(stage4): optimization-loop references — gate-thresholds + backprop-heuristic (T6)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 7: wrap — full-suite regression + global audits + ledger

**Files:**
- Create: `ladder-foundry/tests/test_stage4_audit.py`
- Modify: `D:\YOGSOTH-AI\.superpowers\sdd\progress.md` (ledger; gitignored — not committed)
- Modify: `D:\YOGSOTH-AI\CLAUDE.md` (status section; gitignored — not committed)

**Interfaces:**
- Consumes: every STAGE-4 artifact. `generator/leak_audit.py`.
- Produces: a global audit test + updated ledger/status. No new runtime symbols.

This task adds ONE global audit test that sweeps the whole `skills/` tree (so a future edit that introduces a leak / banned flag / log-path is caught), then runs the full STAGE 1+2+3+4 suite green.

- [ ] **Step 1: Write the global audit test**

Create `ladder-foundry/tests/test_stage4_audit.py`:

```python
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILLS = LF / "skills"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit, LeakHit

TEXT_FILES = list(SKILLS.rglob("*.md")) + list(SKILLS.rglob("*.json"))


def test_skills_tree_nonempty():
    assert len(TEXT_FILES) >= 7      # 5 SKILL.md + 2 references + schemas


def test_w5_leak_sweep_all_skill_text():
    # every committed .md / .json under skills/ is leak-clean
    for f in TEXT_FILES:
        leak_audit(f.read_text(encoding="utf-8"))


def test_no_banned_cc_flags_anywhere():
    banned = ["--resume", "--session-id", "--allowedTools",
              "drive_cc", "pexpect"]
    for f in SKILLS.rglob("*.md"):
        t = f.read_text(encoding="utf-8")
        for b in banned:
            assert b not in t, (f.name, b)
        # "-p " print flag and bare "PTY" — guard against the claude print flag
        assert " -p " not in t, f.name
        assert "PTY" not in t, f.name


def test_no_log_path_signatures_committed():
    # 3 privacy signatures: Windows projects dir, POSIX projects dir, bare slug.
    # ponytail: literal-substring scan, the same shape T7's shell grep uses.
    sigs = ["\\.claude\\projects", "/.claude/projects", ".claude\\projects"]
    for f in TEXT_FILES:
        t = f.read_text(encoding="utf-8")
        for s in sigs:
            assert s not in t, (f.name, s)


def test_save_transcript_logs_dir_required_in_loop():
    # the optimizer skill must carry the privacy line
    sk = (SKILLS / "optimization-loop" / "SKILL.md").read_text(encoding="utf-8")
    assert "--logs-dir" in sk and "required" in sk.lower()
```

- [ ] **Step 2: Run the audit test**

Run: `cd ladder-foundry && python -m pytest tests/test_stage4_audit.py -v`
Expected: PASS (all STAGE-4 artifacts already authored leak-clean by T1–T6).

- [ ] **Step 3: Run the full regression suite**

Run: `cd ladder-foundry && python -m pytest -q`
Expected: PASS. STAGE 1+2+3 = 70 tests; STAGE 4 adds the 6 new test files. Confirm the total is 70 + the new count and zero failures. If any STAGE 1/2/3 test broke, a STAGE-4 file touched something it should not have — fix before committing.

- [ ] **Step 4: Commit the audit test**

```bash
cd ladder-foundry
git add tests/test_stage4_audit.py
git commit -m "test(stage4): global W5 + banned-flag + privacy audit sweep; full-suite regression (T7)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

(Optional human sanity glance — NOT a gating step; the three signatures it would scan for are already asserted by `test_stage4_audit.py` (privacy + banned flags) and `test_references_audit.py::test_gate_owns_only_unowned_numbers` (the `0.90` point-back). Run a manual `Select-String` over `skills/` only if you want eyes-on confirmation.)

- [ ] **Step 5: Update the progress ledger + CLAUDE.md status (not committed — gitignored)**

Append a STAGE 4 section to `D:\YOGSOTH-AI\.superpowers\sdd\progress.md` recording T1–T7 commits and the final suite count. Update the `## Status as of 2026-06-30` section of `D:\YOGSOTH-AI\CLAUDE.md` to mark STAGE 4 delivered (artifacts authored + locally verified, codex/run-nesting STAGE-5-deferred) and set the next action to STAGE 5. These two files are gitignored; do not `git add` them.

---

## Self-Review (writing-plans checklist, run against the spec)

**1. Spec coverage:**
- S1 formated-specs → T1 ✅; S2 formated-results → T1 ✅ (paired, tested together against concat_triple).
- S3 injection-fidelity + loss1.schema.json → T2 ✅ (6 signals, bands, drift, falsifiers in prose; schema required keys).
- S4 ladder-quality-order + loss2.schema.json → T3 ✅ (pairwise, endpoint K-vote, z⊥C, D1–D5; optional fields OMITTED — asserted).
- L15 run_codex_loss.py → T4 ✅ (subcommands, codex_fn isolation, minimal validator, shuffle/τ/K-vote, bad-JSON→exit 2, schema beside script, byte-identical copies; no-fake-stub forbidden line honored — no test asserts a gate outcome from canned output).
- S5 optimization-loop → T5 ✅ (§loop/§gate/§backprop/§state/§tools; relative anchors; child-launch iron rules; threshold point-back; banned-flag absence asserted).
- S6 references → T6 ✅ (gate-thresholds point-back + owned-here numbers; backprop-heuristic 3 disciplines + 5 lines + pre-gate).
- §10 honest verification ledger → distributed across T1–T7 local checks; STAGE-5-deferred items NOT tested (honestly). T7 = global sweep + regression.
- §12 constraints carried → Global Constraints block + per-task assertions.

**2. Placeholder scan:** No TBD/TODO/"handle edge cases"/"similar to Task N". Every code step shows complete content. ✅

**3. Type consistency:** `codex_fn(payload, schema_path)->str` consistent T4↔T5. Schema required-key sets match between the loss skills (T2/T3) and the byte-identical copies + validator (T4). `gate_eval` flag names (`--mono`/`--endpoint`/`--fidelity-rate`, string `"true"`/`"false"`) consistent T3↔T5. `weights.TRAINABLE`/`INTERP_KEYS` vocabulary consistent T5↔T6. Threshold owners (`gate_eval` 0.90/0.80; `run_codex_loss` TAU_MIN/ENDPOINT_K/ALLOWANCE/EPS) consistent T4↔T6. ✅

No gaps found.
