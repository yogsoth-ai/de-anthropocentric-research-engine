# generate-counterexample
## Purpose
Generate a counterexample candidate within the target claim scope and record whether exclusion is principled.
## Input contract
```yaml
required: [claim, scope, claimed_conclusion]
optional: [known_cases, construction_rules]
constraints: [candidate must satisfy stated scope before challenging conclusion]
```
## Procedure
1. Identify the claim's necessary commitments.
2. Construct a candidate satisfying scope but violating conclusion.
3. Test the candidate and classify principled versus ad hoc exclusion.
## Output contract
```yaml
produces: [counterexample_candidate, scope_check, violation, exclusion_assessment]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Preserve the original scope and show the violated conclusion explicitly.
## Failure and counterexamples
An out-of-scope case is not a counterexample; record it separately.
## Provenance map
- resolved: counterexample-generation
- resolved: counterexample-heuristics
