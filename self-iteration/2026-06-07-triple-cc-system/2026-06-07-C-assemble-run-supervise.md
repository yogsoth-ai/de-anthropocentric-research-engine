# Plan C — assemble + run + pilot gating + live supervision Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **The "tests" in stage C are primarily on-device, repeatable real-model verification commands** (pilot go/no-go, full-batch convergence, supervision inspection); the pure-function parts (topics schema, coverage_report whitelist) still use pytest. Honor the `feedback-no-e2e-shell` iron rule — sim/exec/codex are all real processes.

**Goal:** Assemble the parts B built into a self-running whole machine — PT5 pilot hard gate → full LOOP-2 (48-run batch) loop to convergence → claude inspection supervision → freeze + full labeled dataset output. Once it runs end-to-end, the three-stage delivery is complete.

**Architecture:** The pilot is a front-loaded hard gate (if the 2 endpoint samples don't pass → stop and return to B, never burn full-batch token). At the end of each full-loop batch, route on the (`batch_passed` × `converged`) two-boolean cross into three mutually exclusive paths: T (converged, freeze) / F1 (passed but not converged, byte-copy weights forward) / F2 (not passed, backprop attributes and revises one weight). backprop is the only intelligent point in the whole system, and is genuinely put to the test in C. Supervision = primary (claude periodically SSHes in for read-only inspection) + auxiliary (CHECKPOINT artifacts are self-explanatory); human intervention = explicit HALT.json on disk + inspection findings.

**Tech Stack:** All of B's components (three weights + 9 leaves + 2 loss skill + optimization-loop skill) · tmux long-running optimizer · real claude/codex · `/compact` cross-batch state recovery · third-party proxy `api.ikuncode.cc`.

---

## Key discipline (applies to every Task — read first)

- **The pilot is a hard gate**: if C1 (PT5 two-sample endpoint pilot) doesn't pass → write HALT, stop and return to Spec B to revise prose / endpoint coordinates, **never enter C2 and burn full-batch**. no-go is also a legitimate delivery (it correctly blocked burning full-batch).
- **C builds no parts**: the construction and unit testing of the components themselves is Spec B; environment setup is Spec A. C only assembles, runs, supervises, and produces.
- **Single-variable controlled backprop**: in the full loop, one batch revises only ONE of the three weights, and the next batch observes the effect of that change. Attribute-then-revise (§backprop decision table).
- **disk is the only source of truth**: the optimizer is a tmux long-running REPL; it runs `/compact` at the end of each batch, and after compact rebuilds state from disk (weights/revision_log/trace tail), never relying on memory.
- **Supervision is observation, not a control console**: claude inspection is read-only, and never triggers control or revises weights.
- **Privacy red line**: the CC log absolute path never enters any committed artifact; reading logs goes only through the `--logs-dir`-required scripts; `runs/` is entirely device-local gitignore; dataset/coverage passes a whitelist check before being written to disk, and any field outside the whitelist (log path, device username, raw transcript) → hard failure; the values of the two API keys never enter any committed artifact.

## Dependency prerequisites (must be genuinely green before C starts)

- **Spec A all green**: the four identities can start, skills are visible, restart-reconnect works, thin-slice E1–E5 pass.
- **Spec B all green**: three weights + 9 leaves pytest all pass; B7 single-topic 6-rung e2e genuinely ran (loss-2 τ + endpoint separation + gate arithmetic verified).
- **`optimization-loop` skill fully written** (B6); its §backprop section was only written out, not deeply verified, in stage B — **C is its real testing ground**.

---

## File Structure

Files created/modified in stage C (`<proj> = self-iteration/2026-06-07-probe-pretrain/`):

```text
<proj>/
├── config/topics.json              # ★C fills 8 real frontier topics (B holds just 1 placeholder)
├── skills/optimization-loop/
│   ├── scripts/freeze.py           # freeze weights (NEW)
│   ├── scripts/coverage_report.py  # coverage report (NEW, pure generation-side aggregation, no log path)
│   └── references/                 # measured during pilot: F8/K/allowance/completability thresholds
├── ops/
│   ├── start_optimizer.sh          # tmux ignition + readiness probe + send opening prompt (NEW, once at startup)
│   └── optimizer-opening-prompt.txt# optimizer opening prompt full text (NEW)
└── tests/
    ├── test_topics.py              # P: 8 topic schema validation
    ├── test_coverage_report.py     # P: whitelist + no log path
    └── e2e/                        # R: C1 pilot / C2 full-batch / supervision inspection checklists
```

**Test-method markers**: P = pure-function pytest; R = real-model e2e; S = skill/script file.

**Build order**: C0 real topics + ignition deliverables → C1 PT5 pilot hard gate → C2 full LOOP-2 convergence → C3 freeze + output → C4 supervision interface. The Task numbering below aligns to this order.

---

### Task C0a: config/topics.json — fill 8 real frontier topics

**Files:**
- Modify: `<proj>/config/topics.json` (B's single placeholder → 8 real frontier topics)
- Test: `<proj>/tests/test_topics.py` (P)

C is the only stage that runs the full 8 topics (A/B use a single placeholder). The 8 topics are chosen by two criteria: ① all are research-design questions of the form "design a study/evaluation", whose research object is an **external** frontier DL/AI phenomenon (never let exec touch DARE self-reference/eval/check — the W5 source-material-level defense line); ② each comes with an F7 prerequisite the community is currently debating (giving A4=C- premise-corrigibility the cleanest leverage point).

- [ ] **Step 1: write the topics schema failing test**

Create `<proj>/tests/test_topics.py`:
```python
import json
from pathlib import Path

REQUIRED = {"topic_id","title_short","full_text","F7_prerequisite"}

def test_eight_topics_full_schema():
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))
    assert len(topics) == 8                                   # C fills all 8
    ids = [t["topic_id"] for t in topics]
    assert ids == [f"topic-0{i}" for i in range(8)]           # topic-00..topic-07
    for t in topics:
        assert REQUIRED <= set(t)                             # four fields present
        assert len(t["full_text"]) > 200                      # rich research brief, not a one-line synopsis
        assert t["F7_prerequisite"]                           # F7 non-empty

def test_topics_check_blind():
    """W5 source-material-level defense: topic text contains no detection-signature words (topics talk only about external phenomena)."""
    from generator.leak_audit import leak_audit
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))
    for t in topics:
        leak_audit(t["full_text"]); leak_audit(t["F7_prerequisite"])
```

- [ ] **Step 2: run red**

Run: `cd <proj> && python -m pytest tests/test_topics.py -v`
Expected: FAIL — the current topics.json has only 1 placeholder topic (left by B), len != 8.

- [ ] **Step 3: write the 8 real topics (full_text written as a rich research brief)**

Modify `<proj>/config/topics.json` into an 8-element array. The eight topics (title_short / full_text in three parts: motivation + research question + expected deliverable / F7):
- **topic-00 · CoT faithfulness** — test whether "the CoT text the model outputs faithfully reflects the internal reasoning"; intervention (perturb/truncate/inject a misleading step) + contrast with the "CoT is mere post-hoc rationalization" null hypothesis. F7: "the CoT text faithfully records the real reasoning steps" (challenged by latent-reasoning).
- **topic-01 · Agentic long-horizon reliability** — evaluate the reliability and failure modes of an autonomous agent on multi-step long-horizon real tasks; a step-count-controllable difficulty-tiered task set + compound-error attribution. F7: "given enough tools and memory, success rate extrapolates roughly linearly with step count" (ignoring compound error).
- **topic-02 · Multi-agent vs monolithic** — under fixed total compute, is multi-agent collaboration still better than an equal-budget monolith; strictly align the "total compute budget" control variable. F7: "multi-agent debate/collaboration necessarily improves reasoning quality" (often vanishes under equal-compute control).
- **topic-03 · MoE quantization sensitivity** — evaluate the quality-loss distribution of low-bit MoE quantization + locate the most sensitive experts/layers; uniform vs mixed precision contrast. F7: "all MoE experts can be uniformly low-bit quantized with near-lossless quality" (expert-level sensitivity differs markedly).
- **topic-04 · Multimodal capability tax** — test whether a unified multimodal model has a systematic capability loss on single-modality tasks; comparable-scale paired contrast + cross-modal asymmetry. F7: "unified multimodal is no weaker than specialized models on each single modality" (the capability tax often makes this false).
- **topic-05 · AI for Science hypothesis novelty** — evaluate whether LLM-generated scientific hypotheses are genuinely novel and verifiable rather than recombinations of the known; an operationalizable novelty definition + expert blind review + literature verification. F7: "LLMs can already autonomously produce novel and verifiable scientific hypotheses" (mostly recombinations of the known).
- **topic-06 · Agent benchmark representativeness** — test whether existing agent benchmarks cover the real task distribution + a "streetlight effect" audit; characterize the real-task-distribution dimensions + blind-spot probing. F7: "existing agent leaderboard scores represent real-world capability" (benchmark coverage is narrow).
- **topic-07 · Shallow alignment hypothesis** — distinguish whether alignment fine-tuning changes the underlying disposition or the surface expression; distribution shift/jailbreak/internal-representation probe/fine-tuning reversal + a contrast criterion. F7: "alignment fine-tuning genuinely changes the model's internal value disposition" (the shallow alignment hypothesis claims much of it is on the surface).

> **★full_text grounding**: write each full_text as the complete three-part research brief of Spec C §8.3 (motivation/background + core research question + expected deliverable), landing it verbatim into the JSON string (>200 chars). The eight topics differ methodologically (empirical test / long-horizon evaluation / equal-budget contrast / quantization sensitivity / multimodal contrast / novelty determination / benchmark audit / deep-vs-shallow alignment probing), so the ladder doesn't test only one research routine.

- [ ] **Step 4: run green + commit**

Run: `cd <proj> && python -m pytest tests/test_topics.py -v`
Expected: two PASS (8 topics full schema + check-blind).
```bash
git add config/topics.json tests/test_topics.py
git commit -m "feat(C0): 8 real frontier topics (external DL phenomenon research-design questions + contested F7 prerequisites)"
```

---

### Task C0b: optimizer ignition deliverables — opening prompt full text + start_optimizer.sh

**Files:**
- Create: `<proj>/ops/optimizer-opening-prompt.txt` (opening prompt full text, English, never simplified)
- Create: `<proj>/ops/start_optimizer.sh` (tmux ignition + readiness probe + send prompt, once at startup)

C is the only stage that ignites the optimizer. The opening prompt is the optimizer's "identity + discipline charter" for its long run; the readiness probe holds only at the optimizer's single location (the only layer that uses tmux send-keys).

- [ ] **Step 1: write the opening prompt full text (Spec C §7.1 finalized, landed verbatim)**

Create `<proj>/ops/optimizer-opening-prompt.txt` (full English text, honoring the locked constraints: no `-p`/`--resume`/`--session-id`/`--allowedTools`):
```text
You are optimizer-cc — the host of a "pseudo-neural-network pretraining"
training loop. Your role is equivalent to train.py in PyTorch. You are NOT
here to answer questions, NOT here to chat with anyone, NOT here to be
helpful in the ordinary assistant sense. The only reason you exist is to
drive one full training run from cold start until convergence, and then to
freeze the result and stop.

# Your goal
Through repeated epoch/batch loops, you optimize three trainable weights:
  (1) level prose      (axis_prose,       read by axes.py)
  (2) interpolator     (interp_params,    read by interpolator.py)
  (3) assembly logic   (assembler_params, read by assembler.py)
You optimize them so that the system produces a batch of labeled data
samples whose quality forms a clean, monotone, well-separated ladder across
six rungs (id0 best -> id5 worst) for each of eight topics. The LABEL of
every sample is its known generating condition (the PolicyCard that produced
it) — it is NEVER a subjective quality score. The label is objective because
it is the cause, not a judgement of the effect.

# What one batch is
One batch = one epoch = 8 topics x 6 rungs = 48 runs. In every batch you
MUST, strictly in this order:
  1. read the current weights/<batch>.json
  2. gen_configs -> 48 research_config cards (6-rung ladder x 8 topics),
     each passing leak_audit (W5)
  3. for each topic, for each rung: spawn a fresh sim-cc, inject the config,
     let sim spawn a fresh exec-cc and drive a real multi-turn research
     session, concat the (config, graph, result) triple, run codex loss-1
     (injection-fidelity, per run)
  4. after a topic's 6 rungs: run codex loss-2 (ladder-quality-order,
     per topic), evaluate the per-topic gate, write the 6 dataset samples
  5. after 8 topics: compute batch_pass_ratio, judge the gate
  6. if converged (3 consecutive passing batches): freeze + stop
     else if passed-but-not-converged (F1): byte-copy weights forward, no
        weight change
     else (F2): attribute-then-revise exactly ONE weight, then continue

# Your only source of action
Your complete task specification is written in the `optimization-loop`
skill. Load that skill NOW and execute strictly according to its sections:
  loop     — the two-level loop control flow above
  gate     — per-topic AND gate, batch_pass_ratio, convergence
  backprop — attribute-then-revise heuristic (the ONE place you think)
  state    — cross-batch disk persistence and post-/compact recovery
  tools    — the leaf scripts and child-CC spawn convention
Do NOT improvise the flow. Do NOT skip the skill and act on intuition.
Do NOT deviate from the skill to do anything it did not ask for.
Whatever the skill says, that is exactly what you do — with one exception:

# The single intelligent point (backprop)
The ONLY place you exercise genuine judgement is backprop: when a batch
fails the gate, you must attribute-then-revise. First diagnose WHICH weight
is at fault from the loss signals (loss-1 fidelity failure -> (1) prose;
loss-2 endpoints-not-separated -> first read rigor_floor_flag, if true do
NOT train (2) else (1) endpoint cells; loss-2 middle-rung collapse with
separated endpoints -> (2) interp_params; structural multi-rung breakage
-> (3) assembler_params). Then revise exactly ONE weight this batch
(single-variable discipline), so the next batch's loss change attributes
cleanly to this one edit. Everywhere else is deterministic; here you reason.

# Long-running discipline
You will run for a long time and /compact at the END OF EVERY batch. ALL
cross-batch state MUST live on disk, never in your conversation memory.
After each /compact you MUST rebuild your state from disk before doing
anything else:
  - weights/<batch+1>.json   (the next batch's weights; batch_id = the
                              highest-numbered weights file, do NOT add 1)
  - revision_log.jsonl       (what you have already changed)
  - trace.jsonl tail         (recent_ratios for the convergence test,
                              current batch_id, and the last seq)
"Memory is not trustworthy; disk is the only source of truth." If ever
unsure of the current state, re-read these from disk rather than guessing.

# Boundary (W5 — check-blind, absolute)
You never see and never emit the detection signatures. The loss skills judge
"was the generating condition faithfully executed" and "is the quality
ladder monotone", NOT "does this research pass some specific check". The
probe (a separate, downstream session) is the ONLY session that ever sees
the checks. Every config and every revised prose you produce passes
leak_audit. Not one step beyond the skill on this.

# If you get stuck
If backprop cannot resolve a failure (e.g. you keep revising the same weight
across batches and the loss will not move), do NOT thrash. Write a HALT.json
(cause + on-disk snapshot pointers) per the skill and stop in place; a human
inspector will pick it up. Halting cleanly with a stated cause is a correct
outcome, not a failure.

# Begin
Load the `optimization-loop` skill and start the epoch loop from cold start
(batch-0, weights/batch-0.json from weights.dump_initial) now.
```
Expected: full text landed on disk; `grep -E -- '-p |--resume|--session-id|--allowedTools' ops/optimizer-opening-prompt.txt` returns no match (honors the locked constraints).

- [ ] **Step 2: write start_optimizer.sh (tmux ignition + readiness probe + send prompt)**

Create `<proj>/ops/start_optimizer.sh`:
```bash
#!/usr/bin/env bash
# C's one-time startup script (not a hot path). tmux long-running optimizer + readiness probe + send opening prompt.
set -euo pipefail
PROMPT_FILE="$(dirname "$0")/optimizer-opening-prompt.txt"
READY_MARKER='<REPL_READY_MARKER>'   # filled by measurement: the claude 2.1.x readiness-screen signature string

# 1. create session + prepare environment + set the optimizer's dedicated config-dir
tmux new-session -d -s opt
tmux send-keys -t opt 'source /workspace/env.sh && source /workspace/bootstrap.sh' Enter
tmux send-keys -t opt 'export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude' Enter

# 2. ignite the optimizer's claude
tmux send-keys -t opt 'cd /workspace/work/optim && claude' Enter

# 3. poll capture-pane until the REPL prompt appears stably (≤0.5s interval, local probe, only once at startup)
until tmux capture-pane -p -t opt | tail -n 5 | grep -q "$READY_MARKER"; do
  sleep 0.5
done

# 4. once ready, send the opening prompt full text (multi-line: load into tmux buffer then paste, to avoid truncation by a mid-stream Enter)
tmux load-buffer "$PROMPT_FILE"
tmux paste-buffer -t opt
tmux send-keys -t opt Enter
```
Expected: the script is executable; the readiness probe polls tmux output (no fixed sleep).

> **Three grounding points**: ① `<REPL_READY_MARKER>` is determined by measurement against the claude version (written into a script comment, not hard-coded into the spec); ② the multi-line prompt is sent as one block via `load-buffer`+`paste-buffer`, avoiding truncation by a mid-stream Enter; ③ this script runs only once at optimizer cold start, never on the batch hot path.

- [ ] **Step 3: commit C0b**
```bash
git add ops/optimizer-opening-prompt.txt ops/start_optimizer.sh
git commit -m "feat(C0): optimizer ignition — opening prompt full text + start_optimizer.sh (tmux readiness probe)"
```

---

### Task C1: PT5 two-sample endpoint pilot (go/no-go hard gate)

**Files:**
- Create: `<proj>/tests/e2e/test_pt5_pilot.md` (R, manually-executed checklist + go/no-go criteria)
- artifacts land in `runs/<pilot-id>/` (device-local, gitignore)

Build only **2 endpoint samples**: id0 (genius, A5=G+ generativity) / id5 (absurd-contrarian, completability floor). Real CC/codex full-chain run, specifically verifying the #1 kill-risk. **This is the hard gate: not passing → write HALT and return to B, never enter C2.**

- [ ] **Step 1: write the PT5 pilot execution checklist + two-probe criteria**

Create `<proj>/tests/e2e/test_pt5_pilot.md`:
```markdown
# C1 PT5 pilot: 2 endpoint samples (real claude/codex, go/no-go hard gate)
Prerequisites: A environment green, B components green (incl. B7 single-topic 6-rung having run). Use the two endpoints of topic-00 (or any real topic).

## Run (only 2 runs, don't burn full-batch)
1. new_run_id.py creates runs/<pilot-id>/; weights.dump_initial emits batch-0.json.
2. gen_configs builds only 2 cards: id0 (A1=L0 high-substance/A5=G+ generative) + id5 (A1=L4 low-substance/contrarian/clinging to F7).
3. run each full chain: sim really plays its role → exec really researches → concat the triple → loss-1.
4. run_codex_loss (loss-2) does K pairwise judgments over (id0,id5) → endpoint_separation.

## Two probes (the #1 kill-risk)
- **AS-1 probe (does the rigor floor resist downward pressure?)**: can id5 be pressured bad enough to separate from the id0 endpoint?
  Criterion: loss-2 `endpoint_separation_pass=true` (id0 beats id5 ≥ K−allowance times across the K pairwise judgments).
- **AS-4 probe (does revising the prose layer move loss-2?)**: revise `interp_params` once (endpoint_spread or granularity_map), rerun the two endpoints, observe whether loss-2 endpoint separation/τ changes.
  Criterion: after revising the prose layer, loss-2 shows a **measurable change** (no movement at all → interpolator trainability is null).

## Gate decision (already decided)
- **go (unlock C2)**: endpoints separate (AS-1 passes) + revising the prose layer moves loss-2 (AS-4 passes).
- **no-go (write HALT, return to B)**: endpoints don't separate / revising the prose layer doesn't move loss-2 → write runs/<pilot-id>/HALT.json (cause=pilot_fail + on-site pointers) → stop and return to Spec B to revise prose or endpoint coordinates. **no-go is also a legitimate delivery** (it correctly blocked burning full-batch).
```

- [ ] **Step 2: genuinely run PT5 pilot on device (2 runs, all real)**

Run (on device, both key sets configured): run the 2 endpoint samples full chain per the checklist + the AS-4 prose-layer-revision rerun.
Expected: produce 2 endpoint triples + loss-2 endpoint_separation + AS-4 before/after prose-layer-revision comparison.

- [ ] **Step 3: fill measured thresholds during pilot (F8 / K / allowance / completability)**

From pilot measurements, write these pilot-tunable thresholds into `<proj>/skills/optimization-loop/references/gate-thresholds.md` (overriding B's placeholders):
- `turn_budget` (=F8): the measured pressure_turns / closing_turns for exec running one formated-specs closed loop.
- the measured `K` / `allowance` values for loss-2 endpoint separation (B placeholder K=5, allowance=1).
- the per-run timeout / turn cap for completability failure (a child CC with no return for over N minutes is judged failed).
Expected: the pilot-tunable values in gate-thresholds.md are switched from placeholders to measured values.

- [ ] **Step 4: gate decision — go enters C2, no-go writes HALT and returns to B**

Decision:
- **go**: AS-1 passes (endpoints separate) + AS-4 passes (prose layer is movable) → record in the pilot report, unlock C2.
- **no-go**: write `runs/<pilot-id>/HALT.json`:
```json
{"cause":"pilot_fail","detail":"endpoints don't separate / revising prose layer doesn't move loss-2","snapshot":{"weights":"weights/batch-0.json","loss2":"loss/<topic>.loss2.json"},"action":"return to Spec B to revise prose or endpoint coordinates"}
```
Expected: go → enter C2; no-go → stop at HALT, **never enter C2** (legitimate delivery).
```bash
git add tests/e2e/test_pt5_pilot.md skills/optimization-loop/references/gate-thresholds.md
git commit -m "feat(C1): PT5 two-sample endpoint pilot hard gate (AS-1 endpoint separation + AS-4 prose-layer trainability)"
```

> **★C1 is C's hard gate**: it specifically blocks the two #1 kill-risks B never deeply verified — "the endpoints can't be separated by nature / interpolator trainability is null". Burning full-batch when the pilot doesn't pass = feeding the whole batch of token to a system that can't be trained. no-go correctly blocking it is a victory of the design, not a failure.

---

### Task C2: full LOOP-2 loop to convergence (the backprop intelligent point genuinely tested)

**Files:**
- Create: `<proj>/tests/e2e/test_full_loop.md` (R, full-loop execution + acceptance checklist)
- artifacts land in `runs/<run-id>/` (device-local, gitignore)

Entered only after pilot go. The 48-run batch (8 topics × 6 rungs) runs repeatedly, routing through T/F1/F2 three branches at the end of each batch, until **3 consecutive batches pass the gate**. The backprop intelligent point ③ genuinely revises weights here. tmux long-running optimizer + `/compact` self-recovery.

- [ ] **Step 1: write the full-loop execution + three-branch routing acceptance checklist**

Create `<proj>/tests/e2e/test_full_loop.md`:
```markdown
# C2 full LOOP-2 (real claude/codex, run to convergence)
Prerequisites: C1 pilot go; ops/start_optimizer.sh ready; optimization-loop skill already copied into the optim config-dir.

## Run (tmux long-running)
1. bash ops/start_optimizer.sh → optimizer-CC starts, loads the skill, receives the opening prompt.
2. optimizer self-runs per §loop: each batch = 48 runs (8 topics × 6 rungs), cold-start batch-0 (weights.dump_initial).
3. at the end of each batch, three branches per (batch_passed × converged):
   - **T** (3 consecutive batches passed): emit converged + run_end → enter C3 freeze.
   - **F1** (passed but not 3 in a row): apply_weight_update --copy byte-copies weights/<batch+1>.json (no revision_log, no weight_revised) → batch_id+1 and run again.
   - **F2** (not passed): §backprop attributes first (read batch_done.topic_pass_flags → the topic_done of the failed topic → if needed the loss/*.json verdict) → revise one of the three weights (single variable) → apply_weight_update writes weights/<batch+1>.json + revision_log + weight_revised → /compact → recover from disk → next batch.
4. optimizer runs /compact at the end of each batch, and after compact rebuilds state from disk (weights/<batch+1>.json + revision_log + trace tail).

## Acceptance (C2 core)
- [ ] At least one **F2 backprop genuinely revising a weight**: revision_log.jsonl gains one {target,key,old,new,reason}; trace gains weight_revised; weights/<batch+1>.json has only that one key in that one section changed (single-variable controlled).
- [ ] At least one **F1 byte-copy forward**: weights/<batch+1>.json is byte-identical to <batch>.json, with no corresponding revision_log line, no weight_revised.
- [ ] **/compact self-recovery**: after /compact at the end of some batch, the optimizer reads back the correct batch_id from disk (the highest-numbered weights file itself, not +1) + recent_ratios, and continues without confusion.
- [ ] **Final convergence**: trace gains converged (the last 3 of recent_ratios all ≥0.80) + run_end.
- [ ] **Or write HALT exposing AS-4**: if backprop repeatedly revises the same weight and loss doesn't drop → optimizer writes HALT.json (can't be trained), also a legitimate exposure (see C4).
- [ ] **no-fake**: real sim/exec/codex throughout; the only synthesized things are config+topic.

## Not verified (already the endpoint)
C2 is the whole-system terminal loop; there is no higher layer.
```

- [ ] **Step 2: genuinely run full LOOP-2 to convergence on device (or write HALT)**

Run (on device, tmux long-running): `bash ops/start_optimizer.sh`, then the optimizer self-runs.
Expected: ≥1 F2 genuine weight revision + ≥1 F1 byte-copy forward, finally 3 consecutive batches pass the gate and converge; or write HALT exposing AS-4 trainability doubt (also a legitimate delivery).

- [ ] **Step 3: verify three-branch routing + batch_id recovery invariant**

Run (on device, read-only check):
```bash
RID=$(ls -t runs | head -1)
# F2 traces
grep -c weight_revised runs/$RID/trace.jsonl          # ≥1
wc -l runs/$RID/revision_log.jsonl                    # ≥1 (F2 revision history)
# batch_id recovery invariant: the highest-numbered weights file = the next batch
ls runs/$RID/weights/                                  # batch-0.json .. batch-N.json contiguous, no gaps
# convergence
grep -c converged runs/$RID/trace.jsonl                # 1 (if converged) or check HALT.json
ls runs/$RID/HALT.json 2>/dev/null && echo "HALTED" || echo "no halt"
```
Expected: F2 traces present; weights numbering contiguous (both F1/F2 pre-write the next batch, confirming the "max not +1" invariant); convergence emits converged, or one of them writes HALT.
```bash
git add tests/e2e/test_full_loop.md
git commit -m "feat(C2): full LOOP-2 convergence (F2 backprop genuine revise + F1 byte-copy forward + /compact self-recovery)"
```

> **★C's biggest risk point**: backprop is the only intelligent point in the final design, and stage B never deeply verified it. After C2 starts running, if backprop repeatedly revises the same weight and still can't move it (suspected AS-4 trainability null) → write HALT (C4). This is the core that C must watch on-site.

---

### Task C3: freeze + coverage_report + full labeled dataset output

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/freeze.py` (NEW)
- Create: `<proj>/skills/optimization-loop/scripts/coverage_report.py` (NEW, pure generation-side aggregation, no log path)
- Test: `<proj>/tests/test_coverage_report.py` (P)

After convergence, freeze the weights + emit the coverage report + land the full labeled dataset in `dataset/`.

- [ ] **Step 1: implement freeze.py (copy the last gate-passing batch weights as frozen.json)**

Create `<proj>/skills/optimization-loop/scripts/freeze.py`:
```python
#!/usr/bin/env python3
"""Copy the last gate-passing batch's weights/<batch>.json into weights/frozen.json. All historical snapshots are kept (for replaying the backprop trajectory)."""
import argparse, shutil
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights-dir", required=True)
    ap.add_argument("--batch-id", required=True)     # the last gate-passing batch
    a = ap.parse_args()
    src = Path(a.weights_dir)/f"{a.batch_id}.json"
    shutil.copy(src, Path(a.weights_dir)/"frozen.json")   # frozen is the finalized version; batch-* snapshots are not deleted

if __name__ == "__main__":
    main()
```
Expected: frozen.json = the finalized three weights; all batch snapshots retained.

- [ ] **Step 2: write the coverage_report failing test (whitelist + no log path)**

Create `<proj>/tests/test_coverage_report.py`:
```python
import json, subprocess, sys
from pathlib import Path

# forbidden probe-side/privacy fields (coverage holds only generation-side)
FORBIDDEN = ["PG","NG","GG","OB","/workspace/home", ".claude/projects", "--logs-dir"]

def test_coverage_no_forbidden_fields(tmp_path):
    # build a minimal dataset + trace
    ds = tmp_path/"dataset"/"topic-00"; ds.mkdir(parents=True)
    (ds/"s.json").write_text(json.dumps({"sample_id":"batch-0-topic00-id0",
        "label":{"rung_id":0,"axis_levels":{"A1":"L0"}},"loss1_fidelity":1.0,"topic_pass":True}))
    trace = tmp_path/"trace.jsonl"
    trace.write_text(json.dumps({"event":"batch_done","pass_ratio":0.875,"batch_passed":True,"recent_ratios":[0.875]})+"\n")
    out = tmp_path/"coverage_report.md"
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/coverage_report.py",
        "--dataset", str(tmp_path/"dataset"), "--trace", str(trace), "--out", str(out)])
    txt = out.read_text()
    for f in FORBIDDEN:
        assert f not in txt           # probe-side distribution + log path never enter the report
    assert "topic-00" in txt          # generation-side coverage really was tallied
```

- [ ] **Step 3: run red → implement coverage_report.py → run green**

Run → FAIL. Create `<proj>/skills/optimization-loop/scripts/coverage_report.py`:
```python
#!/usr/bin/env python3
"""Scan dataset/ + trace, emit coverage_report.md. Pure generation-side aggregation, passes a whitelist before writing to disk (no PG/NG/GG/OB, no log path)."""
import argparse, json
from pathlib import Path

FORBIDDEN = ["PG","NG","GG","OB","/workspace/home",".claude/projects","--logs-dir"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True); ap.add_argument("--trace", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    # generation-side aggregation: per-axis per-level counts + samples per topic + gate-pass/yield
    axis_counts, topic_counts = {}, {}
    for f in Path(a.dataset).rglob("*.json"):
        s = json.loads(f.read_text())
        topic = f.parent.name
        topic_counts[topic] = topic_counts.get(topic,0)+1
        for ax,lv in s.get("label",{}).get("axis_levels",{}).items():
            axis_counts.setdefault(ax,{}).setdefault(lv,0)
            axis_counts[ax][lv]+=1
    lines = ["# Coverage Report (generation-side aggregation, no log path)", ""]
    lines.append("## samples per topic")
    for t,c in sorted(topic_counts.items()): lines.append(f"- {t}: {c}")
    lines.append("\n## axis-coordinate coverage (RR-2: make monoculture visible)")
    for ax,lvs in sorted(axis_counts.items()):
        lines.append(f"- {ax}: " + ", ".join(f"{lv}={n}" for lv,n in sorted(lvs.items())))
    report = "\n".join(lines)
    # whitelist check before writing: hitting a forbidden word is a hard failure (privacy + no probe-side)
    for bad in FORBIDDEN:
        if bad in report:
            raise SystemExit(f"FATAL: coverage report contains forbidden token {bad!r}")
    Path(a.out).write_text(report, encoding="utf-8")

if __name__ == "__main__":
    main()
```
Run → PASS.
```bash
git add skills/optimization-loop/scripts/freeze.py \
        skills/optimization-loop/scripts/coverage_report.py tests/test_coverage_report.py
git commit -m "feat(C3): freeze.py (finalize + keep snapshots) + coverage_report.py (generation-side aggregation, whitelist hard failure)"
```

- [ ] **Step 4: genuinely run freeze + coverage on device after convergence**

Run (on device, after convergence):
```bash
RID=$(ls -t runs | head -1)
python skills/optimization-loop/scripts/freeze.py --weights-dir runs/$RID/weights --batch-id <last gate-passing batch>
python skills/optimization-loop/scripts/coverage_report.py \
  --dataset runs/$RID/dataset --trace runs/$RID/trace.jsonl --out runs/$RID/coverage_report.md
grep -rlE '/workspace/home|\.claude/projects' runs/$RID/dataset runs/$RID/coverage_report.md && echo LEAK || echo "NO LEAK"
```
Expected: frozen.json + coverage_report.md both landed; dataset/ full labeled samples present; prints `NO LEAK`.

---

### Task C4: supervision interface — primary (claude inspection) + auxiliary (self-explanatory artifacts) + HALT.json

**Files:**
- Create: `<proj>/tests/e2e/test_supervision.md` (R, inspection checklist + HALT criteria)
- do NOT write inspect.py (decided: inspection is on-site read-only manual checking, not solidified into a script)

Supervision = primary (claude periodically SSHes in for read-only inspection) + auxiliary (CHECKPOINT artifacts are complete and self-explanatory). Human intervention = explicit HALT.json on disk + inspection findings. **Read-only, never triggers control, never revises weights.**

- [ ] **Step 1: write the inspection checklist (on-site Bash read-only manual check, not solidified)**

Create `<proj>/tests/e2e/test_supervision.md`:
```markdown
# C4 supervision: claude SSH read-only inspection (on-site Bash manual check, no inspect.py written)
The user periodically calls me onto the remote, and I judge progress health with on-site read-only commands (RID=$(ls -t runs|head -1)):

## Progress
- tail -n 20 runs/$RID/trace.jsonl → which batch/topic/rung we're at now, recent_ratios, consecutive gate-passes.

## Health
- whether a rung is stuck: some sample's dialogue_turn not increasing for a long time (compare ts).
- completability failures piling up: grep completability runs/$RID/trace.jsonl.
- leak_audit interrupting repeatedly: check optimizer output/HALT.json.

## Trajectory
- tail runs/$RID/revision_log.jsonl → which weight the most recent weight_revised changed (see what backprop is doing).

## Anomalies
- loss schema parse failure / codex error / trace seq break (seq should increase contiguously).

## HALT
- ls runs/$RID/HALT.json → locate the optimizer's self-stop cause at a glance (see table below).

## Judgment (read-only, no control)
healthy → continue / stuck → needs clearing / off-track → stop and return to B. Never trigger control, never revise weights.
```

- [ ] **Step 2: HALT.json four-stop-cause convention (optimizer self-stop + my inspection findings)**

When the optimizer hits a situation it can't handle, it writes the stop cause + on-site snapshot pointers to `runs/<run_id>/HALT.json`, stays put in tmux, and waits for an inspection to find it:

| Stop cause | Criterion | Handling |
| --- | --- | --- |
| pilot fails | C1 endpoints don't separate / prose layer doesn't move | return to Spec B to revise prose or endpoint coordinates |
| rung stuck | dialogue_turn times out without increasing / child CC doesn't return | judge that run a completability failure, clear and rerun that rung |
| leak hard interrupt | leak_audit still hits after 3 consecutive times | prose weight is broken, return to B to check axis_prose |
| can't be trained (suspected AS-4) | backprop repeatedly revises the same weight and loss doesn't drop | trainability in doubt, return to B to re-review interp_params / endpoint coordinates |

HALT.json schema (self-explanatory CHECKPOINT artifact):
```json
{"cause":"<pilot_fail|rung_stuck|leak_hard|untrainable>","detail":"<human-readable explanation>","snapshot":{"weights":"weights/<batch>.json","trace_tail_seq":<N>},"action":"<suggested handling>"}
```
Expected: the four-stop-cause convention is written into the optimization-loop skill §state (B6 wrote the skeleton, C adds the HALT-writing); inspection can locate it at a glance.

- [ ] **Step 3: verify the supervision interface (artifacts can rebuild state + HALT is locatable)**

Run (on device, read-only): inspect a running (or already-converged) run once per the `test_supervision.md` checklist.
Expected: can fully rebuild "where we are now, healthy or not, what was changed" from the artifacts; if there's a HALT, can locate the stop cause at a glance.

- [ ] **Step 4: commit C4**
```bash
git add tests/e2e/test_supervision.md
git commit -m "feat(C4): supervision interface — claude read-only inspection checklist + HALT.json four-stop-cause convention"
```

> **★HTML readable window deferred**: once it's genuinely running with data, tune the styling against real data, not against an empty runs/. C's supervision responsibility converges to one sentence: "artifacts are complete, self-explanatory, read-only inspectable".

---

## Completion criteria (Spec C = three-stage wrap-up)

- **C1 acceptance**: PT5 pilot real CC/codex produces 2 endpoints → clear go (endpoints separate + prose layer movable) or no-go (write HALT, return to B). **no-go is also a legitimate delivery**.
- **C2 acceptance**: after go, full LOOP-2 genuinely runs, with ≥1 F2 backprop genuine weight revision + ≥1 F1 byte-copy forward, finally 3 consecutive batches pass the gate and converge (or write HALT exposing AS-4).
- **C3 acceptance**: frozen.json + full weights snapshots + coverage_report.md (pure generation-side, no log path) + dataset/ labeled samples all present.
- **Supervision acceptance**: can fully rebuild "where we are now, healthy or not, what was changed" from the artifacts; HALT can be located at a glance.
- **Privacy acceptance**: no committed artifact has a CC log path or key value; dataset/coverage passes the whitelist check.

## Self-Review (checking against Spec C)

- **Three stages (§1) covered**: C1 PT5 pilot hard gate (Task C1), C2 full LOOP-2 (Task C2), C3 freeze+output (Task C3) — each has a Task.
- **Convergence routing T/F1/F2 (§2) covered**: Task C2 Step 1 three-branch routing + Step 3 batch_id "max not +1" recovery-invariant verification; F2 backprop single-variable, F1 byte-copy each have an acceptance item.
- **Supervision primary+auxiliary (§3) covered**: Task C4 primary (claude read-only inspection checklist, no inspect.py written) + auxiliary (self-explanatory artifacts); HTML deferral noted.
- **HALT.json four stop causes (§4) covered**: Task C4 Step 2 four-stop-cause table + schema.
- **Ignition deliverables (§7) covered**: Task C0b opening prompt full text (honoring locked constraints) + start_optimizer.sh readiness probe.
- **8 real topics (§8) covered**: Task C0a eight topics + schema test + check-blind test.
- **Privacy red line (§6) covered**: coverage_report whitelist hard failure (C3 test), dataset NO LEAK scan (C3 Step 4), runs/ gitignore, keys don't enter committed artifacts.
- **Type consistency**: `apply_weight_update --copy` (F1) and `--target/--key/--new/--reason` (F2) signatures follow B6; `gate_eval` three modes follow B5; trace event names (weight_revised/converged/run_end/batch_done) follow B's trace_emit; HALT.json schema is consistent across C1/C4.
- **Placeholder scan**: `<REPL_READY_MARKER>` (claude-version-dependent, filled by measurement at grounding), the pilot-tunable values of gate-thresholds (filled by measurement at C1 Step 3), the 8 topic full_text (landed verbatim per §8.3 at C0a Step 3) are all **deliberately deferred to grounding/pilot**, with who fills and when noted — not plan gaps.

## Execution Handoff

See the index plan `2026-06-07-INDEX-triple-cc-pretrain.md`. C depends on A (environment) + B (components) all green; the C1 pilot is the hard gate, no-go means stop and return to B.
