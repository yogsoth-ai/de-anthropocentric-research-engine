# execute-research-spec

## Purpose

Execute the approved Research Spec phase by phase, producing checkpointed research state and a final summary. The execution path is deterministic from the current SpecView and state events.

## Input Contract

```yaml
required: [approved_spec, context_index, phase_context_file]
optional: [latest_checkpoint]
constraints:
  - the target Phase must have exactly one context file
  - a complete checkpoint is required before a phase can be considered complete
```

## Execution Protocol

Before each route, reconstruct the in-memory `SpecView` by replaying the current Phase checkpoint events in sequence. `decisions` are the plan source; `open_questions` annotate existing plan items; the other Delta fields do not alter plan structure unless a decision explicitly references them.

For each phase:

1. Read `context/INDEX.md`, locate the unique Phase context file, validate checkpoint numbering, and load the latest complete checkpoint.
2. Select the first active Spec item whose dependencies are satisfied and whose status is not `complete`.
3. Load only the context and state slice required by that item. You MUST load the selected tactic as a skill; do not perform its research operation inline. The tactic body controls its required SOP calls and scientific thresholds.
4. After the tactic/SOP operation, append one checkpoint containing the eight Delta fields, process, results, status, and open questions. Do not edit earlier checkpoints.
5. Evaluate the current completion gate. Mark the plan item complete only when the gate is objectively satisfied. If it is not satisfied, keep the item active and record the gap.
6. Evaluate the backtrack condition. A triggered condition requires an explicit user decision, recorded as a new `decisions` event, before returning to an earlier stage.

## Checkpoint Contract

Each appended checkpoint contains:

```text
Checkpoint: <unique increasing number>-<UTC timestamp>
Phase: <phase-slug>
Source: <tactic/sop or product layer>
Status: complete | partial
Input slice: <state range read>
Process: <operation performed>
Results: <observed result>
Delta:
  findings: []
  evidence_updates: []
  hypothesis_updates: []
  assumption_updates: []
  uncertainties: []
  decisions: []
  open_questions: []
  recommended_jumps: []
Open questions: <unresolved items>
```

Merge fields by stable keys. Preserve replaced decisions with their replacement reason. Deduplicate recommended jumps by `(target, reason)` and treat them as suggestions, never as permission to bypass a gate.

## Recovery Protocol

On a new session, read `context/INDEX.md`, find the target Phase file and latest checkpoint, replay events to rebuild `SpecView`, and resume at the first incomplete item. If the latest checkpoint is `partial`, read its open questions, return to the latest `complete` checkpoint, and rebuild from there. Check Phase, sequence continuity, and all eight Delta fields before continuing. Do not use scratch text as evidence and do not rerun an item already recorded complete unless a new decision explains why.

## Output Contract

```yaml
produces:
  - appended_phase_checkpoints
  - merged_research_state
  - final_research_summary
delta_fields:
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

Every required Spec item has a complete checkpoint whose completion gate is satisfied, or the final report names the first unmet gate and its supporting evidence. The final summary references all Phase context files and the checkpoints used to derive it.

## Failure and Backtrack

Missing or damaged context, a non-contiguous checkpoint sequence, an absent Delta field, or a missing SpecView source blocks routing and reports the exact location. Conflicting facts or decisions are retained as `uncertainties`; the dependent path remains paused until a user or designated reviewer writes a resolving decision. Execution never substitutes elapsed time, an empty result, or an external interruption for a scientific completion gate.

## Boundary

Persistence is append-only Markdown checkpoints in the existing Phase context file. `SpecView` is an in-memory projection and is never persisted as a second object. This product-shell skill is not a graph node and must not be added to the 267-node registry.
