# ladder-foundry STAGE 3 — Run-Scripts Core Design (L8–L14, 7 leaf scripts)

> Created: 2026-06-30 22:30
> Topic: ladder-foundry STAGE 3 (run 骨架 + 数据落盘 leaf 脚本)
> Branch: self-iteration/ladder-foundry (continue, do NOT branch off)
> Depends on: STAGE 1 data-core (L1 weights) + STAGE 2 persona core (L7 gen_configs, generator/).

## Goal

Build the 7 deterministic, pure-function **leaf scripts** that turn the STAGE 1/2
"weights + persona" core into the run skeleton + data-sink layer a future optimizer-CC
(STAGE 4) will chain in `§loop` order. Every script is a standalone CLI; none import
each other; all are locally pytest-verifiable with synthetic inputs — NO remote CC, NO
codex, NO key, NO token. This is the last all-local stage before the cloud nesting
(STAGE 5+).

The 7 scripts (blueprint track L, components L8–L14):

| # | Script | One-line job |
| --- | --- | --- |
| L8 | `new_run_id.py` | system-time → `run_id` (yyyy-mm-dd-hh-mm-ss) + build `runs/<id>/` skeleton |
| L9 | `trace_emit.py` | append one jsonl event line (7-field common header + per-event body, seq self-increment) |
| L10 | `save_transcript.py` | read exec session jsonl → `transcript.md` (user/assistant only, `--logs-dir` required) |
| L11 | `concat_triple.py` | config + transcript fence blocks → `(config, graph, result)` triple |
| L12 | `gate_eval.py` | pure gate arithmetic: per-topic 3-way AND / batch pass_ratio / converged |
| L13 | `apply_weight_update.py` | F2 revise one JSON segment + revision_log / F1 byte-identical copy |
| L14 | `write_dataset.py` | privacy-whitelist trim + schema → `dataset/<topic>/<sample>.json` |

## Section 1 — Scope: what STAGE 3 IS and IS NOT

**IS:** the 7 scripts above, each a `scripts/<name>.py` CLI, each with a `test_<name>.py`
using `subprocess` to exercise the real CLI (argparse required-args, exit codes,
end-to-end behavior). All land in a NEW top-level `ladder-foundry/scripts/` directory.

**IS NOT (explicit boundary, do not pull in):**

- `gen_configs.py` (L7) — a STAGE 2 deliverable, already built and reviewed, **stays in
  `generator/`, untouched**. STAGE 3 does not move or rewrite it.
- `run_codex_loss.py` (L15) — STAGE 4 (needs real codex + loss schemas, not locally
  verifiable). NOT in this stage.
- loss skills / formated-specs / formated-results / optimization-loop (S1–S6) — STAGE 4.
- the `runs/` directory itself — NOT pre-created. Scripts are parameter-driven
  (`--run-dir` / `--runs-root`); the caller (future optimizer-CC) decides where to write.
  Tests use `tmp_path`. No speculative empty directories committed.

**The M1 carry-over (logged, NOT fixed this stage):** STAGE 2's `gen_configs.py` names
configs `config_{rung}.json` (rung only) — at 48 configs (8 topics) this collides across
topics. STAGE 3's data-sink scripts contract on a **topic-bearing sample name**
(`<batch>-topic<NN>-id<N>`), which is the correct shape. The two meet only at STAGE 5+
when a real optimizer chains gen_configs → these scripts. **Fixing gen_configs to emit
the topic-bearing name is a standalone STAGE 2 patch (M1), out of scope here.** STAGE 3
tests feed the topic-bearing sample name directly via `tmp_path`, so the stage is
internally self-consistent and pytest-green without touching gen_configs.

## Section 2 — Directory & import convention (the load-bearing path fix)

New layout (only the STAGE 3 additions shown):

```text
ladder-foundry/
├── generator/          # STAGE 1/2 pure weight bodies (weights/axes/interpolator/
│   │                   #   assembler/cards/contract/leak_audit/gen_configs) — UNTOUCHED
├── scripts/            # NEW — the 7 STAGE 3 leaf scripts
│   ├── new_run_id.py        trace_emit.py        save_transcript.py
│   ├── concat_triple.py     gate_eval.py         apply_weight_update.py
│   └── write_dataset.py
├── weights/batch-0.json     # already exists (STAGE 1 dump_initial output)
└── tests/              # test_new_run_id.py … test_write_dataset.py (subprocess CLI)
```

