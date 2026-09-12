# design-mitigation
## Purpose
Design an intervention that prevents, detects, responds to, removes, or relaxes a failure mode.
## Input contract
```yaml
required: [failure_mode, causal_mechanism, resource_limits]
optional: [existing_controls, timeline, acceptance_criteria]
constraints: [residual risk and validation evidence must be explicit]
```
## Procedure
1. Classify the failure and locate controllable causal points.
2. Generate prevention, detection, response, removal, and relaxation options.
3. Sequence selected actions with resources and validation tests.
4. Estimate residual risk and define escalation conditions.
## Output contract
```yaml
produces: [mitigation_plan, validation_tests, residual_risk, success_criteria]
delta_fields: [decisions, findings, uncertainties]
```
## Quality gates
- Plan contains at least 3 sequenced actions when a multi-step intervention is feasible.
- Each action has an owner-independent resource statement, validation test, and success criterion.
- Residual risk is not reported as zero without evidence.
## Parameterization
Caller supplies failure taxonomy, causal graph, intervention classes, resource schema, timeline, and risk scale.
## Failure and counterexamples
Reject vague actions, controls that do not touch the mechanism, or plans without residual-risk accounting.
## Provenance map
- concept: stress-test/mitigation-design-sop
- concept: stress-test/re-scoring
- concept: convergence/removal-path
- intermediate: Pass3/design-mitigation
- intermediate: Pass3/design-removal-path
