---
name: boundary-condition-specification
description: 'SOP: Specify the boundary conditions under which a hypothesis holds'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: Hypothesis draft (with statement + variables + mechanism)
output: Boundary condition list (temporal/spatial/population/conditional/exclusions)
dependencies:
  skills:
  - subagent-spawning
---

# Boundary Condition Specification
Systematically identify the preconditions required for a hypothesis to hold, preventing overgeneralization.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 hypothesis draft is available (with statement and mechanism)
2. The hypothesis involves identifiable entities, time, or context

Not satisfied → stop and return error: hypothesis draft incomplete, cannot determine boundary conditions.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the hypothesis draft
2. Temporal boundary: in what time period/historical era does the hypothesis hold? Is there a time sensitivity?
3. Spatial boundary: within what geographic/cultural/organizational scope does the hypothesis hold?
4. Population boundary: to what kind of subjects does the hypothesis apply (populations, species, system types)?
5. Conditional boundary: what preconditions are required for the hypothesis to hold (technical, institutional, environmental)?
6. Exclusion conditions: explicitly list the situations where the hypothesis does not apply
7. Output structured boundary condition list

## Output Format
```json
{
  "hypothesis_id": "H1 (or hypothesis statement snippet)",
  "boundary_conditions": {
    "temporal": "Time period or duration constraints",
    "spatial": "Geographic, cultural, or organizational scope",
    "population": "Subject type, sample characteristics",
    "conditional": ["Prerequisite condition 1", "Prerequisite condition 2"],
    "exclusions": ["Situation where hypothesis does NOT apply"]
  },
  "generalizability": "narrow | moderate | broad",
  "notes": "Any additional caveats"
}
```
Each hypothesis draft yields 1 boundary condition object.
</output>
