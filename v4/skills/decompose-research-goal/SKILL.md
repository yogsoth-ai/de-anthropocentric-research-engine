---
name: decompose-research-goal
description: "Turn a research direction into an AND/OR goal DAG with testable leaves, dependency structure, and feasibility annotations."
---

# decompose-research-goal

## Purpose

Turn a research direction into an AND/OR goal DAG with testable leaves, dependencies, and feasibility annotations.

## Input contract

```yaml
required: [research_direction, constraints]
optional: [actor_profile, obstacle_report, timeline, north_star]
constraints: [goal wording, constraints, and source context must be explicit]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `formulate-top-goal` to formalize the top goal and desired effect.
2. You MUST load skill `decompose-and-or-goal` to recursively construct AND/OR branches and executable leaves.
3. You MUST load skill `validate-goal-tree` to check leaf specificity, testability, coverage, and dependency consistency.
4. You MUST load skill `assess-goal-feasibility` to annotate feasibility and alternatives.
5. You MUST load skill `map-dependencies` to map the goal dependencies. You MUST load skill `crystallize-north-star` to compress the result into a North Star.

Deviation: Omit feasibility annotations when no actor, resource, or timeline constraints are supplied; mark the tree provisional rather than inventing constraints. Re-run only the affected branch after a decision changes its parent goal.

## Output contract

```yaml
produces: [goal_tree_dag, executable_leaves, dependency_map, feasibility_annotations, research_north_star]
delta_fields: [findings, hypothesis_updates, decisions, uncertainties, open_questions]
```

## Thresholds and quality gates

- Every leaf must be testable or executable and trace to a parent goal.
- AND/OR semantics must be explicit; unresolved feasibility remains an uncertainty.
- Completion requires coverage of the declared top goal, not a fixed leaf count.

## Failure and counterexamples

Reject trees with circular dependencies, vague leaves, or branches that cannot be tied to the declared direction. Do not treat a polished sentence as evidence that decomposition is complete.

## Provenance map

- `resolved: goal-decomposition`
- `resolved: north-star-crystallization-formulate-top-goal`
- `resolved: north-star-crystallization-and-or-decompose`
- `resolved: north-star-crystallization-validate-leaves`
- `resolved: north-star-crystallization-feasibility-check`
- `resolved: north-star-crystallization-ask-decomposition-validation`

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| none retained | - | - | No source numeric/textual criterion retained after normalization. |

## Context checkpoint / Delta notes

Append the goal DAG, leaf validation, feasibility annotations, dependency changes, and unresolved validation questions.
