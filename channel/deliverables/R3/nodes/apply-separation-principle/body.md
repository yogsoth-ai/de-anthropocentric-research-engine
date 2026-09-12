# apply-separation-principle
## Purpose
Resolve a physical contradiction by separating conflicting requirements in time, space, scale, condition, or system level.
## Input contract
```yaml
required: [contradiction, conflicting_requirements]
optional: [system_boundary, operating_conditions]
constraints: [requirements must be stated as mutually conflicting outcomes]
```
## Procedure
1. State the useful and harmful effects that cannot coexist (`conflicting_requirements`).
2. Test separation in time, space, scale, condition, and system level.
3. Select the separation that removes the conflict and state its operating condition.
## Output contract
```yaml
produces: [separation_candidates, selected_principle, operating_condition]
delta_fields: [findings, hypothesis_updates, decisions, uncertainties]
```
## Quality gates
- Each candidate names the separated dimension and preserves the useful effect while removing the harmful one.
## Failure and counterexamples
Do not call parameter tuning a separation when both requirements still occur under the same condition.
## Provenance map
- `triz/separation-principles`: concept (the exact pool entry is singular `separation-principle`; near-name substitution is forbidden).
