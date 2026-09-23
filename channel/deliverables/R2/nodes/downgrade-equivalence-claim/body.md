# downgrade-equivalence-claim
## Purpose
When full equivalence fails, downgrade to the strongest defensible relation and record what was not preserved.
## Input contract
```yaml
required: [equivalence_claim, preservation_report, counterexamples]
optional: [relation_ladder, scope]
constraints: [each downgrade must name lost structures or operations]
```
## Procedure
1. List failed preservation obligations.
2. Test candidate weaker relations.
3. Select the strongest relation supported and document exclusions.
## Output contract
```yaml
produces: [downgraded_relation, lost_invariants, supporting_mapping, exclusions]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Downgrade cannot silently retain a failed invariant.
## Failure and counterexamples
Do not downgrade by vocabulary alone; provide the preserved relation and counterexample boundary.
## Provenance map
- resolved: isomorphism-falsification
