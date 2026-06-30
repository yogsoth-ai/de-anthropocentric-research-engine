# ladder-foundry STAGE 2 — Persona Core Design (D1 + D2 + L7 + smoke test)

> Created: 2026-06-30 17:02
> Topic: ladder-foundry STAGE 2 (persona 内核)
> Branch: self-iteration/ladder-foundry (continue, do NOT branch off)
> Depends on: STAGE 1 data-core (L1 weights / L3 axes / L4 interpolator / L5 assembler / L6 cards), all merged on this branch.

## Goal

Turn STAGE 1's seed-prose data-core into a real persona core: finalize the PolicyCard
field semantics (D1), author the two real endpoint personas + the locked rung
coordinates (D2), build the deterministic config-generation pipeline (L7), and run the
FIRST real sim-cc — a persona-injection smoke test — inside a local Windows sandbox.

## Section 1 — Architecture: STAGE 2 splits into 2A (pure data) + 2B (first real CC)

The stage has two milestones with different risk classes and acceptance methods. A hard
gate separates them.

- **STAGE 2A — persona data core** (local pure-functions, NO key / NO token / NO runtime).
  The last clean local milestone. Three deliverables, all reading STAGE 1's `weights.py`:
  D1 (PolicyCard semantic contract + validator), D2 (two endpoint personas + filled
  `coord_table`), L7 (`gen_configs.py` deterministic pipeline). Acceptance = pytest +
  human-eye read of the 6 generated config personas.
- **HARD GATE:** 2A must pass pytest AND the human-eye read (id0 reads genius, id5 reads
  contrarian, middle 4 monotone) before 2B starts. A bad data core is not allowed to
  reach a real CC.
- **STAGE 2B — persona-injection smoke test** (first real sim-cc + sandbox). Introduces
  key / token / privacy-red-line / sandbox-confinement. Spawns a real sim-cc, injects each
  endpoint persona against a FIXED stimulus, reads sim's own session jsonl, verifies the
  persona was worn and the two endpoints visibly diverge. **Explicitly NOT the AS-1
  quality-separation gate** (that needs exec + loss-2, deferred to STAGE 5/6).

## Global Constraints (every task inherits these — copied verbatim from project rules)

- **Build on branch `self-iteration/ladder-foundry`.** Do NOT branch off, do NOT push to
  main. Commit trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- **NO `-p` / `--resume` / `--session-id` / `--allowedTools`** anywhere — all CC layers are
  normal interactive REPLs.
- **W5 leak boundary:** generation is check-blind. F0–F9 prose must pass `leak_audit` — no
  32-check / 6-primitive / detection-signature vocabulary. `leak_audit.py` (STAGE 1) is the
  only file allowed to name the denied terms.
- **Privacy red line:** the CC log path (`C:\Users\...\.claude\projects\...`) and any path
  derived from it (the cwd-slug) MUST NEVER appear in a committed artifact. The jsonl reader
  takes `--logs-dir` as a REQUIRED arg with no default. Committed pilot output is
  de-identified / aggregate only.
- **Two API-key groups (Claude / Codex) physically isolated;** key VALUES never enter a
  committed artifact — reference by variable name only. (2B touches only the Claude key.)
- **Data-oriented invariant:** training edits the JSON DATA segments only; the `.py` sources
  never move. `frozen_label` (rank_order + coord_table) is LOCKED — `revise` rejects it.
- **AS-3 structural lock:** `interp_params` key-set = exactly
  {collision_offset_axis, endpoint_spread, granularity_map}; collision_offset_axis ∈
  {B1, expression} only, NEVER an A1–A5 label axis.
- **Write/Edit calls stay under 13000 chars;** build large files in parts.
- **5-dim DARE standard only** (D1–D5 meaningfulness/skill-value/use-to-DARE/4-layer/
  prerequisites). Academic standards (novelty/baseline/rigor/citations/publishability) are
  FORBIDDEN as judging criteria.

---

## Section 2 — 2A-D1: PolicyCard semantic contract

PolicyCard keeps the STAGE 1 shape (cards.py: F0–F9 prose fields + `axis_levels` dict).
D1 does NOT change cards.py; it adds the SEMANTIC contract (which field reads which axis)
plus a validator. The field→axis map is one-to-one for A1–A5:

| Field | Semantics | Source |
| --- | --- | --- |
| F0 | persona identity / role header | composite rung + B1 tone |
| F1 | substance demand | ← A1 |
| F2 | request legitimacy / coherence | ← A2 |
| F3 | operationalization insistence | ← A3 |
| F4 | premise corrigibility | ← A4 |
| F5 | generativity | ← A5 |
| F6 | acceptance rule, DERIVED from F1/F3/F2 (= A1/A3/A2) | `assembler_params.f6_derivation` |
| F7 | prerequisite facts | ← `topic.F7_prerequisite` + A4 overlay |
| F8 | turn budget (constant per batch) | `assembler_params.turn_budget` |
| F9 | framing / tone directive | ← B1 (confound) |

**Deliverable:** this contract (documented) + `validate_card(card)` — checks `axis_levels`
keys = {A1..A5, B1}, values in-enum, F-fields non-empty. `leak_audit` is reused from STAGE 1.

