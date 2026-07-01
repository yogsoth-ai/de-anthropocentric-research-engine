# ladder-foundry — Working Notes for a Fresh Session

Orientation for whoever (human or CC) picks this up next. Local-only handoff
doc; the authoritative design lineage lives in the specs/plans referenced
below. **Read this first, then the STAGE-5 section, before touching anything.**

## What this is

ladder-foundry is the built form of the triple-CC pretrain generator
(design doc: `D:\YOGSOTH-AI\context\2026-06-06-20-18-triple-cc-architecture.md`).
Three nested Claude Code sessions act as a pseudo-NN training loop:

```
optimizer-cc  (long-running orchestrator; = the driving CC session itself)
  └─ sim-cc   (fresh per run; injected a PolicyCard persona)
       └─ exec-cc (fresh per run; the 773-skill DARE body doing the research)
```

Each run yields a labeled `(research_config, research_graph, research_result)`
triple. The **label = the generating PolicyCard** (the known supervision
condition), which sidesteps the no-ground-truth problem. A batch = 6 rungs ×
8 topics = 48 runs. Converged = 3 consecutive batches with pass_ratio ≥ 0.80.

## Status: STAGE 1–4 DELIVERED (all local), STAGE 5 = wire + run

Branch: `self-iteration/ladder-foundry` (NOT main; continuous iteration — do
NOT merge/push-to-main/finish). STAGE 1–4 built every part and verified it
**locally**: 8 leaf scripts (`scripts/`), 3 trainable weights + generator
(`generator/`), 7 skill artifacts (`skills/`), loss harness
(`skills/optimization-loop/scripts/run_codex_loss.py`), optimizer brain
(`skills/optimization-loop/SKILL.md`). Full suite: 117 passed. Final
whole-branch review: READY TO MERGE. **The blocks are all there.**

STAGE 5 does not author new components — it **wires the existing ones into
the real 3-layer nesting and runs them.** That is where a real machine and
real keys come in.

## Why STAGE 5 needs a dedicated machine (read carefully — two reasons, only one is real)

### Reason 1 (real): clean isolation + cost + long-run
This dev box is Windows / Git-Bash, has **no tmux**, and `D:\YOGSOTH-AI\.mcp.json`
carries **9 inline API keys** (SS_API_KEY, BRAVE_API_KEY, APIFY_TOKEN,
RUNPOD_API_KEY, 2× AWS pairs, …) plus `.env` (NPM_TOKEN, GITHUB_TOKEN). A
48-run × N-batch nested job wants a clean Linux box with strict role
isolation. **This reason justifies renting.**

### Reason 2 (NOT solved by renting): the transport-layer deadlock
The core action — **a parent CC launching a child `claude` in its own Bash
tool and holding a multi-turn conversation with it** — has NEVER been run,
and by pure reasoning it collides with the locked constraints:

- A Bash tool call is one-shot: run → wait for exit → collect stdout.
- Interactive `claude` (no print flag) is a TUI: it does not exit, it waits
  on a TTY. A one-shot Bash call cannot feed it multiple turns.
- The known ways to drive CC programmatically across turns are: (a) the print
  flag + resume/session-id continuation, (b) the SDK, (c) a persistent
  terminal via PTY/tmux.
- **All three are banned** (print/resume/session-id/PTY/tmux-for-children/
  driver-script are hard-forbidden — see constraints). That ban set closes
  *every* known path to a multi-turn sim↔exec conversation.

**This contradiction is OS-independent.** Renting a Linux box lets the cheap
scaffolding (Reason 1) go up smoothly, but the job will still stall at "parent
CC says the second sentence to the child." So:

> **Recommended order: do NOT rent yet.** First run a ~15-minute transport
> spike on ANY machine (this one is fine) inside `sandbox/`: can a parent CC
> `claude`-launch a child and receive one reply? Three outcomes —
> (1) it works some way I didn't foresee → transport confirmed, then rent &
> scaffold with confidence; (2) it needs exactly one ban relaxed (e.g. allow
> the print flag, fresh process per turn, no continuation) → bring the
> evidence back and let the user trade "fully-interactive-REPL aesthetics" for
> "it runs"; (3) it cannot work at all → save the rent money, redesign.

The spike is the ONE genuine unknown in STAGE 5. Everything else is
determinate labor.

## Decisions locked this session (2026-07-01)

