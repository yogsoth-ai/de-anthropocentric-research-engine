---
name: validate-goal-tree
description: "Check leaf specificity, testability, coverage of the parent goal, logical completeness, and dependency consistency."
---

# validate-goal-tree

## Purpose

Check leaf specificity, testability, coverage of the parent goal, logical completeness, and dependency consistency.

## Input contract

```yaml
required: [goal_dag, top_goal, validation_criteria]
optional: [actor_profile, constraints, feasibility_annotations]
constraints: [each validation judgment cites the affected node and criterion]
```

## Procedure

1. Check that every leaf is observable or executable and traces to the top goal.
2. Verify AND/OR semantics, dependency direction, and absence of cycles.
3. Check coverage, feasibility annotations, and unresolved branches against the declared constraints.
4. Return node-level revisions and a validation summary without silently repairing the graph.

## Output contract

```yaml
produces: [leaf_validation, coverage_assessment, dependency_audit, feasibility_gaps, validation_summary]
delta_fields: [findings, decisions, uncertainties, open_questions]
```

## Quality gates

- Every failed criterion identifies a node and reason.
- A complete-looking tree cannot pass with untestable leaves or circular dependencies.

## Failure and counterexamples

Do not validate a tree because its prose is polished, and do not infer missing feasibility constraints.

## Provenance map

- `resolved: north-star-crystallization/validate-leaves`
- `resolved: ask-decomposition-validation`