**The single most important correctness fix (P1):** the two scripts that import the
`generator` package (`apply_weight_update.py`; and any future script needing weights)
use `sys.path.insert(0, str(Path(__file__).resolve().parents[N]))`. Plan B assumed the
scripts lived at `skills/optimization-loop/scripts/` (3 levels below the project root),
so it wrote `parents[3]`. In `ladder-foundry/scripts/` the script is **1 level** below
`ladder-foundry/`, and `generator/` is its sibling — so the correct value is
**`parents[1]`**. `parents[3]` would walk above the repo and raise
`ModuleNotFoundError: No module named 'generator'`.

**The batch correctness fix (P2):** Plan B's tests invoke
`subprocess([sys.executable, "skills/optimization-loop/scripts/<name>.py", ...])` with
pytest run from the project root. STAGE 3 runs pytest from `ladder-foundry/`, so every
test's subprocess path prefix becomes **`"scripts/<name>.py"`**. Missed prefixes →
`FileNotFoundError` / non-zero exit on every test, regardless of logic correctness.

## Section 3 — Per-script design

Each script keeps Plan B's verbatim logic (these are transcription + test tasks) with
the path fixes from Section 2 and the targeted corrections called out below.

### L8 `new_run_id.py` — run skeleton

- CLI: `--runs-root` (default `"runs"`). Prints `run_id` = `now().strftime("%Y-%m-%d-%H-%M-%S")`.
- Builds `runs/<run_id>/{configs,transcripts,triples,loss,weights}/`.
- No `generator` import (pure stdlib). Verifies: run_id format regex + 5 subdirs exist.

### L9 `trace_emit.py` — 11-event ledger (CLI form, two micro-fixes)

- CLI: `--trace` (required) + the 5 header args `--run_id/--event/--batch_id/--topic_id/
  --rung_id` + arbitrary `--key val` pairs for the per-event body. `ts` (ISO8601) and
  `seq` are generated inside (never caller-supplied). Final jsonl line carries all **7
  common-header fields** (ts, run_id, event, batch_id, topic_id, rung_id, seq) + the body.
- **Architecture decision — CLI script, NOT the `TraceEmitter` class.** The trace-schema
  HTML proposed an importable `TraceEmitter` class holding a file handle / injectable
  sink. That presumes a long-running Python runner. This architecture has none: the
  optimizer-CC calls each leaf as a fresh process via its Bash tool (no driver script, no
  tmux for leaves). A class instance cannot survive across Bash calls; a stateless append
  CLI is the only form that matches the process model. The class is旧-runner遗留 → dropped.
- **Micro-fix A (nested/array body fields):** several event bodies are nested objects or
  arrays — `rung_start.config_full` (PolicyCard F0–F9 verbatim), `rung_start.axis_levels`,
  `rung_done.per_axis_evidence`, `topic_start.intended_order`, `batch_done.recent_ratios`,
  `converged.ratios`. A raw `--key val` stringifies these. Fix: when parsing each extra
  value, attempt `json.loads(v)` and store the parsed object on success, else the raw
  string (one try/except). Caller passes nested fields as a JSON string.
- **Micro-fix B (seq robustness):** `next_seq` reads the file's last non-blank line and
  `json.loads(...)["seq"] + 1`. Wrap the parse in try/except so a truncated final line
  (crash mid-write) doesn't crash the emitter — scan upward to the last valid line.
- seq is safe under the single-writer (serial CC) model; empty-file and all-blank-line
  edges already return 1.

### L10 `save_transcript.py` — exec transcript → .md (DRY: reuse read_session)

- CLI: `--logs-dir` **required, no default** (privacy red line — the only place that reads
  CC logs), `--cwd` (to locate the right session), `--out` (the `.md` path), `--sample`
  (metadata header).
- **DRY decision — reuse, do NOT rewrite.** STAGE 2 already shipped
  `sandbox/read_session.py` with `cwd_to_slug`, `find_latest_session(logs_dir, slug)`
  (newest `.jsonl` under `projects/<slug>/`), and `read_turns(session_path)` (list of
  `{role,text}`, correctly handling `content` as either a str OR a list-of-blocks).
  `save_transcript` **imports those three functions** and adds only a thin shell:
  `read_turns(...)` → format as markdown → write `--out` + a `--sample` header. ~10 lines.
- **This reuse fixes two real bugs in Plan B's draft:** (1) Plan B globbed
  `<logs-dir>/*.jsonl` and merged ALL sessions — wrong semantics (we want THIS run's exec
  conversation, located by cwd-slug, not every historical session). (2) Plan B read
  `content` as a plain str — real CC assistant turns are list-of-blocks, so the draft would
  dump `[{'type':'text',...}]` noise into the `.md`. `read_turns` already handles both.
