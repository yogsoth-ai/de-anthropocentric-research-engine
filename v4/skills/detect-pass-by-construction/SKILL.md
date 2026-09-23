---
name: detect-pass-by-construction
description: "Identify cases where the validator is structurally unable to reject the target because acceptance follows from assumptions copied from the target theory or construction process."
---

# detect-pass-by-construction
## Purpose
Identify validators structurally unable to reject a target because acceptance follows from copied assumptions.
## Input contract
```yaml
required: [target_claim, validator, noncircularity_matrix]
optional: [acceptance_rule, construction_history]
constraints: [copied, shared, derived, and independent assumptions must be distinguished]
```
## Procedure
1. Find validator assumptions copied from the target.
2. Trace whether acceptance follows without an independent test.
3. Report pass-by-construction and required failure channels.
## Output contract
```yaml
produces: [pass_by_construction_finding, copied_assumptions, missing_failure_channels]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- A finding requires an explicit dependency path from target assumption to acceptance rule.
## Failure and counterexamples
Do not call shared domain knowledge circular without tracing how it enters acceptance.
## Provenance map
- resolved: circular-validation-audit
