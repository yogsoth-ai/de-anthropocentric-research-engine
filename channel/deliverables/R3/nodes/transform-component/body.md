# transform-component
## Purpose
Apply one explicit structural or functional operator to a named component and record the resulting variant.
## Input contract
```yaml
required: [component, operator, system_context]
optional: [target_function, constraints, parent_design]
constraints: [operator must be one of remove, substitute, combine, divide, redirect, redistribute, reverse]
```
## Procedure
1. Identify the component's current function, interfaces, and dependencies.
2. Apply the named operator: remove; substitute; combine; divide; redirect; redistribute; or reverse.
3. Record changed functions, dependencies, constraints, and the resulting variant.
4. Return compatibility checks to the calling tactic.
## Output contract
```yaml
produces: [transformed_component, changed_functions, changed_dependencies, variant_record]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Exactly one operator is named per variant unless the caller explicitly records a composed sequence; all affected interfaces and constraints are visible.
## Failure and counterexamples
Reject unnamed transformations, variants that silently break dependencies, and “remove” operations that leave the same function in disguise.
## Provenance map
- `creative-ideation/scamper-transformation`: resolved.
- `creative-ideation/function-redistribution`: resolved.
- `creative-ideation/trimming-execution`: resolved.
- `creative-ideation/separation-principle`: resolved.
