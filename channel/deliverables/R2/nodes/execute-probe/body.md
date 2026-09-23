# execute-probe
## Purpose
Execute one test or attack and record outcome, evidence, and severity.
## Input contract
```yaml
required: [probe_spec, target, success_and_failure_conditions]
optional: [tool_context, severity_scale]
constraints: [probe scope and interpretation rule must be fixed before execution]
```
## Procedure
1. Verify target and probe conditions.
2. Run the probe and capture observations.
3. Classify outcome against the predeclared conditions.
## Output contract
```yaml
produces: [probe_record, observations, outcome, severity]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Preserve raw observation, execution context, and interpretation separately.
## Failure and counterexamples
An unavailable tool or inconclusive observation is uncertainty, not a passing probe.
## Provenance map
- resolved: probe-execution
