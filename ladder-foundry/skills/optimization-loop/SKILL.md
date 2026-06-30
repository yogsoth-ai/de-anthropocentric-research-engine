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