> Note on B1: F9 is the single field that CARRIES the B1 framing/tone directive. F0's "B1
> tone" means the role header is written in a tone CONSISTENT with B1 — F0 does not encode a
> second, independent B1 value. B1 has one source of truth (the card's `axis_levels.B1`).

### A4/A5 schema decision (ruled: Option A — the ponytail call)

STAGE 1 locked `axis_prose = {axis: {L0..L4}}` UNIFORMLY for all 5 axes; the codex CONFORMS
audit explicitly verified no C±/G± leaked into `axis_prose`. The A4 C+/C-/C0 and A5 G0/G+
overlays were deferred to STAGE 2.

**Decision:** keep `axis_prose` indexed L0..L4 for all 5 axes — do NOT special-case A4/A5 in
`weights.py`, do NOT break the STAGE 1 schema lock. Represent the overlay as a FIXED
level↔tag convention:

- A4: `{L0 ↔ C-, L2 ↔ C0, L4 ↔ C+}`
- A5: `{L0 ↔ G0, L4 ↔ G+}`

The config's `axis_levels` RECORDS the human-meaningful tag (C+/G+) for A4/A5 as the label;
`axis_prose` stays L0..L4-indexed.

**Convention's home = the D1 contract document** (a fixed structural convention L7 reads as a
constant — NOT a trainable weight, NOT silently hardcoded). Stated explicitly in D1:

- A4/A5 are OFF-SPINE overlays — they are NOT part of `primary_sort` {A1, A3, A2} and do not
  participate in the composite ladder ordering.
- A4 L1/L3 and A5 L1/L2/L3 are unused seed-prose slots (cheap waste, accepted).

This honors the doc's `axis_levels {"A4": "C+"}` format AND keeps STAGE 1's lock + codex
audit intact.

---

## Section 3 — 2A-D2: two endpoint personas + coord_table

Author REAL prose to replace STAGE 1's seed prose (`"A1.L0 seed prose"` → real bodies).

**The two endpoints:**

- **id0 genius:** A1=L4, A2=L4, A3=L4, A4=C+, A5=G+, B1=neu
- **id5 absurd-contrarian:** A1=L0, A2=L0, A3=L0, A4=C-, A5=G0, B1=buz

**axis_prose bodies to author:** the FULL L0..L4 five levels for A1/A2/A3 (the interpolator
needs the intermediate rungs); A4 at L0/L2/L4 (= C-/C0/C+); A5 at L0/L4 (= G0/G+).

### The coord_table provenance rule (the load-bearing fidelity fix)

The audit settled the central mechanic: **per-axis prose is selected by the LOCKED
`coord_table` level**, via `axes.level_text(w, axis, coord[axis])`. `level_idx`
(= `granularity_map(t)`, the spread layer) is used ONLY for collision detection +
elaboration intensity — it NEVER selects a prose body. If `level_idx` drove prose, then
training `interp_params` would move which prose is selected → move the per-rung axis levels
→ move the LABEL, which is exactly the "标签随训练漂移 = 数据集失效" that `frozen_label`
exists to prevent.

**Consequence:** `coord_table` must define coordinates for ALL 6 rungs, but D2 only authors
the 2 endpoints. The 4 intermediate rungs (1–4) need a defined, LOCKED origin.

**Decision (ruled):** compute the intermediate-rung coordinates ONCE at AUTHORING time (the
`round` strategy may be used as an authoring-time tool to interpolate between the two
endpoints), then FREEZE them into `coord_table`. At GENERATION time, `granularity_map` NEVER
recomputes a per-axis coordinate — it only reads. This keeps the label fully determined by
the locked `coord_table` while letting the spread layer remain trainable.

### Two STAGE-1 landmines D2/L7 must defuse

1. **`coord=None` fallback trap.** batch-0's `coord_table={}` → `coord` is `None` today. An
   implementer who sees `coord=None` and a handy `level_idx` will be tempted to wire
   `level_text(w, axis, f"L{level_idx}")` as a fallback — that IS the label-drift bug.
   **Mandate:** prose selection reads `coord[axis]`; if `coord is None`, FAIL LOUD; never
   fall back to `level_idx`.
2. **Ordering lock.** D2 must fill `coord_table` BEFORE L7 runs, or L7 crashes on
   `None[axis]`. The plan orders D2 before L7.

### coord_table keying + endpoint spread

- **Keyed by rung_id `"0".."5"`** (string), NOT by topic. The same 6-rung ladder is reused
  across all (eventual) 8 topics; topic enters via `build_batch(..., topic_id)` and is
  orthogonal to `coord_table`. (Topics are deferred to STAGE 6/7 — see Section 4.)
- **Endpoint spread (AS-1 headroom):** the two endpoint coordinates must be spread far
  enough by design to leave the spread layer training headroom. NOTE: this is a data-design
  constraint only; the real AS-1 quality-separation verification is NOT in 2A — it needs
  exec + loss-2, deferred to STAGE 5/6.

---

## Section 4 — 2A-L7: gen_configs.py pipeline