- Verifies: missing `--logs-dir` → non-zero exit (privacy); only user/assistant rows reach
  the `.md`; no absolute log path / cwd-slug ever written into the `.md` body.
- **DRY placement (locked):** `read_session.py` stays in `sandbox/` (where its tests
  already live); `save_transcript` adds `sys.path` to import its three functions directly.
  No `session_utils.py` shared module — that would be a single-consumer forwarding layer
  (ponytail: no middle layer for one caller). Direct import it is.
- **Reuse precondition (verified):** `sandbox/read_session.py` exists and exposes
  `cwd_to_slug(cwd)`, `find_latest_session(logs_dir, cwd_slug)`, `read_turns(session_path)`
  — confirmed present with matching signatures. T3 must re-confirm before transcribing.
- **Test-input privacy:** `--cwd` and `--logs-dir` in every test use `tmp_path` synthetic
  values only — NEVER a real device path hard-coded into a committed test.

### L11 `concat_triple.py` — fence blocks → triple

- CLI: `--run-dir` + `--sample`. Reads `run-dir/configs/<sample>.json` +
  `run-dir/transcripts/<sample>.md`, writes `run-dir/triples/<sample>.json` =
  `{research_config, research_graph, research_result}`.
- Cuts by info-string fence (```` ```research-graph ```` / ```` ```research-result ````),
  **takes the LAST** block of each kind (the accepted draft after pushback), raises
  `ValueError` if a required fence is absent.
- **STAGE-boundary note:** the fence info-strings are the contract STAGE 4's
  formated-specs/formated-results must honor. STAGE 3 BUILDS-NOW with synthetic fence
  text, **locking the contract in the test** — when STAGE 4 writes those skills they must
  match this already-pinned fence name, else the test goes red. This is the right
  direction (契约靠测试固定,非代码耦合). No real CC transcript needed.

### L12 `gate_eval.py` — pure gate arithmetic

- CLI subcommands: `topic` (`--fidelity-rate/--mono/--endpoint` → 3-way AND), `batch`
  (`--flags` comma list → pass_ratio ≥0.80, hard integer line ≥7/8), `converged`
  (`--recent` → last 3 all ≥0.80). No CC/codex. Thresholds centralized (see Section 5).
- Verifies positive boundary (7/8 pass), negative boundary (6/8 fail), each false branch.

### L13 `apply_weight_update.py` — change weights JSON (data-oriented invariant)

- CLI: `--weights-dir` + `--batch-id`; F2 mode `--target/--key/--new/--reason`, F1 mode
  `--copy`. Imports `generator.weights` (needs the **`parents[1]`** fix).
- F2: `W.revise(cur, target, key, new, reason)` (signature confirmed byte-identical to the
  real `weights.py` — no change), writes `weights/<batch+1>.json` + appends
  `revision_log.jsonl`. F1: byte-for-byte copy forward, **no log, no revision**.
- **Data-oriented invariant enforced by `weights.revise` itself:** `frozen_label` and
  unknown targets are rejected; `collision_offset_axis` accepts only `B1`/`expression`.
  STAGE 3 does not re-implement these — it relies on the STAGE 1 validator. The script
  only tests "can change a segment + F1 copy"; backprop-driven intelligence is STAGE 4+.
- Verifies: F2 changes exactly one cell + writes revision_log; F1 byte-identical + writes
  NO log.

### L14 `write_dataset.py` — privacy whitelist → dataset

- CLI: `--run-dir/--sample/--topic/--rung/--out-root` + `--axis-levels/--loss1/
  --topic-pass`. Reads the triple, hard-fails (`sys.exit`) if it carries any field outside
  `{research_config, research_graph, research_result}` (catches a leaked `logs_dir`),
  assembles a whitelisted sample, hard-fails again if the output has any non-whitelist key.
