---
name: enumerate-validator-assumptions
description: "Enumerate assumptions embedded in a validator/test/sandbox, including data-generation, measurement, simulator, oracle, metric, initialization, and acceptance assumptions."
---

# enumerate-validator-assumptions
## Purpose
Enumerate assumptions embedded in a validator, benchmark, sandbox, or test.
## Input contract
```yaml
required: [validator_artifact, target_claim]
optional: [data_generation, measurement, simulator, oracle, metric, initialization, acceptance_rule]
constraints: [assumptions must be classified by source and role]
```
## Procedure
1. Inspect data generation, measurement, simulator, oracle, metric, initialization, and acceptance.
2. Record each assumption and its relation to the target.
3. Mark evidence, uncertainty, and potential circularity.
## Output contract
```yaml
produces: [validator_assumption_inventory, dependency_links, circularity_candidates]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```
## Quality gates
- No assumption is omitted merely because it is conventional.
## Failure and counterexamples
An unstated assumption remains unknown, not independent.
## Provenance map
- resolved: circular-validation-audit
