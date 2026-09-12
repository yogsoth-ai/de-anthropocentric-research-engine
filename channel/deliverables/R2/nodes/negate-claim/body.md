# negate-claim
## Purpose
Produce a scope-preserving logical negation of a claim or assumption.
## Input contract
```yaml
required: [claim, scope, quantifiers]
optional: [formalization, assumptions]
constraints: [negation must preserve the original domain and quantifier structure]
```
## Procedure
1. Formalize the claim's subject, predicate, and quantifiers.
2. Negate the claim without changing its scope.
3. Record changed commitments and ambiguities.
## Output contract
```yaml
produces: [negated_claim, scope_check, changed_commitments]
delta_fields: [findings, uncertainties, decisions]
```
## Quality gates
- Quantifier and boundary changes are explicit.
## Failure and counterexamples
Do not substitute a contrary claim with a different scope.
## Provenance map
- resolved: claim-negation
- resolved: negation-definition
- resolved: axiom-negation
