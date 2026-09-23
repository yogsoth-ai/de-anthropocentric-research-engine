# de-anthropocentric-research-engine

## Purpose

DARE v4 is the product-level orchestrator for a research run. It turns a user request into a controlled sequence of North Star crystallization, executable specification, and phase-by-phase execution. It is not a scientific graph node and must not be counted among the 267 tactic/SOP nodes.

## Input Contract

```yaml
required: [user_request]
optional: [existing_context, north_star, research_brief, constraints]
constraints:
  - a run may start with an existing North Star only when it is explicit and user-confirmed
  - execution requires a current SpecView reconstructed from checkpoint events
```

## Execution Protocol

DARE enforces this order and does not skip a phase:

1. **North Star**: if a confirmed North Star and ResearchBrief are absent, collect and crystallize them from the user request. If they are present, verify that they still describe the request.
2. **Spec**: You MUST load skill `research-catalog` to expose the available tactics. You MUST load skill `write-research-spec` to turn the confirmed North Star, ResearchBrief, and user constraints into an executable Research Spec. Do not execute research while this phase is incomplete.
3. **Execution**: after the user approves the Spec, You MUST load skill `execute-research-spec` to execute its phases and checkpoints. Do not select a tactic directly from the flat skill directory.

At every phase boundary, record the decision and its reason in the current Phase checkpoint event stream. A plan change is an appended `decisions` event, never an edit to an earlier checkpoint. The product shell may present progress, but scientific conclusions remain in tactic/SOP Delta fields.

## Output Contract

```yaml
produces:
  - confirmed_north_star
  - research_brief
  - spec_view
  - phase_execution_results
  - final_research_summary
state_delta_fields:
  - findings
  - evidence_updates
  - hypothesis_updates
  - assumption_updates
  - uncertainties
  - decisions
  - open_questions
  - recommended_jumps
```

## Completion Criteria

- A confirmed North Star and ResearchBrief exist before spec construction.
- The Spec has explicit stages, inputs, tactics, completion gates, and backtrack conditions.
- Execution reaches a complete checkpoint for every required stage, or reports the first unmet gate with its evidence.
- The final summary cites the context files and checkpoints that support it.

## Failure and Backtrack

Missing intent or scope blocks entry to specification and returns `NEEDS_CONTEXT`. An unmet completion gate keeps the current stage active. A triggered backtrack condition is presented for user confirmation and, if approved, is recorded as a new decision before execution returns to the target stage. DARE never treats an empty result, elapsed time, or an execution interruption as stage completion.

## Boundary

This entry layer is installed under `v4/skills/` by the build owner. It is not added to `graph.json`, does not create a third scientific layer, and does not replace tactic or SOP contracts.
