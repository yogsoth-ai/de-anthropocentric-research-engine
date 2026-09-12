# classify-research-gap
## Purpose
Classify a candidate research gap by type and record implications for the next research action.
## Input contract
```yaml
required: [gap_statement, supporting_evidence]
optional: [domain_scope, candidate_gap_types]
constraints: [gap type must be supported by evidence and distinguished from absence of search]
```
## Procedure
1. Compare the gap claim with the declared evidence and scope.
2. Test evidence, method, mechanism, population, theory, measurement, contradiction, boundary, and translation categories.
3. Assign one or more justified types and map each to a next action.
## Output contract
```yaml
produces: [typed_gap, classification_rationale, action_implications]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- Classification names the evidence boundary and does not treat unsearched space as a confirmed gap.
## Failure and counterexamples
Return `unsubstantiated_gap` when the claimed absence is caused by inadequate retrieval or incompatible scope.
## Provenance map
- `deep-insight/gap-classification`: resolved.
