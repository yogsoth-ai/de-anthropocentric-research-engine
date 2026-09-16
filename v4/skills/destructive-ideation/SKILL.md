---
name: destructive-ideation
description: "Break fixation by surfacing assumptions and applying deliberate provocation modes (reversal, negation, random entry, exaggeration, extreme/zero-resource constraint, distortion), then extract constructive movement and synthesize candidate directions."
---

# destructive-ideation
## Purpose
Break fixation with explicit provocation modes, then extract constructive movement and candidate directions.
## Input contract
```yaml
mode_contracts:
  reverse: &destructive_input
    required: [current_frame, target_problem]
    optional: [load_bearing_assumptions, constraints]
    constraints: [provocation_must_name_the_frame_or_assumption_it_attacks]
  negation: *destructive_input
  random-entry: *destructive_input
  extreme-constraint: *destructive_input
  sacred-cow: *destructive_input
  distortion: *destructive_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `surface-assumptions` to surface assumptions.
2. You MUST load skill `generate-provocation` to generate the mode-specific provocation.
3. You MUST load skill `extract-constructive-movement` to extract constructive movement.
4. You MUST load skill `synthesize-idea` to synthesize an idea.
5. You MUST load skill `build-concept-fan` to expand the concept fan.
   If the idea now requires explicit component transformation, consider `structural-transformation`. If it exposes a technical or physical contradiction, consider `resolve-inventive-contradiction`.
Deviation: mode may be reverse, negation, random-entry, extreme-constraint, sacred-cow, or distortion; record the selected mode.
## Mode branches
- `reverse`: invert the current desired/undesired relation.
- `negation`: negate a load-bearing assumption or axiom.
- `random-entry`: introduce an explicitly recorded external/random concept.
- `extreme-constraint`: force zero-resource or boundary conditions.
- `sacred-cow`: challenge an explicitly protected convention.
- `distortion`: exaggerate, compress, or otherwise perturb a salient feature.
## Output contract
```yaml
mode_contracts:
  reverse: &assumption_attack_output
    produces: [assumption_targets, provocations, constructive_movements, idea_set]
    delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, recommended_jumps]
  negation: *assumption_attack_output
  random-entry: &provocation_output
    produces: [provocations, constructive_movements, idea_set]
    delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, recommended_jumps]
  extreme-constraint: *assumption_attack_output
  sacred-cow: *assumption_attack_output
  distortion: *provocation_output
```
## Thresholds and quality gates
- B: selected mode is explicit; each provocation has a constructive movement; candidate ideas retain a trace to the attacked frame.
## Failure and counterexamples
Reject unbounded randomness, provocation without a target, and ideas that cannot state what constructive movement they preserve.
## Provenance map
- `assumption-destruction`, `axiom-negation`, `provocation-and-movement`, `provocation-generation`, `movement-extraction`: resolved/concept per exact v3 lookup.
- Status: `assumption-destruction`, `axiom-negation`, `provocation-and-movement`, `movement-extraction` resolved; `provocation-generation` concept (only package-prefixed variants found).
## Preserved source criteria ledger
- Preserve reversal, negation, random entry, exaggeration/extreme constraint, distortion, and movement extraction.
## Context checkpoint / Delta notes
Append mode, attacked assumptions, provocations, movements, and selected directions.
