# Index — Triple-CC Pseudo-Neural-Network Pretraining (three-way split A/B/C) Implementation Plan Index

> **For agentic workers:** This file is a **navigation index**; it contains no executable steps. Each of the three concrete plans is implemented Task-by-Task using superpowers:subagent-driven-development (recommended) or superpowers:executing-plans. **Strictly follow the A→B→C order**; only proceed to the next split once the previous one is fully green.

**Goal:** On a rented RunPod machine, build from bare metal a pseudo-neural-network pretraining system in which **four CC identities (optimizer / sim / exec / loss) collaborate**, run it to convergence, and produce a labeled research-quality-ladder dataset. The whole project is split into three independently deliverable plans.

**Architecture:** Three layers of CC (optimizer drives → sim simulates the user → exec runs DARE research) + codex computes the loss (a different model family, to avoid same-source bias). The data-faction three weights (prose ①/interpolation ②/assembly ③) are JSON data segments; the `.py` files are read-only and never modified. The optimizer is a tmux long-running train.py; one epoch = 8 topics × 6 rungs = 48 runs; the gate decides pass/fail by arithmetic, and backprop is the system's only point of intelligence. Everything is check-blind (W5) + the privacy red line (CC log paths and key values must NEVER enter any committed artifact).

**Tech Stack:** Ubuntu 22.04 · Python 3.11 + pytest · real claude/codex CLI · tmux · node (installed under /workspace) · third-party proxy `api.ikuncode.cc`.

---

## The three plans (strict order)

| Split | Plan file | Scope | Final acceptance |
| --- | --- | --- | --- |
| **A** | `2026-06-07-A-remote-env-from-scratch.md` | Remote environment from scratch: bare metal → four identities startable + survives restart | Smoke S1–S4 all pass + real vertical-slice e2e E1–E5 (1 run, all-real CC/codex) |
| **B** | `2026-06-07-B-system-build.md` | System build: three weight bodies + 9 leaf scripts + 2 codex loss skills + optimization-loop skill | Pure-function pytest all green + single-topic 6-rung e2e (loss-2 monotone τ + endpoint separation + gate arithmetic) |
| **C** | `2026-06-07-C-assemble-run-supervise.md` | Assemble & run: PT5 pilot hard gate → full LOOP-2 convergence → supervision → freeze + full dataset | C1 pilot go/no-go + C2 convergence (F2 real revise + F1 advance) + C3 freeze/coverage/dataset all present |

## Dependency chain (why this order)

```text
A(env)  ──►  B(components)  ──►  C(assemble & run)
  │              │              │
  │              │              └─ depends on B fully green: three weights + 9 leaves pytest pass, B7 single-topic 6-rung e2e really ran;
  │              │                 depends on A fully green: four identities startable, skills visible, slice E1–E5 pass
  │              └─ depends on A fully green: four identities startable (B's real-model e2e must start real sim/exec/codex)
  └─ no prerequisite (starts from bare metal)
```

- **A goes first**: all of B/C's real-model components (integration e2e) must start a real sim/exec/codex, and the way the four identities are started, skill visibility, and the isolation of the two key groups all rely on A being set up. If A is not green, B's e2e cannot start.
- **B in the middle**: the "parts" that C assembles (three weights, 9 leaves, 2 loss skills, optimization-loop skill) are all built and unit-tested by B. C builds no parts; it only assembles.
- **C closes it out**: assembles B's parts into a self-running whole machine, runs to convergence, and produces the dataset. C1 pilot is a hard gate — if it does not pass, stop and return to B.

## Golden synthetic sample (the regression baseline running through A→C)

A's slice e2e uses one synthetic config+topic, fixed and archived at `<proj>/fixtures/golden-slice/`, becoming the shared regression scenario across all three splits — deepened layer by layer, continuously comparable:

| Split | What is verified on the golden sample |
| --- | --- |
| A | 1-run vertical path: injection → nesting → real research → real loss → trace (E1–E5) |
| B | Grown into finished components: gen_configs really builds cards, 6-rung ladder, loss-2 monotone, gate arithmetic (component integration + 6-run e2e) |
| C | Grown into the full loop: 48-run batch, three-consecutive-pass convergence, backprop revises weights, real-time supervision (full e2e) |

## Iron rules throughout (shared by all three splits, applies to every Task)

