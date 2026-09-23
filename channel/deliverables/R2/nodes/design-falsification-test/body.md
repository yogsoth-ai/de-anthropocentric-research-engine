# design-falsification-test
## Purpose
Specify a concrete observation, computation, intervention, counterexample, or measurement that could count against a claim.
## Input contract
```yaml
required: [sharp_claim, scope, candidate_observables]
optional: [cost, available_tools, competing_predictions]
constraints: [test must identify a failure condition and measurement rule]
```
## Procedure
1. Enumerate claim commitments and possible failure observations.
2. Rank tests by information value and cost.
3. Specify the cheapest decisive test with pass/fail interpretation.
## Output contract
```yaml
produces: [falsification_test, failure_condition, measurement_plan, priority_rationale]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Test must be capable of producing evidence against the claim, not only confirming examples.
## Failure and counterexamples
Do not design a test whose acceptance criterion is copied from the claim.
## Provenance map
- resolved: red-team-truthseeking
