---
name: problem-reframing
description: "Change the problem representation when the current frame is limiting: dominant-frame escape, stakeholder/worldview rotation, forced perspective shifts, dialectical/polarity reframing, or abstraction/scope shifts."
---

# problem-reframing
## Purpose
Change a limiting problem representation through frame escape, perspective rotation, polarity, or abstraction/scope shifts.
## Input contract
```yaml
required: [problem_statement, current_frame]
optional: [stakeholders, assumptions, reframe_mode]
constraints: [each reframe states what changed and what remains invariant]
```
## Execution protocol
1. Identify the dominant frame (`identify-dominant-frame`).
2. Generate a targeted provocation (`generate-provocation`).
3. Derive consequences (`derive-consequences`).
4. Assess wickedness (`assess-problem-wickedness`).
5. Apply appreciative reframe (`appreciative-reframe`).
6. Construct perspectives (`construct-perspective-set`).
7. Rotate perspectives (`rotate-perspective`).
8. Map productive polarity (`map-productive-polarity`).
9. Adjust abstraction/scope (`adjust-abstraction-scope`).
10. Map disagreement (`map-disagreement`).
Deviation: mode selects a subset, but every omitted operation must be justified by the declared reframe mode and input.
## Mode branches
- `dominant-frame-escape`: identify and challenge the frame governing the current question.
- `perspective-shift`: rotate explicit reviewer, practitioner, theorist, time, or novice views.
- `stakeholder/worldview`: reframe around stakeholder interests and lived assumptions.
- `polarity`: expose productive opposition and map its consequences.
- `abstraction-scope`: move up/down the abstraction or scope ladder and preserve invariants.
## Output contract
```yaml
produces: [dominant_frame, reframe_set, consequence_map, perspective_map, polarity_map]
delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, open_questions, recommended_jumps]
```
## Thresholds and quality gates
- B: at least two materially distinct frames are recorded; invariants, changed assumptions, and downstream consequences are explicit.
## Failure and counterexamples
Reject cosmetic wording changes, perspective lists without consequence changes, and reframes that erase the original decision target.
## Provenance map
- `problem-reformulation`, `dominant-idea-escape`, `multi-perspective-reframing`, `dialectical-reformulation`, `question-reformulation`, `creative-ideation/perspective-forcing`, `six-thinking-hats`, `role-storming`, `perspective-rotation`, `synectics/personal-analogy`, `Pass8/force-perspective-shift`: resolved/concept per exact lookup.
- Status: `problem-reformulation`, `dominant-idea-escape`, `multi-perspective-reframing`, `dialectical-reformulation`, `question-reformulation`, `creative-ideation/perspective-forcing`, `synectics/personal-analogy` resolved; `six-thinking-hats`, `role-storming`, `perspective-rotation`, `Pass8/force-perspective-shift` concept.
## Preserved source criteria ledger
- Preserve Six Hats, synectics/personal analogy, dialectical polarity, dominant-frame escape, and abstraction/scope shifts.
## Context checkpoint / Delta notes
Append frame changes, perspective consequences, polarity tensions, and selected reframe.
