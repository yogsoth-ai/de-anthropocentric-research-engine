# classify-falsification-verdict
## Purpose
Classify a tested claim as BROKEN, CORROBORATED, or UNFALSIFIABLE.
## Input contract
```yaml
required: [claim, falsifier, test_result, adequacy_assessment]
optional: [scope, power_or_precision]
constraints: [falsifier must be legitimate and within scope]
```
## Procedure
1. Check the falsifier and scope.
2. Assess whether the test was adequate.
3. Return exactly one permitted verdict with rationale.
## Output contract
```yaml
produces: [falsification_verdict, verdict_rationale, adequacy_assessment]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- BROKEN requires a successful legitimate falsifier.
- CORROBORATED requires an adequate test that failed to falsify.
- Otherwise return UNFALSIFIABLE.
## Failure and counterexamples
Do not treat an underpowered or unreachable test as corroboration.
## Provenance map
- resolved: falsification-first-stress-test
