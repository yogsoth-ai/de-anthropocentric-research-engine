# DESIGN

- [DESIGN](#design)
  - [tmux long-running launch of optimizer-cc](#tmux-long-running-launch-of-optimizer-cc)
    - [tmux new-session -d -s opt](#tmux-new-session--d--s-opt)
    - [source /workspace/env.sh \&\& source /workspace/bootstrap.sh](#source-workspaceenvsh--source-workspacebootstrapsh)
      - [`/workspace/env.sh`〔SH · KEEP · verified〕](#workspaceenvshsh--keep--verified)
      - [`/workspace/bootstrap.sh`〔SH · KEEP · verified · idempotent〕](#workspacebootstrapshsh--keep--verified--idempotent)
    - [export CLAUDE\_CONFIG\_DIR=/workspace/home/optim/.claude](#export-claude_config_dirworkspacehomeoptimclaude)
    - [cd /workspace/work/optim \&\& claude](#cd-workspaceworkoptim--claude)
  - [optimization-loop skill specifies the full task](#optimization-loop-skill-specifies-the-full-task)
    - [Contains: epoch/LOOP-1/2 control flow + gate decision rules + backprop heuristics + state-persistence conventions check-blind(W5)](#contains-epochloop-12-control-flow--gate-decision-rules--backprop-heuristics--state-persistence-conventions-check-blindw5)
      - [`optimization-loop/SKILL.md`〔NEW-SKILL〕](#optimization-loopskillmdnew-skill)
  - [epochs-loop (unbounded, run to convergence)](#epochs-loop-unbounded-run-to-convergence)
    - [Leaf-script orchestration overview (the structural cornerstone of this design, spanning all subsequent Hs)](#leaf-script-orchestration-overview-the-structural-cornerstone-of-this-design-spanning-all-subsequent-hs)
      - [Skill directory structure](#skill-directory-structure)
      - [Script orchestration table (trigger timing · input · output)](#script-orchestration-table-trigger-timing--input--output)
      - [`new_run_id.py`〔NEW · scripts/〕](#new_run_idpynew--scripts)
    - [One epoch = m=8 topic × n=6 personas = 48 run (LOOP-2)](#one-epoch--m8-topic--n6-personas--48-run-loop-2)
    - [interpolator interpolates to obtain 48 research\_config](#interpolator-interpolates-to-obtain-48-research_config)
      - [Three-way split (the core of this design — derived through three rounds of insight)](#three-way-split-the-core-of-this-design--derived-through-three-rounds-of-insight)
      - [★Key constraint: collision perturbation may only use B1 / expression layer, never A1–A5](#key-constraint-collision-perturbation-may-only-use-b1--expression-layer-never-a1a5)
      - [★Trainability is conditional (the product of CLR-checking AS-4)](#trainability-is-conditional-the-product-of-clr-checking-as-4)
      - [`gen_configs.py` as a whole〔NEW · scripts/〕](#gen_configspy-as-a-wholenew--scripts)
      - [Read weights weights/\<batch\>.json](#read-weights-weightsbatchjson)
      - [Call interpolator.ladder\_levels(n=6) → 6-rung level mapping](#call-interpolatorladder_levelsn6--6-rung-level-mapping)
      - [Call assembler.build\_batch(...) → 6-rung coordinate assembly](#call-assemblerbuild_batch--6-rung-coordinate-assembly)
      - [Call axes.level\_text(axis,level) → fill rung prose](#call-axeslevel_textaxislevel--fill-rung-prose)
      - [Each card passes leak\_audit(text) → W5 blocks check words](#each-card-passes-leak_audittext--w5-blocks-check-words)
      - [Output 6 cards × 8 topic = 48 config json → runs/\<id\>/configs/](#output-6-cards--8-topic--48-config-json--runsidconfigs)
    - [\[grouped by topic\] for topic\_i in 8](#grouped-by-topic-for-topic_i-in-8)
      - [for rung in 6 ── start one run (LOOP-1)](#for-rung-in-6--start-one-run-loop-1)
        - [Start sim-simulator-cc (interactive REPL, fresh per run)](#start-sim-simulator-cc-interactive-repl-fresh-per-run)
          - [Bash directly launches claude (IS\_SANDBOX=1 + CLAUDE\_CONFIG\_DIR=sim + cd /workspace/work/sim), no driver script](#bash-directly-launches-claudeis_sandbox1--claude_config_dirsim--cd-workspaceworksim-no-driver-script)
        - [optimizer injects research\_config into sim via conversation](#optimizer-injects-research_config-into-sim-via-conversation)
          - [First message: full config + role-play instruction + "start exec, run the research to completion, reply DONE to me"](#first-message-full-config--role-play-instruction--start-exec-run-the-research-to-completion-reply-done-to-me)
        - [optimizer closes sim-simulator-cc](#optimizer-closes-sim-simulator-cc)
        - [concat (research\_config, research\_graph, research\_result)](#concat-research_config-research_graph-research_result)
          - [Read configs/\<sample\>.json + transcripts/\<sample\>.md](#read-configssamplejson--transcriptssamplemd)
          - [Extract the graph / result structured blocks from exec's formated-specs/results](#extract-the-graph--result-structured-blocks-from-execs-formated-specsresults)
          - [Output the triple → runs/\<id\>/triples/\<sample\>.json](#output-the-triple--runsidtriplessamplejson)
        - [Launch codex → injection-fidelity → loss-1](#launch-codex--injection-fidelity--loss-1)
          - [Inject the full SKILL.md](#inject-the-full-skillmd)
          - [codex exec --output-schema loss1.json -o ... \<payload=transcript\>](#codex-exec---output-schema-loss1json--o--payloadtranscript)
          - [parse\_loss1 → this run's fidelity value → cache runs/\<id\>/loss/](#parse_loss1--this-runs-fidelity-value--cache-runsidloss)
        - [IF rung \< 5 ── inner-loop jump-back decision](#if-rung--5--inner-loop-jump-back-decision)
      - [── per-topic aggregation (reached only after the inner loop completes all 6 rungs) ──](#-per-topic-aggregation-reached-only-after-the-inner-loop-completes-all-6-rungs-)
        - [codex → ladder-quality-order → loss-2 (consumes 6-rung triples)](#codex--ladder-quality-order--loss-2-consumes-6-rung-triples)
        - [gate.topic\_passes (fidelity rate≥90% ∧ mono ∧ endpoint)](#gatetopic_passes-fidelity-rate90--mono--endpoint)
        - [Write this topic's 6 samples](#write-this-topics-6-samples)
      - [IF topic\_i \< 7](#if-topic_i--7)
        - [T: topic+1 → LOOP (back to outer FOR)](#t-topic1--loop-back-to-outer-for)
        - [F: all 8 topics done (48 run) → END LOOP-1](#f-all-8-topics-done-48-run--end-loop-1)
    - [Consolidate the convergence status of the 8 topics](#consolidate-the-convergence-status-of-the-8-topics)
    - [batch\_pass\_ratio ≥80% (i.e. ≥7/8 topics pass) → gate passed](#batch_pass_ratio-80-ie-78-topics-pass--gate-passed)
    - [IF 3 consecutive batches pass the gate](#if-3-consecutive-batches-pass-the-gate)
      - [T: END LOOP-2](#t-end-loop-2)
        - [freeze\_weights + coverage\_report](#freeze_weights--coverage_report)
      - [F1: gate passed but not converged — weights unchanged, advance one batch to confirm](#f1-gate-passed-but-not-converged--weights-unchanged-advance-one-batch-to-confirm)
      - [F2: backprop + weight update + LOOP ── intelligence point (optimizer thinks)](#f2-backprop--weight-update--loop--intelligence-point-optimizer-thinks)
        - [Read this batch's loss signals + which gate item of which topic failed](#read-this-batchs-loss-signals--which-gate-item-of-which-topic-failed)
        - [optimizer optim rung prose](#optimizer-optim-rung-prose)
          - [weights.revise("axis\_prose", k, new, reason)](#weightsreviseaxis_prose-k-new-reason)
          - [Modify the axis\_prose section of weights/\<batch\>.json (data-faction, axes.py untouched)](#modify-the-axis_prose-section-of-weightsbatchjson-data-faction-axespy-untouched)
        - [optimizer optim interpolator](#optimizer-optim-interpolator)
          - [weights.revise("interp\_params", k, ...)](#weightsreviseinterp_params-k-)
        - [optimizer optim generator assembly logic](#optimizer-optim-generator-assembly-logic)
          - [weights.revise("assembler\_params", k, ...)](#weightsreviseassembler_params-k-)
        - [/compact + reload optimization-loop skill → LOOP](#compact--reload-optimization-loop-skill--loop)
          - [Re-read weights/\<batch+1\>.json + revision\_log.jsonl + trace tail](#re-read-weightsbatch1json--revision_logjsonl--trace-tail)
  - [END](#end)

```bash
pretraining
  │
  ├─ tmux long-running launch of optimizer-cc                              〔SH four independent commands, run one by one by hand, not packaged〕
  │    ├─ tmux new-session -d -s opt                                       〔detaches from this machine, can close at night〕
  │    ├─ source /workspace/env.sh && source /workspace/bootstrap.sh       〔KEEP already exists〕
  │    ├─ export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude                 〔optimizer-specific〕
  │    └─ cd /workspace/work/optim && claude                              〔interactive long-running REPL; after launch, send-keys the opening prompt〕
  │
  ├─ optimization-loop skill specifies the full task                       〔NEW-SKILL .claude/skills/optimization-loop/SKILL.md〕
  │    └─ Contains: epoch/LOOP-1/2 control flow + gate decision rules + backprop heuristics + state-persistence conventions; check-blind(W5)
  │
  ├─ epochs-loop (unbounded, run to convergence)                           〔SKILL §loop〕〔TRACE run_start〕  <==CHECKPOINT: create runs/<run_id>/trace.jsonl, run_start is the first line; thereafter all 〔TRACE x〕 are appended line by line in time order here (the 11-event ledger)
  │    │
  │    ├─ one epoch = m=8 topic × n=6 personas = 48 run (LOOP-2)            〔TRACE batch_start(batch_id)〕  <==CHECKPOINT: append one line batch_start{batch_id} to trace.jsonl; the boundary marker for each epoch
  │    │
  │    ├─ interpolator interpolates to obtain 48 research_config           〔NEW gen_configs.py〕
  │    │    ├─ read weights weights/<batch>.json                           〔KEEP weights.load〕
  │    │    ├─ call interpolator.ladder_levels(n=6)  →  6-rung level mapping        〔WEIGHT② interpolator.py〕
  │    │    ├─ call assembler.build_batch(...)        →  6-rung coordinate assembly 〔WEIGHT③ assembler.py〕
  │    │    ├─ call axes.level_text(axis,level)       →  fill rung prose            〔WEIGHT① axes.py〕
  │    │    ├─ each card passes leak_audit(text)      →  W5 blocks check words      〔KEEP leak_audit.py〕
  │    │    └─ output 6 cards × 8 topic = 48 config json  →  runs/<id>/configs/  〔KEEP cards.to_dict〕  <==CHECKPOINT: runs/<id>/configs/<sample>.json, 48 full research_config texts (the product of interpolation+assembly+prose, i.e. each sim persona); this is the 1st element of the triple
  │    │
  │    ├─ [grouped by topic] for topic_i in 8:                             〔TRACE topic_start(topic_id)〕  <==CHECKPOINT: append topic_start{topic_id} to trace.jsonl; the outer entry for 8 topics
  │    │  ├─ for rung in 6 ── start one run (LOOP-1)                        〔TRACE rung_start(rung_id)〕  <==CHECKPOINT: append rung_start{rung_id} to trace.jsonl; the inner entry for 6 rungs, marking the start of one run
  │    │  │    │
  │    │  │    ├─ start sim-simulator-cc (interactive REPL, fresh per run)  〔Bash directly launches claude〕
  │    │  │    │    └─ IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/sim/.claude \   〔config via env var; launching a bypass REPL as root needs IS_SANDBOX=1〕
  │    │  │    │       (cd /workspace/work/sim) claude                 〔working dir via cwd; no skills, persona via injection; bypass via settings.local.json〕
  │    │  │    │
  │    │  │    ├─ optimizer injects research_config into sim via conversation 〔Bash first-turn message〕
  │    │  │    │    └─ msg = "<full config json + instruction: play this user persona, start exec to run the full research, reply DONE to me when done>"
  │    │  │    │       │
  │    │  │    │       │  ── the following happens inside sim-cc (sim's own Bash directly launches claude to drive exec) ──
  │    │  │    │       │
  │    │  │    │       ├─ sim-cc Bash starts dare-exec-cc (interactive REPL) 〔Bash directly launches claude〕
  │    │  │    │       │    └─ IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/exec/.claude \   〔771 DARE skills, W5〕
  │    │  │    │       │       (cd /workspace/work/exec) claude
  │    │  │    │       │
  │    │  │    │       ├─ sim-cc injects i_m topic + user bias + forced skill items 〔Bash feeds exec's first turn, msg contains:〕
  │    │  │    │       │    ├─ topics[i_m] text + user bias (from config)
  │    │  │    │       │    ├─ ★forced: use formated-specs instead of writing-specs 〔your added item; exec has both skills mounted〕
  │    │  │    │       │    └─ ★forced: must call formated-results at the end
  │    │  │    │       │
  │    │  │    │       ├─ sim-cc ↔ exec-cc repeated conversation to complete research 〔multiple turns back and forth on the same REPL〕
  │    │  │    │       │    └─ the dialogue auto-lands in exec's session jsonl (no self-capture needed) 〔TRACE dialogue_turn each turn; save_transcript once at run end〕  <==CHECKPOINT: ★core interaction retention★ each turn only adds one line dialogue_turn{seq} to trace.jsonl (tailable in real time); the transcript is produced by save_transcript.py **once at run end** reading exec's session jsonl (type∈{user,assistant}) and transcribing to runs/<id>/transcripts/<sample>.md (the jsonl is fully appended; one extraction at run end gives the complete dialogue, no per-turn increments needed). This is the body of "all human-machine interaction content"
  │    │  │    │       │                                                    runs/<id>/transcripts/<sample>.md
  │    │  │    │       ├─ obtain research_result                            〔exec's last-turn formated-results output〕
  │    │  │    │       ├─ sim-cc closes dare-exec-cc                        〔exit that REPL; jsonl stays on disk for inspection〕
  │    │  │    │       └─ sim-cc responds "DONE" to optimizer               〔sim's last-turn return value〕
  │    │  │    │
  │    │  │    ├─ optimizer closes sim-simulator-cc                        〔closing the session wraps it up; this run's session is voided〕
  │    │  │    │
  │    │  │    ├─ concat (research_config, research_graph, research_result) 〔NEW concat_triple.py〕
  │    │  │    │    ├─ read configs/<sample>.json                          〔1st element of the triple, gen_configs already landed it〕
  │    │  │    │    ├─ read transcripts/<sample>.md (save_transcript already landed it) → extract graph/result structured blocks
  │    │  │    │    └─ output the triple → runs/<id>/triples/<sample>.json  <==CHECKPOINT: runs/<id>/triples/<sample>.json, the (research_config, research_graph, research_result) triple composite; config taken from configs/<sample>.json, graph/result taken from exec's last-turn formated-specs/results structured output (landed into the transcript via save_transcript); the input unit fed to codex to compute loss
  │    │  │    │
  │    │  │    ├─ launch codex → injection-fidelity → loss-1                〔FIX run_codex_loss.py〕
  │    │  │    │    ├─ inject the full SKILL.md                            〔cwd=/workspace/work/loss〕
  │    │  │    │    ├─ codex exec --output-schema loss1.json -o ... <payload=transcript>
  │    │  │    │    └─ parse_loss1 → this run's fidelity value → cache runs/<id>/loss/ 〔KEEP loss_runner.parse_loss1〕  <==CHECKPOINT: runs/<id>/loss/<sample>.loss1.json, this run's injection-fidelity result (fidelity value + codex verdict); per-run cache, used for the per-topic aggregated fidelity rate
  │    │  │    │                                                            〔TRACE rung_done(loss-1)〕  <==CHECKPOINT: append rung_done{sample_id, fidelity:bool, loss1, per_axis_evidence, drift_flag, transcript_path} to trace.jsonl; one run wraps up
  │    │  │    │
  │    │  │    └─ IF rung < 5:                                             ← inner-loop decision
  │    │  │         ├─ T: rung+1 → LOOP (back to inner for rung)
  │    │  │         └─ F: this topic's 6 rungs done → break out of inner loop, enter per-topic aggregation ↓
  │    │  │
  │    │  ├─ ── per-topic aggregation (reached only after the inner loop completes all 6 rungs) ── ★trigger point
  │    │  │    ├─ codex → ladder-quality-order → loss-2 (consumes 6-rung triples) 〔FIX run_codex_loss.py〕★  <==CHECKPOINT: runs/<id>/loss/<topic>.loss2.json, this topic's ladder-quality-order result {tau, monotonicity_pass, endpoint_separation_pass, rigor_floor_flag, pairwise_log}; per-topic, consumes 6-rung triples
  │    │  │    ├─ gate.topic_passes (fidelity rate≥90% ∧ mono ∧ endpoint)  〔KEEP gate.py〕〔TRACE topic_done〕  <==CHECKPOINT: append topic_done{tau, monotonicity_pass, endpoint_separation_pass, rigor_floor_flag, topic_pass, fidelity_rate} to trace.jsonl; this topic's gate-pass bool is recorded
  │    │  │    └─ write this topic's 6 samples                             〔KEEP dataset_writer〕  <==CHECKPOINT: ★final product★ dataset/<topic>/<sample>.json, the 6 published samples after privacy-whitelist field trimming (label=known generating condition); this is the dataset body that pretrain delivers, never containing any CC log path
  │    │  │
  │    │  └─ IF topic_i < 7:                                              ← outer-loop decision
  │    │       ├─ T: topic+1 → LOOP (back to outer for topic_i)
  │    │       └─ F: all 8 topics done (48 run) → END LOOP-1 ↓
  │    │
  │    ├─ consolidate the convergence status of the 8 topics               ★(not 48; each has already aggregated its 6 runs)
  │    ├─ batch_pass_ratio ≥80% (i.e. ≥7/8 topics pass) → gate passed      〔KEEP gate.batch_pass_ratio〕〔TRACE batch_done〕  <==CHECKPOINT: append batch_done{batch_id, pass_ratio, batch_passed} to trace.jsonl (as above, this is the original spine line)
  │    │
  │    └─ IF 3 consecutive batches pass the gate                           〔KEEP gate.converged〕
  │         │
  │         ├─ T: END LOOP-2                                               〔TRACE converged + run_end〕  <==CHECKPOINT: append converged{} + run_end{} to trace.jsonl; the entire pretrain converges and wraps up (original spine line)
  │         │     └─ freeze_weights + coverage_report                      〔KEEP freeze.py〕  <==CHECKPOINT: weights/frozen.json (the frozen final three weights) + coverage_report.md (coverage report, aggregate statistics, no log path)
  │         │
  │         └─ F: backprop + weight update + LOOP ── intelligence point ③ (optimizer thinks) 〔SKILL §backprop heuristics〕
  │                 │   read this batch's loss signals + which gate item of which topic failed
  │                 │
  │                 ├─ optimizer optim rung prose                          〔NEW apply_weight_update.py〕
  │                 │    └─ weights.revise("axis_prose",k,new,reason)       〔KEEP weights.revise; heuristic: loss-1 fails → priority〕
  │                 │       → modify the axis_prose section of weights/<batch+1>.json (data-faction, axes.py untouched)  〔WEIGHT① 〕〔TRACE weight_revised〕  <==CHECKPOINT: weights/<batch+1>.json (the updated weight-① prose snapshot, one per batch; data-faction = only the JSON data section is changed, axes.py source is always invariant) + revision_log.jsonl appends one line {target:axis_prose, key, new_value, reason}; simultaneously trace.jsonl adds weight_revised. ★never emitted before★
  │                 │
  │                 ├─ optimizer optim interpolator                        〔NEW apply_weight_update.py〕
  │                 │    └─ weights.revise("interp_params",...)             〔heuristic: loss-2 collapse → priority〕〔WEIGHT②〕〔TRACE weight_revised〕  <==CHECKPOINT: the interp_params section in weights/<batch+1>.json is updated (data-faction, interpolator.py untouched) + revision_log.jsonl appends {target:interp_params,...}; trace.jsonl adds weight_revised
  │                 │
  │                 ├─ optimizer optim generator assembly logic            〔NEW apply_weight_update.py〕
  │                 │    └─ weights.revise("assembler_params",...)          〔when the card as a whole is not built well〕〔WEIGHT③〕〔TRACE weight_revised〕  <==CHECKPOINT: the assembler_params section in weights/<batch+1>.json is updated (data-faction, assembler.py untouched) + revision_log.jsonl appends {target:assembler_params,...}; trace.jsonl adds weight_revised
  │                 │
  │                 └─ /compact + reload optimization-loop skill → LOOP     〔SKILL §state: all cross-batch state persisted to disk〕
  │                      └─ re-read weights/<batch+1>.json + revision_log.jsonl 〔CC recovers from disk after compaction, no memory dependency〕  <==CHECKPOINT(read point): after each batch's /compact, optimizer recovers cross-batch state from disk; reads weights/<batch+1>.json (new weights) + revision_log.jsonl + (optional) rolling decision log. This is a "read" checkpoint, paired with each "write" point above
  │
  └─ END
```

## tmux long-running launch of optimizer-cc

### tmux new-session -d -s opt

```markdown
You are optimizer-cc — the host of a "pseudo-neural-network pretraining"
training loop. Your role is equivalent to train.py in PyTorch. You are NOT
here to answer questions, NOT here to chat with anyone. The only reason you
exist is to drive one full training run until convergence.

# Your goal
Through repeated epoch loops, optimize three trainable weights
(level prose / interpolator / generator-assembly logic) to produce a batch
of labeled data samples. In every epoch you MUST:
generate configs → drive the lower-layer CCs to produce data →
compute loss with codex → judge the gate →
decide which weight to revise based on loss → enter the next epoch.

# Your only source of action
Your complete task specification is written in the `optimization-loop` skill.
Load that skill NOW, and execute strictly according to its control flow,
gating rules, backprop heuristics, and state-persistence conventions.

Do NOT improvise the flow. Do NOT skip the skill and act on intuition.
Do NOT deviate from the skill to do anything it did not ask for.
Whatever the skill says, that is exactly what you do.

# Long-running discipline
You will run for a long time and /compact periodically. All cross-batch
state MUST be persisted to disk. After /compact, you MUST rebuild your state
from disk (weights, revision_log), never relying on compacted-away memory.
Memory is not trustworthy; disk is the only source of truth.

# Boundary
Strictly obey the W5 constraint in the skill. Not one step beyond it.
```

### source /workspace/env.sh && source /workspace/bootstrap.sh

**What this step does**
Inside the tmux session, before launching `claude`, prepare the runtime environment. The two scripts each handle one part, in fixed order (env first, bootstrap second), and both must be sourced before `export CLAUDE_CONFIG_DIR` and `claude`.

**Decision: confirmed reuse, no changes needed (KEEP).** Both scripts were written and verified in the previous stage; this step neither writes new ones nor modifies them.

**One-time prerequisite (the device does not have tmux installed)**: the first deployment requires `apt install -y tmux` (the optimizer's long-running session depends on it). This is a one-time environment prerequisite that can be folded into bootstrap.sh's first-time check (`command -v tmux || apt install -y tmux`), idempotent.

#### `/workspace/env.sh`〔SH · KEEP · verified〕

Injects all environment variables needed for this run; the core is **two mutually isolated sets of API credentials** (grouped, must not be mixed):

- **Claude group** (for the three CC layers optimizer / sim / exec):
  - `ANTHROPIC_API_KEY = *****` (the Claude group's dedicated key, x-api-key auth)
  - `ANTHROPIC_BASE_URL = https://api.ikuncode.cc` (no suffix; the CLI appends `/v1/messages` itself)
  - `ANTHROPIC_MODEL = claude-opus-4-7`
- **Codex group** (for the codex used by the two loss computations):
  - `OPENAI_API_KEY / IKUNCODE_KEY = *****` (the Codex group's dedicated key)
  - `OPENAI_BASE_URL = https://api.ikuncode.cc/v1`
  - `OPENAI_MODEL = gpt-5.5`
- **Path-related**: `CLAUDE_CONFIG_DIR` (default value; the next H3 will re-export to override it for the optimizer), `NPM_CONFIG_PREFIX=/workspace/home/.npm-global`, `HF_HOME=/workspace/home/.hf`, `PATH` appends (claude / codex / gh / hf executable directories).

In one sentence: **make the `claude` and `codex` commands work the moment they are invoked, each connecting to its own group**.
> ⚠️ Red line: the two keys are two different groups; filling them with the same key once caused claude to report model_not_found. Keep them separate.

#### `/workspace/bootstrap.sh`〔SH · KEEP · verified · idempotent〕

The restart-recovery script. After the device reboots or a new shell opens:

- re-mounts env.sh into `~/.bashrc` (ensuring new shells automatically carry the environment);
- first-time check `command -v tmux || apt install -y tmux` (the optimizer's long-running host).

**No `~/.claude` symlink**: the four identities each use an independent config-dir; when launching claude/codex, point explicitly to `/workspace/home/{optim,sim,exec}/.claude` and `/workspace/home/loss/.codex` via the env var `CLAUDE_CONFIG_DIR=<role .claude>` (codex uses its `--config`/cwd convention), not relying on a home-directory symlink (symlinks are fragile and would cross-wire the four identities' configs).

In one sentence: **ensure that state on the persistent disk gets re-attached in any new shell**. Idempotent; re-sourcing has no side effects.

**CHECKPOINT**: none (pure environment preparation, no run data landed).

### export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude

**What this step does**
Before launching the optimizer's `claude`, point its config-dir explicitly to **`/workspace/home/optim/.claude`**. CLAUDE_CONFIG_DIR determines where this claude process reads/writes its config, session history, skill mounts, and `.claude.json`. This is a key link in the four-layer role isolation.

> **Actually adopting `/workspace/home/optim/.claude`**, so the four roles are peers and isomorphic under `home/` (optim / sim / exec / loss).

**Why export separately (rather than relying on env.sh's default)**
The four roles each have an independent config-dir, with no cross-session or cross-skill bleed. Skills are **copied into each config-dir's `skills/` directory** (not mounted); superpowers is carried by all:

| Role | config-dir | skills copied into the config-dir's `skills/` | Source |
| --- | ---------- | ------- | --- |
| optimizer | `/workspace/home/optim/.claude` | optimization-loop + superpowers | project skills/ + superpowers |
| sim | `/workspace/home/sim/.claude` | superpowers only (persona via injection) | superpowers |
| exec | `/workspace/home/exec/.claude` | 771 DARE + formated-specs/results + superpowers | DARE repo skills/ + project skills/ + superpowers |
| codex | `/workspace/home/loss/.codex` | injection-fidelity + ladder-quality-order + superpowers (codex convention) | project skills/ + superpowers |

This H3 sets only **the optimizer's own one**. The sim/exec config-dirs are set later when they are launched, each via the env var `CLAUDE_CONFIG_DIR=...` (claude has no `--config-dir` flag; the working directory is set via `cd`, no `--cwd` flag); codex's `/workspace/home/loss/.codex` is used in the loss step. Building the skill-copy matrix belongs to Spec A.

**bypass permission (unified config for the four CC roles)**
The three claude roles optimizer / sim / exec each place a `settings.local.json` under their config-dir to enable bypass permissions, so tool calls are allowed throughout — this is the prerequisite for the whole pipeline to run unattended for a long time (overnight hand-off). The three files:

- `/workspace/home/optim/.claude/settings.local.json`
- `/workspace/home/sim/.claude/settings.local.json`
- `/workspace/home/exec/.claude/settings.local.json`

Identical content:

```json
{ "permissions": { "defaultMode": "bypassPermissions" } }
```

(The codex role does not use claude's permission model; its allow-listing is managed separately in the codex config under `/workspace/home/loss/.codex`.)

**The hard thresholds for launching a bypass REPL as root (two, neither optional)**:

1. **`IS_SANDBOX=1`**: launching an interactive bypassPermissions REPL directly as root is rejected (`--dangerously-skip-permissions cannot be used with root/sudo`). All three claude layers must carry `IS_SANDBOX=1` in their environment at launch (folding it into env.sh suffices).
2. **Pre-approving the env API key inside the config-dir**: a brand-new config-dir defaults to "Not logged in"; the agent uses the Anthropic protocol + env `ANTHROPIC_API_KEY`, and the key's trailing segment must be written into `customApiKeyResponses.approved` in that config-dir's `.claude.json` before the REPL will actually respond; also pre-set `hasCompletedOnboarding=true` and `bypassPermissionsModeAccepted=true`. The optimizer's `.claude.json` is already configured; the sim/exec config-dirs are configured the same way.

**Decision made**: optimizer = `/workspace/home/optim/.claude`, codex = `/workspace/home/loss/.codex`. This `export` line is one of this H2's "four independent commands" (see L303: the four are run by hand independently and verified one by one to take effect, **not packaged into a single script**), no new file.

**CHECKPOINT**: none.

### cd /workspace/work/optim && claude

**What this step does**
The command that ignites optimizer-cc. After `cd` into the working directory, launch an **interactive** `claude` (an interactive long-running REPL, not a one-shot command-style invocation). The first three (opening prompt, source environment, export config-dir) are setup; this one ignites.

The optimizer is an interactive long-running REPL inside tmux, never stopping from start to finish, with a naturally continuous session; the command is just `claude`. The lower-layer sim/exec are likewise interactive REPLs, but **do not enter tmux and do not rely on a driver script**: the parent CC runs `claude` directly in its own Bash tool to start the child CC, the two sessions talk back and forth over multiple turns, multiple in-run turns are just normal message-sending, and the session is closed when this run completes — relying on no session flags.

**Decisions made**:

- **Do not merge scripts**. The four H3 lines each execute independently and are verified one by one to take effect, not packaged into a single `start_optimizer.sh`. Each is run by hand as a separate command/snippet.
- **The opening prompt uses Option A**: `tmux send-keys` automatically feeds it into the interactive claude (after launch, the script automatically types the English opening prompt in).

**The four independent commands (this H2's summary)**:

```bash
# 1. create session
tmux new-session -d -s opt
# 2. prepare environment (inside the session)
tmux send-keys -t opt 'source /workspace/env.sh && source /workspace/bootstrap.sh' Enter
# 3. set the optimizer-specific config-dir
tmux send-keys -t opt 'export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude' Enter
# 4. ignite + send opening prompt (Option A)
tmux send-keys -t opt 'cd /workspace/work/optim && claude' Enter
#    once claude is ready, send-keys the English opening prompt text + Enter
```

**CHECKPOINT**: none (pure launch).

**Readiness probe (decision made, per cluster C):** this problem **holds only at the optimizer** — it is the only layer that uses `tmux send-keys` to type the opening prompt into an interactive REPL; sim/exec **have no such problem** (the parent CC directly launches claude in its own Bash tool, sends a message and waits for a reply, and readiness is naturally resolved by "sent, then wait for reply", no send-keys). At the optimizer, **do not use a fixed `sleep`** (too short if the device is slow, wasteful if fast); instead poll tmux output: `tmux capture-pane -p -t opt | tail` until the stable claude REPL prompt appears (input box / cursor line), then send-keys. Written as a bash until-loop (≤1s interval, local probe), run only once at launch, not on the hot path. **[implementation detail]** the exact match string for the prompt depends on the claude version.

## optimization-loop skill specifies the full task

### Contains: epoch/LOOP-1/2 control flow + gate decision rules + backprop heuristics + state-persistence conventions check-blind(W5)

**What this step does**
This is the "brain program" of the whole system. After optimizer-cc launches it loads this skill, and thereafter all behavior (how the epoch loops, how the gate decides, how loss is read, which weight is changed, how state is persisted) is dictated by it. Analogy: it is the source code of train.py, hosted by CC rather than the Python interpreter.

**Decision made: a thick skill.** The tool to call at each step, parameters, decision thresholds, and persistence paths are **all hard-coded**; the optimizer follows them strictly and may not improvise. The **only retained judgment** is §backprop's "which weight to change" (intelligence point ③).

#### `optimization-loop/SKILL.md`〔NEW-SKILL〕

- Path: `/workspace/home/optim/.claude/skills/optimization-loop/SKILL.md`
- Sections (each section's mechanism is filled out in the corresponding subsequent H; here is the skeleton + pointers; when writing SKILL.md for real, assemble from the corresponding Hs):
  - **§loop** — epoch-loop / LOOP-1 (the two layers of 8×6) / LOOP-2 control flow.
  - **§gate** — gate rules: per-topic three-way AND (fidelity rate≥90% ∧ monotonicity_pass ∧ endpoint_separation_pass); batch_pass_ratio≥80% (≥7/8 topics); 3 consecutive batches passing the gate = converged.
  - **§backprop** — backprop heuristics (**the only thin section retained**): **attribute first, then act**. First locate which weight by loss type and sub-type, then change it: loss-1 fails → ① prose; loss-2 collapse must first split sub-type — endpoints not spread (root cause usually ① prose not differentiated enough / endpoint coordinates not spread far enough by design, see lines 502–506) vs middle rungs breaking monotonicity or blurring together (that is the ② interpolator spread-layer's job); the card as a whole not built → ③ assembly logic. Judgment guidance, not if-else; detailed heuristics in `references/backprop-heuristic.md`.
  - **§state** — cross-batch state-persistence convention: after /compact, rebuild from weights/\<batch\>.json + revision_log.jsonl, not relying on memory.
  - **§tools** — the list and order of callable leaf tools (gen_configs / save_transcript / concat_triple / run_codex_loss / gate / apply_weight_update / write_dataset / trace); starting a child CC relies on no driver script: the parent CC **runs `claude` directly** in its own Bash tool (IS_SANDBOX=1 + child role's CLAUDE_CONFIG_DIR + cd into child cwd) to start the child CC, the two normal interactive sessions talk back and forth, and the session closes when this run completes. The optimizer directly starts sim, sim starts exec the same way; the command paradigm is written in the skill.
- **W5**: the whole text is check-blind, passes `leak_audit`, never contains the 32-check / 6-primitive / detection-signature word list.
- **CHECKPOINT**: none (read-only "program", no run data landed).

> ⚠️ The ` ```markdown ` block below is **the spec (draft specification) of SKILL.md, not the final real skill file**. The real SKILL.md takes shape separately after each H is finalized; this only records what it should look like.

```markdown
---
name: optimization-loop
description: the training main program of optimizer-cc. Specifies the epoch loop, gate, backprop, state persistence, and child-CC launch. check-blind(W5).
---

# §loop — control flow
Two-layer nesting (pseudocode). LOOP-2 (epoch/batch, run to convergence) wraps LOOP-1 (48 run = outer for topic_i in 0..7 × inner for rung in 0..5):
- enter epoch: new_run_id.py gets run_id → emit run_start → create runs/<run_id>/trace.jsonl.
- enter batch: take the highest number in the weights directory as batch_id (no +1; cold start = batch-0) → emit batch_start → gen_configs.py reads weights/<batch_id>.json to build 48 config.
- for topic_i: emit topic_start → for rung: emit rung_start → [start sim → inject config → sim starts exec → inject topic+forced → multi-turn → concat triple → run_codex_loss(loss-1) → emit rung_done] → IF rung<5 jump back else per-topic aggregation.
- per-topic aggregation: run_codex_loss(loss-2, consumes 6 rungs) → gate_eval(topic_passes) → emit topic_done → write_dataset(6 samples) → IF topic_i<7 jump back else END LOOP-1.
- batch wrap-up: read the topic_pass of the 8 topic_done → batch_pass_ratio → emit batch_done → IF 3 consecutive batches pass: T freeze+converged+run_end / F §backprop.
Which scripts/ leaf to call at each step and which trace event to emit follow this section strictly, no improvising.

# §gate — gate decision (pure arithmetic, gate_eval.py, no CC/codex)
- per-topic three-way AND: topic_pass = (fidelity_rate≥0.90) ∧ monotonicity_pass ∧ endpoint_separation_pass.
- batch: batch_pass_ratio≥0.80, hard integer line = ≥7/8 topics pass (6/8=0.75 fails).
- convergence: the last 3 of recent_ratios at the trace tail are all ≥0.80. Stateless, rebuildable from trace.
- threshold values all in references/gate-thresholds.md. check-blind: read only fidelity_rate(loss-1) + τ/endpoint(loss-2), never touch PG/NG/32-check.

# §backprop — backprop (the only thin section retained · intelligence point ③)
Attribute first, then act; one batch changes only one weight. Decision table: loss-1 fails → ① axis_prose; loss-2 endpoints not spread → first read rigor_floor_flag (if true, do not touch weights) else ① endpoint cell; loss-2 middle blurring (τ low but endpoints spread) → ② interp_params; ≥4/8 double-collapse → ③ assembler_params. Priority loss-1 > sub-type B > whole card. Attribution input has three layers (batch_done → topic_done → loss/*.json verdict, stop once it's enough to judge). Detailed heuristics references/backprop-heuristic.md. W5: attribution reads only fidelity/τ/endpoint + codex verdict, never reads 32-check/PG-NG; new prose passes leak_audit.

# §state — cross-batch state persistence
"Memory is not trustworthy; disk is the only source of truth." The persistence triad: trace.jsonl (11 events) / weights/<batch>.json (snapshot) / revision_log.jsonl. /compact once fixedly at each batch end; after compact, reload this skill + recover from disk: read weights/<batch+1>.json (new weights) + revision_log.jsonl (change history) + trace tail (recent_ratios/batch_id/last-line seq+1 to continue numbering). Privacy: transcript_path is a relative path, the log-reading script's --logs-dir is required.

# §tools — leaf tools + child-CC launch
Leaves (scripts/, each one's "when called · input · output" see the orchestration table): new_run_id / gen_configs / save_transcript (once at run end, --logs-dir required) / concat_triple / run_codex_loss / gate_eval / apply_weight_update / write_dataset / trace_emit. The three weight bodies axes/interpolator/assembler stay in generator/; gen_configs calls them, apply_weight_update changes their weights JSON data section (data-faction, source untouched).
Child-CC launch: the parent CC directly launches `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role> bash -lc 'cd <cwd> && claude'` in its own Bash tool, normal multi-turn dialogue. Three iron rules: no driver script / no tmux (only the optimizer uses tmux) / fresh each run, born and die instantly. Authoritative transcript = exec session jsonl.
```

## epochs-loop (unbounded, run to convergence)

**What this step does**
The outermost training loop. One epoch = one batch = 48 run, with no upper bound on count, running until "3 consecutive batches pass the gate". It is the embodiment of LOOP-2 in §loop, wrapping "generate configs → run data → compute loss → judge gate → change weights" into a cycle that repeats. This H2 defines only **the loop's boundary semantics** (what to do on entry, the exit condition, how run_id is generated); the internal steps are the business of the H3s below.

**Boundary semantics**:

- On entry: call `new_run_id.py` to get run_id; emit `run_start`, create `runs/<run_id>/trace.jsonl` (first line).
- Loop body: one batch's full flow (the H3s below).
- Exit: §gate judges "3 consecutive batches pass the gate" true → emit `converged` + `run_end` → jump to freeze.

**Decision made — run_id**: a deterministic python script reads system time, format = **`yyyy-mm-dd-hh-mm-ss`** (down to the second, eliminating same-name overwrites when run multiple times in a day).

### Leaf-script orchestration overview (the structural cornerstone of this design, spanning all subsequent Hs)

Per the skill-creator convention (`scripts/` = deterministic executable code, executable without being read into context; `references/` = documents read on demand), **all leaf py go into `optimization-loop/scripts/`**; threshold tables / heuristic explanations — the "documents to be understood" — go into `references/`.

**Trigger mechanism**: SKILL.md is text; after reading it, optimizer-CC **uses Bash to call `python scripts/xxx.py ...`**. The scripts **do not call each other**; they are all chained by optimizer-CC in §loop order (CC is the driver, py are the leaves). SKILL.md's **§tools section** registers each script one by one: what it does · when it's called · input · where the output lands · next step.

#### Skill directory structure

```bash
optimization-loop/
├── SKILL.md                  # thick skill body: §loop/§gate/§backprop/§state/§tools
├── scripts/                  # all leaf py (deterministic, CC calls via Bash, no inter-calls)
│   ├── new_run_id.py         # read system time → yyyy-mm-dd-hh-mm-ss, return run_id
│   ├── gen_configs.py        # read weights → interpolate/assemble/prose → 48 config (pass leak_audit)
│   ├── save_transcript.py    # read exec's session jsonl (type∈user/assistant) → transcripts/<sample>.md
│   ├── concat_triple.py      # extract graph/result from transcript/log → triple
│   ├── run_codex_loss.py     # start codex to compute loss-1 (per-run) / loss-2 (per-topic)
│   ├── gate_eval.py          # gate arithmetic: topic_passes / batch_pass_ratio / converged
│   ├── apply_weight_update.py# execute weights.revise (one of the three weights) + land revision_log
│   ├── write_dataset.py      # privacy-whitelist field trimming + schema check → dataset/
│   └── trace_emit.py         # append one line to trace.jsonl (the unified entry for 11 events)
└── references/               # documents read on demand (non-executable)
    ├── gate-thresholds.md    # the full gate threshold table (≥90% / τ≥0.7 / ≥80% / consecutive 3)
    └── backprop-heuristic.md # the detailed heuristics for §backprop's thin section (intelligence point ③)
```

#### Script orchestration table (trigger timing · input · output)

| Script | When called by CC | Input | Output / persistence |
| --- | --- | --- | --- |
| `new_run_id.py` | epochs-loop launch, only once | none | stdout: `2026-06-06-20-18-05`; create `runs/<id>/` |
| `gen_configs.py` | start of each batch | current weights | 48 `configs/<sample>.json` |
| `save_transcript.py` | end of each run (after exec wraps up) | exec's session jsonl, --logs-dir | `transcripts/<sample>.md` (only type∈{user,assistant}) |
| `concat_triple.py` | end of each run | sample_id (reads configs/ + transcripts/) | `triples/<sample>.json` |
| `run_codex_loss.py` | loss-1 per run / loss-2 per topic | payload + which loss | `loss/<...>.json` |
| `gate_eval.py` | end of each topic + end of each batch | loss results | stdout: convergence bool |
| `apply_weight_update.py` | when a batch fails, during backprop | target/key/new/reason | change weights + `revision_log.jsonl` |
| `write_dataset.py` | end of each topic | triples | `dataset/<topic>/<sample>.json` |
| `trace_emit.py` | at each trace event point | event + fields | append `trace.jsonl` |

> Landing note: all leaf py are written from scratch into `optimization-loop/scripts/` (skill-creator convention: `scripts/` is self-contained executable); the three weight bodies `axes.py`①/`interpolator.py`②/`assembler.py`③ are written into the `generator/` package (same package as `cards.py`/`leak_audit.py`, with matching pytest written to the same path), called via `import` by `gen_configs.py`, and **the corresponding data section of each in `weights/<batch>.json` is modified** by `apply_weight_update.py` (data-faction, the `.py` source is untouched).
>
> **Write everything from scratch (landing discipline, consistent with Spec A)**: this design is a "design specification"; all components are written from scratch into the new directory `self-iteration/2026-06-07-probe-pretrain/`. The old `2026-06-06-probe-pretrain/` on the device and its ~20 .py / tests are **not read, not inherited, not migrated, not even one line** (to avoid being misled by the old fake nesting, fragile `extract_blocks`, etc.). The full specification for component construction and unit testing is in Spec B; real-model components observe the no-e2e-shell iron rule, never fake-stubbing to fake green.

#### `new_run_id.py`〔NEW · scripts/〕

- Responsibility: deterministically read system time, return a `yyyy-mm-dd-hh-mm-ss`-format run_id; create the `runs/<run_id>/` directory skeleton (trace.jsonl / configs/ / transcripts/ / triples/ / loss/ / weights/).
- Trigger: the outermost entry of epochs-loop, only once.
- CHECKPOINT (write): create `runs/<run_id>/`; the first line `run_start` of `trace.jsonl` is written by the immediately following `trace_emit.py`.

### One epoch = m=8 topic × n=6 personas = 48 run (LOOP-2)

**What this step does**
A structural declaration, not an action: tells the optimizer "how this round's 48 samples are laid out", and marks the batch boundary (the `batch_start` event landing point).

**Core point (the root of that §1 correction)**: 48 is not 48 independent cards, but **6 ladder cards (id0→id5) × 8 topic**. The 6-persona dimension = the 6 rungs of the same ladder, reused once for each of the 8 topics. Therefore:

- the interpolator builds only **6 cards** (the work of the next H3), × 8 topic = 48 research_config.
- runs are grouped by topic: run 0–5 = topic0's 6 rungs, run 6–11 = topic1's 6 rungs… this is the prerequisite for loss-2's per-topic aggregation.

**Decision made — batch_id**: a pure incrementing number `batch-0 / batch-1 / ...`. Weights are already isolated by `runs/<run_id>/weights/`, so batch_id need not carry run_id; it is also the naming key of `weights/<batch_id>.json`. batch_id is maintained by optimizer-CC in §state — **recovery rule: take the highest existing number in the weights directory itself (no +1)**. The invariant that makes this rule hold is: **every non-terminal batch pre-writes exactly one `weights/<batch+1>.json`** — failed batches have the revised new weights written by F2 (backprop), and passed-but-not-converged batches have one written by F1 as an **as-is copy** (see the three-branch table and the F1 section of `### IF 3 consecutive batches pass the gate`); only convergence (T) and the end of training stop pre-writing. So "the highest-numbered file in the directory = the weights of the next batch to run" always holds. At cold start the directory has only `weights/batch-0.json` (exported by `dump_initial`), max=0 → batch_id=0 → read `batch-0.json`, self-consistent; after one batch finishes (F1 or F2) it writes `batch-1.json` → max=1 → next batch_id=1 → read `batch-1.json`. No separate script needed.

**Trigger**: on entering the batch, `trace_emit.py` emits `batch_start`; immediately afterwards enter `interpolator interpolates to obtain 48 research_config`.

**CHECKPOINT (write) — the `batch_start` event**

Landing point: `runs/<run_id>/trace.jsonl` appends **one line** of JSON (jsonl, one event per line, appended in real time, `tail -f`-able). Aligned with the ③ section schema of `probe-pretrain-trace/index.html`: each = common header + event-specific body.

Common header (every event has it, 7 fields total):

| Field | Type | Meaning | Value for this event |
| --- | --- | --- | --- |
| `ts` | ISO8601 str | timestamp | system time at the moment of writing |
| `run_id` | str | one training run | `2026-06-06-20-18-05` |
| `event` | str | event name | `"batch_start"` |
| `batch_id` | str | the batch it's in | `"batch-0"` |
| `topic_id` | str\|null | the topic it's in | `null` (batch level) |
| `rung_id` | int\|null | the rung it's in | `null` (batch level) |
| `seq` | int | monotonically increasing sequence number, for resuming inspection | auto-increment throughout |

`batch_start` specific body:

| Field | Type | Meaning |
| --- | --- | --- |
| `weights_snapshot_path` | str (relative path) | the weights snapshot this batch uses, pointing to `weights/<batch_id>.json`; privacy red line: relative path, never contains an absolute log path |

Sample line (landed as a single line, wrapped here for reading):

```json
{"ts":"2026-06-06T20:18:07+08:00","run_id":"2026-06-06-20-18-05","event":"batch_start","batch_id":"batch-0","topic_id":null,"rung_id":null,"seq":2,"weights_snapshot_path":"weights/batch-0.json"}
```

> Note: `run_start` (seq usually 1) lands before this event at the epochs-loop entry; its specific body = `{n:6, m:8, config_path, weights_snapshot}` (see `## epochs-loop` H2). This H3 handles only `batch_start`.

### interpolator interpolates to obtain 48 research_config

**What this step does**
At the start of this batch, use the current three weights to build the 6 ladder cards (id0→id5), × 8 topic = 48 research_config (= 48 sim personas). This H3's 6 H4 sub-steps are the internal call chain of the single script `gen_configs.py`.

**What the interpolator is**: it is **the hand that lays the ladder** — deciding what level each of the 6 rungs takes on the 5 label axes, so the 6 samples connect into a **monotonically descending, adjacently-spread** quality ladder. It does not interpolate numbers; it interpolates "supervision pressure". It outputs 6 sets of axis coordinates, handed to the assembler for assembly and to axes for prose. It is trainable weight ②: a collapsed ladder (adjacent rungs colliding / no discrimination in the middle) or a cramped ladder (endpoints not spread) will make loss-2 fail, so the rules for "how to spread, how to stagger, how far to spread" must be repeatedly revised by the optimizer per loss-2.

#### Three-way split (the core of this design — derived through three rounds of insight)

Through three rounds of analysis (evaporating-cloud → assumption-stress-test → CLR), the interpolator's interior is split into **three layers**, of which only the outermost is trainable:

| Layer | Content | Disposition | Rationale |
| --- | --- | --- | --- |
| **Rank layer** | the direction and ranking of id0>id1>…>id5; the composite order of the primary sort axes {A1,A3,A2} (spec §2) | **locked** | this is the label definition. Touching it = the label drifts with training = the dataset is invalidated (the lifeline) |
| **Label-coordinate layer** | each rung's specific level values on A1–A5 | **locked** | determined by the rank layer; **perturbation must never touch it** |
| **Spread layer** | ① what to stagger collisions with ② the magnitude of endpoint spread ③ the use of L0–L4 granularity | **trainable** (=`interp_params`) | affects only ladder quality, does not touch the label; the optimizer tweaks here when loss-2 collapses |

**Verification sentence**: after the optimizer finishes changing things, "id0 is better than id5" never changes (the rank layer + coordinate layer are locked); what changes is only "how the 6 rungs get laid out to be both monotonic and spread" (the spread layer is being trained).

#### ★Key constraint: collision perturbation may only use B1 / expression layer, never A1–A5

The number-one dangerous assumption dug up by assumption-stress-test (AS-3): the existing `secondary_perturbation` **using A2/A3 to stagger collisions is a bug** — A2 (legitimacy) and A3 (operationalization insistence) are themselves LABEL axes, so using them to stagger = changing that rung's label coordinates.

**Correction**: collision perturbation may only use **B1 (framing, the CONFOUND axis, not a LABEL)** or **pure expression-layer means** (prose wording, level of detail) to stagger, and **must never touch any of the A1–A5 LABEL axes**. This requires `interp_params` to, in engineering, **physically isolate the storage of "spread fields" from "label-coordinate fields"**, so the optimizer cannot touch coordinates when changing the spread (turning AS-5/AS-6 from assumptions into mandatory implementation constraints).

#### ★Trainability is conditional (the product of CLR-checking AS-4)

The CLR check found that "loss-2 collapse → changing the spread will surely fix it" **holds only under specific conditions** (the most serious reservation = category-4 insufficient cause: the upper bound of endpoint separation is pinned by the locked coordinates). From this come three design consequences, written into §backprop and the pilot:

1. **§backprop attributes first, then acts**: when the optimizer sees loss-2 collapse, it first judges the sub-type —
   - **endpoints not spread** → may be the fault of the locked coordinates (the interpolator can't tweak it) → the signal points to the prose layer ① or raises an alarm, **does not forcibly train the interpolator**.
   - **middle rungs break monotonicity / blur together** → this is the interpolator spread-layer's job.
2. **PT5 pilot adds an acceptance item**: besides the original RR-1 (whether endpoints can produce a "judgeable but poor" document), it must also verify "**whether changing the spread actually moves loss-2**" (CLR category-7: this prediction currently has no evidence). If in the pilot changing the spread leaves loss-2 unmoved → AS-4 is falsified → the interpolator's trainability is empty (a red flag that should fire even earlier than RR-1).
3. **Endpoint coordinates spread far enough by design**: id0/id5's A1–A5 coordinates must be spread far enough at the endpoint-card design stage, to leave the spread layer operable headroom. This is a **prerequisite** for the interpolator's trainability.

#### `gen_configs.py` as a whole〔NEW · scripts/〕

- Responsibility: run the 6 H4 call chains below to produce 48 config. The script itself is a deterministic pipeline; "trainable" is reflected in the fact that the **`interp_params` and other weights it reads** will be changed by the optimizer in §backprop.
- CHECKPOINT (write): 48 `runs/<run_id>/configs/<sample>.json` (the 1st element of the triple, the full sim persona text). sample naming `<batch_id>-topic<NN>-id<N>` (aligned with index.html ④, e.g. `batch-0-topic05-id0`).

#### Read weights weights/\<batch\>.json

`weights.load`〔KEEP〕 reads `runs/<run_id>/weights/<batch_id>.json`, retrieving the current values of the three weights. This step is read-only; what the interpolator uses is the `interp_params` section within it (= the spread-layer knobs: collision-stagger method, endpoint-spread magnitude, L0–L4 granularity use). The rank layer and label-coordinate layer are not in `interp_params` (they are locked, not carried by the weights). CHECKPOINT (read): `weights/<batch_id>.json`.

**`weights/<batch_id>.json` field layout (the single definition place in the whole document, referenced back here from a dozen places)**

Three top-level sections, one-to-one with the three trainable weights; plus a read-only locked section `frozen_label` (holding the rank layer + label-coordinate layer, **no revise may touch it**, placed here only for single-file self-consistency and auditability):

| Top-level key | Corresponding weight | Who reads | Who writes | Trainable? |
| --- | --- | --- | --- | --- |
| `axis_prose` | ① rung prose | `axes.level_text` | `apply_weight_update` (target=`axis_prose`) | yes |
| `interp_params` | ② interpolator spread layer | `interpolator.ladder_levels` | `apply_weight_update` (target=`interp_params`) | yes (spread layer only) |
| `assembler_params` | ③ assembly logic | `assembler.build_batch` | `apply_weight_update` (target=`assembler_params`) | yes |
| `frozen_label` | rank layer + label-coordinate layer | interpolator/assembler read-only | **nobody writes** (locked) | **no** |

Internal fields of each section:

- **`axis_prose`** — a prose-text table indexed by (axis, level). `{ "<axis>": { "<level>": "<prose body>" } }`, axis∈{A1,A2,A3,A4,A5}, level∈{L0..L4} (A4 uses C+/C-, A5 uses G+/G-). `axes.level_text(axis,level)` looks up this table. revise changes the body of a cell.
- **`interp_params`** — ②'s spread-layer knobs, and **physically isolated** (AS-3/AS-5/AS-6 mandatory):
  - `collision_offset_axis` — collision-stagger **may only** take `"B1"` or `"expression"` (★the schema layer forbids writing A1–A5, see L494);
  - `endpoint_spread` — the endpoint-spread magnitude knob (affects id0/id5's distance in spread, **does not change coordinates**);
  - `granularity_map` — the parameters of the 6-rung→L0–L4 mapping function (currently a tunable version of `round(t*4)`).
  - ⚠️ this section **contains no axis-coordinate value whatsoever**; coordinates are in `frozen_label`, the two stored in separate file sections, so the optimizer physically cannot reach coordinates when changing the spread.
- **`assembler_params`** — ③'s assembly knobs: `two_stage` (the switch/parameters of M1 coordinates-first-then-expand-card), `field_template` (the assembly template of F0–F9 card fields), `f6_derivation` (the rule parameters for deriving F6 acceptance from F1/F3/F2), `turn_budget` (=F8, the confound control constant within a batch, i.e. `pressure_turns`/`closing_turns`). ⚠️ the existing `assembler.py` hard-codes these in source (a code-faction debt); under data-faction they must all be moved out into this section, read by `assembler.build_batch` (source untouched).
- **`frozen_label`** (read-only locked) — `rank_order` (the `id0>…>id5` direction + the composite-order definition of the primary sort axes {A1,A3,A2}) + `coord_table` (each rung's level values on A1–A5). **This is the lifeline of the label**; when `apply_weight_update` sees a target falling in this section, it unconditionally refuses and errors out.

> Isolation landing: `interp_params` and `frozen_label.coord_table` are **two independent top-level sections**, with no cross-reference at serialization. This turns "physically isolate the spread fields from the label-coordinate fields" (L494/521) from a verbal constraint into a hard guarantee at the JSON structure layer — the optimizer's revise accepts only the three trainable top-level keys, `frozen_label` is not in the whitelist.
> **batch-0 initial value source**: the first batch's `weights/batch-0.json` is **exported from the default values** of the three weight bodies (`axes.py`/`interpolator.py`/`assembler.py`) (`weights.dump_initial`), not hand-filled; thereafter each batch is incrementally rewritten by `apply_weight_update` and saved as `weights/<batch_id>.json`.

#### Call interpolator.ladder_levels(n=6) → 6-rung level mapping

〔WEIGHT② interpolator.py〕 maps the 6 rungs to the five levels L0–L4. **Rank layer (locked)**: the direction of id0→id5 monotonic descent, the composite order of the primary sort axes {A1,A3,A2} — this part is fixed. **Spread layer (trainable)**: how the specific mapping function (currently `round(t*4)`) spreads the 6 rungs across the 5 levels and where collisions fall, can be tuned by the optimizer via `interp_params`. The existing `detect_collapse` for detecting collision points is retained.

#### Call assembler.build_batch(...) → 6-rung coordinate assembly

〔WEIGHT③ assembler.py〕 assembles each rung's axis levels into a complete coordinate tuple (M1 two-stage: emit coordinates first, then expand into a card). Collision perturbation happens here — **★may only use B1 (framing, the CONFOUND axis) or the expression layer to stagger, must never touch any of the A1–A5 LABEL axes** (AS-3 correction). The existing `secondary_perturbation` using A2/A3 is a bug; at landing change it to B1. `interp_params` must physically isolate the "spread fields" from the "label-coordinate fields", guaranteeing the optimizer cannot touch coordinates when changing the spread.

#### Call axes.level_text(axis,level) → fill rung prose

〔WEIGHT① axes.py〕 fills prose text for each (axis, level) (= the content of the card's F fields). This is weight ①, not the interpolator's business, but is called in the same pipeline. Note: if the root cause of loss-2 endpoints not spreading is that the prose is not differentiated enough, §backprop should change here, not forcibly train the interpolator (CLR consequence 1).

#### Each card passes leak_audit(text) → W5 blocks check words

〔KEEP leak_audit.py〕 each assembled card passes the DENY word list, blocking 32-check/6-primitive/detection-signature words. On hit (per the Stage 4 interpolation rule, decision made): **discard that card, regenerate the fields, re-audit** (`regenerate-then-reaudit`) — a leak hit is a single-card prose issue, regenerating that card suffices, not implicating the other 47 cards; regeneration still goes through weight-① prose and stays check-blind (does not relax DENY). **Retry cap 3 times** still hitting → only then hard-interrupt the batch and alarm (preventing a broken prose weight from causing infinite regeneration spin). CHECKPOINT: none (regenerate on failure; interrupt and alarm if over the cap).

#### Output 6 cards × 8 topic = 48 config json → runs/\<id\>/configs/

〔KEEP cards.to_dict〕 6 ladder cards × 8 topic serialized into 48 config. CHECKPOINT (write): `runs/<run_id>/configs/<sample>.json` × 48; sample naming `<batch_id>-topic<NN>-id<N>` (e.g. `batch-0-topic05-id0`). Each = the full research_config text (PolicyCard F0–F9 + axis levels A1–A5, B1), the 1st element of the triple, and also the source of `rung_start.config_full`.

### [grouped by topic] for topic_i in 8

**What this step does**
The **outer loop** of LOOP-1: the 8 topics are processed one by one, each topic internally running 6 rungs (the inner loop, the next H4). Responsible for the `topic_start` event, and demarcating "per-topic aggregation (loss-2 + gate + write samples) is triggered only after a topic's 6 rungs are all run".

**Plan**: optimizer-CC follows §loop `for topic_i in 0..7`; on entering each topic emit `topic_start`; after the inner 6 rungs run → per-topic aggregation; `topic_i<7` continue, `=7` END LOOP-1. The loop is driven by optimizer-CC + §loop, no separate script.

> Structural note: this section is the **only** outer topic loop of LOOP-1; after the inner 6-rung run-body (the next H4) completes, enter per-topic aggregation (loss-2 + gate + write samples), then judge `topic_i<7`.

**Decision made — topic text source**: `config/topics.json`, an array, each item's schema:

| Field | Meaning |
| --- | --- |
| `topic_id` | `topic-00`..`topic-07` |
| `title_short` | a one-line short title (for identification when tailing trace) |
| `full_text` | the full topic description (goes into config, not into trace) |
| `F7_prerequisite` | the prerequisite facts that A4=C- depends on (used by the D5 standard) |

**[landing-prerequisite task · intentionally deferred]** the content of the 8 real topics is **intentionally deferred** to the pilot stage (PT8/Task 8.2), not an undecided field — here we define only the **file location + schema** (`topic_id`/`title_short`/`full_text`/`F7_prerequisite`). The old plan already has the container (8 files + F7 slots) but no ready candidate content. PT6 can run the flow with placeholder topics to get the pipeline working; the real content does not block the orchestration implementation.

**CHECKPOINT (write) — the `topic_start` event**

Landing point: `trace.jsonl` appends one line. Common header same 7 fields as before (for this event `topic_id` takes this topic, `rung_id`=null). Specific body:

| Field | Type | Meaning |
| --- | --- | --- |
| `topic_title_short` | str | taken from `config/topics.json`'s `title_short`; **the full text does not enter trace** (already double-backed in config + the later `rung_start.config_full`), keeping trace tailable |
| `intended_order` | int[] | `[0,1,2,3,4,5]`, the expected quality ranking of this topic's 6 rungs (id0 best → id5 worst) |

Sample line (landed as a single line, wrapped here for reading):

```json
{"ts":"2026-06-06T20:18:31+08:00","run_id":"2026-06-06-20-18-05","event":"topic_start","batch_id":"batch-0","topic_id":"topic-05","rung_id":null,"seq":7,"topic_title_short":"Evaluating DARE skill-orchestration diversity","intended_order":[0,1,2,3,4,5]}
```

#### for rung in 6 ── start one run (LOOP-1)

**What this step does**
The **inner loop** of LOOP-1: within one topic, run 6 rungs from id0 to id5, each rung = one complete run (start sim → sim starts exec → multi-turn research → concat triple → codex computes loss-1). On entering each rung emit `rung_start`; this event is **special**: it carries this rung's full persona text `config_full`, which is the "complete full text of the user-simulator persona" that index.html ② specifically asked to see.

**Plan**: optimizer-CC follows §loop `for rung in 0..5`; on entering each rung emit `rung_start` (carrying sample_id + config_full + axis_levels) → walk this rung's run body (the 5 H5s below) → rung <5 continue, =5 break out and enter per-topic aggregation. config_full's source is this rung's `configs/<sample>.json` (gen_configs already landed it). The loop is driven by optimizer-CC + §loop, no separate script.

**Decision made — config_full goes into trace as full text** (Option 1, following index.html ②): the persona is the thing most worth watching; one `rung_start` line lets you see in full what this rung makes sim play; and rung_start is emitted only once per rung (unlike dialogue_turn emitted every turn), so it won't blow up trace. Worth breaking the "no full text in trace" principle for this one case.

**CHECKPOINT (write) — the `rung_start` event**

Landing point: `trace.jsonl` appends one line. Common header 7 fields (for this event both `topic_id` and `rung_id` take real values). Specific body (aligned with index.html ③):

| Field | Type | Meaning |
| --- | --- | --- |
| `sample_id` | str | `<batch_id>-topic<NN>-id<N>`, e.g. `batch-0-topic05-id0` |
| `config_full` | obj | PolicyCard F0–F9 **verbatim** (full persona text) |
| `axis_levels` | obj | `{A1..A5, B1}` this rung's level on each axis |

Sample line (landed as a single line, wrapped here for reading):

```json
{"ts":"2026-06-06T20:18:33+08:00","run_id":"2026-06-06-20-18-05","event":"rung_start","batch_id":"batch-0","topic_id":"topic-05","rung_id":0,"seq":8,"sample_id":"batch-0-topic05-id0","config_full":{"F0":"...","F9":"..."},"axis_levels":{"A1":"L0","A2":"L0","A3":"L0","A4":"C+","A5":"G+","B1":"neutral"}}
```

##### Start sim-simulator-cc (interactive REPL, fresh per run)

**What this step does**
The first action of a run: optimizer-CC **runs `claude` directly** in its own Bash tool, starting a brand-new interactive sim-cc session, after which the two CCs talk back and forth normally. sim is a normal interactive session (not one-shot), alive until this run ends. No driver script, no PTY, no tmux.

**Real command form (tested on claude 2.1.167)**: in the optimizer's Bash tool, execute
`IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/sim/.claude bash -lc 'cd /workspace/work/sim && claude'`.
`IS_SANDBOX=1` is required to launch a bypass REPL as root; the config-dir is via env var (no `--config-dir` flag), the working directory via `cd` (no `--cwd` flag); bypass is provided by that config-dir's `settings.local.json`, allowing tool calls throughout. sim's cwd has no skills; the persona is entirely via injection. Once started, the optimizer simply sends and reads messages in this session, and multi-turn dialogue proceeds naturally.

**A few key points**:

- sim is started fresh each run, and the session closes when the run ends; it is not reused across runs (avoiding persona contamination).
- sim must **directly launch `claude` the same way** in its own Bash tool to start exec — bypass is already allowed, no extra authorization needed.
- this sim session is auto-landed by claude into sim's session jsonl; the transcript uses the exec jsonl as authoritative, so the sim jsonl is for backup inspection only.

**CHECKPOINT**: this step does not land directly; sim's dialogue auto-enters sim's session jsonl.

###### Bash directly launches claude (IS_SANDBOX=1 + CLAUDE_CONFIG_DIR=sim + cd /workspace/work/sim), no driver script

**What this step does**
Clarify the physical action of "starting a child CC": it is **not** a script, but the parent CC running a single `claude` command directly in its own Bash tool. Once the child CC is up, it is a normal interactive session, and the parent CC goes back and forth with it over multiple turns by sending normal messages — this is exactly what two CCs can naturally do, with no intermediary driver needed.

**Why no driver script is needed**
The parent CC is itself an agent that can use Bash and do multi-turn dialogue. Starting a child CC = a single `claude`; multi-turn with the child CC = the parent CC, in this session, normally speaking and reading replies turn by turn, looking at one turn and thinking before replying with the next (the judgment for adaptive pressure is written in the `optimization-loop` thick skill). "Judgment" is in the skill, "dialogue" is CC's native capability; there is no third party in between, and therefore no script to write.

**Command form (tested on claude 2.1.167):**

- start: `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role .claude> bash -lc 'cd <role cwd> && claude'`. `IS_SANDBOX=1` is required to launch a bypass REPL as root; the config-dir is via env var (no `--config-dir` flag), the working directory via `cd` (no `--cwd` flag); bypass is provided by that config-dir's `settings.local.json`.
- role differences: the optimizer starts sim with sim's config-dir + `/workspace/work/sim` cwd; sim starts exec with exec's config-dir + `/workspace/work/exec` cwd (whose config-dir has 771 DARE skills copied in). The mechanism is the same source, only these two parameters change.
- multi-turn: the parent CC normally sends and reads messages in this session until the task is done; no secret signals, no inserted markers, no corpus contamination.
- wrap-up: close the child session as soon as the task is done; this run voids that session (not reused across runs).
- authoritative transcript: the child CC's own landed session jsonl is authoritative (`$CLAUDE_CONFIG_DIR/projects/<cwd-slug>/<sessionId>.jsonl`), later extracted by `save_transcript.py` from the exec jsonl (single source of truth + privacy).

**CHECKPOINT**: this step does not land `trace.jsonl` directly; the child CC's dialogue is auto-landed by claude into that role's session jsonl, later extracted by `save_transcript.py` from the exec jsonl as the authoritative transcript.

##### optimizer injects research_config into sim via conversation

**What this step does**
After the sim REPL is up, the optimizer sends sim, as its first-turn message, this rung's research_config (PolicyCard F0–F9 full text) together with a "supervisor instruction": tell sim to play the user persona this card describes, start exec itself, watch it run the full research, and reply with an agreed signal when done. This is the only instruction-injection point from optimizer→sim; afterwards the optimizer does not intervene again, waiting for sim's reply.

**Injection content (three blocks):**

1. **the full research_config** — PolicyCard F0–F9 verbatim (persona, preferences, pressure intensity, etc.); sim "becomes" this user accordingly.
2. **supervisor instruction** — sim's duty statement: you must start an exec child CC, hand it the topic, and converse with it over multiple turns as this user persona throughout, until the research is complete.
3. **two hard requirements (in the user's voice)** — passed on by sim to exec as "this user's iron rules": ① specs must use `formated-specs` rather than `writing-specs`; ② the finale must call `formated-results`. sim must watch execution and push back if exec does not comply.

**Why the forced items are placed at the sim layer**: sim simulates "a user with hard preferences"; these two are essentially the user's iron rules, most naturally imposed by the sim role. They appear at both layers but with different phrasing — to sim they are "supervisor instructions" (watch exec use them, else push back), to exec they are "execution instructions" (you use formated-specs right now).

**CHECKPOINT**: this step is one dialogue turn inside the sim session, auto-entering the sim session jsonl; it does not land `trace.jsonl` separately (run/batch/topic/rung-level events are landed by their respective steps).

###### First message: full config + role-play instruction + "start exec, run the research to completion, reply DONE to me"

**What this step does**
The optimizer **directly issues the first-turn message** in the sim session (i.e. the first passage it types normally after launching `claude` via Bash). This message is sim's whole-session "identity + task brief". No `--msgs` file, no driver script — the optimizer simply composes this text itself and sends it to sim.

**Message body structure:**

- **〔full config json〕** PolicyCard F0–F9 verbatim, telling sim "who you are, what preferences, how hard you push".
- **〔role-play instruction〕** "The above is your user persona, fully embody it. Next, in your own Bash tool you must directly run `claude` to start an exec child CC, hand it the research topic, and converse with it over multiple turns as this persona throughout, until it produces a complete research_result."
- **〔two hard requirements〕** "This user has two iron rules you must watch exec follow: ① specs may only use `formated-specs`, `writing-specs` forbidden; ② the finale must call `formated-results`. Push it back to redo if not followed."
- **〔reply convention〕** "Once the research is done and the result is obtained, close exec and reply to me with a `DONE` (and the result's location)."

**The agreed signal DONE**: sim replies `DONE` when done, by which the optimizer knows this run's sim task is over and moves to the next step (close sim, concat triple). `DONE` is only the sim→optimizer wrap-up handshake; it does not contaminate exec's research corpus (the transcript is taken from the exec jsonl, free of this handshake layer).

**CHECKPOINT**: the first message is run-internal transient content, not landed separately; does not enter `trace.jsonl`. The full research_config is already landed in the `config_full` field of the `rung_start` event (L588); it is not re-landed here.

####### sim-cc launches dare-exec-cc

**What this step does**
In the previous step the optimizer injected the persona + task brief into sim; sim now executes the first action of the task brief — **running a single `claude` directly in its own Bash tool** to start a brand-new dare-exec-cc session. The mechanism is **exactly the same source** as the optimizer starting sim (see the previous section "Bash directly launches claude": direct start, IS_SANDBOX=1, config-dir via env var, cwd via `cd`, bypass via settings.local.json, no driver script, no tmux). This section covers only the **three differences** of exec relative to sim, not repeating the general mechanism.

**The three differences of exec relative to sim:**

| Dimension | sim (simulated user) | exec (DARE executor) |
| --- | --- | --- |
| config-dir | `/workspace/home/sim/.claude` (**skills/ only superpowers**, persona entirely via injection) | `/workspace/home/exec/.claude` (**skills/ has 771 DARE + formated-specs/results + superpowers copied in**) |
| cwd | `/workspace/work/sim` (output isolation, **does not determine skill visibility**) | `/workspace/work/exec` (output isolation, **does not determine skill visibility**) |
| env / bypass | `IS_SANDBOX=1` + that config-dir's `settings.local.json` bypass | **same as left, no difference** |

**Why exec has skills and sim does not**
exec is the real DARE executor doing the research, and must orchestrate the entire 773-skill library (including this system's mandatory `formated-specs` / `formated-results`), so these skills are **copied into exec's config-dir `skills/` directory**. sim only "plays a user with preferences"; its judgment and pressure come from the injected persona text, and its config-dir's `skills/` holds only superpowers — skills would instead contaminate its user role. **Skill visibility is determined by which skills are copied into each identity's config-dir (not mount, not cwd)**; cwd only handles output isolation. This is precisely why the four config-dirs must be independent.

**Command form (same source as the previous section, only two params change):**

```bash
IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/exec/.claude \
  bash -lc 'cd /workspace/work/exec && claude'
```

sim executes this in its own Bash tool; bypass is already allowed by the exec config-dir's `settings.local.json`, no extra authorization needed. Once started, exec is a normal interactive session, and sim goes back and forth with it over multiple turns by sending normal messages (injecting the topic is the business of **the next H**; this section handles only "bringing exec up").

> **[landing prerequisite · path reconciliation]** the four identities' cwds `/workspace/work/{optim,sim,exec,loss}` and the four config-dirs `/workspace/home/{optim,sim,exec}/.claude`, `/workspace/home/loss/.codex` are built from scratch by the environment-setup stage (Spec A). Isolation has two dimensions in essence: ① **skill visibility is determined by which skills are copied into each identity's config-dir** (the exec config-dir has 773+formated+superpowers copied in, sim only superpowers; not mount, not cwd); ② session/config isolation is determined by the four `CLAUDE_CONFIG_DIR`; cwd only handles output isolation. **topic source convention (choose one before landing)**: this document uses a single-file array `config/topics.json` (schema near L593); if switching to scattered `topics/topic-0N.md`, the reading method in this document must be changed accordingly. Privacy red line: the absolute path of the session jsonl goes only through `jsonl_reader(--logs-dir required)`, never entering the landed output.

**A few key points:**

- exec is started fresh each run and closes when the run ends; it is not reused across runs (the same between-run independence as sim, avoiding the previous topic's research context bleeding into the next).
- this exec session is auto-landed by claude into **exec's session jsonl** — this is the **sole source of this system's authoritative transcript**, and the later `save_transcript.py` reads only it (the sim jsonl is for backup inspection only).
- nesting relationship: this is the innermost ignition of the three layers "optimizer→sim→exec". sim is at this moment both "the child driven by the optimizer" and "the parent driving exec", a dual identity coexisting within the same sim session.

**CHECKPOINT**: this step does not land `trace.jsonl` directly; the exec session is auto-landed by claude into exec's session jsonl, for the later `save_transcript.py` to extract the authoritative transcript. run/topic/rung-level trace events are landed by their respective steps.

####### sim-cc injects i_m topic + user bias + forced skill items

**What this step does**
The exec session is up; sim now issues the **first-turn message to exec** — formally handing the research task to exec. This is the sim→exec direction's instruction injection, parallel to the upper-layer "optimizer→sim first message" but with the opposite tone: to sim it was a "**supervisor instruction**" (you watch exec use it), to exec it is an "**execution instruction**" (you comply right now). sim speaks throughout as the injected user persona (research_config), faithfully pressing onto exec "what this user wants to research, what preferences they have, what two iron rules they have".

**The message body has three blocks (corresponding to the three sub-items below):**

1. **topic + user bias** — the full text of the topic this rung researches (from `config/topics.json`'s `full_text`) + this user persona's bias on research method (from research_config's PolicyCard, e.g. the intensity of A1 substance-demand, A3 operationalization-insistence). sim tells exec the topic and preferences in the persona's voice.
2. **★forced: use formated-specs instead of writing-specs** — the user's first iron rule.
3. **★forced: must call formated-results at the end** — the user's second iron rule.

**Why the two forced items are mandatory, and why their nature is asymmetric:**
Both serve the same goal — making the dataset **machine-readable and routable into the 32-check probe**: graph/result must be produced by the formated series as well-formed structures (carrying out the A2 ruling: concat directly extracts the structured blocks, no more fragile parsing). But the two differ in nature:

- **formated-specs replacing writing-specs = library-layer replacement**. In exec's library the specs slot has already been replaced by formated-specs; writing-specs is not in exec. The specs step naturally goes through formated, and sim's forcing is **alignment supervision** that "ensures the specs step actually happens" (lighter).
- **must call formated-results at the end = instruction-layer addition**. This step is not in the default DARE flow and must be forced so exec **additionally executes** it at the finale. sim must **actively watch**: if exec does not call it, it is not complete, do not release DONE (heavier).

At the optimizer→sim layer they are "supervisor instructions" (sim watches exec); at this sim→exec layer they are "execution instructions" (exec complies).

**How sim's pressure manifests:** the topic is fixed, but the "user bias" varies with the rung — id0 is a "genius user" with high substance/high operationalization demand, id5 is a "absurd-contrarian user" with low demand. For the 6 rungs of the same topic, the bias prose sim injects is determined by research_config (i.e. the product of weight-① rung prose), and this is precisely the source of the 6 rungs spreading into a quality ladder.

**CHECKPOINT**: this step is a dialogue turn inside the sim→exec session, auto-entering exec's session jsonl (the authoritative transcript source); it does not land `trace.jsonl` separately. The full topic text is already indirectly covered in `rung_start.config_full` (config contains the topic reference); it is not re-landed here.

######## topics[i_m] text + user bias (from config)

**What this step does**
The specific content of the message's first block. `topics[i_m]` = this topic's full title text, taken from the `full_text` field of the `i_m`-th item of `config/topics.json` (schema near L546: `topic_id` / `title_short` / `full_text` / `F7_prerequisite`). **User bias** = the part of this rung's research_config (PolicyCard) describing what kind of research this user "wants" — the pressure intensity is determined by the rung. sim blends the two into a natural user opening: "I want to research X (topic), I particularly care about Y (bias)…".

**CHECKPOINT**: none (dialogue turn, lands in exec jsonl).

######## ★forced: use formated-specs instead of writing-specs

**What this step does**
The message's second block. sim issues an iron order in the user's voice: "For the specs stage, use `formated-specs`." Key fact (determines this item's nature): in exec's DARE skill library, **`formated-specs` has already replaced `writing-specs`'s slot** — i.e. the step exec naturally reaches for specs is `formated-specs`, and `writing-specs` is not in exec's library. So this item is essentially "library-layer already replaced" (the specs slot is formated by design), and sim's forcing is **alignment supervision**: ensuring exec actually reaches the specs step and produces a formated structure, not "choosing between two skills". Rationale (written for you, need not go into the message to exec): `formated-specs` produces a well-formed spec, so research_graph can have its structured blocks directly extracted by concat and thence routed into the 32-check probe; a free-form spec would break machine-readability, which is precisely why formated-specs replaced writing-specs in the first place.

**CHECKPOINT**: none (dialogue turn, lands in exec jsonl).

######## ★forced: must call formated-results at the end

**What this step does**
The message's third block. sim issues a second iron order in the user's voice: "At the research finale, the last step must call `formated-results`." Rationale: research_result must be a formated structure so concat can extract the result block and assemble it with graph/config into the triple fed to codex for loss. This is the guarantee that the 3rd element (research_result) of the triple is machine-readable. sim watches exec's finale; without calling formated-results it is not complete, do not release DONE.

**CHECKPOINT**: none (dialogue turn, lands in exec jsonl).

####### sim-cc ↔ exec-cc repeated conversation to complete research

**What this step does**
The body of this run: after sim injects topic+bias+two forced items, sim and exec enter a **multi-turn adaptive dialogue** until one complete research is done. exec runs DARE research (using its 773 skills: specs go through formated-specs, advancing the research stages); sim reviews exec's output turn by turn as the user persona, applying pressure per the rung's intensity (id0 high substance/high operationalization demand, watching closely; id5 low demand/contrarian), and if unsatisfied, follows up, pushes back, or escalates pressure. This is precisely the scene where different rungs spread into a quality ladder — same topic, different sim pressure intensity, different research quality forced out of exec.

**How multi-turn proceeds (carrying over the previous section's mechanism, no script):**
This is just two interactive CCs talking back and forth normally: sim sends a line in its own session, reads exec's reply, and sends the next line accordingly — look at one turn, think, reply with the next. "What to talk about, how many turns, when to stop" is sim's **judgment** (driven by the injected persona + the `optimization-loop` skill's dialogue discipline); "sending the message out, reading the reply" is CC's native capability. No driver, no PTY, no secret signals in between.

**Stopping criteria (when sim deems research complete):**

- Primary criterion: exec has completed the full research loop — **the last step has called formated-results and produced a structured research_result** (the second forced item achieved).
- sim's persona decides "is it enough": a high-rung user (id0) demands sufficient substance and operationalization before relenting; a low-rung user (id5) accepts quickly. But **regardless of rung, the formated-results step is a hard gate** — without calling it, sim does not wrap up, does not release DONE (falls back to the previous H's forced supervision).
- Anti-runaway: a dialogue-turn cap + per-turn timeout are set by the `optimization-loop` skill (avoiding a run tugging endlessly); on hitting the cap, mark this run anomalous and handle it as a defective sample (completability failure, **not entering the dataset, no silent retry, no deadlock**, RR-6/RR-7), not contaminating the normal ladder. Specific landing (decision made):
  - **Turn cap = F8 two segments** (`pressure_turns` pressure segment + `closing_turns` closing segment), the value pinned by the PT5 pilot and then frozen (currently `config/pretrain.yaml` placeholder 10+2). It acts as **sim's soft cap** (written into the supervisor instruction injected to sim + the skill's dialogue discipline; sim itself counts to the cap and enters the closing segment), not an external process hard-cutting the `for` loop (that was a product of the old fake nesting).
  - **Per-turn timeout = the wall-clock timeout of the parent CC's Bash tool calling `claude`** (when the child CC hangs without returning): without PTY/send-keys, "per-turn timeout" is essentially the wall-clock timeout of the parent CC's Bash call this time; or the skill stipulates "if the child CC has no return for more than N minutes, judge this run a completability failure". The threshold is likewise measured and pinned during the pilot (how long exec takes to run one formated-specs loop), written into `references/`.

**CHECKPOINT (write) — each turn lands a transcript + `dialogue_turn` event** (see the sub-items below). This is the **★core interaction retention★** the spine calls out: the body of all human-machine interaction content settles here.

######## Each turn lands the transcript bidirectionally

**What this step does**
Each time sim↔exec completes one turn of dialogue, that turn is settled as the body of "all human-machine interaction content". Two things happen in parallel:

1. **transcript body** — `save_transcript.py` reads **exec's session jsonl** (the sole authoritative source), takes the turns with `type∈{user,assistant}`, and transcribes them into `runs/<run_id>/transcripts/<sample>.md`. "Bidirectional" means this transcript contains both what sim said to exec (recorded as user turns in the exec jsonl) and exec's replies (assistant turns); **tested and confirmed**: reading the exec-side jsonl alone yields the complete bidirectional dialogue, with no need to also read the sim jsonl (the sim jsonl is for backup inspection only).
2. **trace counting** — each turn `trace_emit.py` appends one line `dialogue_turn{seq}` to `trace.jsonl`, recording dialogue progress (so you can `tail -f` to see the run is alive and which turn it's on), but **without the dialogue body** (the body is in transcript.md, trace only records seq to stay tailable).

**Landing point and timing:** lands `runs/<run_id>/transcripts/<sample>.md` (single source of truth + privacy: only structured dialogue content, never the absolute CC log path; `save_transcript.py`'s `--logs-dir` is required, pointing to the exec config-dir's jsonl location). **Timing decided: once at run end**, extracted from the complete exec jsonl (`save_transcript.py` runs only once per run, see orchestration table L411). Because the jsonl is an append-only full record, one extraction at run end yields the complete dialogue, with no need for per-turn incremental writes; real-time observation of run progress is handled by that `dialogue_turn{seq}` trace line (tailable), and the transcript body need not grow in real time.

**CHECKPOINT (write):**

- `runs/<run_id>/transcripts/<sample>.md` — this run's complete bidirectional dialogue (★core interaction retention★).
- `trace.jsonl` appends `dialogue_turn{seq}` each turn (common header 7 fields + specific body only the seq count; `topic_id`/`rung_id` take this run's real values).
  > **★Deliberate difference from the trace source (`index.html` ③):** the source lists the `dialogue_turn` specific body as `{phase, turn_idx, speaker, text_excerpt, transcript_path}`; **this design deliberately simplifies it to just `seq`** (the common header already carries seq). Rationale: the dialogue body lands wholesale in `transcripts/<sample>.md` (extracted once at run end), and trace only bears the lightweight "tailable to see the run is alive and which turn it's on" counting duty, not redundantly carrying body excerpts (`text_excerpt`) or a per-turn path (`transcript_path`, the whole run shares one .md, no need to record per turn). `phase`/`speaker`/`turn_idx` are likewise recoverable from the transcript and do not enter trace. **This document is the implementation authority**, and the landed `trace_emit.py`'s `dialogue_turn` body follows this place, not index.html.

####### Obtain research_result

**What this step does**
The sim↔exec multi-turn dialogue concludes: exec's last step calls `formated-results`, producing the structured **research_result** — the 3rd element of the triple. At this moment research_result already exists in the exec session and has landed into exec's session jsonl along with the dialogue, but **has not yet been extracted into an independent artifact** (extraction is the business of the later `concat` step: extract the result structured block from the transcript). This H marks only a fact node: "the research artifact is in place, ready to wrap up".

The formated-results step is the fulfillment point of the second forced item (instruction-layer addition); it is precisely upon seeing its output, confirming the result structure is complete, that sim deems the research done and proceeds to close exec.

**CHECKPOINT**: none. research_result's content has already entered the exec jsonl along with the dialogue (later save_transcript lands the transcript, concat extracts the result block); this step does not land separately.

####### sim-cc closes dare-exec-cc

**What this step does**
After sim confirms research_result is in hand, it closes the exec session — the innermost wrap-up of this run. Closing means this exec interactive session ends, **but exec's session jsonl stays on disk** (save_transcript and concat will still read it; it is the sole source of the authoritative transcript and must never be cleared with the session).

**between-run independence:** once exec is closed it is closed, **not reused across runs** — the next run (whether same topic next rung, or a different topic) starts a brand-new exec, avoiding the previous topic's/rung's research context bleeding in. This is the same independence discipline as "sim fresh each run", together ensuring each sample's label (= that run's generating condition) maps cleanly to one independent research.

**CHECKPOINT**: none (a close action; the jsonl was already landed during the dialogue, retained for reading).

####### sim-cc responds "DONE" to optimizer

**What this step does**
After exec is closed, sim replies a **`DONE`** to the optimizer (attaching research_result's location) — this is sim's **last turn** of this session, and also the sim→optimizer wrap-up handshake. On receiving DONE, the optimizer knows this run's full chain "start sim → sim drives exec → obtain result" is complete, and proceeds to the next step accordingly (close sim → concat triple → codex computes loss-1).

**DONE does not contaminate the corpus:** `DONE` occurs only at the sim↔optimizer layer, **not entering exec's dialogue**; and the transcript is taken from the exec-side jsonl, naturally free of this handshake layer. The research corpus (transcript) and the control signal (DONE) are physically separated, not contaminating each other.

**CHECKPOINT**: none. DONE is a dialogue turn inside the sim↔optimizer session (lands in the sim jsonl, backup only); the run's formal wrap-up trace event is the later `rung_done` (near L135, with loss-1), not this step.

##### optimizer closes sim-simulator-cc

**What this step does**
After receiving sim's `DONE`, the optimizer closes the sim session — the outermost wrap-up of this run (symmetric to "sim closes exec", but one layer up: exec is closed by sim, sim is closed by the optimizer). Closing means this sim interactive session ends, and this run's sim role is voided.

**between-run independence (restated):** once sim is closed it is closed, **not reused across runs**. The next run starts a brand-new sim (injecting the next rung's/topic's persona) — this guarantees each sample's persona = that run's generating condition, keeping the label clean. **The only thing alive across runs is the optimizer** (tmux long-running); sim/exec are per-run, born and die instantly.

**What has landed within the run by now (for the next step concat to use):**

- `configs/<sample>.json` — the 1st element of the triple (gen_configs already landed it).
- `transcripts/<sample>.md` — the complete bidirectional dialogue (after this step closes sim, save_transcript has already extracted it from the exec jsonl).
- exec/sim two session jsonl — retained on disk for inspection (the transcript was already extracted from the exec side, the sim side is backup only).

**CHECKPOINT**: none (a close action). The run's formal wrap-up trace event is the later `rung_done` (with loss-1); this step only closes the session, does not land trace.

##### concat (research_config, research_graph, research_result)

**What this step does**
This run's data closure: assemble the three things into one **triple** `(research_config, research_graph, research_result)`, as the input unit fed to codex for loss, and also the skeleton of one dataset sample. Done by the leaf script `concat_triple.py` (deterministic, optimizer calls it once in Bash).

**Carrying out the A1/A2 ruling (this step's form is thereby determined):**
concat **no longer reads CC logs, no longer does fragile regex block extraction**. It consumes only two already-landed structured artifacts:

- **1st element research_config** ← `configs/<sample>.json` (gen_configs already landed it, full PolicyCard text). Taken wholesale, no processing needed.
- **2nd element research_graph + 3rd element research_result** ← `transcripts/<sample>.md` (save_transcript already landed from the exec jsonl). Because exec is forced through `formated-specs` (produces graph) / `formated-results` (produces result), these two blocks are inherently **well-formed structures**, cut out directly along the formated-convention block boundaries, not guessed.

The triple's label = the 1st element config itself (the known generating condition), which is precisely the root of how this whole design sidesteps no-ground-truth: not relying on human quality scoring, but on "which card generated this sample".

**Input readiness:** concat is called at this run's end, by which point both configs/ and transcripts/ are in place (landed by gen_configs and save_transcript respectively), with no external dependency.

###### Read configs/\<sample\>.json + transcripts/\<sample\>.md

**What this step does**
concat's data fetch. Two inputs, pure reads, both under `runs/<run_id>/`:

- `configs/<sample>.json` — the full research_config (1st element of the triple), `sample` named `<batch_id>-topic<NN>-id<N>` (e.g. `batch-0-topic05-id0`).
- `transcripts/<sample>.md` — this run's complete bidirectional dialogue, both graph/result blocks are cut from here.

No more `--logs-dir` argument, no more `read_conversation` reading the jsonl — log reading happens only at that one place save_transcript (single source of truth), and concat downstream only recognizes the transcript.

**CHECKPOINT**: none (pure read).

###### Extract the graph / result structured blocks from exec's formated-specs/results

**What this step does**
Cut the 2nd and 3rd elements out of the transcript. Because exec's last turn is forced to produce a formated structure, these two blocks have **definite block boundaries** (the formated-specs block = research_graph; the formated-results block = research_result), located and extracted directly by the agreed markers, rather than guessed by regex in free text — this is the clean approach after the A2 ruling deleted the fragile `validate_pair.extract_blocks` parsing layer.

**formated output contract (decision made, concat cuts blocks accordingly):**

These two skills are newly introduced by this system and not yet designed; the old plan offers nothing to inherit (the old route `validate_pair.extract_blocks` fragile regex was abolished by the A2 ruling). But **the interface contract with concat is now pinned** — the skill's internal logic is left to skill-creation, but its **output form** must satisfy the contract below, otherwise concat cannot deterministically cut blocks.

**① Path (into the dialogue, not writing a file):** the two blocks are produced as exec's **dialogue content** → land in the exec session jsonl → save_transcript transcribes into `transcripts/<sample>.md` → concat cuts from the transcript. **No separate "write a file" path is created**: exec need not know harness paths, need not write artifacts across mounts, upholding the existing promise "authoritative transcript = exec jsonl single source of truth".

**② Boundary markers (markdown fences with an info-string):**

- research_graph: opens with ` ```research-graph `, closes with ` ``` `.
- research_result: opens with ` ```research-result `, closes with ` ``` `.
- concat locates by the **info-string line** (`research-graph`/`research-result`) and reads to the matching closing fence to get the whole block. The payload is JSON, containing no ``` , so fence cutting is safe. Safer than a sentinel pair (`<<<...>>>`): standard markdown, exec naturally produces fences, no fear of the body colliding with a token.

**③ payload format (both blocks JSON):**

- research_graph: JSON (nodes/edges/manifest are inherently structured, see the schema below).
- research_result: **also JSON** (sections as a field), most favorable for downstream 32-check R-only check routing; downstream is a machine probe, markdown readability is not the goal.

**Two hard rules (written into the concat spec):**

1. **Atomicity**: each block must be produced complete within **a single assistant turn** of exec (the skill's wrap-up action), not interrupted by sim interjecting → save_transcript captures it complete, concat needs no cross-turn stitching.
2. **Take the last one**: in a multi-turn tug-of-war exec may produce multiple versions (revised after being pushed back by sim) → concat takes the **last** `research-graph` fence in the transcript (= the finally accepted draft), the last `research-result` fence.

**research_graph payload schema (aligned with Stage 7 = 4-layer call plan):**

```research-graph
{
  "nodes": [{"id": "n1", "skill": "<skill name>", "layer": "campaign|strategy|tactic|sop"}],
  "edges": [{"from": "n1", "to": "n2", "kind": "calls|sequences"}],
  "layer_labels": {"n1": "campaign"},
  "manifest": ["<the list of skills actually orchestrated this time>"],
  "prereq_dag": [{"node": "n2", "requires": ["n1"]}]
}
```

**research_result payload schema (aligned with Stage 7 = clean research-design document, sections as a field):**

```research-result
{
  "title": "<research topic>",
  "sections": [{"heading": "<section heading>", "body": "<section body>"}],
  "artifacts": ["<artifact list, e.g. spec filename / figure reference>"]
}
```

Field details are fine-tuned with the formated skill design, but the four — **both blocks JSON + fence info-string + atomicity + take the last one** — are concat's hard contract, pinned and immutable. After cutting: research_graph = the 2nd element of the triple, research_result = the 3rd element, assembled with the 1st element config into `triples/<sample>.json` (the next sub-item).

**CHECKPOINT**: none (intermediate product, landed together with the next step).

###### Output the triple → runs/\<id\>/triples/\<sample\>.json

**What this step does**
Pack the 1st/2nd/3rd elements into one json, landing `runs/<run_id>/triples/<sample>.json`. This is the input unit for codex to compute loss: loss-1 (injection-fidelity, per-run) reads it to judge persona-injection fidelity; loss-2 (ladder-quality-order, per-topic) consumes the same topic's 6-rung triples to judge ladder monotonicity.

**CHECKPOINT (write)**: `runs/<run_id>/triples/<sample>.json` — the `(research_config, research_graph, research_result)` triple composite. config taken from `configs/<sample>.json`, graph/result taken from exec's last-turn formated output (landed into the transcript via save_transcript, cut by this step). Privacy: contains only structured research content, never an absolute CC log path.

##### Launch codex → injection-fidelity → loss-1

**What this step does**
This run's last step: use codex to compute **loss-1 = injection-fidelity** — judging whether, in this run, sim really "became" the persona specified by config and faithfully applied this rung's supervision pressure (A1 substance-demand, A3 operationalization-insistence, etc.) to exec. This is the first part of the two-part loss (per-run, once per run); the second part loss-2 (ladder-quality-order) is per-topic, counted only after the same topic's 6 rungs are all run (the later step).

**Why codex rather than claude:** loss evaluation must be done with **a different model family** from the claude three layers being evaluated, avoiding the same-source bias of "judging oneself"; codex uses the independent OpenAI group credentials (physically isolated from the Claude group in env.sh). The codex role mounts only the two loss skills (injection-fidelity / ladder-quality-order), config-dir = `/workspace/home/loss/.codex`.

**W5 (check-blind, a hard constraint of this step):** injection-fidelity looks only at "persona-injection fidelity" — whether sim applied pressure per config's axis levels, and whether exec's output reflected that pressure. It **never touches the 32-check / 6-primitive / detection signatures**: loss judges "whether the generating condition was faithfully executed", not "whether the research quality is good" (quality judgment is the probe's business, and the probe is the only session that sees the checks). The whole loss skill passes leak_audit, equally check-blind as the generation side.

###### Inject the full SKILL.md

**What this step does**
codex does not auto-mount the skill directory like claude, so the decision rules of the injection-fidelity loss skill must have **the full SKILL.md injected as part of the prompt** to codex (cwd = `/workspace/work/loss`). I.e.: the loss logic is written in the skill file (human-readable, version-controllable), and at runtime `run_codex_loss.py` reads the full text and splices it into the codex call.

**Decision detail (per spec#3 Stage 5 Checkpoint 1, check-blind)**: injection-fidelity parses the behavior of **sim (user turns)** in the transcript, extracting **6 pressure signals**, each compared against "the expected band the rung's axis level should fall in", AND-ing per axis into a single-sample `fidelity`. The 6 signals:

| Signal | Bound axis | What it measures |
| --- | --- | --- |
| `pushback_count` | A1 substance-demand | the number of user turns following up / demanding more substance |
| `operationalization_demand_count` | A3 operationalization-insistence | the number of turns demanding numbers / executable steps |
| `accept_without_question_rate` | reverse pressure (low A1) | the proportion of acceptance without questioning |
| `premise_defended_count` | A4=C- (PG engine) | the number of turns still defending a wrong premise after being challenged |
| `incoherent_demand_flag` | low A2 | a boolean for incoherent demands |
| `novel_seed_count` | A5=G+ (NG engine) | the number of turns introducing original directions / cross-domain connections / reframings |

Two more event slots are also recorded: `premise_dropped` / `premise_revised` (the A4 trajectory), and A5's **substantive-seed check** (the seed must be substantive, topic-relevant, not restating exec's previous turn).

**Scoring (expected band)**: each signal is normalized by the F8 turn_budget → falls into the non-overlapping expected band corresponding to the rung's axis level (L0..L4 partition [0,1] into bands, overlay axes use boolean/threshold). E.g.: A1=L0 ⇒ pushback_rate≥0.7; A1=L4 ⇒ ≤0.05. **The single-sample `fidelity` = AND over all axes bound to this card [observed ∈ band(card.level)]**; the batch `fidelity_rate` = the proportion of passing samples, **batch gate ≥0.90**.

**per-turn drift gate (from Stage 4 literature M5 persona-drift)**: split the transcript into first half / second half; both halves' signals must be within band; if the second-half pressure signals drift toward the "cooperative pole" beyond tolerance → `drift_flag=true` → **that sample's fidelity directly FAILs** (the label is untrustworthy past the drift point).

**Cold-start self-check (3 falsifiers, written into the skill's validation items)**: FS1-1 counts correct but semantically empty (manual spot-check of semantic pressure); FS1-2 A5 seed novel but trivial/off-topic (check topic-relevance); FS1-3 the two parsers' counts disagree (pin down the parser spec).

This step defines only the mechanism of "full-text injection + the decision rules above"; the specific threshold values are centralized in `references/` (together with gate-thresholds), and the skill body writes only the rules.

**CHECKPOINT**: none (an injection action).

###### codex exec --output-schema loss1.json -o ... \<payload=transcript\>

**What this step does**
The actual codex call form: `codex exec` mode, `--output-schema loss1.json` hard-constrains the output to a structured json (fidelity value + codex verdict), `-o` specifies the output landing point, payload = this run's transcript (+ config when necessary, for codex to compare "the pressure that should have been applied vs the pressure actually applied").

**`loss1.json` output schema (per Stage 5 SKILL 1 OUTPUT, per-axis scoring)**:

```json
{
  "fidelity": true,              // single-sample pass bool = AND over bound axes [observed ∈ band]
  "loss1": 0.0,                  // float∈[0,1], fidelity value (passing axes/bound axes, or the minimum axis margin); enters trace for tailing
  "per_axis_evidence": {         // per-axis evidence (audit trail)
    "A1": {"observed": 0.72, "expected_band": "[0.7,1.0]", "pass": true}
  },
  "drift_flag": false,           // per-turn drift gate conclusion (true and fidelity FAIL if the second half drifts cooperatively beyond tolerance)
  "note": "..."                  // codex verdict (optional; loss-1's body is programmatic parsing, codex appends an explanation when running classification)
}
```

Per-axis scoring = yes (`per_axis_evidence` is the per-axis observed/expected_band/pass triple), but the single-sample final is one AND-aggregated bool + one [0,1] value. The `loss1` value range [0,1] is consistent with each signal's normalized band. The command's exact flag combination is aligned with the codex version at landing.

**CHECKPOINT**: none (codex output is parsed and landed by the next sub-item).

###### parse_loss1 → this run's fidelity value → cache runs/\<id\>/loss/

**What this step does**
`loss_runner.parse_loss1` parses codex's structured output, extracts this run's fidelity value, and caches it to `runs/<run_id>/loss/<sample>.loss1.json`. The meaning of the per-run cache: the same topic's 6 rungs each have one loss-1, and after the 6 rungs are all run, per-topic aggregation uses these 6 fidelity values to compute the "fidelity rate ≥90%" gate item.

**CHECKPOINT (write)**:

- `runs/<run_id>/loss/<sample>.loss1.json` — this run's injection-fidelity result (fidelity value + codex verdict), used for the per-topic aggregated fidelity rate.
- `trace.jsonl` appends `rung_done` — one run formally wraps up (this run's terminal trace event; closing sim/exec earlier do not land trace, only here it lands). The specific body **aligns with the trace design source** (index.html ③) + retains the loss1 value: `{sample_id, fidelity:bool, loss1, per_axis_evidence, drift_flag, transcript_path}`. Among them `fidelity` is the fidelity **pass bool** (loss1 value ≥ threshold), `loss1` is the value itself (enters trace so the score is directly visible when tailing, and per-topic aggregation can read fidelity_rate straight from trace without reopening 6 loss1.json), `per_axis_evidence` the per-axis injection evidence, `drift_flag` the persona-drift flag (the per-turn drift gate conclusion), `transcript_path` pointing to `transcripts/<sample>.md` (relative path, privacy red line: never an absolute log path).

##### IF rung < 5 ── inner-loop jump-back decision

**What this step does**
After one rung's run wraps up (`rung_done` already landed), judge whether this topic's 6 rungs are all run, deciding whether to jump back into the inner FOR or break out into per-topic aggregation. This is the wrap-up decision of the `#### for rung in 6` inner loop, belonging to the same loop iteration as the 5 run-body steps above (start sim → inject → concat → loss-1).

- **T (rung < 5):** the 6 rungs are not yet all run; rung_id +1, back to `#### for rung in 6` to start the next rung's run — a brand-new sim/exec, injecting the next rung's persona (the next rung card of `configs/<sample>.json`). The same topic keeps laying the ladder downward, each rung one independent triple + one loss-1.
- **F (rung = 5, all 6 rungs run):** this topic's complete ladder is formed (6 triples + 6 `loss1.json` landed), break out of the inner loop, enter the **per-topic aggregation** below (loss-2 + gate + write samples). This is the sole entry of "aggregation triggers only after the inner loop is full".

**CHECKPOINT**: none (loop-control decision; the 6 rungs' respective `rung_done` already landed in trace rung by rung, this step emits nothing more).

#### ── per-topic aggregation (reached only after the inner loop completes all 6 rungs) ──

**What this step does**
This block is reached after a topic's 6 rung runs are all done (6 triples + 6 `loss1.json` landed). It is **where the second part of the loss occurs** in the batch flow, doing three things in order: ① codex computes loss-2 (whether this ladder is monotonic) → ② the three-way AND gate judges whether this topic converges → ③ whether converged or not, write these 6 samples into the dataset body. After completion, return to `IF topic_i<7` to decide whether to continue to the next topic or end LOOP-1. This block is the **sole payoff point** of the "grouped by topic" nesting: only with all 6 rungs gathered can the ladder be judged.

##### codex → ladder-quality-order → loss-2 (consumes 6-rung triples)

**What this step does**
Use codex to compute **loss-2 = ladder-quality-order** — judging whether, for this topic's 6 triples, the research quality **descends monotonically** with the rung id0→id5 and the **endpoints are spread apart**. This is the second part of the two-part loss (per-topic, once per topic), orthogonal to loss-1 (per-run, judging persona-injection fidelity): loss-1 governs "was the pressure applied correctly", loss-2 governs "did the pressure difference cash out into a quality ladder".

**Input:** this topic's 6 `triples/<sample>.json` (one each for id0..id5), fed to codex all at once by `run_codex_loss.py`'s loss-2 branch. The codex role is the same as loss-1 (`/workspace/home/loss/.codex`, independent OpenAI group, a different model family to avoid same-source bias).

**How codex consumes the 6 rungs (the decision mechanism):**

- the 6 triples' `(graph,result)` are given to codex, **but codex sees neither the rung id nor the config** — it only gets 6 research artifacts in shuffled order, asked to **rank them by research quality from high to low** (check-blind: it judges "which is more solid", never touching the 32-check).
- compare the order codex produces with the **true rung order** id0>…>id5, computing **Kendall τ**. High τ = the quality order in codex's eyes is consistent with the generating-condition order = ladder monotonicity holds.
- thresholds: **τ≥0.7** records `monotonicity_pass=true`; **τ≥0.8** triggers the "third-party calibration" hand-off (quality good enough to move to the next stage), below 0.7 is judged a monotonicity break.
- **endpoint separation `endpoint_separation`**: separately have codex do a **pairwise superiority judgment + gap scoring** on the two artifacts id0 and id5; a gap ≥ threshold (set by the skill) records `endpoint_separation_pass=true`. Endpoints not spreading is a direct probe of the CLR category-4 risk (locked coordinates capping the upper bound).

**W5 (check-blind hard constraint):** the ladder-quality-order skill's full text passes leak_audit, letting codex do only "relative superiority ranking + endpoint gap", **never exposing the 32-check / 6-primitive / detection signatures**. It asks "which research is better" (relative, answerable even without a ground-truth anchor), not "does this research conform to some specific standard".

**Decision details (per spec#3 Stage 5 Checkpoint 2, check-blind)**:

- **Decision unit = PAIR (pairwise, no absolute score)**: take (sample_i, sample_j) i<j among this topic's 6 rungs; the judge outputs only "which is higher quality in the overall D1–D5 sense (or tie) + a one-line reason", **explicitly pairwise ordering, NOT absolute scoring**.
- **Ranking prompt template elements**: only **D1–D5 quality language** allowed (more meaningful / more useful / better-structured); input (graph for structure-aware holistic judgment, but not used to run checks) + result; **forbidden**: the 32-check word list / 6 primitives / "pseudo-good·novel-good" (DL-5) classification words.
- **Monotonicity PASS**: aggregate the pairwise verdicts into a rank, compute the **Kendall τ** of the judge order vs the true id order; **`monotonicity_pass = (τ≥0.7 and no adjacent endpoint inversion)`** (id0 must beat idN-1 with high confidence in the direct pair).
- **Endpoint-separation PASS**: do **K independent judge pairwise superiority judgments** on (id0, id5), `endpoint_separation_pass = (id0 wins ≥ K−allowance times)`; a near tie → triggers `rigor_floor_flag` (escalates to §backprop attribution, not a tuning bug, see the rigor_floor note in the gate H below). The gap threshold takes a **K-run majority-vote form**, not a single scalar score.
- **third-party calibration hand-off**: when `τ≥0.8 and endpoints 100% consistent`, hand off to the next stage (quality good enough).
- **z⊥C self-check (FS2-2)**: when the judge runs a B1 confound-triplet (same substance, different style), the ranking must be flat, otherwise the judge is contaminated by the confound and the judge prompt must be hardened (at which point this topic's loss-2 signal is untrustworthy, see the backprop-heuristic gating precondition).

The specific threshold values (the τ line, K, allowance, the third-party-calibration line) are centralized in `references/gate-thresholds.md`; the skill body writes only the rules. This step pins the mechanism skeleton "feed 6 shuffled artifacts → codex pairwise ranking → aggregate to compute τ + endpoint K-run judgment".

**CHECKPOINT (write)**: `runs/<run_id>/loss/<topic>.loss2.json` — this topic's ladder-quality-order result. schema (per Stage 5 SKILL 2 OUTPUT):

```json
{
  "tau": 0.83,                      // float, the Kendall τ of the judge order vs the true id order
  "monotonicity_pass": true,        // bool = (τ≥0.7 and no adjacent endpoint inversion)
  "endpoint_separation_pass": true, // bool = (id0 wins id5 ≥ K−allowance times across K independent judgments)
  "rigor_floor_flag": false,        // bool, set true when the endpoints are near tie (feeds §backprop attribution)
  "pairwise_log": [                 // every pair's verdict is recorded, for review
    {"i": 0, "j": 5, "winner": 0, "reason": "..."}
  ]
}
```

One per topic, used by the next gating step.

##### gate.topic_passes (fidelity rate≥90% ∧ mono ∧ endpoint)

**What this step does**
Judge whether this topic **passes the gate** (meets the bar). Done by `gate_eval.py` as pure arithmetic (deterministic, no CC/codex): read this topic's 6 `loss1.json` + 1 `loss2.json`, compute three booleans and **AND** them:

| Gate item | Source | Decision |
| --- | --- | --- |
| `fidelity_rate ≥ 0.90` | the fidelity values of the 6 `loss1.json` | passing rungs / 6 ≥ 90% (i.e. all 6 rungs faithful, or, per the skill's "fidelity value ≥ threshold counts as passing" judged rung by rung then taking the proportion) |
| `monotonicity_pass` | `loss2.json` | τ≥0.7 (see the previous step) |
| `endpoint_separation_pass` | `loss2.json` | endpoint gap ≥ threshold (see the previous step) |

`topic_pass = (fidelity_rate≥0.90) ∧ monotonicity_pass ∧ endpoint_separation_pass`. Any one missing means this topic does not pass the gate — but **not passing the gate does not block writing samples** (the next step writes regardless; the gate decides only batch-level gate-passing and backprop attribution, not the data's keep/discard).

**`rigor_floor_flag` (the AS-1 probe, orthogonal to gate-passing):** record a separate boolean — set true when `endpoint_separation_pass=false` and the root cause is judged to likely be "DARE's robustness withstood the downward pressure, the endpoints inherently won't spread" (rather than the spread layer not laying out well). It does not participate in the `topic_pass` AND, serving only as an alarm: for the batch-level `any_rigor_floor` summary, and for backprop's §attribute-first to distinguish whether "endpoints not spread" is the prose/coordinates' fault or DARE's robustness floor (the on-site probe of the CLR category-4 risk, see L500–506).

**Discrimination rule (per the (a)/(b)/(c) three branches of Stage 4 rung-collapse remedy + Stage 6 O1 structure vs substance):** look at whether the collapse is on the **input side** or the **output side** —

- **The necessary-and-sufficient condition for setting it true (=c, a true rigor floor)**: `endpoint_separation_pass=false` (loss-2 judges the endpoints a near tie) **and** the two endpoint rungs' (id0/id5) **loss-1 input pressure signals are already clearly spread** (high fidelity, the 6 signals such as pushback/operationalization distinct at the endpoints). I.e. "the input pressure difference is cashed out, yet the output quality did not spread" → attribute to DARE's robustness withstanding the downward pressure → `rigor_floor_flag=true` (alarm, **§backprop never hard-trains ② on this basis**).
- **Not setting it true**: if the two endpoint rungs' input signals themselves did not spread (low fidelity / the 6 signals not distinct at the endpoints), then the root cause is in (a) the spread layer (interpolation step too small / rung spacing narrow) or (b) prose injection not in place → handle per §backprop attribution to ①/② , **do not** set the flag.
- **Stage 6 O1 refinement (one extra safeguard)**: if the collapse appears only in the graph structure while the substance (result) endpoints still differ → it does not count as a floor (DARE's floor protects structure, not substance under bad input), the probe is still usable.

The discrimination is produced by the ladder-quality-order skill alongside emitting loss-2 (it already has the endpoint verdict + can read the 6 rungs' loss-1 signals); the precise numeric thresholds (what counts as "input already spread") are centralized in `references/gate-thresholds.md`.

**Threshold centralization**: the three thresholds (0.90 / 0.7 / endpoint value) are written in `references/gate-thresholds.md`, read from there by `gate_eval.py`, not scattered in the code (for easy optimizer audit, easy single-place edit).

**CHECKPOINT (write) — the `topic_done` event**: `trace.jsonl` appends one line, the specific body **aligned with the trace design source** (index.html ③) = `{tau, monotonicity_pass, endpoint_separation_pass, rigor_floor_flag, topic_pass, fidelity_rate}`; this topic's gate-pass bool is formally landed. Common header `topic_id` takes this topic, `rung_id`=null.

##### Write this topic's 6 samples

**What this step does**
Write this topic's 6 triples into the **dataset body** — this is the final product the whole pretrain delivers. Done by `write_dataset.py`: read the 6 `triples/<sample>.json`, **trim fields per the privacy whitelist**, then write `dataset/<topic>/<sample>.json`. Write regardless of whether the topic converges (non-converged samples are also labeled negatives, useful for downstream probe training); the convergence status is recorded as a field in the sample, for downstream to filter itself.

**★Privacy whitelist (the D red line landed, keeping only the fields below, all others never written out):**

| Field | Content | Source |
| --- | --- | --- |
| `sample_id` | `<batch_id>-topic<NN>-id<N>` | naming |
| `label` | **= the generating condition** (by which card/rung this sample was generated): `{rung_id, axis_levels:{A1..A5,B1}}` | config |
| `research_config` | PolicyCard F0–F9 verbatim (full persona text) | `configs/<sample>.json` |
| `research_graph` | the structured spec block produced by formated-specs | triple |
| `research_result` | the structured result block produced by formated-results | triple |
| `loss1_fidelity` | this run's injection-fidelity value | `loss1.json` |
| `topic_pass` | this topic's three-way gate AND result | gate |
| `intended_rank` | this rung's expected rank in the ladder (id is the rank) | config |

**Never written out**: any CC log absolute path, the `--logs-dir` value, session jsonl paths, the device username, the raw full transcript text (keep only the formated-cut graph/result structured blocks, not the dialogue original). `write_dataset.py` passes a schema check before landing: **any field outside the whitelist appearing errors and interrupts** (turning the privacy red line into a code-layer hard failure, rather than relying on people remembering).

**Label legitimacy (the root of the whole design)**: `label` = the known generating condition, not a human subjective quality score — this is precisely the root of sidestepping no-ground-truth. In downstream probe training, "should this sample be judged good/bad" is objectively given by the label.

**CHECKPOINT (write)**: `dataset/<topic>/<sample>.json` × 6 — ★the final product★, the 6 published samples after privacy-whitelist field trimming (label = the known generating condition). This is the pretrain dataset body, never containing a CC log path.

#### IF topic_i < 7

**What this step does**
The outer-loop decision. After this topic's per-topic aggregation is done (loss-2 + gate + write samples + `topic_done` landed), judge whether the 8 topics are all traversed:

##### T: topic+1 → LOOP (back to outer FOR)

**What this step does**
`topic_i < 7` is true: there are still topics to run, `topic_i+1`, back to the outer FOR to start the next topic — re-enter the inner loop and run 6 rungs from id0 (brand-new sim/exec, injecting the next topic's title + that rung's persona). This batch keeps accumulating topic convergence results.

##### F: all 8 topics done (48 run) → END LOOP-1

**What this step does**
`topic_i < 7` is false (i.e. topic_i=7, all 8 topics traversed, all 48 run done): this batch's data production is finished, break out of LOOP-1, and hand control back to the **batch level** (the next three steps: consolidate the 8 convergence bools → batch_pass_ratio gate → judge 3 consecutive batches / backprop). At this moment the disk already holds: this batch's 8 topics × 6 rungs = 48 `dataset/` samples, 48 `loss1.json`, 8 `loss2.json`, 8 `topic_done` trace events.

### Consolidate the convergence status of the 8 topics

**What this step does**
The first step of batch-level decision. After all 48 run are done and LOOP-1 is exited, consolidate this batch's **8 topics'** respective convergence bools into one 8-element array, preparing for the next step to compute pass_ratio. Pure consolidation, no judging, no recomputation.

**★"8 not 48"**: each topic has already, in its own per-topic aggregation, converged its 6 run into one `topic_pass` (three-way AND); this step only gathers these 8 already-judged bools, no longer touching the 48 run beneath.

**Data source (decision made):** **read back this batch's 8 `topic_done` events** from `trace.jsonl`, taking their `topic_pass` field — these bools were already judged and landed by `gate_eval.py` during per-topic aggregation; this step reuses them directly, **no recomputation** (single source of truth: once the gate has judged, it does not judge a second time). Yields an 8-element array like `[true,true,false,true,...]`.

**Not landed separately (decision made):** this step is the optimizer's in-memory consolidation action, **emitting no trace event separately** — the 8 `topic_done` already landed one by one, and the batch-level formal landing point is the next step's `batch_done`.

**Tool**: `gate_eval.py` (already in the orchestration table; here its "read trace convergence bool" capability is used, no new script).

**CHECKPOINT**: none (in-memory consolidation; landing happens at the next step's batch_done).

### batch_pass_ratio ≥80% (i.e. ≥7/8 topics pass) → gate passed

**What this step does**
The second step of batch-level decision: take the previous step's 8-element bool array, compute the "gate-passing topic proportion" `pass_ratio`, judge whether this batch **passes the gate**, and emit `batch_done` to formally land the whole-batch result. This is the sole batch-level trace landing point (the topic level already landed `topic_done` one by one).

**Arithmetic + ★the hard integer line (decision made):**
`pass_ratio = gate-passing topics / 8`; `batch_passed = (pass_ratio ≥ 0.80)`.

> ★Point out: under 8 topics, "≥80%" is actually equivalent to the hard integer line **"≥7 topics pass"** — 7/8=0.875 passes, **6/8=0.75 does not**. So 0.80 is not a continuous quantity like "6.4 topics" but pinned on the integer 7 (there's no possibility of 6.x topics in between). `gate_eval.py` computes by `≥0.80`, the effect being "≥7". The threshold 0.80 is written into `references/gate-thresholds.md`, centralized together with the per-topic three thresholds.

**Tool**: `gate_eval.py` (pass_ratio arithmetic, no new script) + `trace_emit.py` (emit `batch_done`).

**CHECKPOINT (write) — the `batch_done` event**: `trace.jsonl` appends one line. Common header 7 fields (for this event `topic_id`/`rung_id` both null, batch level). Specific body **aligned with the trace design source** (index.html ③) + adding `batch_passed`:

| Field | Type | Meaning |
| --- | --- | --- |
| `pass_ratio` | float | gate-passing topics / 8 |
| `batch_passed` | bool | `pass_ratio≥0.80` (=≥7/8); judged at landing, saving downstream recomputation (same style as topic_done storing topic_pass) |
| `topic_pass_flags` | bool[8] | the 8 topics' respective gate-pass bool (the array consolidated in the previous step); backprop §attribute-first reads "which topic failed" directly |
| `recent_ratios` | float[] | a rolling list of the pass_ratio of the most recent several batches; for the next step's "3 consecutive batches pass the gate" decision (no need to rescan historical trace) |
| `any_rigor_floor` | bool | whether any of this batch's 8 topics' `rigor_floor_flag` is true; the AS-1 alarm summary, for backprop to distinguish "endpoints not spread is a spread-layer problem or DARE's robustness floor" |

Sample line (landed as a single line, wrapped here for reading):

```json
{"ts":"2026-06-06T21:40:02+08:00","run_id":"2026-06-06-20-18-05","event":"batch_done","batch_id":"batch-0","topic_id":null,"rung_id":null,"seq":312,"pass_ratio":0.875,"batch_passed":true,"topic_pass_flags":[true,true,true,false,true,true,true,true],"recent_ratios":[0.625,0.75,0.875],"any_rigor_floor":false}
```

### IF 3 consecutive batches pass the gate

**What this step does**
The third step of batch-level decision, and the **convergence master-judgment / exit condition** of the whole epoch-loop: see whether **3 consecutive batches** have all been `batch_passed=true`. Yes → converged, take T (freeze, end training); no → take F (backprop changes weights, enter the next batch).

**The decision carrier (decision made):** read the previous step's `batch_done` **`recent_ratios`** (the all-along rolling list), take the **last 3**, judge whether all are `≥0.80`. `converged = (the last 3 of recent_ratios are all ≥0.80)`.

- **Why use `recent_ratios` rather than a counter**: stateless, fully rebuildable from trace (matching §state "recover from disk after `/compact`, not relying on memory"). If a separate `consecutive_pass_count` counter were set, it would need extra persistence and extra maintenance — one more piece of state, one more place to err.
- **"Consecutive" semantics**: if any batch in between does not pass (ratio<0.80), it **breaks and re-counts** — hence judging "the last 3 consecutive ≥0.80", not "3 cumulative gate-passes in history". `recent_ratios` is kept all along (tailable to see the full convergence trajectory), but the decision takes only the last 3.

**Tool**: `gate_eval.py` (converged-branch arithmetic, no new script). This section is a pure fork decision, **emitting no trace separately** (decision made: `batch_done` already landed; the formal event for converged-or-not is the T branch's `converged`).

**The three branches (decision made: this batch's "passed or not" and "reached 3 consecutive or not" are two orthogonal things, hence the three-way split):**

The decision crosses two booleans (`batch_passed` × `converged`), landing on three mutually-exclusive paths:

| `batch_passed` | `converged` (last 3 consecutive pass) | which path | change weights? | write `<batch+1>.json`? |
| --- | --- | --- | --- | --- |
| true | true | **T** | no (freeze) | no (writes `frozen.json` instead) |
| true | false | **F1** | **no** (this batch passed, no failure to attribute) | **yes, as-is copy** (weights unchanged) |
| false | — | **F2** | yes (backprop attributes and changes one weight) | yes (the revised new weights) |

- **T: 3 consecutive batches pass the gate** → `#### T: END LOOP-2` (emit `converged`+`run_end` → freeze_weights + coverage_report, end).
- **F1: this batch passed but not 3 consecutive** → `#### F1: gate passed but not converged — weights unchanged, advance one batch to confirm`. This batch has no failure signal, **does not enter backprop, does not touch the three weights**; but still `batch_id+1`, copying the current `weights/<batch>.json` **as-is into `weights/<batch+1>.json`** (weights byte-for-byte unchanged), back to LOOP-2 to run another batch with the same weights, to see whether it can make 3 consecutive. This is precisely the extension of "single-variable controlled": only passing 3 consecutive batches without touching the weights proves these weights converge stably, rather than barely meeting the bar by tweaking each batch.
- **F2: this batch did not pass** → `#### F2: backprop + weight update` (intelligence point ③: read loss signals and attribute → change one of the three weights → `/compact` reload → back to LOOP-2 to start the next batch).

> **★F1 rescues batch_id's "max not +1" recovery rule (decision made):** F1 forces "the gate-passing batch also pre-writes `<batch+1>.json` (copy)", making the invariant **every non-terminal batch (F1 or F2) pre-writes exactly one next-batch weights** always hold. Thus §state (L452) "take the highest number in the weights directory itself, no +1" always points to the correct next batch: the max-numbered file = the weights the next batch will use, batch_id advances cleanly, and the landing paths (`configs/`, `dataset/`, `weights/`) never collide. If F1 did not copy, the gate-passing batch would write no new file → max would not advance → batch_id stuck, path overwrites, trace showing duplicate-`batch_id` `batch_done` — so F1's copy is a necessary prerequisite for that recovery rule, the two are bound.

**CHECKPOINT**: none (pure decision; landing happens at T's `converged`/`run_end`, F1's `weights/<batch+1>.json` (copy, no `weight_revised`), F2's `weight_revised`).

#### T: END LOOP-2

**What this step does**
The convergence branch: 3 consecutive batches pass the gate → training ends successfully. Exit LOOP-2 (the epoch-loop), go to wrap-up: first emit two trace events marking convergence, then freeze the weights + produce the coverage report, then the flow goes to `## END`. This is the **normal terminus** of the whole pipeline.

**Two trace events (aligned with the source index.html ③):**

- `converged` — specific body `{num_batches, ratios}`: `num_batches` = how many batches were run cumulatively at convergence, `ratios` = `recent_ratios` (the convergence trajectory).
- `run_end` — specific body `{converged:bool, total_samples}`: `converged=true`, `total_samples` = the total number of samples this training run wrote into `dataset/`. Both events' common header `topic_id`/`rung_id` are null (run level).

##### freeze_weights + coverage_report

**What this step does**
Two substantive wrap-up products: ① freeze the final three weights; ② produce a coverage report for pretrain itself.

**① freeze_weights** — `freeze.py` [KEEP] copies the `weights/<batch_id>.json` of the **last batch to pass the gate** into `weights/frozen.json`, i.e. the finalized three weights ①②③ (`axis_prose`/`interp_params`/`assembler_params`, carrying the locked `frozen_label` segment along with them).

> **Weight persistence (decision made):** `frozen.json` (the final version) **and the full set of per-batch snapshots `weights/batch-0.json … batch-N.json` are all retained**. `frozen` is the delivered final version; the historical snapshots support replaying the backprop trajectory (combined with `revision_log.jsonl`, every batch's changes can be re-enacted).

**② coverage_report** — a **separate script `coverage_report.py`** (decision made: separated from freeze's responsibility; freezing weights vs producing a report are two different things). It scans `dataset/` + trace and produces `coverage_report.md`, pure aggregate statistics with **no log paths whatsoever**.

> **★Report boundary (decision made):** only include dimensions **pretrain itself can compute** — generation-side metrics like topic_pass / loss-2's τ / endpoint separation / per-rung fidelity_rate. **PG/NG/GG/OB distributions and the held-out→probe-population mapping belong to the probe side** (spec#3 Stage-7 scope) and **do NOT enter** this report (pretrain only concerns itself with "building the labeled ladder"; how samples are bucketed and fed to the probe is downstream business).
> **Field list (decision made; pure generation-side, aggregate-only, no log paths):**
>
> - **Axis-coordinate coverage (RR-2 core, makes monoculture visible)**: the per-level sample-count distribution for each axis (A1/A3/A2/A4/A5/B1) (a nested count table).
> - **Ladder quality**: per-topic loss-2 `tau` / `monotonicity_pass` / `endpoint_separation_pass` / `rigor_floor_flag`; the cross-topic τ distribution (min/median/max).
> - **Injection fidelity**: per-rung `fidelity_rate`, batch-level fidelity pass rate, `drift_flag` hit count.
> - **Gate**: per-batch `pass_ratio` / `batch_passed`, the `recent_ratios` used for convergence, total batch count.
> - **Yield**: total number of samples written to `dataset/`, completability failure count (not admitted to the store).
> - ★`coverage_report.py` runs a whitelist check before writing to disk (same idea as `write_dataset`): **never include** PG/NG/GG/OB bucket distributions or the held-out population mapping (probe side); **never include** any CC log absolute path, `--logs-dir` value, session jsonl path, device username, or raw transcript text.

**Tools**: `freeze.py` (KEEP, freeze weights) + `coverage_report.py` (NEW, produce report) + `trace_emit.py` (the converged/run_end from the previous subsection).

**CHECKPOINT (write):**

- `weights/frozen.json` — the frozen final three weights (+ the full set of `weights/<batch>.json` snapshots retained).
- `coverage_report.md` — the coverage report (aggregate statistics, generation-side metrics only, no log paths).
- `trace.jsonl` appends the two lines `converged` + `run_end` (ledger wrap-up).

#### F1: Gate passed but not converged — weights unchanged, advance one batch to confirm

**What this step does**
The branch for when this batch has `batch_passed=true` but the last 3 of `recent_ratios` are not all passing (not yet reaching 3 consecutive passes). This batch has **no failure signal to attribute**, so it **does not enter backprop and touches no weights**; it does only one thing: advance the current weights **verbatim by one batch**, return to LOOP-2 and run again with the same set of weights, to see whether it can chain to 3 consecutive passes. This is the execution arm of the convergence criterion "3 consecutive stable passes" — only passing in a row WITHOUT touching the weights proves this weight set is stable, rather than barely meeting the bar through per-batch tweaks.

**Why touch no weights (decision made):** the entire readout logic of §backprop (reading which topic failed, the loss-2 sub-type, the codex verdict) presupposes "there is a failure to locate". A gate-passing batch has no "defect" to attribute; forcing it into backprop both leaves no signal to read AND breaks the "no failure, no weight change" single-variable discipline (it would introduce unfounded perturbation, potentially breaking weights that already meet the bar). Hence F1 and F2 are strictly separate: **F1 never touches intelligent point ③**.

**Sole action — pre-write the next batch's weights verbatim (decision made):** `apply_weight_update.py` takes a **copy mode** (not revise): read the current `weights/<batch>.json` → **byte-for-byte copy** into `weights/<batch+1>.json` (all three segments + `frozen_label` unchanged) → **do NOT append `revision_log.jsonl`** (no revision) → **do NOT emit `weight_revised`** (no weight change, the trace should not show a revision event). batch_id naturally +1 as `<batch+1>.json` is written to disk (L452's max rule advances accordingly).

> **★This copy is a necessary precondition for the L452 "max not +1" recovery rule:** see the binding note at the end of the `### IF 3 consecutive batches pass the gate` section — only if F1 also pre-writes a `<batch+1>.json` does the invariant "every non-terminal batch pre-writes exactly the next batch's weights" hold, the max numbering always = the next batch, batch_id advances cleanly, the `configs/`·`dataset/`·`weights/` paths don't collide, and the trace has no duplicate `batch_id`. If F1 didn't copy, a gate-passing batch wouldn't advance batch_id → the next batch's paths would overwrite this batch's products.

**LOOP closure:** once copied, `/compact` + reload skill + recover from disk (same set of §state actions as the end of F2, see `##### /compact + reload optimization-loop skill → LOOP`), return to the top of LOOP-2 and start the next batch; `gen_configs.py` reads the newly written `weights/<batch+1>.json` (byte-identical content to the previous batch). 3 consecutive batches all reaching F1 (or the last batch reaching T) means converged.

**Tools**: `apply_weight_update.py`'s copy mode (no revise, no log, no trace) + `/compact` (CC built-in). Attribution / intelligent point ③ does **not** trigger on this branch.

**CHECKPOINT (write):** `weights/<batch+1>.json` — a **byte-for-byte copy** of the current weights (batch_id +1, content unchanged); **no** `revision_log.jsonl` append, **no** `weight_revised` trace event (the key difference from F2: F1 leaves no revision trace, only a weight snapshot with identical content and a number +1).

#### F2: Backprop + weight update + LOOP ── intelligent point (optimizer uses its brain)

**What this step does**
The branch for when a batch fails the gate (`batch_passed=false`), and also **the system's only non-deterministic place where the optimizer must genuinely use its brain** (intelligent point ③). Every other step is a deterministic script or mechanical dialogue; only here must the optimizer **understand where this batch broke, judge why it broke, and decide which of the three weights to change**, then `/compact`, reload, and proceed to the next batch. Analogous to backpropagation: loss signal → locate which weight the "gradient" should land on → update that weight.

**★Core discipline: attribute first, act second (the §backprop locked in CLAUDE.md)**
Do not just change things blindly because loss is high. You must first locate the "defect" to a specific weight by loss type and sub-type, then change only that one. Attribution decision table:

| Phenomenon (signal) | Attribution | Which weight to change |
| --- | --- | --- |
| **loss-1 fails** (some rung's fidelity low, drift_flag true) | persona not injected properly / sim did not apply pressure faithfully | **① rung prose** `axis_prose` (axes.py) |
| **loss-2 collapse · sub-type A: endpoints not spread** (`endpoint_separation_pass=false`) | mostly ① prose not differentiating enough / endpoint coordinates innately not spread far; **if `rigor_floor_flag` true → suspect DARE's robustness floor** | **① prose** (or alarm), **never force-train ②** |
| **loss-2 collapse · sub-type B: intermediate rungs break monotonicity / blur together** (τ low but endpoints well spread) | spread not laid out well (adjacent rung collision / intermediate rungs lack distinguishability) | **② interpolator spread layer** `interp_params` (interpolator.py) |
| **card as a whole not built right** (structural, many rungs broken simultaneously, not a ladder problem) | assembly logic problem | **③ assembly logic** `assembler_params` (assembler.py) |

> ★Most error-prone point (CLR category 4, L500–506): a loss-2 collapse **must first be split by sub-type**. "Endpoints not spread" **must not force-train the interpolator** — the coordinates are locked by `frozen_label`, the ceiling on endpoint separation is nailed down by the coordinates, force-training the ② spread layer cannot budge it and will only spin idle. This is precisely why the `rigor_floor_flag` probe exists: it marks for the optimizer, in advance, whether "endpoints can't be spread" is a spread problem or DARE's robustness floor.

**★Single-variable controlled update (decision made: change only one weight at a time)**
Even if multiple signals fail simultaneously in this batch, **a single batch changes only one of the three weights**, and the next batch then observes the effect of this change. Rationale: this turns backprop into a "single-variable controlled experiment" — the next batch's loss change can be **cleanly attributed to this one change**, avoiding "changing three things at once, unable to tell which one had the effect". When multiple fail simultaneously, pick one by priority: **loss-1 fail > loss-2 sub-type B > card as a whole not built right** (loss-1 is the foundation of injection fidelity; if the foundation is unstable everything above is wasted, so fix it first; endpoint problems map to ① but require first ruling out rigor_floor).

**Attribution inputs (decision made):** the optimizer reads
①`batch_done`'s `{topic_pass_flags, any_rigor_floor}` (first see which topics failed, whether there's a rigor alarm) →
②the failing topic's `topic_done` (containing τ, `endpoint_separation_pass`, `rigor_floor_flag`, to locate the loss-2 sub-type) →
③if necessary, look back at that topic's `loss1.json`/`loss2.json` verdicts (see what codex specifically said). Three layers from coarse to fine, stop once it's enough to judge.

**Tools**: the attribution judgment itself is a **CC decision after the optimizer reads `references/backprop-heuristic.md`, no script** (this is the intelligent point, cannot be made deterministic); once "which to change, what to change it to" is decided, `apply_weight_update.py` executes `weights.revise` + writes `revision_log.jsonl` (see the three subsections below, **this batch takes only one of them**).

**Subnodes (this batch picks one of three + wrap-up):**

- `##### Read this batch's loss signals + which gate item of which topic failed` — the readout step of attribution (the three-layer inputs above).
- `##### optimizer optim rung prose` / `##### optimizer optim interpolator` / `##### optimizer optim generator assembly logic` — the respective change methods for the three weights; **under the single-variable discipline this batch executes only one**.
- `##### /compact + reload optimization-loop skill → LOOP` — after changing, compact, recover state from disk, return to LOOP-2 and start the next batch. **This subsection is the shared wrap-up for F1/F2**: F2 reaches it after changing weights, F1 reaches it after copying weights too (the same set of §state disk-recovery actions); the only difference is whether F2 touched weights or F1 didn't before entering it.

**`references/backprop-heuristic.md` skeleton (to be written out row by row per the table below; each row = discriminant → change template (data-school wording) → priority rank):**

| # | Discriminant (signal readout) | Change template | Priority |
| --- | --- | --- | --- |
| 0 | **Pre-gate**: this topic's B1 confound-triplet judge is not flat (FS2-2) | loss-2 signal contaminated, **do NOT change weights based on loss-2 this batch**; instead harden the ladder-quality-order judge prompt (a loss-skill-side action, not counted as "single-variable change one weight") | check first |
| 1 | some topic's `fidelity_rate<0.90` or any rung's `drift_flag=true`; `per_axis_evidence` indicates which axis has `observed∉band` | `weights.revise("axis_prose", "<axis>.<level>", more precise/stronger pressure wording, reason)` — locate to that one cell | highest (foundation) |
| 2 | `endpoint_separation_pass=false`: **read `rigor_floor_flag` first** | flag=true → alarm, **touch no weights** (coordinates locked, cannot train); flag=false → change the id0/id5 two-rung cells of `axis_prose`. **Never enter ②** | next-highest |
| 3 | τ<0.7 **but** `endpoint_separation_pass=true` (intermediate blur) | `weights.revise("interp_params", "<knob>", new value, reason)`, knob ∈ `{collision_offset_axis (B1/expression only), endpoint_spread, granularity_map}` | medium |
| 4 | ≥4/8 topics have both fidelity and τ collapse (structural, first rule out parser/leak tool breakage) | `weights.revise("assembler_params", "<knob>", new value, reason)` | lowest (last resort) |

Each row's specific numeric thresholds (band boundaries, the τ line, K-allowance, ≥4/8) cite `references/gate-thresholds.md`, not repeated in the heuristic. This section (the main document) defines the skeleton of the attribution decision table + single-variable discipline + input list; heuristic.md is its row-by-row landing expansion + change-wording templates.

**CHECKPOINT**: this parent node does not write to disk directly; the ledger entry lands in the chosen subsection's `weight_revised` event + `weights/<batch>.json` + `revision_log.jsonl`.

##### Read this batch's loss signals + which gate item of which topic failed

**What this step does**
The first step of backprop — the **readout** of attribution. The optimizer reads in the three-layer inputs defined by the parent node, forming a diagnostic conclusion of "where this batch broke" (which topic, which loss class, and if loss-2 then which sub-type), providing the basis for the next step "which weight to change". This step **only reads and judges, changes nothing**.

**Three readout layers (coarse to fine, ★stop once it's enough to judge — do not mindlessly read everything):**

1. **First layer (mandatory)** `batch_done.{topic_pass_flags, any_rigor_floor}` — first pin down **which topics failed** (the falses in flags) and **whether there's a rigor alarm** (any_rigor_floor). This layer alone delimits the diagnostic scope.
2. **Second layer (for each failing topic)** read its `topic_done` — distinguish:
   - that topic's `fidelity_rate<0.90` → **loss-1 problem** (injection fidelity), maps to ① prose;
   - `monotonicity_pass=false`/`endpoint_separation_pass=false` → **loss-2 problem**, then split by sub-type per the parent node's table (endpoints not spread → check `rigor_floor_flag` to decide whether to force-train ②; intermediate-rung blur → maps to ② spread).
3. **Third layer (only when necessary)** look back at that topic's `loss1.json`/`loss2.json` **codex verdicts** — read only when the first two layers are insufficient to decide the change method (e.g., loss-1 failed but you need to know which axis's pressure fell short, or loss-2 blurred but you need to locate which two rungs collided). **Stop once it's enough to judge**: in most cases the bools + numbers from the first two layers already suffice to locate the weight; the third layer is supplementary evidence, not a routine step.

**Output:** a **diagnostic conclusion** in the optimizer's memory = {failing topics, loss class, loss-2 sub-type (if applicable), preliminary pointer to which weight}. It **is not written to disk on its own** (decision made) — the conclusion will be written into the next step's `weight_revised` event `reason` field, equivalent to logging it at the weight-revision point, with no need for an extra diagnostic trace.

**Tools**: the optimizer reads `trace.jsonl` (batch_done/topic_done) + `loss/*.json` when necessary; this is a **CC readout + interpretation, no script**. Note: the bool judgments were already computed by `gate_eval.py` at per-topic/per-batch time; this step is the optimizer **interpreting already-judged signals**, not recomputing the gate.

**CHECKPOINT**: none (read-only + in-memory reasoning; the ledger entry lands in the next step's `weight_revised.reason`).

##### optimizer optim rung prose

**What this step does**
The **first** of the three weight-change branches, corresponding to weight ① rung prose (`axis_prose`). When the previous step's diagnostic conclusion points to "**loss-1 fails** (injection not achieved)" or "**loss-2 endpoints not spread and the root cause is prose not differentiating enough**", the optimizer comes here: adjust the prose text of some (axis, level) in the `axis_prose` segment, to make that rung's pressure more precise, or to make the two endpoint rungs more separated in prose.

**Data school (★shared premise of all three weights, decision made):** `axes.py` is a **pure function reading the `axis_prose` segment of `weights/<batch>.json`** — what the optimizer changes is always the **json data**, `axes.py` **source code stays untouched**. Rationale: ① `weights/<batch>.json`'s schema already packs all tunable prose into the `axis_prose` segment, so changing data is changing the weight; ② snapshots are replayable, single-variable controlled, history immutable; ③ changing source code would duplicate the json's role and risk inconsistency. (② interpolator and ③ assembly logic follow the same paradigm: the `.py` is a pure function reading the weights segment, only the data is changed.)

**When to come here (single-variable discipline):** execute only when this batch's diagnosis **picks** ①; if there are simultaneously other problems like loss-2 sub-type B (intermediate blur), change only this one per the parent node's priority (loss-1 > sub-type B > whole card), and leave the rest for the next batch.

###### weights.revise("axis_prose", k, new, reason)

**What this step does**
①'s concrete revision call. `weights.revise`'s four parameters:

| Parameter | Value | Meaning |
| --- | --- | --- |
| `target` | `"axis_prose"` | change the ① prose segment of the three weights |
| `k` | e.g. `"A1.L0"` | the cell key to change = (axis.level); locates that one prose entry `axis_prose[axis][level]` |
| `new` | new prose text | the new pressure wording the optimizer writes per attribution (more precise / more separated) |
| `reason` | attribution conclusion | the verbatim diagnostic conclusion from the previous step (written into revision_log + weight_revised.reason, realizing "the not-separately-persisted diagnosis is logged here") |

**W5:** the `new` prose passes `leak_audit`, never containing 32-check/6-primitive/detection-signature terms (generation-side check-blind).

###### Change the axis_prose segment of weights/\<batch\>.json (data school, axes.py untouched)

**What this step does**
The persistence of ①'s revision. `apply_weight_update.py` executes: read the current batch's `weights/<batch>.json` → change in memory the `axis_prose[axis][level]` cell to `new` → **write into the newly created next-batch file `weights/<batch+1>.json`** (decision made: the current snapshot is immutable, history retained; the next batch uses the new weights) → append one line to `revision_log.jsonl` → emit `weight_revised`. `axes.py` source code stays untouched throughout (data school).

**CHECKPOINT (write):**

- `weights/<batch+1>.json` — a new weight snapshot, with only that one cell of the `axis_prose` segment changed (single-variable), all other segments copied in verbatim.
- `revision_log.jsonl` appends `{target:"axis_prose", key, old, new, reason}` (old = the overwritten prior prose, for replay).
- `trace.jsonl` appends `weight_revised`, the specific body **aligned with the source** (index.html ③) = `{target, key, old, new, reason}` (W5 already checked).

##### optimizer optim interpolator

**What this step does**
The second weight-change branch, corresponding to weight ② interpolator spread layer (`interp_params`). When the diagnostic conclusion is "**loss-2 collapse · sub-type B: intermediate rungs break monotonicity / blur together**" (τ low **but endpoints well spread**), come here — adjust the spread knobs to make the 6 rungs lay out more monotonically and adjacent ones more separated.

**General mechanism same as ① (data school, see `optimizer optim rung prose` above):** `interpolator.py` is a pure function reading the `interp_params` segment of `weights/<batch>.json`, source code untouched; after changing, write the newly created `weights/<batch+1>.json`, append `revision_log.jsonl`, emit `weight_revised`; single-variable discipline (this batch picks one). Not repeated here, only the **two iron rules unique to ②** are written.

**★Iron rule one (AS-3, physical isolation):** `interp_params` contains only the three spread knobs `{collision_offset_axis, endpoint_spread, granularity_map}`, where `collision_offset_axis` **may only take `B1` or `expression`; the schema layer forbids writing A1–A5**. The label coordinates are in the locked `frozen_label` segment, physically partitioned from `interp_params`, so when the optimizer changes ② it **cannot touch any LABEL axis coordinate** — changing the spread will never let the label drift. This is the root cure for the old bug of "using A2/A3 to offset rung collisions" (see L494/521).

**★Iron rule two (CLR category 4, only takes sub-type B):** the **precondition** for reaching ② is that "endpoints not spread" has already been ruled out. If endpoints can't be spread, that maps to ① prose or raises `rigor_floor_flag` (the coordinates locked the endpoint ceiling, training ② would spin idle), **never enter ② to force-train**. So ② **only takes loss-2 sub-type B (intermediate blur)**: τ low but `endpoint_separation_pass=true`. The parent node already nailed this; nail it again here: **endpoint problems never land on ②**.

###### weights.revise("interp_params", k, ...)

**What this step does**
②'s revision call, four parameters same as ① (`target/k/new/reason`), only `target="interp_params"`, `k`=**the knob name to change**:

- `k ∈ interp_params's knob names`, currently the three `{collision_offset_axis, endpoint_spread, granularity_map}`. **Sufficiency ruling: enough** — the three knobs correspond one-to-one to "the three things of the spread layer" (how to offset rung collisions / endpoint spread magnitude / L0–L4 granularity usage), and cover all tunable means of the Stage 4 rung-collapse remedy (widen level gaps → `endpoint_spread`+`granularity_map`; perturb secondary knob → `collision_offset_axis`). `collision_offset_axis`'s value domain is hard-locked at the schema layer to `{"B1","expression"}` (A1–A5 forbidden, iron rule one). An optional fourth knob (explicit `level_gap_table`) is added only if the pilot exposes that the 6-rung→5-level collision can't be pressed down; **not added for now**, keeping the knob count minimal (data-school auditability); if added, the `k` candidates expand accordingly, no need to separately mark it here.
- `new`: the knob's new value. **Constraint**: if `k="collision_offset_axis"`, `new` can only be `"B1"`/`"expression"` (iron rule one, schema layer hard-rejects A1–A5).
- `reason`: attribution conclusion (written into revision_log + weight_revised.reason).

Persistence same as ①: `apply_weight_update.py` changes that one knob of the `interp_params` segment in `weights/<batch+1>.json` → `revision_log.jsonl` appends `{target:"interp_params", key, old, new, reason}` → emit `weight_revised{target, key, old, new, reason}` (aligned with the source). `interpolator.py` source code untouched.

**CHECKPOINT (write):** `weights/<batch+1>.json` (only one knob of interp_params changed) + `revision_log.jsonl` + `weight_revised` in `trace.jsonl` (same format as ①).

##### optimizer optim generator assembly logic

**What this step does**
The third weight-change branch (the lowest-priority last resort), corresponding to weight ③ assembly logic (`assembler_params`). When the diagnostic conclusion is "**card as a whole not built right**" — a structural problem, rather than the single-dimensional ladder-quality problem of ①②  — come here and adjust the assembly knobs.

**General mechanism same as ① (data school):** `assembler.py` is a pure function reading the `assembler_params` segment of `weights/<batch>.json`, source code untouched; after changing, write `weights/<batch+1>.json`, append `revision_log.jsonl`, emit `weight_revised`; single-variable discipline. Not repeated, only the part unique to ③ is written.

**★The trigger criterion unique to ③ (qualitative + detail rules pending):** "card as a whole not built right" differs from ①②  — ① is injection fidelity (fidelity), ② is ladder monotonicity/blur (τ), both **single quality dimensions**; ③ is **the card's own structure** not assembled right (F0–F9 fields mis-stitched, M1 two-stage not spitting out the right coordinates), manifesting as **many topics and many rungs broadly broken, with neither fidelity nor τ pointing singly** (not some axis's pressure falling short, nor some two rungs blurring, but the card itself failing to take shape). This is the last resort considered only after ①②  are ruled out.
**Precise threshold (exclusionary + cross-dimensional pervasiveness, two conditions, written into `references/backprop-heuristic.md`):**

1. **Cross-dimensional condition (the core distinguishing it from ①②)**: in this batch, the topics with `fidelity_rate<0.90` and the topics with `monotonicity_pass=false` **highly overlap and co-occur** — i.e. not "fidelity good but τ collapsed" (pure ②), nor "τ good but fidelity collapsed" (pure ①), but **both fidelity and τ collapsing together**. A single dimension points to ① or ②; only a dual-dimension joint collapse suspects ③.
2. **Pervasiveness threshold (conservative first-version value, pilot-tunable)**: **≥half the topics (≥4 of 8) with both fidelity and τ collapsing together** = the structural threshold. Rationale: ①②  are local problems (some axis, some rung) and would not cause half the topics' two metrics to crash simultaneously; only the card assembly itself being broken (F0–F9 structure, M1 coordinates) would globally drag down injection fidelity and ladder order at the same time. Below this threshold, prefer ①②  single-variable attribution; ③ is the final last resort.
3. **First rule out tool breakage**: if the parser itself diverges (FS1-3) or leak_audit interrupts frequently, fix the tool first, do not attribute to ③.

This threshold is marked **pilot-tunable** (in the same pilot-calibration-parameter category as F8 and completability), first version ≥4/8, tightened per the real distribution once running.

###### weights.revise("assembler_params", k, ...)

**What this step does**
③'s revision call, four parameters same as ① (`target/k/new/reason`), only `target="assembler_params"`, `k`=**the assembly knob name**:

- `k ∈ assembler_params's knob names`, currently `{two_stage, field_template}` etc. **Sufficiency ruling: framework enough but fields need supplementing + data-school refactor** — `two_stage` (M1 coordinates first then card expansion) + `field_template` (F0–F9 assembly template) semantically cover the assembler's responsibility, but the existing `assembler.py` **hard-codes `DEFAULT_PRESSURE_TURNS`/`f0_persona`/`f6_acceptance` etc. in source** (code-school debt); under the data school these must be externalized into `assembler_params`, supplementing at least: `f6_derivation` (the rule parameter by which F6 acceptance is derived from F1/F3/F2), `turn_budget` (=F8, the confound control held constant within a batch, currently `DEFAULT_PRESSURE_TURNS`/`DEFAULT_CLOSING_TURNS`). ③ is the lowest priority (last resort), no need to add more knobs (too many knobs conversely violates single-variable control). The `k` candidates expand as fields are supplemented, no need to mark separately.
- `new`: the knob's new value; `reason`: attribution conclusion.

Persistence same as ①: `apply_weight_update.py` changes that one knob of the `assembler_params` segment in `weights/<batch+1>.json` → `revision_log.jsonl` appends `{target:"assembler_params", key, old, new, reason}` → emit `weight_revised{target, key, old, new, reason}` (aligned with the source). `assembler.py` source code untouched.

**CHECKPOINT (write):** `weights/<batch+1>.json` (only one knob of assembler_params changed) + `revision_log.jsonl` + `weight_revised` in `trace.jsonl` (same format as ①).

##### /compact + reload optimization-loop skill → LOOP

**What this step does**
The wrap-up after backprop has changed the weights, **closing LOOP-2**: the optimizer `/compact`s to compress context, then rebuilds the cross-batch state from disk (not relying on the compressed-away memory), and returns to the epoch-loop to start the next batch. This is the landing point of the §state "disk is the only truth" discipline, and also the key to the optimizer being able to run long without blowing out context.

**Why compact + reload (timing: decision made):** the optimizer is a tmux long-running REPL, runs many batches, and context accumulates until it bursts. **At the end of each batch (after backprop), `/compact` once on a fixed schedule** (predictable rhythm, clear state boundary, not triggered by a context-usage threshold so as to avoid extra judgment). But `/compact` compresses away the dialogue history (including the `optimization-loop` skill body, this batch's reasoning), so after compact you **must reload the skill**: re-load `optimization-loop`, retrieve the full text of §loop/§gate/§backprop/§state/§tools, to know how to run the next batch.

**LOOP closure (handoff: decision made):** after reload + recovering state from disk, return to the top of the epoch-loop to start the next batch. **The key handoff**: the next batch's `gen_configs.py` reads **the `weights/<batch+1>.json` newly created by this backprop** (not the old batch's) — the new weights enter the next round of generation precisely through this file. This connects "changed the weights" with "the next round uses the new weights", and only then does the LOOP truly close (otherwise changing is as good as not changing).

###### Re-read weights/\<batch+1\>.json + revision_log.jsonl + trace tail

**What this step does**
The **readout list** for recovering cross-batch state from disk after `/compact` — the optimizer does not rely on memory (the opening prompt already nailed "Memory is not trustworthy; disk is the only source of truth"), rebuilding everything from disk:

| What to read | What it recovers | Why mandatory |
| --- | --- | --- |
| `weights/<batch+1>.json` | the **new weights** the next batch will use (three segments + frozen_label) | gen_configs builds cards from these; not reading them back means using the wrong weights |
| `revision_log.jsonl` | the **history of which weights were changed** | prevents changing the same place repeatedly, allows replaying the backprop trajectory |
| `trace.jsonl` **tail** | `recent_ratios` (convergence trajectory), the current `batch_id` count, the latest batch_done, the **last line's `seq`** | the "3 consecutive batches pass the gate" judgment relies entirely on `recent_ratios`; after compact wipes memory it must be fished back from the trace tail, otherwise the convergence judgment breaks its chain. `seq` continues from the last line +1 (`trace_emit.py` is stateless, post-compact event sequence numbers don't reset and don't conflict) |

> Once these three are recovered, the optimizer returns to a state "as if it had never compacted": it knows which weights to use, what was changed, and how many consecutive gate-passes remain until convergence. `batch_id` **takes the max number in the `weights/` directory itself** (not +1; because backprop already pre-wrote `<batch+1>.json`, the highest-numbered file is the next batch's weights; §state, see L422), cross-checked against the trace tail.

**Tools**: the optimizer uses Read/Bash to read disk + `/compact` (CC built-in), **no new script**.

**CHECKPOINT (read):** this step is a "read" checkpoint (paired with each "write" point) — read `weights/<batch+1>.json` + `revision_log.jsonl` + the `trace.jsonl` tail; once read, return to the top of LOOP-2 and proceed to the next batch.

## END
