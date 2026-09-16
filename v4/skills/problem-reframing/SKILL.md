---
name: problem-reframing
description: "Change the problem representation when the current frame is limiting: dominant-frame escape, stakeholder/worldview rotation, forced perspective shifts, dialectical/polarity reframing, or abstraction/scope shifts."
---

# problem-reframing
## Purpose
Change a limiting problem representation through frame escape, perspective rotation, polarity, or abstraction/scope shifts.
## Input contract
```yaml
mode_contracts:
  dominant-frame-escape: &reframing_input
    required: [problem_statement, current_frame]
    optional: [stakeholders, assumptions]
    constraints: [each_reframe_must_state_what_changed_and_what_remains_invariant]
  perspective-shift: *reframing_input
  stakeholder/worldview: *reframing_input
  polarity: *reframing_input
  abstraction-scope: *reframing_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. Select the reframe mode that matches the declared failure in the current frame.
2. Execute the mode-specific operations below without deleting the original frame or its evidence.
3. Record the transformed frame, derived consequences, invariants, and unresolved disagreement.
   If a reframed question is ready to generate testable explanations, consider `formulate-hypotheses`. If opposing frames require a structured exchange, `adversarial-deliberation` may be the better next tactic.
Deviation: mode selects a subset, but every omitted operation must be justified by the declared reframe mode and input.
## Mode branches
- `dominant-frame-escape`: identify and challenge the frame governing the current question. You MUST load skill `identify-dominant-frame` to identify that frame. You MUST load skill `generate-provocation` to challenge it. You MUST load skill `derive-consequences` to trace the resulting consequences. You MUST load skill `appreciative-reframe` to retain generative strengths while escaping the dominant frame.
- `perspective-shift`: rotate explicit reviewer, practitioner, theorist, time, or novice views. You MUST load skill `construct-perspective-set` to construct the explicit views. You MUST load skill `rotate-perspective` to rotate them. You MUST load skill `map-disagreement` to retain their substantive disagreements.
- `stakeholder/worldview`: reframe around stakeholder interests and lived assumptions. You MUST load skill `construct-perspective-set` to construct stakeholder worldviews. You MUST load skill `rotate-perspective` to apply each worldview. You MUST load skill `assess-problem-wickedness` to assess conflicts that prevent a single stable frame. You MUST load skill `map-disagreement` to preserve unresolved interests.
- `polarity`: expose productive opposition and map its consequences. You MUST load skill `map-productive-polarity` to map the opposing poles. You MUST load skill `derive-consequences` to derive their consequences.
- `abstraction-scope`: move up/down the abstraction or scope ladder and preserve invariants. You MUST load skill `adjust-abstraction-scope` to move the frame while preserving declared invariants.
## Output contract
```yaml
mode_contracts:
  dominant-frame-escape:
    produces: [dominant_frame, reframe_set, consequence_map]
    delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, open_questions, recommended_jumps]
  perspective-shift:
    produces: [reframe_set, perspective_map, consequence_map]
    delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, open_questions, recommended_jumps]
  stakeholder/worldview:
    produces: [reframe_set, perspective_map]
    delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, open_questions, recommended_jumps]
  polarity:
    produces: [reframe_set, consequence_map, polarity_map]
    delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, open_questions, recommended_jumps]
  abstraction-scope:
    produces: [dominant_frame, reframe_set]
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
