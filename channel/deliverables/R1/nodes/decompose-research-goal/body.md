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

1. Formalize the top goal and desired effect (`formulate-top-goal`).
2. Recursively construct AND/OR branches and executable leaves (`decompose-and-or-goal`).
3. Check leaf specificity, testability, coverage, and dependency consistency (`validate-goal-tree`).
4. Annotate feasibility and alternatives (`assess-goal-feasibility`).
5. Map dependencies and compress the result into a North Star (`map-dependencies`, `crystallize-north-star`).

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
| none retained | — | — | No source numeric/textual criterion retained after normalization. |

## Context checkpoint / Delta notes

Append the goal DAG, leaf validation, feasibility annotations, dependency changes, and unresolved validation questions.
