---
name: assess-system-boundary
description: "Define and challenge the system boundary: what actors, processes, externalities, timescales, and value assumptions are included or excluded."
---

# assess-system-boundary
## Purpose
Define and challenge which actors, processes, externalities, timescales, and values are inside or outside a system boundary.
## Input contract
```yaml
required: [target_system, boundary_candidate]
optional: [actors, processes, externalities, time_horizon, value_assumptions]
constraints: [every inclusion and exclusion must be explicit]
```
## Procedure
1. Inventory actors, processes, externalities, and timescales.
2. Mark each item inside, outside, or contested under the candidate boundary.
3. Generate boundary alternatives and compare consequences for the research question.
## Output contract
```yaml
produces: [system_boundary, inclusion_exclusion_register, boundary_alternatives, consequence_map]
delta_fields: [findings, assumption_updates, uncertainties, decisions]
```
## Quality gates
- Boundary is reproducible from the register; contested items and value assumptions remain visible.
## Failure and counterexamples
Reject a boundary that hides material externalities or treats excluded stakeholders as irrelevant.
## Provenance map
- `critical-systems-heuristics/boundary-critique`: resolved.
