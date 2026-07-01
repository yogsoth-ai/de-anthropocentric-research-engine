# ladder-foundry STAGE 4 — Loss Skills + Optimizer Brain Design (L15 + S1–S6, 7 artifacts)

> Created: 2026-06-30 23:26
> Topic: ladder-foundry STAGE 4 (loss skills + formated-* contracts + run_codex_loss + optimization-loop brain)
> Branch: self-iteration/ladder-foundry (continue, do NOT branch off, do NOT merge/push/finish)
> Depends on: STAGE 1 data-core (weights) + STAGE 2 persona-core (gen_configs, sandbox/read_session) + STAGE 3 run-scripts (7 leaf scripts L8–L14).

## Goal

Author the 7 STAGE-4 artifacts that turn the STAGE 1–3 weights + persona + run-skeleton
core into the **loss layer + optimizer brain** a real three-layer-nested CC run (STAGE 5)
will execute. Five of them are prompt artifacts (CC/codex scripts, not runnable Python);
one (`run_codex_loss.py`, L15) is the last leaf script; one is the thick `optimization-loop`
SKILL that plays the whole training loop. STAGE 4 crosses the all-local line: most of it
is **authored now, behaviorally verified at STAGE 5** (needs real codex + keys). What CAN
be verified locally this stage — leak-audit, fence-contract-against-concat_triple, schema
validation, run_codex_loss payload/parse plumbing — is verified; everything else is
honestly marked STAGE-5-deferred, never faked green.

The 7 artifacts (blueprint components: L15 leaf + S1–S6 skills):

