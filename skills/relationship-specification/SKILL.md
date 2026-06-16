---
name: relationship-specification
description: 'SOP: specify the direction and form of relationships between variables'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Variable-pair list (from variable-identification output)'
output: 'Relationship specification list: direction + functional form + theoretical basis'
dependencies:
  skills:
  - subagent-spawning
---

# Relationship Specification
For each pair of key variables, specify the relationship direction (positive/negative) and functional form (linear/nonlinear/U-shaped/threshold), citing the theoretical basis.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 variable pair of 1 IV + 1 DV exists
2. Relevant mechanism or theory information is provided (used to judge the relationship form)

Not satisfied → stop, return error: cannot determine the relationship, missing variable pairs or theoretical basis.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the variable pairs
2. Direction determination: for each variable pair, determine the relationship direction (positive/negative/bidirectional/none)
3. Form determination: judge the functional form of the relationship (linear/nonlinear/U-shaped/inverted-U/threshold/saturating)
4. Theoretical-basis citation: for each determination, cite the theory or empirical evidence supporting that relationship form
5. Uncertainty annotation: if the direction/form is contested, annotate the competing prediction
6. Output a structured relationship-specification list

## Output Format
```json
[
  {
    "pair": "IV_name → DV_name",
    "direction": "positive | negative | bidirectional | unknown",
    "form": "linear | nonlinear | U-shaped | inverted-U | threshold | saturating | unknown",
    "theoretical_basis": "Theory or evidence supporting this specification",
    "competing_prediction": "Alternative specification if contested (null if uncontested)",
    "confidence": "high | medium | low"
  }
]
```
Cover at least all IV→DV pairs; optionally include IV→mediator and mediator→DV.
