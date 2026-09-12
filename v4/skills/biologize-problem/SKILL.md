---
name: biologize-problem
description: "Translate a target problem from implementation language into biological function/constraint language suitable for biological analogy search."
---

# biologize-problem
## Purpose
Translate an implementation-specific problem into biological function and constraint language for mechanism-directed analogy search.
## Input contract
```yaml
required: [target_problem, target_function]
optional: [materials, environment, performance_constraints]
constraints: [function must be implementation-independent and testable]
```
## Procedure
1. Remove target-domain nouns and restate the desired function.
2. State environmental pressures, resources, and failure constraints.
3. Produce biological search terms at function, process, and adaptation levels.
## Output contract
```yaml
produces: [biological_problem_statement, function_terms, constraint_terms]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- The biological formulation preserves the target function and names constraints without prescribing a target technology.
## Failure and counterexamples
Reject keyword-only translations that retain the original implementation vocabulary.
## Provenance map
- `biomimicry/biologize`: concept (no exact pool entry; `biologize-and-discover` is a distinct name).
