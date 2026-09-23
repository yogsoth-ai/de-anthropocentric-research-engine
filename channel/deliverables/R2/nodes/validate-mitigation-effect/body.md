# validate-mitigation-effect
## Purpose
Re-run the relevant failure or adversarial test after mitigation and verify actual risk reduction without unacceptable new failures.
## Input contract
```yaml
required: [failure_mode, baseline_risk, mitigation, validation_test]
optional: [new_failure_conditions, residual_risk_scale]
constraints: [baseline and post-mitigation tests must be comparable]
```
## Procedure
1. Reproduce the baseline failure or risk measurement.
2. Apply the mitigation and re-run the relevant test.
3. Compare residual risk and inspect new failure modes.
## Output contract
```yaml
produces: [validation_result, residual_risk, new_failure_modes, mitigation_decision]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Mitigation passes only when risk decreases under comparable testing and no unacceptable new mode appears.
## Failure and counterexamples
Do not infer mitigation effectiveness from implementation alone.
## Provenance map
- resolved: mitigation-validation
