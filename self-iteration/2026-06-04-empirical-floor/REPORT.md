# Phase 1 — Empirical Floor: Findings & Verdict

> DARE's first executable self-analysis. Source design:
> `../../docs/superpowers/specs/2026-06-04-phase1-empirical-floor-design.md`.
> All numbers below are produced by the scripts in `scripts/` against the live
> 771-skill body and the local Claude Code logs; regenerate with the commands in
> `README.md`. Telemetry input paths are never committed.

## TL;DR

- The body parses cleanly into a **756-node, 1430-edge** forward call graph once
  three real-world frontmatter encoding variants are handled (UTF-8 BOM,
  comma-joined scalar lists, dict-form `dependencies`).
- The completeness map labels **709 in-use / 47 suspect-redundant / 0 unknown**
  — but "suspect-redundant" here means *no frontmatter caller edge and never
  observed firing*, NOT "deletable." The 47 are concentrated in prose-routed
  entry points (the orchestrator, `cold-start`/`hot-start`, north-star SOPs).
- Telemetry coverage is thin **by design** (cold-start): only **19 distinct
  skills** fired across the observed sessions, and most are *build-time* tooling
  (`superpowers:*`, `skill-creator`), not DARE's own research skills. This is
  Constraint B made concrete — existing logs are "building DARE," not "DARE
  doing research."
- **eval-anchor probe: Krippendorff α = 1.00**, anchor discriminating (3 planted
  fabrications all caught by 3 independent raters). Both pre-registered gate
  conditions met. → **Study 4-v2: GO.**

---

## N1 — Structure

### Forward graph (`data/forward_graph.json`)

| Metric | Value |
|--------|-------|
| Nodes (parseable skills) | 756 |
| Edges (forward call relations) | 1430 |
| Dangling targets | 10 |

