---
name: destructive-ideation
description: "Break fixation by surfacing assumptions and applying deliberate provocation modes (reversal, negation, random entry, exaggeration, extreme/zero-resource constraint, distortion), then extract constructive movement and synthesize candidate directions."
---

# destructive-ideation
## Purpose
Break fixation with explicit provocation modes, then extract constructive movement and candidate directions.
## Input contract
```yaml
required: [current_frame, target_problem]
optional: [mode, load_bearing_assumptions, constraints]
constraints: [provocation must name the frame or assumption it attacks]
```
## Execution protocol
1. Surface assumptions (`surface-assumptions`).
2. Generate a deliberate provocation (`generate-provocation`).
3. Extract constructive movement (`extract-constructive-movement`).
4. Synthesize an idea (`synthesize-idea`).
5. Expand the concept fan (`build-concept-fan`).
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
produces: [assumption_targets, provocations, constructive_movements, idea_set, concept_fan]
delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, recommended_jumps]
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
