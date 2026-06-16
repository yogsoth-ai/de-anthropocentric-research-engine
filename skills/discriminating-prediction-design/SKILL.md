---
name: discriminating-prediction-design
description: 'SOP: design key predictions and observation plans that can distinguish competing hypotheses'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Set of competing hypotheses (from competing-hypothesis-generation output)'
output: 'Discriminating prediction list + suggested observation/experiment methods'
dependencies:
  skills:
  - subagent-spawning
---

# Discriminating Prediction Design
Design the key predictions that can discriminate between competing hypotheses, providing direction for subsequent experiment design.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. There are ≥2 competing hypotheses (each with a unique_prediction field)
2. Each hypothesis has an explicit mechanism description

Not satisfied → stop and return an error: at least 2 competing hypotheses are required to design discriminating predictions.
</HARD-GATE>

## Pipeline
1. Pre-check: verify the completeness of the competing-hypotheses set
2. Pairwise comparison: for each pair of hypotheses, find the situations where they predict differently
3. Divergence-point identification: find the conditions or measurement dimensions where prediction differences are largest
4. Discriminating observation/experiment design: design an observation or experiment that produces different results at the divergence point
5. Feasibility assessment: technical feasibility + ethical feasibility + resource requirements
6. Output the discriminating prediction list

## Output Format
```json
[
  {
    "comparison": "H1 vs CH1",
    "divergence_point": "The condition or measurement where predictions differ",
    "h1_prediction": "What H1 predicts in this condition",
    "ch1_prediction": "What CH1 predicts in this condition",
    "discriminating_observation": "The observation or experiment that would distinguish them",
    "method": "Suggested research method (experiment/survey/natural experiment/meta-analysis/etc.)",
    "feasibility": "high | medium | low",
    "feasibility_notes": "Why feasible or what barriers exist"
  }
]
```
Covers all major hypothesis pairs (primary vs. each competing).
