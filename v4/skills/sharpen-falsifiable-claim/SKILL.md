---
name: sharpen-falsifiable-claim
description: "Steelman a claim into its strongest precise, bounded, testable form while making hidden quantifiers, scope, mechanisms, and commitments explicit."
---

# sharpen-falsifiable-claim
## Purpose
Steelman a claim into a precise, bounded, testable form with explicit quantifiers, scope, mechanisms, and commitments.
## Input contract
```yaml
required: [claim, context, available_evidence]
optional: [mechanism, boundary_conditions]
constraints: [strengthening may not add unsupported commitments]
```
## Procedure
1. Expose hidden quantifiers, variables, mechanisms, and boundaries.
2. Remove ambiguity while preserving the strongest evidence-supported meaning.
3. State observable consequences and candidate falsifiers.
## Output contract
```yaml
produces: [sharp_claim, quantifiers, scope, mechanisms, falsifiers]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Every commitment has an observable or computational consequence.
## Failure and counterexamples
Do not sharpen by turning a weak claim into an unsupported stronger one.
## Provenance map
- resolved: adversarial-debate-truthseeking