1. **Sandbox location:** build the runtime sandbox under a directory inside
   `D:\YOGSOTH-AI\` (build-on-site), NOT the design doc's POSIX `/workspace`.
   All four role config-dirs move inside it. **Hard boundary: all reads/writes
   stay within that sandbox + standard config locations — never touch anything
   else.**
2. **Drop codex; loss also runs on CC.** Chosen form: keep ALL of
   `run_codex_loss.py`'s harness logic unchanged (shuffle / Copeland / Kendall
   τ / K-vote / schema validation / all thresholds), and swap only the
   innermost `codex_fn` from calling `codex exec` to calling `claude` in a
   clean config-dir carrying just the two loss skills. The independent,
   check-blind 4th judge role is PRESERVED (no-fake-stub red line intact) —
   it just runs on `claude` instead of `codex`.
3. **Cost knob (deferred switch):** to save money, either point the loss/exec
   CCs at a third-party API base-url, or run everything on haiku. Implement as
   a fillable knob per config-dir; do not let it block sandbox bring-up.

## Isolation red line (STAGE-5 scaffolding MUST honor)

The four role config-dirs (`home/optim`, `home/sim`, `home/exec`, `home/loss`)
must be **clean** — they must NOT inherit `D:\YOGSOTH-AI\.mcp.json` (9 keys)
or `.env` (2 tokens). Each role carries only what it needs:
- optim: this project's optimization-loop skill + superpowers
- sim: superpowers only (persona is injected, no skills)
- exec: the 773 DARE skills + formated-specs/formated-results + superpowers
- loss: injection-fidelity + ladder-quality-order only (check-blind)

## Environment facts (this box, verified 2026-07-01, read-only)

- `claude` 2.1.197 on PATH; global config `C:\Users\<user>\.claude`.
- `codex` 0.120.0 on PATH (`~/.codex` has auth) — present, but we drop it.
- Shell: Git Bash / MSYS2 (`MINGW64`), NOT WSL. `$HOME=/c/Users/<user>`.
- **tmux: NOT installed.** No terminal multiplexer available.
- `ladder-foundry/sandbox/` already has a prototype (`.claude/`,
  `settings.local.json.template`, `read_session.py`, `smoke_test.py`) but NO
  runtime `home/{optim,sim,exec,loss}/`, `work/`, or `runs/` yet — those are
  what STAGE-5 scaffolding creates.

## STAGE-5 scaffolding checklist (the cheap, determinate "A-class" work)

Do this ONLY after the transport spike passes:
- Create clean role config-dirs `home/{optim,sim,exec,loss}/.claude` (each with
  `settings.local.json` = `{"permissions":{"defaultMode":"bypassPermissions"}}`),
  `work/{sim,exec,loss}` cwds, `runs/` skeleton.
- Apply the `codex_fn → claude` swap in `run_codex_loss.py`.
- Fix **M1**: `gen_configs.py` names configs `config_{rung}.json` (rung only) →
  collides across 8 topics at 48-run scale. Rename to
  `config_{topic}_{rung}` BEFORE the optimizer chains gen_configs into the loop.

## Standing hard constraints (carry every session — do NOT violate)

- **Privacy red line:** the CC log path (`C:\Users\...\.claude\projects\...`,
  its POSIX form, and any derived cwd-slug) MUST NEVER appear in any committed
  artifact. Log-reading scripts take `--logs-dir` as a REQUIRED arg, no
  default. Committed outputs are de-identified/aggregate only. Key VALUES
  never committed.
- **Banned CC flags EVERYWHERE (incl. design text):** the print flag,
  resume, session-id, allowed-tools, PTY/pexpect, tmux-for-children, and any
  driver script. All CC layers are normal interactive REPLs. (This ban is the
  source of the transport deadlock above — relaxing it is a user decision.)
- **Between-run independence:** sim/exec are freshly spawned each run; only
  the optimizer is continuous.
- **W5 leak boundary:** generation + loss skills are check-blind — they never
  see the 32 checks / 6 primitives / detection signatures. The probe is the
  only check-seeing session.
- **4-layer DARE architecture INVARIANT** (campaign→strategy→tactic→sop).
- **D1–D5 evaluation standard ONLY.** Academic criteria
  (novelty/baseline/rigor/citations/publishability) are FORBIDDEN as judging
  criteria.
- **Data-oriented weights:** training edits weights JSON only; `.py` never
  moves. `frozen_label` LOCKED; `collision_offset_axis ∈ {B1, expression}`;
  ONE weight changed per batch (先归因再动手).
- **no-fake-stub:** the loss codex/CC edge is NEVER stubbed to a green gate
  outcome; no local test asserts a gate result from canned output.
- Write/Edit calls stay UNDER 13000 chars; build large files in parts.
- Commit trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

## Known debts to carry into STAGE 5

- M1 gen_configs naming collision (fix as noted above).
- `run_codex_loss.py` tempfile leak (`delete=False` never unlinked).
- `validate()` is one-level (nested `per_axis_evidence` unenforced).
- `copeland_order` lacks a `winner ∈ {0..n-1}` guard (an out-of-range judge
  winner would KeyError rather than exit-2 gracefully).

## Next action

Run the transport spike (see STAGE-5 section). Do not rent a machine, build
the sandbox, or start the 48-run loop before that single unknown is resolved
and the user has ruled on any ban relaxation it surfaces.
