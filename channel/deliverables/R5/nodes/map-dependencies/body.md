# map-dependencies

## Purpose

Construct a dependency graph and identify cycles, critical paths, and parallelizable branches.

## Input contract

```yaml
required: [items, dependency_evidence, relation_schema]
optional: [criticality_rule, execution_context, candidate_order]
constraints: [the graph contains at least 2 items when the source protocol applies; dependency direction and strength are explicit]
```

## Procedure

1. Normalize item identifiers and proposed dependency relations.
2. Classify each edge as strong or weak with evidence.
3. Detect cycles, compute critical paths, and identify independent branches.
4. Return the dependency graph and unresolved relation questions.

## Output contract

```yaml
produces: [dependency_graph, cycle_register, critical_paths, independent_branches]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- At least 2 subproblems are represented where the source protocol applies.
- Every edge has direction, strength, and evidence; cycles are reported rather than silently linearized.
- Parallel branches are descriptive graph properties, not execution instructions.

## Parameterization

The caller must provide item/subproblem schema, edge vocabulary, strength scale, evidence links, critical-path rule, and the scope in which parallel independence is assessed.

## Failure and counterexamples

Reject self-justifying edges, cycles hidden by reordering, or “parallel” labels where shared prerequisites remain.

## Provenance map

- resolved: hypothesis-formation/dependency-mapping
- resolved: creative-ideation/dependency-identification

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| hypothesis-formation/dependency-mapping | 12 | numeric | Requires ≥2 subproblems; labels strong/weak dependencies, detects cycles, identifies critical path and parallel opportunities. |

