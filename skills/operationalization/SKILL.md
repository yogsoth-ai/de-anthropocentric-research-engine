---
name: operationalization
description: 'SOP: operationalize abstract concepts into measurable indicators and methods'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Abstract variable description (from variable-identification output)'
output: 'Operational definition + measurement method + validity argument (content/construct/criterion)'
dependencies:
  skills:
  - subagent-spawning
---

# Operationalization
Convert the abstract concepts in a hypothesis into concrete, measurable indicators, and argue for measurement validity.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 variable needs operationalizing (especially when operationalizable ≠ "high")
2. The variable's theoretical definition is provided (from the description field of variable-identification)

Not satisfied → stop, return error: variable-identification must be completed first.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the variable description
2. Concept analysis: decompose the variable's core attributes (conceptual dimensions)
3. Indicator selection: select 1-2 measurable indicators for each dimension
4. Measurement method determination: specify the data collection method (survey/experiment/observation/archival/computational)
5. Validity argument:
   - Content validity: do the indicators cover all key dimensions of the concept?
   - Construct validity: do the indicators converge with related constructs and diverge from unrelated ones?
   - Criterion validity: are the indicators correlated with a validated standard measure?
6. Output the operational definition

## Output Format
```json
[
  {
    "variable": "Variable name",
    "theoretical_definition": "Abstract definition",
    "dimensions": ["Dimension 1", "Dimension 2"],
    "indicators": [
      {
        "indicator": "Indicator name",
        "measurement_method": "How to collect/measure",
        "scale": "nominal | ordinal | interval | ratio",
        "validity": {
          "content": "Justification",
          "construct": "Justification",
          "criterion": "Justification or null if not applicable"
        }
      }
    ],
    "operationalization_notes": "Any remaining challenges or alternatives"
  }
]
```
