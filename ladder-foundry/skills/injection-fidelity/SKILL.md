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
