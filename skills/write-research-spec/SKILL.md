---
name: write-research-spec
description: "Convert a confirmed North Star, ResearchBrief, and user constraints into an executable multi-stage Research Spec."
---

# write-research-spec

## Purpose

Convert a confirmed North Star, ResearchBrief, and user constraints into an executable multi-stage Research Spec. The spec is a plan projection over checkpoint events, not a second persistent artifact.

## Input Contract

```yaml
required: [confirmed_north_star, research_brief, user_constraints]
optional: [existing_context, preferred_depth, candidate_tactics]
constraints:
  - North Star must be user-confirmed
  - every stage needs objective, inputs, focus, tactic selection, completion gate, backtrack condition, and execution steps
```

## Execution Protocol

1. You MUST load skill `research-catalog` and select candidate tactics from its 51-item index. Use the cards' `requires` and `produces` fields to test stage fit; do not enumerate SOPs in the Spec.
2. Clarify scope, evidence depth, constraints, and stopping conditions from the user input. Preserve unresolved items as explicit open questions rather than guessing.
3. Draft a 5-10 stage outline. Each stage names a tactic and its research transformation; stage order must follow dependencies and the North Star.
4. For each stage, write: objective, expected input, focus areas, recommended tactic and mode, completion criteria, backtrack condition, and execution steps. Completion criteria must be numeric or objectively verifiable.
5. Present the outline for user confirmation. Incorporate only confirmed changes, then run the self-review gate before presenting the complete Spec for approval.

The Spec must describe tactic/SOP work, not runtime implementation. A tactic returns the eight Delta fields: `findings`, `evidence_updates`, `hypothesis_updates`, `assumption_updates`, `uncertainties`, `decisions`, `open_questions`, and `recommended_jumps`.

## Spec Contract

```yaml
spec_header: [topic, generated_at, north_star, scope, estimated_sessions]
global_sections: [context_protocol, execution_rules, backtrack_conditions]
stage_fields:
  - objective
  - expected_input
  - focus_areas
  - recommended_tactic
  - completion_criteria
  - backtrack_condition
  - execution_steps
```

`SpecView` is reconstructed from the current Phase checkpoint event stream. The spec writer records plan creation and revisions as `decisions` events; it does not introduce a spec file, spec version store, or separate progress ledger.

## Output Contract

```yaml
produces: [research_spec, spec_review_report, user_approval_request]
research_spec:
  - north_star
  - research_brief
  - ordered_stages
  - completion_gates
  - backtrack_conditions
```

## Completion Criteria

- The North Star is explicit and confirmed.
- Every stage has a tactic, required input, objective gate, and backtrack condition.
- All required inputs and expected outputs connect between adjacent stages.
- No completion criterion uses only vague language such as "sufficient" or "adequate".
- Self-review finds no unresolved placeholder, impossible dependency, or unquantified gate.

## Failure and Backtrack

Missing North Star or ResearchBrief blocks spec writing. An unanswerable constraint remains an `open_questions` item and prevents approval of the affected stage. If the user changes the objective, required input, completion gate, or dependency after review, append a new decision and re-run self-review; do not rewrite historical checkpoints.

## Boundary

This skill creates the plan projection used by execution. It does not execute tactics, write scientific findings, or persist a second copy of the plan outside the checkpoint event stream.
