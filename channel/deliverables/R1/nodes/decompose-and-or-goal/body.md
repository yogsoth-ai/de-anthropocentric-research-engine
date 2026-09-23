# decompose-and-or-goal

## Purpose

Recursively decompose a goal into an AND/OR DAG whose leaves are executable or testable subgoals.

## Input contract

```yaml
required: [top_goal, constraints]
optional: [actor_profile, obstacle_report, existing_subgoals]
constraints: [branch semantics, dependencies, and leaf criteria must be explicit]
```

## Procedure

1. Split the goal into necessary AND conditions and alternative OR paths.
2. Recurse until each leaf has an observable result or executable action.
3. Attach actors, dependencies, constraints, and unresolved feasibility to each branch.
4. Preserve shared subgoals as DAG nodes rather than duplicating them.

## Output contract

```yaml
produces: [goal_dag, branch_semantics, executable_leaves, dependency_edges, feasibility_questions]
delta_fields: [findings, hypothesis_updates, uncertainties, open_questions]
```

## Quality gates

- Every leaf traces to the top goal.
- AND/OR labels and dependency directions are unambiguous.
- Cycles and duplicate shared nodes are flagged.

## Failure and counterexamples

Do not split prose into labels without changing testability, and do not treat alternatives as simultaneous requirements.

## Provenance map

- `resolved: north-star-crystallization-and-or-decompose`

