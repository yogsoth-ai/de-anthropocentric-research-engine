# decompose-components
## Purpose
Decompose a system into components and functions, preserving dependencies relevant to transformation.
## Input contract
```yaml
required: [system_or_design, decomposition_purpose]
optional: [component_inventory, dependency_evidence]
constraints: [components must have a function or interface and a parent relation]
```
## Procedure
1. Enumerate observable components and their functions.
2. Split compound components until each unit has a distinct transformation boundary.
3. Link dependencies, interfaces, and affected outcomes.
## Output contract
```yaml
produces: [component_tree, function_map, dependency_map]
delta_fields: [findings, assumption_updates, decisions]
```
## Quality gates
- Decomposition is complete for the declared boundary; no dependency is implied only by proximity.
## Failure and counterexamples
Mark a component unresolved when its function or dependency cannot be evidenced; do not invent subcomponents.
## Provenance map
- `creative-ideation/component-decomposition`: resolved.
- `stress-test/function-analysis`: resolved.