Edge provenance (the graph is richer than the spec's "reversed used-by + ~90
dependencies" — the 4-layer architecture contributes three more edge classes):

| Source | Edges | Meaning |
|--------|------:|---------|
| `used-by` (reversed) | 1002 | child declares parent → parent→child edge |
| `sops` | 176 | strategy/tactic forward-calls its SOP |
| `tactics` | 95 | strategy forward-calls its tactic |
| `dependencies` | 95 | skill declares an explicit dependency |
| `campaign` | 62 | campaign orchestrates a member skill |

### Dangling targets (completeness finding, not a bug)

All 10 are genuine references to nodes that have **no `SKILL.md` of their own**:

- **Pipeline phases** (referenced via `used-by`/`campaign`, but phase-level, not
  a skill file): `convergence`, `creative-ideation`, `deep-insight`,
  `knowledge-acquisition`, `knowledge-acquisition (pre-condition)`, `validation`.
- **Infrastructure repos** (declared as `dependencies` but living in separate
  repos): `context-management`, `literature-engine`, `subagent-spawning`,
  `web-browsing`.

These are real cross-phase / cross-repo edges the single-repo parse cannot
resolve — exactly the kind of structural incompleteness N1 is meant to surface.

### Blast radius (`data/blast_radius.json`)

Top transitive-caller counts ("if this changes, how many skills are affected"):

| Skill | Impact set size |
|-------|----------------:|
| `subagent-spawning` | 68 |
| `context-management` | 20 |
| `literature-engine` | 19 |
| `web-browsing` | 15 |
| `metric-specification` | 12 |
| `consistency-pair-evaluation` | 11 |
| `evaluation-filtering` | 11 |
| `idea-synthesis` | 11 |

The four infrastructure SOPs dominate — touching `subagent-spawning` ripples to
68 skills. This is the ablation-roadmap warning the design called for: know the
blast radius before editing anything.

### Completeness / confidence map (`data/completeness_map.json`) — headline

| Label | Count | Rule |
|-------|------:|------|
| `in-use` | 709 | has an incoming forward edge **or** observed firing |
| `suspect-redundant` | 47 | no incoming edge **and** telemetry present **and** never fired |
| `unknown` | 0 | (would apply only if telemetry were absent) |

**This is NOT a pruning verdict.** The 47 "suspect-redundant" skills are not
deletion candidates — they are *flags for review*. Their execution-type
breakdown explains why they have no caller edge:

| execution type | count among the 47 |
|----------------|-------------------:|
| (none declared) | 22 |
| `dialogue` | 10 |
| `subagent` | 9 |
| `import` | 4 |
| `sequential` | 1 |
| `reference` | 1 |

They cluster in **north-star-crystallization**: the top orchestrator
`de-anthropocentric-research-engine`, the strategy entry points
`cold-start`/`hot-start`, and the `ask-*` / `crystallize-*` / `generate-*` SOPs.
These are invoked by **strategy prose** ("invoke cold-start") rather than by a
frontmatter `used-by`/`tactics`/`sops` edge — so the graph genuinely records no
incoming edge, even though they are demonstrably used. This is the design's core
warning made concrete: **"no recorded caller ≠ provably unused."** The
reconstruction cannot see prose-level routing; closing that gap is future work
(N2 emission-by-construction), not a Phase-1 prune list.

## N6 — Telemetry (`data/telemetry.json`)

> Disclaimer (carried in the artifact): firing counts are a snapshot of the
> observed ecosystem. **Low/zero frequency ≠ redundant.** This is NOT a pruning
> verdict.

- Distinct skills observed firing: **19**. Co-occurrence pairs: **39**.
- Top fired skills:

| Skill | Invocations |
|-------|------------:|
| `superpowers:brainstorming` | 8 |
| `superpowers:writing-plans` | 3 |
| `skill-creator:skill-creator` | 2 |
| `superpowers:executing-plans` | 1 |
| `superpowers:subagent-driven-development` | 1 |
| `literature-overview` / `literature-search` / `literature-research` | 1 each |

**Key observation (Constraint B confirmed):** the most-fired skills are
*build-time meta-tooling* (the superpowers + skill-creator plugins used to
**construct** DARE), not DARE's own 771 research skills. Of the body itself,
only a handful (the `literature-engine` SOPs, `context-*`, north-star synthesis)
have fired at all. The existing logs are "building DARE" sessions, not "DARE
doing research" traces. Any firing-based redundancy claim at this coverage would
conflate "never needed yet" with "useless" — hence every non-fired skill rests
on its static edge alone.

## Study 1a — Conformance contract (`data/conformance_contract.md`)

Distribution of the `execution` field over the 756 parseable skills:

| Class | Count | Implied runtime requirement |
|-------|------:|------------------------------|
| `subagent` | 363 | spawn isolated sub-agent, recover structured output |
| `missing` | 225 | none declared — mode implied by parent (see note) |
| `tactic` | 70 | sequence SOPs, aggregate outputs |
| `strategy` | 50 | orchestrate nested tactics with budget/gate tracking |
| `campaign` | 25 | drive end-to-end multi-strategy pipeline w/ phase state |
| `dialogue` | 10 | multi-turn interactive Q&A with the user |
| `sequential` | 7 | ordered in-process steps, no sub-agent spawn |
| `import` | 5 | resolve and inline an external/source skill |
| `reference` | 1 | read-only material, not executable |

**Heaviest requirement:** sub-agent spawn + structured-output recovery dominates
(363 skills). A conforming runtime *must* support nested sub-agent orchestration
to run DARE at all. **Conformance gap:** 225 skills (~30%) declare no `execution`
field; their run mode is inferable only from the parent layer, so a runtime
cannot statically determine how to execute ~30% of the body from frontmatter
alone — a concrete target for a future frontmatter-completion pass.

## Parse fidelity (`data/skills_model.json`)

771 files scanned, **756 parsed, 15 recorded as `parse_error`**. The 15 are
genuinely malformed YAML (unquoted `description:` values containing `: `, e.g.
`Budget: 40 studies`, which strict YAML reads as a nested mapping). Per the
design contract they are recorded as data, not crashed on. Three *other*
real-body variants were handled in-parser via TDD rather than dropped:

- **UTF-8 BOM** before `---` (24 files) — would have been mis-flagged as
  "no-frontmatter"; now stripped.
- **Comma-joined scalar list fields** (~145 files: `used-by: a, b, c`) — would
  have collapsed many edges into one bogus node; now split. Recovered ~360 edges
  and cut dangling targets from 119 → 10.
- **Dict-form `dependencies`** (`{skills: [...], mcp: {...}}`, 65 files) — the
  `skills:` entries are real edges; `mcp:` names external servers (excluded).

## eval-anchor feasibility probe (the kill-switch)

**Question (design §eval-anchor):** in DARE's non-verifiable open-task region,
can an evaluation anchor reach *usable* inter-rater reliability — or does the
anchor degrade and fake success (Failure Mode B)?

**Pre-registered threshold (fixed before scoring):**
1. usable reliability = **Krippendorff's α ≥ 0.67** on the anchored items, AND
2. the external anchor must **remain discriminating** — raters must disagree
   with the anchor on ≥1 item; if every item scores identically the anchor is
   not testing anything.

**Objects scored:** citation claims extracted from the North Star self-evolution
review (`context/2026-06-04-17-17-dare-self-evolution-review.md`). **External
anchor:** "Is this a real, independently-verifiable publication whose
author/title/venue/year are mutually consistent?" — a hard, checkable fact, not
a quality judgement. **Raters:** 3 independent agents, blind to one another, web
search permitted.

**Round 1 (8 items, all drawn verbatim from the review).** All 3 raters scored
all 8 items = real. Notably the two future-looking arXiv IDs the review flagged
as "safe anchors" (`arXiv:2508.06433` Memp; `arXiv:2604.04323` agentic-skills)
*are* genuine. Result: **zero variance → α undefined (Do/De = 0/0), and the
discrimination condition fails.** A probe whose item set contains no true
negative cannot measure reliability. Per the design ("disagree wildly / anchor
unscorable is a *result*"), this triggered a corrected round rather than a
declared pass — itself the Failure-Mode-B guard working.

**Round 2 (10 items: 7 real review citations + 3 deliberately fabricated,
raters blind to which).** The 3 planted fabrications:
- "Karpathy et al. (2019), Transformer-based change impact analysis for Rust, OOPSLA"
- "Nakamura et al. (2021), SkillGraph: dependency reconstruction…, ICSE"
- "Lee & Petrov (2022), Krippendorff-alpha bounds for LLM-as-rater panels, EMNLP"

All 3 raters independently produced the **identical** score vector and caught
**exactly** the 3 fabrications, passing all 7 real citations.

| Metric | Value |
|--------|-------|
| Raters × items | 3 × 10 |
| Per-item unanimous agreement | 10 / 10 |
| Observed disagreement Dₒ | 0.0000 |
| Expected disagreement Dₑ | 0.4345 (7 true-pos, 3 true-neg → real variance) |
| **Krippendorff's α** | **1.0000** |
| Anchor discriminating? | **Yes** — 3/3 fabrications detected, Dₑ > 0 |

## VERDICT — Study 4-v2

- [x] **GO** — probe passed → proceed to Phase 2 (procedural memory / Study 4-v2)
- [ ] NO-GO — probe failed → Study 4-v2 downgraded → skip to Phase 3 (N2 + 3-low)

**Rationale (traceable to the α number):** Both pre-registered conditions are
met — α = 1.00 ≥ 0.67, and the anchor discriminated (all 3 planted fabrications
caught, Dₑ = 0.43 > 0). In DARE's region, an *external-fact* anchor (does the
cited work exist?) reaches ceiling reliability across independent raters. This
does **not** claim that *quality* judgements are reliable — only that a hard,
checkable anchor is feasible and resists the Failure-Mode-B degradation the
probe was built to catch. The lesson from Round 1 is carried forward as a
binding design rule for Study 4-v2: **every reliability claim must include known
true-negatives, or α is undefined and "perfect agreement" is an artifact of an
all-positive item set, not evidence of a working anchor.**

---

## Scope honesty

What Phase 1 did **not** do (deferred by design, not skipped silently): no
pruning/merging/editing of any skill; no `.jsonl` cleaning pipeline / trace
classifier (that is N2); no call-sequence reconstruction from logs (Study
3-high); nothing under `skills/` was modified. Telemetry coverage is one
ecosystem snapshot, not a usage census. The 47 "suspect-redundant" and 15
parse-error skills are review flags, not verdicts.
