# construct-defense
## Purpose
Construct the strongest defensible case while acknowledging valid weaknesses.
## Input contract
```yaml
required: [position, evidence_set, objection_set]
optional: [defense_criteria, audience, weakness_policy]
constraints: [support must be evidence-linked and weaknesses cannot be erased]
```
## Procedure
1. State the position and burden of proof.
2. Select and order the strongest supporting arguments.
3. Address objections and reframe only where evidence supports the reframe.
4. Mark residual weaknesses and scope limits.
## Output contract
```yaml
produces: [defense_case, supporting_arguments, objection_responses, residual_weaknesses]
delta_fields: [findings, decisions, uncertainties]
```
## Quality gates
- At least 3 supporting arguments are supplied when evidence permits.
- At least 1 perceived weakness is tested for legitimate reframing.
- Every claim has an evidence or uncertainty link.
## Parameterization
Caller supplies position schema, evidence rubric, objection taxonomy, argument-count rule, and weakness policy.
## Failure and counterexamples
Reject hedged advocacy, unsupported reframes, or defenses that omit valid objections.
## Provenance map
- concept: stress-test/debate-defender
- concept: convergence/advocate-construction
