---
name: competing-hypothesis-generation
description: 'SOP: Generate mechanistically distinct competing hypotheses for the same phenomenon'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: Phenomenon description + primary hypothesis (from upstream output)
output: Competing hypothesis list (mechanistically distinct, not variants of the primary hypothesis)
dependencies:
  skills:
  - subagent-spawning
---

# Competing Hypothesis Generation
Generate genuinely distinct competing hypotheses for the same phenomenon to guard against confirmation bias and keep explanations open.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 primary hypothesis is available (with statement + mechanism)
2. A phenomenon description is provided (the phenomenon the primary hypothesis attempts to explain)

Not satisfied → stop and return error: primary hypothesis and phenomenon description required.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the primary hypothesis and phenomenon description
2. Alternative mechanism search: look for different causal mechanisms that can explain the same phenomenon
3. Alternative theory application: derive predictions about the same phenomenon from different theoretical frameworks
4. Reverse reasoning: consider explanations with the opposite causal direction
5. Deduplication: ensure each competing hypothesis is mechanistically distinct from the primary hypothesis and from the other competing hypotheses
6. Output competing hypothesis list

## Output Format
```json
[
  {
    "hypothesis_id": "CH1",
    "statement": "Competing hypothesis statement",
    "mechanism": "Different causal mechanism from the primary hypothesis",
    "theoretical_basis": "Theory or reasoning supporting this alternative",
    "key_difference": "How this differs mechanistically from the primary hypothesis",
    "shared_prediction": "Prediction shared with primary hypothesis (makes discrimination hard)",
    "unique_prediction": "Prediction unique to this hypothesis (enables discrimination)"
  }
]
```
At least 2 competing hypotheses, each mechanistically distinct from the primary hypothesis.
</output>