| # | Artifact | One-line job |
| --- | --- | --- |
| S1 | `skills/formated-specs/SKILL.md` | exec spec-slot skill → emits `research-graph` JSON fenced block into the dialogue |
| S2 | `skills/formated-results/SKILL.md` | exec closing skill → emits `research-result` JSON fenced block, same-source paired |
| S3 | `skills/injection-fidelity/SKILL.md` + `loss1.schema.json` | loss-1 codex judge: did sim enact the PolicyCard? check-blind |
| S4 | `skills/ladder-quality-order/SKILL.md` + `loss2.schema.json` | loss-2 codex judge: is the 6-rung quality ladder monotone + endpoints separated? check-blind |
| L15 | `skills/optimization-loop/scripts/run_codex_loss.py` | assemble payload → call real codex → schema-validate → write `loss/*.json` |
| S5 | `skills/optimization-loop/SKILL.md` | the optimizer-cc brain: §loop/§gate/§backprop/§state/§tools |
| S6 | `skills/optimization-loop/references/{gate-thresholds,backprop-heuristic}.md` | new thresholds (point back, don't copy) + attribution heuristic |

## Section 1 — Scope: what STAGE 4 IS and IS NOT

**IS:** the 7 artifacts above, all landing under a NEW top-level `ladder-foundry/skills/`
directory. The division principle for STAGE 4 is **NOT "locally verifiable"** — it is
"authoring the artifacts that need real codex/CC, plus their structural checks." STAGE 5
is "wire into the real nesting and RUN." This was settled by a 3-subagent ruling
(ponytail verifiability audit + prototype-reuse inventory + design-intent alignment) and
two final reviews (ponytail APPROVE + intent ALIGNED); the "split / don't split" question
was a false dichotomy — the roadmap (CLAUDE.md "Next action (STAGE 4)" + STAGE 3 spec
L41) already binds all of {loss skills, formated-*, run_codex_loss.py, optimization-loop
brain} to the same STAGE 4 list.

**IS NOT (explicit boundary, do not pull in):**

- The actual three-layer nested RUN — STAGE 5. STAGE 4 writes the brain; STAGE 5 runs it.
- Real codex invocation behavior — the `run_codex_loss.py` codex edge is isolated behind
  an injectable `codex_fn` and verified at STAGE 5 with real keys. **Never fake-stubbed to
  go green** (the `feedback-no-e2e-shell` red line).
- The 4 STAGE-1/2/3 leaf scripts' relocation — they stay flat in `ladder-foundry/scripts/`
  and `generator/`. `optimization-loop` references them by relative anchor `../../scripts/`
  (D1 below); moving them would break STAGE-3's verified `parents[1]` import.
- The M1 gen_configs naming-collision fix (`config_{rung}` → topic-bearing name) — a
  STAGE-2 patch to land before a real optimizer chains gen_configs → leaves at STAGE 5+.
  STAGE 4 does NOT touch it (touching it early breaks the single-variable boundary); the
  `optimization-loop` §tools merely annotates the dependency.
- The `runs/` directory itself — NOT pre-created; scripts are parameter-driven, the future
  optimizer-CC decides where to write. Tests use `tmp_path`.

## Section 2 — The two declared deviations (logged, not defects)

**D1 — leaves NOT moved into `optimization-loop/scripts/`.** The original architecture
draft (arch doc L406-418) assumed all leaf py would live under
`optimization-loop/scripts/`. STAGE 3 actually shipped them flat under
`ladder-foundry/scripts/` (L8–L14) + `generator/gen_configs.py`. STAGE 4 does NOT relocate
them: `optimization-loop/SKILL.md` §tools registers them via relative anchor
`../../scripts/<name>.py` and `../../generator/gen_configs.py` (from the skill dir).
`optimization-loop` only owns ONE new leaf, `scripts/run_codex_loss.py`. Rationale
(ponytail-confirmed): moving L8–L14 would turn their verified `parents[1]` generator import
into `parents[3]` (the exact brittleness STAGE 3 avoided) and fork a second copy of the leaf
code. Not moving is both lazier and preserves a STAGE-3-verified invariant.

**M1 — gen_configs `config_{rung}.json` naming collision (annotated, NOT fixed here).**
STAGE 2's `gen_configs.py` names configs by rung alone; at STAGE 5's 48 configs (8 topics)
this collides across topics. This is a standalone STAGE-2 patch to land before a real
optimizer chains gen_configs → these leaves at STAGE 5+. STAGE 4 §tools annotates the
dependency but does not fix it (fixing early breaks the single-variable backprop boundary).

## Section 3 — Directory & landing convention

New layout (only the STAGE 4 additions shown):

```text
ladder-foundry/
├── generator/          # STAGE 1/2 weight bodies + gen_configs — UNTOUCHED
├── scripts/            # STAGE 3 leaves L8–L14 — UNTOUCHED
├── sandbox/            # STAGE 2 read_session + smoke — UNTOUCHED
├── skills/             # NEW — the 7 STAGE 4 artifacts
│   ├── formated-specs/SKILL.md
│   ├── formated-results/SKILL.md
│   ├── injection-fidelity/{SKILL.md, loss1.schema.json}
│   ├── ladder-quality-order/{SKILL.md, loss2.schema.json}
│   └── optimization-loop/
│       ├── SKILL.md
│       ├── scripts/run_codex_loss.py        # + loss1.schema.json / loss2.schema.json copies (see S5/L15)
│       └── references/{gate-thresholds.md, backprop-heuristic.md}
└── tests/              # test_formated_contract.py, test_run_codex_loss.py, test_skill_audits.py
```

**skill structure (locked): 1 thick + 4 light.** Only `optimization-loop` is a thick skill
(SKILL.md + scripts/ + references/). The other 4 (2 exec contracts + 2 loss judges) are
single-file skills — just a SKILL.md (+ a co-located output schema for the 2 loss judges),
no scripts/, no references/. Per skill-creator: a light skill does not force child dirs.

**Naming (locked): `formated-results` is PLURAL.** The arch doc pins the plural at L116/
121/268/411/776/822/1114 (it is "the user's second hard rule" = closing must call
`formated-results`). The prototype draft's singular `formated-result` is a typo; corrected
here. (`formated-specs` is plural on both sides — consistent.)

## Section 4 — S1/S2 formated-specs / formated-results (exec contracts)

Two single-file light skills the exec-cc carries. They are the contract STAGE-3's
`concat_triple.py` already pins, so the design contracts AGAINST the delivered consumer.

**Verified consumer facts (concat_triple.py / test_concat_triple.py):**
- fence info-string = `research-graph` and `research-result` (hyphen, NOT ` ```json `).
- concat takes the **LAST** matching fenced pair (the final accepted draft after pushback).
- any kind missing → `raise ValueError` → non-zero exit.
- payload = `json.loads(blocks[-1])`; concat validates NO fields — field completeness is the
  skill contract's job, not concat's (concat-layer cannot test it).

### S1 `formated-specs`

- **Role:** the spec-slot skill that occupies exec's spec step in place of `writing-specs`
  (library-layer replacement — `writing-specs` is not in exec's lib). Emits the actual
  4-layer DARE orchestration as one `research-graph` JSON fenced block.
- **frontmatter:** `name: formated-specs` + a description scrubbed of any 32-check/probe
  wording (the prototype draft's "32-check probe will later read…" is a W5 leak — removed).
- **Contract points:** (1) fence ` ```research-graph ` open / ` ``` ` close, exact string
  `research-graph`. (2) payload = single valid JSON object (schema below). (3) **emit as a
  fenced block in your reply (into the dialogue)** — NOT written to a spec file; the block
  lands in exec's session jsonl → save_transcript → concat cuts it (preserves "authoritative
  transcript = exec jsonl, single source of truth"). (4) atomicity: the whole fenced block
  produced within a single exec assistant turn. (5) take-last: multi-version → concat takes
  the last `research-graph` fence. (6) mandatory chain: last step `load formated-results`.
- **research_graph payload schema** (JSON; `[concat-hard]` = block exists + valid JSON,
  concat's only hard dep; `[contract]` = skill should emit, downstream routing needs it,
  concat does NOT check, STAGE-5-verified):

```text
{
  "nodes":        [ {"id": str, "skill": str, "layer": "campaign|strategy|tactic|sop"} ],  # [contract]
  "edges":        [ {"from": str, "to": str, "kind": "calls|sequences"} ],                  # [contract]
  "layer_labels": { "<node_id>": "campaign|strategy|tactic|sop" },                          # [contract]
  "manifest":     [ str ],                  # skills actually orchestrated; do not fabricate  # [contract]
  "prereq_dag":   [ {"node": str, "requires": [str]} ]                                       # [contract]
}
```

### S2 `formated-results`

- **Role:** the closing skill, loaded as formated-specs' last step. Summarizes the design
  just produced into one `research-result` JSON fenced block, same-source paired with the
  graph block, in the same dialogue. Does NOT execute the research (probe-depth = design
  document level).
- **frontmatter:** `name: formated-results` (plural) + W5-clean description.
- **Contract points:** fence ` ```research-result ` / ` ``` ` exact string `research-result`;
  payload = valid JSON; emit into the dialogue (not a file); atomicity; take-last; same-source
  (only summarize the design formated-specs already produced, add no new research).
- **research_result payload schema:**

```text
{
  "title":     str,                                       # [contract]
  "sections":  [ {"heading": str, "body": str} ],         # [contract]  design body, sectioned for R-only routing
  "artifacts": [ str ]                                    # [contract]  spec filename / figure refs
}
```

### S1/S2 local checks vs STAGE-5-verified

- **Local (test_formated_contract.py):** (a) leak-audit both SKILL.md (W5: no 32-check/
  6-primitive/detection signature). (b) fence contract red/green against concat_triple:
  synthesize a transcript with one `research-graph` + one `research-result` JSON fence →
  assert concat cuts the triple; two result blocks → assert it takes `title=="final"`;
  missing one kind → assert non-zero exit; ` ```json ` info-string drift → assert concat's
  `findall` empties → ValueError (locks the corrected contract).
- **STAGE-5-verified (honestly deferred):** atomicity (single-turn produce), mandatory-chain
  firing, library-layer replacement taking effect, `[contract]` field semantics (graph truly
  reflects orchestration, no fabricated skills), save_transcript fidelity.

## Section 5 — S3 injection-fidelity (loss-1 codex judge)

- **Role:** runs in the codex role (separate model family, anti-self-bias), check-blind.
  Reads one sample's de-identified dialogue + its PolicyCard; decides axis-by-axis whether
  the user-simulator semantically enacted the card's per-axis pressure, ANDs into one
  `fidelity` verdict + a [0,1] diagnostic `loss1`. Judges "was the card enacted", never "is
  the research good."
- **6 named signals × bound axis + 2 event bits + A5 seed test:**

| Signal | Bound axis | What it measures |
| --- | --- | --- |
| `pushback_count` | A1 (primary) | turns demanding more substance / refusing perfunctory answers → `pushback_rate` |
| `accept_without_question_rate` | A1 (mirror) | share of turns accepting without challenge (cross-checks A1) |
| `operationalization_demand_count` | A3 | turns demanding numbers/thresholds/executable steps → `op_demand_rate` |
| `incoherent_demand_flag` | A2 (threshold overlay) | bool: demands self-contradictory / no legitimate throughline |
| `premise_defended_count` | A4 overlay | turns still holding the wrong premise after challenge |
| `novel_seed_count` | A5 overlay | turns introducing original directions (after seed test) |

  Event bits: `premise_dropped` / `premise_revised` (A4 trajectory). **A5 substantive-seed
  test** (all 3 → seed counts): substantive (not pleasantry), topic-relevant (same domain as
  F7 prereq facts), non-restatement (not reskinning exec's prior turn). Each counted seed
  carries a `quote` + the 3 judgments in `per_axis_evidence.A5`.

- **Expected band:** continuous axes A1/A3 → 5 non-overlapping bands covering [0,1],
  monotone increasing L0..L4 (e.g. L0=[0,.10], L1=(.10,.30], L2=(.30,.55], L3=(.55,.80],
  L4=(.80,1]); normalized by the pressure-window user-turn count (pressure_turns, closing
  turns excluded). A1 mirror cross-check uses the `1−x`-flipped band. Overlay axes use
  bool/threshold (A2 flag = (card.A2 ∈ {L0,L1}); A4 by C-/C0/C+ event-bit combos; A5 G+ →
  `novel_seed_count ≥ 1`, G0 → `≤ 1`). NOTE: the arch doc's example at L973 has the A1
  direction backwards (pushback increases with A1 level — L4 high band, L0 low); corrected.
- **Verdict formulas:** `axis_pass[ax] = observed ∈ band(card.level[ax])` for ax∈{A1..A5};
  `fidelity = AND(axis_pass[*]) AND (NOT drift_flag)`; `loss1 = (#axes passed)/5` (diagnostic
  fidelity score, higher=more faithful, for backprop to locate which axis collapsed). B1 is a
  confound, off-spine, NOT in the fidelity AND. Batch `fidelity_rate = #(fidelity)/#samples`,
  gate ≥ 0.90 (**points back to `gate_eval.FIDELITY_MIN`, does not copy the number**).
- **Drift gate (per-turn, from arch M5):** split the pressure window into halves; both halves'
  rates must stay in-band; if the second half drifts toward the cooperative pole (pushback/
  op_demand *drops*) beyond tolerance ε → `drift_flag=true` → that sample's fidelity FAILs
  (post-drift labels untrustworthy). Only penalizes collapse-toward-cooperation, not stronger
  pressure.
- **loss1.schema.json** (co-located; required, additionalProperties:false): `fidelity:bool`,
  `loss1:number[0,1]`, `per_axis_evidence:{A1..A5 each {observed, expected_band:str,
  pass:bool, quote:str(non-empty)}}`, `drift_flag:bool`, `note:str(optional)`. Consistency
  rule (skill text, schema can't express): `fidelity == all(pass) AND ¬drift`; `loss1 ==
  count(pass)/5`.
- **3 cold-start falsifiers (skill validation items):** FS1-1 counts-match-but-semantically-
  empty → quote required non-empty + codex must mark "substantive pressure not surface
  question". FS1-2 A5 seed novel-but-trivial/off-topic → each counted seed carries quote + 3
  judgments. FS1-3 two parsers disagree → A1 judged jointly by pushback_rate (primary) +
  accept_without_question_rate (mirror), directions must agree.
- **Local checks:** leak-audit SKILL.md + loss1.schema.json (W5); schema self-validation
  against synthetic docs (one all-pass, one collapsed-axis, one drift); band arithmetic
  self-consistency (5 bands non-overlapping + cover [0,1]; mirror = 1−x); 6-rung expected
  matrix cross-check against coord_table.
- **STAGE-5-verified:** judge quality (semantic-pressure vs surface-question), ε / band-point
  calibration to real dialogue distribution, whether the ≥0.90 batch gate is achievable
  (AS-1: DARE's rigor floor may resist downward pressure — the STAGE-6 2-sample pilot's
  go/no-go question).

## Section 6 — S4 ladder-quality-order (loss-2 codex judge)

- **Role:** codex role, check-blind, **D1–D5 wording only**. Over one topic's 6 shuffled
  (research_graph, research_result) samples, pairwise-rank by quality, emit loss2.json
  (τ / monotonicity / endpoint separation / rigor_floor). Judges whether the pressure
  difference materialized into a monotone, separable quality ladder.
- **Pairwise mechanism (PAIR, no absolute scores):** harness-side (run_codex_loss) shuffles
  the 6 samples and records the permutation; codex sees 6 anonymous positions, blind to rung
  id / config. Enumerate all i<j (15 pairs); each → `{winner, reason}` (one-line D1–D5
  reason). Copeland-aggregate into an induced order; un-shuffle to real ids; compute Kendall τ
  vs the true rung order id0>…>id5. graph is structure-aware holistic input but NOT used to
  run any check.
- **monotonicity_pass = (τ ≥ 0.7) AND (no adjacent endpoint inversion)** — id0 wins all its
  direct pairs at high confidence, induced first = id0, last = id5.
- **Endpoint separation (K independent judgments + majority):** run K mutually-independent
  codex pair judgments on (id0, id5), count id0 wins `w0`; `endpoint_separation_pass = (w0 ≥
  K − allowance)` (K-run majority form, not a single scalar gap).
- **rigor_floor_flag** = (endpoint_separation_pass == false) AND (endpoints near-tie, w0 in
  [K/2−ε, K/2+ε]) — flags suspected DARE rigor floor (endpoints can't be pulled apart), NOT a
  tuning bug. It does NOT enter the gate AND; it is a batch-level alarm feeding §backprop's
  attribution (tells it: do NOT train ② on this). Distinct from "stable wrong direction"
  (id5 wins) which is a real ordering break.
- **丙-calibration hand-off:** τ ≥ 0.8 AND endpoints 100% consistent (w0 == K) → hand off to
  the next stage (quality good enough). Derived by the optimizer from loss2.json's `tau` +
  endpoint sweep; NOT a persisted schema field (see below).
- **z⊥C self-check (FS2-2):** before the main 6-rung ranking, on the topic's B1 confound
  triplet (same substance, different framing), the order must stay flat; if it varies with
  framing → judge dragged by confound → this topic's loss-2 is untrustworthy (the optimizer
  must treat monotonicity/endpoint as void before feeding the gate). Non-confound topics:
  this gate is a no-op.
- **loss2.schema.json** (co-located; required, additionalProperties:false): `tau:number
  [-1,1]`, `monotonicity_pass:bool`, `endpoint_separation_pass:bool`, `rigor_floor_flag:bool`,
  `pairwise_log:[{i:int, j:int, winner:int, reason:str(non-empty)}]`. pairwise_log i/j/winner
  un-shuffled to real ids before write. **The optional `calibration_handoff` /
  `confound_flat_pass` fields are NOT in the schema** (ponytail must-fix: STAGE-5 behaviors,
  read by no one / validated by no one now; the concept lives in prose; promote to required
  only when §gate actually reads them at STAGE 5).
- **Downstream:** `gate_eval.py topic` consumes `monotonicity_pass`→`--mono`,
  `endpoint_separation_pass`→`--endpoint`; tau/rigor_floor_flag/pairwise_log are for the
  optimizer + replay.
- **Local checks:** leak-audit SKILL.md + loss2.schema.json (W5: D1–D5 only, no 32-check /
  pseudo-good / detection signature); schema self-validation; downstream alignment (bools →
  gate_eval's "true"/"false" string compare); 15-pair / K-count structural checks.
- **STAGE-5-verified:** judge reasons truly use D1–D5 substance (not framing/length), τ true
  value, endpoint K-run stability, z⊥C flatness, 丙-calibration triggering.

## Section 7 — L15 run_codex_loss.py (the last leaf script)

- **Landing:** `skills/optimization-loop/scripts/run_codex_loss.py` (the thick skill's leaf).
  Called loss-1 per-run, loss-2 per-topic. The only STAGE-4 script crossing a real codex
  edge — so the isolation design IS the core.
- **CLI (subcommands, like gate_eval.py):**
  - `loss1`: `--transcript` (de-identified .md from save_transcript), `--config`
    (`configs/<sample>.json`), `--skill-md` (injection-fidelity/SKILL.md path), `--out`
    (`runs/<id>/loss/<sample>.loss1.json`).
  - `loss2`: `--triples` (6 `triples/<sample>.json`, id0..id5), `--intended-order`
    (`id0,…,id5` high→low), `--skill-md` (ladder-quality-order/SKILL.md), `--out`
    (`runs/<id>/loss/<topic>.loss2.json`), `--seed` (shuffle seed; fixed in tests for
    reversibility).
  - Does NOT touch `--logs-dir` — the input transcript is already de-identified by
    save_transcript; this script never reads CC logs (privacy edge is clean by construction).
- **Schema path (ponytail must-fix):** `Path(__file__).parent / "loss{1,2}.schema.json"` —
  the schema is the SCRIPT's contract, so a copy lives beside run_codex_loss.py, NOT derived
  from `--skill-md` (avoids coupling the executable's schema-find to a doc's location, and the
  parents[N] brittleness). The loss skills also co-locate their authoritative schema; the
  script-side copy is the one the script reads.
- **Payload assembly:** loss1 = injection-fidelity SKILL.md full text + de-identified
  transcript + config. loss2 = ladder-quality-order SKILL.md full text + the shuffled 6
  (graph,result) (sample_id/config dropped → blind), harness records `perm: pos→sample_id`,
  dumps to `runs/<id>/loss/<topic>.perm.json` (reversible). Endpoint K judgments = K
  independent codex_fn calls on (id0,id5).
- **codex edge isolation (no-fake-stub red line):** `codex_fn(payload, schema_path) -> raw_str`
  default = `_default_codex_call` (real `codex exec --output-schema <schema> -o <tmp>
  <payload>`, cwd=/workspace/work/loss, config=/workspace/home/loss/.codex). Local tests
  **inject a fake codex_fn returning fixture JSON, whose ONLY purpose is verifying harness
  plumbing** (payload keys, unshuffle∘shuffle==id, known-permutation τ, disk path). The fake
  is a stub at the network boundary, NOT a fake-stub of the judgment. **Forbidden line (pinned
  in tests, ponytail must-fix): no local test may assert a gate outcome (fidelity_rate≥0.90,
  monotonicity_pass, endpoint_separation_pass) from canned codex output.** `_default_codex_call`
  never executes locally; its real-flag correctness is explicitly on the STAGE-5 list.
- **Parse + validate + land:** no `jsonschema` dependency (ponytail-confirmed: ladder-foundry
  is dep-free through STAGE 3; a minimal validator over required-keys + top-level-type is the
  lazier correct choice; full JSON-Schema validation = STAGE-5 optional). Bad JSON → loud,
  NOT silent: degrade-to-disk (`{...pass:false, parse_error:...}`) + `sys.exit(2)` so the
  optimizer SEES the broken loss rather than mis-reading it as a pass.
- **Local checks (test_run_codex_loss.py, subprocess):** payload assembly (full SKILL.md +
  blocks), minimal schema validation (required present → ok; missing/wrong-type →
  CodexOutputError), shuffle→un-shuffle reversibility (fixed seed), un-shuffle ranking → real
  id mapping, Kendall τ arithmetic, endpoint K-vote count, landing paths (loss1.json /
  loss2.json / perm.json), bad-JSON → degrade + exit 2 (no crash).
- **STAGE-5-verified:** real `codex exec --output-schema -o` flag combo + version alignment,
  whether real codex output conforms to schema, the loss-1/loss-2 semantic correctness, note
  free-text leak-audit.

## Section 8 — S5 optimization-loop thick skill (the optimizer brain)

The optimizer-cc's "train.py source", hosted by CC not Python. Control flow fully scripted;
the only thin section = §backprop "which weight to change" (the one intelligence point).

- **frontmatter:** `name: optimization-loop` + W5-clean description (must pass leak-audit).
- **§loop:** two-level nesting — LOOP-2 (epoch/batch, runs to convergence) ⊃ LOOP-1 (48-run
  = 8 topic × 6 rung). Each step names the real leaf CLI + the trace event to emit, traced
  against the spine landing table (arch L85–175): epoch → `new_run_id.py --runs-root runs` +
  `run_start`; batch → batch_id = max weights/ number (no +1; cold-start = batch-0) +
  `batch_start` + `gen_configs.py main(out_dir, w)`; per rung → spawn sim → inject config →
  sim spawns exec → inject topic + bias + 2 hard rules (formated-specs/results) → multi-turn
  (`dialogue_turn`) → `save_transcript.py --logs-dir <REQ> …` → `concat_triple.py` →
  `run_codex_loss.py` (loss-1) → `rung_done`; per-topic aggregate → `run_codex_loss.py`
  (loss-2) → `gate_eval.py topic` → `topic_done` → `write_dataset.py` ×6; batch close →
  `gate_eval.py batch` → `batch_done` → `gate_eval.py converged` → T: freeze + `converged` +
  `run_end` / F: §backprop. Strictly per this section, no improvisation.
- **§gate:** delegates to gate_eval.py (pure arithmetic, no CC/codex). per-topic 3-way AND
  (fidelity_rate≥0.90 ∧ monotonicity_pass ∧ endpoint_separation_pass); batch pass_ratio≥0.80
  hard integer line ≥7/8; converged = trace-tail recent_ratios last-3 all ≥0.80. Thresholds:
  **points back to `gate_eval.FIDELITY_MIN`/`BATCH_RATIO_MIN` module constants (single source
  of truth, does NOT copy)**; new thresholds live in references/gate-thresholds.md. check-blind:
  reads only fidelity_rate + τ/endpoint, never PG/NG/32-check. rigor_floor_flag is an
  orthogonal alarm, NOT in the AND.
- **§backprop (the thin section, attribute-first):**先归因再动手, one batch changes ONE
  weight. Decision table — loss-1 fail → ①axis_prose; loss-2 endpoints-not-separated → read
  rigor_floor_flag first (true → alarm, do NOT touch ② [coords frozen_label-locked, training
  ② is a no-op]; false → ①axis_prose id0/id5 cells); loss-2 middle-collision (τ<0.7 but
  endpoints separated) → ②interp_params (knobs ∈ {collision_offset_axis [B1/expression only],
  endpoint_spread, granularity_map}); ≥4/8 double-collapse → ③assembler_params. Priority:
  loss-1 > loss-2 subtype-B > whole-card. z⊥C-not-flat is a pre-gate: don't change weights on
  that topic's loss-2 this batch. Attribution reads 3 layers coarse→fine (batch_done →
  topic_done → loss/*.json verdicts), stops when decided. Execution: attribution is a CC
  decision (no script); then `apply_weight_update.py … --target --key --new --reason` (F2,
  auto revision_log) or `--copy` (F1, no log, when deciding NOT to change). **New axis_prose
  text passes leak_audit before commit.** W5: reads only fidelity/τ/endpoint + codex verdicts,
  never 32-check/PG-NG. Detail → references/backprop-heuristic.md.
- **§state:** "Memory is not trustworthy; disk is the only source of truth." Three persisted
  artifacts: trace.jsonl / weights/<batch>.json / revision_log.jsonl. Each batch end:
  `/compact` + reload this skill + recover from disk (read weights/<batch+1>.json [new
  weights for gen_configs], revision_log.jsonl [change history], trace.jsonl tail
  [recent_ratios + batch_id + last seq → +1 continuation]). Privacy: trace transcript_path is
  relative; save_transcript.py --logs-dir required, no default. frozen_label lock verified
  unchanged after recovery (weights.revise("frozen_label",…) raises).
- **§tools:** leaf registry via relative anchor `../../scripts/<name>.py` +
  `../../generator/gen_configs.py` (D1: leaves NOT moved; gen_configs is `main(out_dir, w)`,
  non-argparse; M1 collision annotated as a STAGE-5-prerequisite STAGE-2 patch). Only own leaf
  = `scripts/run_codex_loss.py`. Child-CC launch (3 iron rules): parent CC directly runs
  `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role> bash -lc 'cd <cwd> && claude'` in its own Bash tool;
  no driver script / no PTY; no tmux for children (tmux only for the optimizer itself);
  fresh sim/exec each run (between-run independence, only optimizer continuous);
  authoritative transcript = exec session jsonl. **NO `-p`/`--resume`/`--session-id`/
  `--allowedTools` anywhere (not even in the design text).** 4 role config-dirs: optimizer
  /workspace/home/optim/.claude (this skill + superpowers) · sim /workspace/home/sim/.claude
  (superpowers only, persona injected) · exec /workspace/home/exec/.claude (771 DARE +
  formated-specs/results + superpowers) · codex /workspace/home/loss/.codex (2 loss skills).

## Section 9 — S6 references (gate-thresholds.md + backprop-heuristic.md)

- **gate-thresholds.md (new thresholds only):** opening hard statement — `fidelity≥0.90` and
  `batch pass_ratio≥0.80` are NOT here; the single source of truth is gate_eval.py's
  FIDELITY_MIN/BATCH_RATIO_MIN module constants; this doc points back, never copies the
  numbers (prevents a second truth source). New entries (the ONLY home for these — the loss
  skills point back, do NOT inline the digits): F8 turn_budget, loss-2 τ line 0.7, 丙 line
  0.8, K, endpoint allowance, drift ε. check-blind (no 32-check/PG-NG).
- **backprop-heuristic.md:** the §backprop thin section expanded line-by-line —
  `discriminant(signal reading) → fix template(data-oriented wording) → priority`. 5 lines +
  the z⊥C pre-gate, matching §8's table. Stresses the 3 disciplines: attribute-first /
  single-variable (one weight per batch) / loss-2 must split subtype first (endpoints-not-
  separated must NOT train the interpolator — coords are frozen_label-locked). Numeric limits
  reference gate-thresholds.md, not repeated. check-blind: attribution input list is only
  fidelity/τ/endpoint/codex-verdict.

## Section 10 — Honest verification ledger (local now vs STAGE-5)

| Local this stage (must all go green) | STAGE-5-verified (honestly marked unverified, never faked) |
| --- | --- |
| 5 SKILL.md + 2 references all pass leak-audit (W5) | codex semantic verdicts (loss-1 signal extraction / loss-2 ranking) |
| formated fence red/green against concat_triple | §loop full 48-run orchestration end-to-end |
| both loss output schemas validate | §state /compact disk-recovery actually resumes |
| run_codex_loss payload + minimal schema + shuffle reversibility + Kendall τ + landing path + bad-JSON-no-crash | child-CC direct launch + DONE handshake |
| §tools leaf names/CLI match real scripts/ (grep + argparse introspection, a real assertion — ponytail must-fix, NOT a prose read) | §backprop real attribution correctness |
| thresholds point-back-not-copy (grep includes the new literals τ/0.8/K/allowance/ε, not just 0.90/0.80) | run_codex_loss real codex flag combo |
| §backprop target/key match weights.TRAINABLE + INTERP_KEYS | — |
| word audit: no -p/--resume/--session-id/--allowedTools/drive_cc/pexpect/PTY in any artifact | — |
| privacy: save_transcript --logs-dir required; transcript_path relative | — |

## Section 11 — Tasks (one artifact ≈ one task ≈ one commit)

7 tasks. The 5 prompt artifacts: author → leak-audit green → (loss skills) schema validate →
(formated) fence contract red/green → commit. L15: TDD subprocess (red → green) the plumbing,
codex edge behind injectable codex_fn. S5/S6 author + structural checks (C1–C9).

- **T1 formated-specs/formated-results** (S1+S2, one task — paired contract, tested together
  by test_formated_contract.py against concat_triple).
- **T2 injection-fidelity** (S3: SKILL.md + loss1.schema.json + leak-audit + schema +
  band/matrix checks).
- **T3 ladder-quality-order** (S4: SKILL.md + loss2.schema.json, optional fields OMITTED +
  leak-audit + schema + downstream alignment).
- **T4 run_codex_loss.py** (L15: subprocess TDD plumbing, injectable codex_fn, no-fake-stub
  forbidden-line pinned, schema beside script).
- **T5 optimization-loop SKILL.md** (S5: five sections, leaf relative anchors, child-launch
  iron rules, §backprop table).
- **T6 references** (S6: gate-thresholds.md point-back + new thresholds; backprop-heuristic.md).
- **T7 wrap:** full-suite regression (STAGE 1+2+3+4 green); privacy grep (3 log-path
  signatures: Windows / POSIX / cwd-slug) over skills/ + tests/; W5 leak-audit sweep over all
  5 SKILL.md + 2 references; word audit (no banned flags / drive_cc / PTY anywhere); threshold
  point-back grep; update progress ledger + CLAUDE.md status.

Order follows S1→S6 + L15 for a clean review narrative. T1 is the contract the delivered
concat_triple pins; T4 carries the no-fake-stub red line; T5 carries the brain.

## Section 12 — Constraints carried (every task)

- **W5 leak boundary:** generation + loss skills check-blind — never see 32-check /
  6-primitive / detection signatures. optimizer attribution reads only fidelity/τ/endpoint +
  codex verdicts; new axis_prose passes leak_audit. The probe is the ONLY check-seeing session.
- **Privacy red line:** save_transcript --logs-dir required, no default; no CC log absolute
  path / cwd-slug in any committed artifact; trace transcript_path relative; committed outputs
  de-identified; API key VALUES never committed. T7 greps to confirm.
- **NO `-p`/`--resume`/`--session-id`/`--allowedTools` anywhere** (not even design text). All
  three CC layers are normal interactive REPLs.
- **Child-CC launch:** parent CC directly runs `claude` in its own Bash; no driver script / no
  PTY / no tmux for children (tmux only for the optimizer). Fresh sim/exec each run
  (between-run independence); only optimizer continuous. Authoritative transcript = exec jsonl.
- **Data-oriented invariant:** training edits weights JSON data segments only; `.py` sources
  never move; frozen_label LOCKED (enforced by weights.revise); collision_offset_axis ∈
  {B1, expression} only. One weight changed per batch (先归因再动手).
- **no-fake-stub:** run_codex_loss codex edge never fake-stubbed to green; local tests verify
  plumbing only, semantic judgment deferred to STAGE 5.
- **4-layer DARE invariant + D1–D5-only** (academic standards novelty/baseline/rigor/citations/
  publishability FORBIDDEN as judging criteria); 1 thick + 4 light skill structure;
  Write/Edit < 13000 chars; commit only when asked, trailer `Co-Authored-By: Claude Opus 4.8
  <noreply@anthropic.com>`.
- **D1 (leaves not moved, relative anchors) + M1 (gen_configs collision annotated not fixed)**
  are declared deviations, not defects.