1. **Everything lands in `/workspace`, never in `/` or `~`** (`/` is only a 5G overlay, wiped on restart; `/workspace` is 851 TB persistent).
2. **The two API key groups are physically isolated** (Claude group for optim/sim/exec; Codex group for loss), and **key values must NEVER enter any committed artifact** (scripts/specs/reports/commits); reference them only by variable name, filled in by the operator.
3. **Rewrite everything from scratch**: the three-layer-architecture final draft is treated only as a design spec; the old `2026-06-06-probe-pretrain/` on the machine is not read at all, not inherited (to avoid being misled by the old fake nesting / brittle parsing / A2-A3 collision bug). All new code goes into `self-iteration/2026-06-07-probe-pretrain/`, pushed to branch `self-iteration/probe-pretrain`, **never pushed to main**.
4. **Data-faction three weights**: `axes.py`①/`interpolator.py`②/`assembler.py`③ are pure functions that read the corresponding segment of `weights/<batch>.json`; **the source code never changes — revising a weight means editing the JSON**. The rank layer + label-coordinate layer are locked in `frozen_label` (no one writes it).
5. **W5 check-blind**: every generation-side artifact (config, prose, loss skill, topic) passes `leak_audit` in full, and must NEVER contain the 32-check / 6-primitive / detection signatures. Loss judges "whether the generating condition was faithfully executed / whether the ladder is monotone," not "whether the research quality is good."
6. **No-fake iron rule**: components requiring real models (sim/exec/codex) must be real processes; the only synthetic part is the "input config+topic." Any fake-stub that fakes a green is not a pass (`feedback-no-e2e-shell`).
7. **Privacy red line**: CC log absolute paths must NEVER enter any committed artifact; reading logs goes only through the `--logs-dir`-required script (`save_transcript`); `runs/` is gitignored locally on the machine; dataset/coverage pass a whitelist check before landing, and any field outside the whitelist (log path, machine username, raw transcript) → hard-fail abort.

## Three-split boundaries (who manages what, no crossing over)

- **A manages the environment**: package install, env.sh/bootstrap.sh, four config-dir pre-approvals, skill-copy mechanism, slice 1-run. **Does not manage** component code or skill content; does not manage the full loop.
- **B manages parts + single-topic 6-rung**: three weights, 9 leaves, 2 loss skills, optimization-loop skill authoring. **Does not manage** multi-batch, real backprop revise, tmux long-running, pilot, supervision, full dataset (the §backprop section is written by B but left for C to deep-verify).
- **C manages assembly & operation**: pilot hard gate, full LOOP-2, real backprop revise, long-running, supervision, freeze + full output + 8 real topics. **Builds no parts, sets up no environment.**

## Machine access + credentials (★LOCAL-ONLY · MUST be gitignored · NEVER push)

> ⚠️ **Red-line reminder**: This section contains a real SSH private-key path and API key values, which **violates iron rule 2 "key values must never enter a committed artifact."** It is recorded here only at the user's explicit request; **it must NOT be committed to git along with this file** — when implementing, the operator should excise this section and move it into the machine-local `/workspace/env.sh` (A's Task 4), or delete this section before committing / add this file to `.gitignore`. Once a key enters git history it is permanently leaked and must be rotated.

- **Machine SSH**: `ssh root@***** -p ***** -i ~/.ssh/id_ed25519` (IP/port redacted, operator fills in)
- **Claude group (for optim / sim / exec)**:
  - `ANTHROPIC_API_KEY=*****` (**use `ANTHROPIC_API_KEY`, not `ANTHROPIC_AUTH_TOKEN`** — x-api-key auth)
  - `ANTHROPIC_BASE_URL=https://api.ikuncode.cc` (no suffix; the CLI appends `/v1/messages` itself)
  - `ANTHROPIC_MODEL=claude-opus-4-7`
- **Codex group (for loss)**:
  - `OPENAI_API_KEY=*****` (also as `IKUNCODE_KEY`)
  - `OPENAI_BASE_URL=https://api.ikuncode.cc/v1` (with `/v1`)
  - `OPENAI_MODEL=gpt-5.5`, wire-api=`responses`
- **★The two key groups are physically isolated**: mixing them makes claude report `model_not_found` (`.claude.json`'s `customApiKeyResponses.approved` holds the Claude-group key tail `*****`).
- **git commit identity**: `Pthahnix <Pthahnix@proton.me>`.

## Information sources (the sole basis for this index and the three plans)

- Design specs: `docs/superpowers/specs/2026-06-07-remote-env-from-scratch-design.md` (A), `...-system-build-design.md` (B), `...-assemble-run-design.md` (C); three-layer-architecture final draft `context/2026-06-06-20-18-triple-cc-architecture.md` (system-design authority).
- Code sources: DARE repo (771-skill copy source, used by `exec`); the project skills/ `formated-specs` / `formated-result` (B only interfaces with the output contract, does not rewrite them).

## Execution Handoff

Execute split by split; each split has two options:

**1. Subagent-Driven (recommended)** — dispatch a new subagent per Task, review between Tasks, fast iteration. REQUIRED SUB-SKILL: superpowers:subagent-driven-development.

**2. Inline Execution** — batch execution within this session + checkpoint review. REQUIRED SUB-SKILL: superpowers:executing-plans.

**Starting point: Plan A.** A fully green (S1–S4 + E1–E5) → Plan B; B fully green (pytest + B7 6-rung e2e) → Plan C; C1 pilot hard gate, no-go means stop and return to B.