A deterministic pipeline that wires together every STAGE 1 component and emits config
personas:

```
load(weights)
  -> interpolator.ladder_levels(n=6)              # 6 rungs: rung_id, level_idx, coord
  -> per rung: assembler.build_batch(w, n=6, topic_id)   # coord, perturb_axis, params
  -> axes.level_text(w, axis, coord[axis])        # fill F1-F5 prose (reads LOCKED coord,
                                                  #   never level_idx)
  -> assemble F0/F6/F7/F8/F9 per f6_derivation / turn_budget
  -> validate_card(card) + leak_audit(each card)  # W5 interception
  -> output config JSON
```

**Constraints carried into the pipeline (all from earlier sections):**

- F1–F5 prose selected by `coord[axis]`; `coord is None` → fail loud; NEVER use `level_idx`.
- Collision stagger uses B1 / expression only, never A1–A5 (STAGE 1 physical lock).
- Each card passes `leak_audit`; on hit → regenerate-then-reaudit (bounded retries, alarm
  on ceiling), never silent.

**Topics deferred ⇒ 2A runs ONE placeholder topic ⇒ output = 6 config personas** (the
blueprint's "本地 6", not the full 48). The full 48 = 6 rungs × 8 real topics, which waits
for STAGE 6/7's D3 `topics.json`.

**Acceptance** = pytest (pipeline determinism, coord-driven selection, leak_audit fallback,
`validate_card`) + **human-eye read of the 6 configs**: id0 reads like a genius user, id5
like a contrarian user, the middle 4 rungs a monotone transition. This is the blueprint's
mandated human gate.

---

## Section 5 — 2B: persona-injection smoke test + sandbox

### Sandbox (local Windows, under `ladder-foundry/sandbox/`)

- Child sim-cc started by running `claude` DIRECTLY in a Bash tool (NO driver script, NO
  PTY, NO tmux) — a normal interactive REPL.
- **Banned flags forbidden:** `-p` / `--resume` / `--session-id` / `--allowedTools`.
- Confinement = `cwd=sandbox` + `CLAUDE_CONFIG_DIR=sandbox/.claude` + `settings.local.json`
  with `{permissions: {defaultMode: bypassPermissions, deny: ["Read(<everything outside
  sandbox, esp. the CC-log path>)"]}}` — see the ponytail narrowing below for why this is
  ONE deny rule, not the heavy STAGE-5 list. `deny` is evaluated BEFORE `bypassPermissions`
  (authoritatively confirmed).

**Ponytail narrowing (audit-driven):** 2B's sim is a PURE conversational responder — it does
NOT spawn exec (exec is out of 2B scope) and makes essentially no tool calls. The heavy
deny-list (deny Bash/Write/Edit outside sandbox + CC-log path + other-role key dir) is
scoped for STAGE 5's sim (which DOES Bash-spawn exec). 2B does not import that threat model.
**2B needs only:** dedicated cwd + `CLAUDE_CONFIG_DIR` isolation (bounds it naturally) + ONE
deny rule preventing reads outside the sandbox (especially the CC-log path). Full OS-hard
boundary + heavy deny is left to STAGE 5.

### The load-bearing empirical check (gates whether 2B runs locally at all)

Because `--allowedTools` is banned and `bypassPermissions` auto-approves everything,
`permissions.deny` is the ONLY in-claude confinement lever. **Before building 2B, empirically
verify on this machine that a `deny` rule still fires under `bypassPermissions`.** If it does
NOT fire, that is decisive evidence that 2B must run on the remote box (STAGE 5 R1 env)
rather than locally. (Ceiling noted: the Windows Bash tool has no OS sandbox; `deny` governs
Read/Write/Edit only — adequate for a non-adversarial persona-player, OS-hard boundary
deferred.)

### Smoke-test flow

1. A FIXED written stimulus (a placeholder research proposal) — sim has no exec to talk to,
   so it needs something to react to.
2. Inject id0 → read sim's own session jsonl (located by globbing `projects/<cwd-slug>/`,
   NOT `--session-id`).
3. Spawn a FRESH sim, inject id5 (between-run independence — no session reuse) → read jsonl.
4. Verify: (1) the persona was worn; (2) the two endpoints visibly diverge in their reaction
   to the same stimulus. **Does NOT verify AS-1 quality separation.**

### Privacy (two nailed-down rules)

- The jsonl reader takes `--logs-dir` as a REQUIRED arg, no default; committed pilot output
  is de-identified / aggregate; the sandbox `CLAUDE_CONFIG_DIR` path AND its derived cwd-slug
  NEVER appear in a committed file; output lands under a gitignored path.
- "One-shot injection" must stay an INTERACTIVE turn — never degrade to `claude -p` / headless.

---

## Honest boundary

STAGE 2 finalizes the persona core (field semantics, real endpoint prose, locked
coordinates) and proves a real sim-cc WEARS the persona (loss-1 precursor). It does NOT prove
the eventual (graph, result) samples are quality-separated — AS-1 — which needs exec + loss-2
in STAGE 5/6. The 2B smoke test is named to make this boundary explicit and must not be
mistaken for the AS-1 gate.
