---
name: construct-hierarchy
description: "Construct an acyclic is-a/part-of/instance-of hierarchy with explicit roots, depth, and transitivity constraints."
---

# construct-hierarchy

## Purpose
Construct an acyclic is-a/part-of/instance-of hierarchy with explicit roots, depth, and transitivity constraints.

## Input contract
```yaml
required: [entity_set, relation_assertions, hierarchy_scope]
optional: [root_policy, multiple_inheritance_policy, depth_limit]
constraints: [relations use declared types; cycles are invalid]
```

## Procedure
1. Normalize entity identifiers and relation types.
2. Insert high-confidence edges and infer only declared transitive edges.
3. Detect cycles, orphan nodes, missing intermediate levels, and root violations.
4. Repair or quarantine invalid edges, then emit roots, depth, and edge rationale.

## Output contract
```yaml
produces: [hierarchy_graph, roots, depth_report, cycle_report, edge_rationales]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates
- Graph is acyclic and every node has an allowed path to a root or an explicit orphan status.
- Transitive closure does not introduce relation-type violations.
- Depth is reported; depth >5 requires explicit justification.

## Parameterization
Caller supplies entity schema, relation ontology, root and multiple-inheritance policies, transitivity rules, and depth limit.

## Failure and counterexamples
Reject an edge that creates a cycle or conflates is-a with part-of.

## Provenance map
- resolved: hierarchy-construction
- intermediate: Pass4/map-field-taxonomy

## Preserved source criteria ledger

| source | criterion |
|---|---|
| hierarchy-construction | Acyclic always; cycles are logical errors. |
| hierarchy-construction | Multiple inheritance is allowed. |
| hierarchy-construction | Depth ≤5 unless explicitly justified. |
