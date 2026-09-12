# appreciative-reframe
## Purpose
Reframe a problem around functioning exceptions, strengths, positive deviance, and conditions supporting desired behavior.
## Input contract
```yaml
required: [problem_statement, functioning_exceptions]
optional: [stakeholders, outcome_definition]
constraints: [exceptions must be observed cases, not aspirations]
```
## Procedure
1. Identify cases where the desired behavior already occurs.
2. Extract the enabling conditions and strengths present in those cases.
3. Rewrite the research question around reproducing or extending those conditions.
## Output contract
```yaml
produces: [exception_inventory, enabling_conditions, appreciative_reframe]
delta_fields: [findings, hypothesis_updates, decisions]
```
## Quality gates
- Each positive exception has evidence and a condition set; the reframe preserves the target outcome.
## Failure and counterexamples
Reject success stories that are unverified, incomparable, or explained only by selection bias.
## Provenance map
- `deep-insight/appreciative-reframing`: resolved.