- **STAGE-boundary note:** `loss1_fidelity`/`topic_pass` are CLI **parameters** (filled by
  STAGE 4's loss later); the whitelist hard-fail path doesn't touch their values, so fake
  `--loss1 1.0 --topic-pass true` fully exercises the privacy logic. BUILD-NOW.
- Verifies: non-whitelist field in triple → non-zero exit (privacy); whitelisted sample
  lands with `output keys ⊆ WHITELIST` and `label.rung_id` correct.

## Section 4 — The minimal invariant each script truly verifies

Per the ponytail pre-audit (all 7 BUILD-NOW, none deferred):

| Script | The one thing its test fails on if logic breaks |
| --- | --- |
| new_run_id | run_id matches `yyyy-mm-dd-hh-mm-ss` AND 5 subdirs built |
| trace_emit | 7 header fields present, seq strictly increments, nested body round-trips |
| save_transcript | missing `--logs-dir` exits non-zero; only user/assistant reach `.md` |
| concat_triple | same-name fence → takes LAST; missing fence → ValueError |
| gate_eval | 3-way AND; 7/8 pass & 6/8 fail integer line; converged last-3 |
| apply_weight_update | F2 writes revision_log; F1 byte-identical & writes NO log |
| write_dataset | non-whitelist field → non-zero exit; output keys ⊆ whitelist |

**Two test-hole fixes** (Plan B tests that could pass while broken):

- `trace_emit` test: add `assert all(v is not None for k,v in row.items() if k in COMMON)`
  so present-but-None header fields can't slip through the `COMMON <= set(row)` check.
- `apply_weight_update` F1 test: add `assert nxt_path.stat().st_size > 0` so an
  accidental empty file can't pass the byte-compare.

**Two micro-fix coverage tests** (the trace_emit fixes are non-trivial branches — each
needs a test that goes red if the branch breaks):

- Micro-fix A (json.loads body parsing): a test passing a malformed JSON string as a body
  value → it must store the raw string (graceful fallback, no crash, no silent data loss),
  AND a test passing a valid nested JSON → it round-trips as a parsed object.
- Micro-fix B (truncated-last-line recovery): a test writing a trace file whose final line
  is a truncated/corrupt JSON → next `trace_emit` still increments seq correctly without
  crashing (scans up to the last valid line).

## Section 5 — Thresholds & test method

- **Thresholds central location:** `gate_eval.py` reads its constants from one place. Plan
  B put them in `skills/optimization-loop/references/gate-thresholds.md` — but that skill
  dir is STAGE 4. For STAGE 3, the thresholds live as module-level constants in
  `gate_eval.py` itself (`FIDELITY_MIN=0.90`, `BATCH_RATIO_MIN=0.80`), with a one-line
  comment that STAGE 4 may externalize them to the references file. No speculative skill
  dir created now.
- **Test method (decided):** all 7 use `subprocess` to run the real CLI — verifies
  argparse required-args, exit codes, and end-to-end behavior (the privacy `--logs-dir`
  required check depends on this). Verbatim to Plan B's form, zero deviation. Sub-second
  each; whole STAGE 3 suite adds ~7 files, a few seconds.

## Section 6 — Tasks (one script = one task = one commit)

7 tasks, each: write failing subprocess test → run red → transcribe Plan B code with the
Section 2/3 fixes → run green → commit. Plus a wrap task.

- **T1 new_run_id** · **T2 trace_emit** (+ 2 micro-fixes) · **T3 save_transcript** (reuse
  read_session) · **T4 concat_triple** · **T5 gate_eval** · **T6 apply_weight_update**
  (parents[1] fix) · **T7 write_dataset**.
- **T8 wrap:** full-suite regression (STAGE 1+2+3 all green), privacy grep over
  `scripts/` + `tests/` covering all three log-path signatures — Windows
  (`C:\Users\...\.claude\projects`), POSIX (`/workspace/home/.../.claude/projects`), and
  any bare cwd-slug — all must be clean; update progress ledger.

Order is dependency-free (no script imports another), but T1→T7 follows blueprint L8→L14
for a clean review narrative. T6 carries the load-bearing `parents[1]` fix and the
real `generator.weights` import; T3 carries the DRY reuse.

## Section 7 — Constraints carried (every task)

- Privacy red line: `save_transcript --logs-dir` required no default; no CC log absolute
  path / cwd-slug in any committed artifact; T8 greps to confirm.
- Data-oriented invariant: training edits JSON only, `.py` never moves; `frozen_label`
  locked (enforced by `weights.revise`); `collision_offset_axis ∈ {B1,expression}` only.
- W5 check-blind: these scripts never name 32-check / 6-primitive / detection signatures.
- No `-p`/`--resume`/`--session-id`/`--allowedTools` anywhere; no driver/PTY/tmux for
  leaves. (These scripts are pure-function; the constraint binds their future CC caller.)
- 4-layer DARE invariant untouched; Write/Edit < 13000 chars; commit only when asked,
  trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
