---
name: hypothesis-comparison-matrix
description: 'SOP: Build a multi-dimensional comparison matrix of competing hypotheses'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: Set of competing hypotheses + discriminating predictions (from upstream output)
output: Structured comparison matrix (table + overall assessment)
dependencies:
  skills:
  - subagent-spawning
---

# Hypothesis Comparison Matrix
Build a multi-dimensional comparison matrix of competing hypotheses, highlight key differences, and support informed selection.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. ≥2 hypotheses already exist (primary hypothesis + ≥1 competing hypothesis)
2. Hypotheses contain basic components such as mechanism and predictions

Not met → stop and return error: at least 2 hypotheses are required to build a comparison matrix.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the hypothesis set
2. Dimension determination: select comparison dimensions (default: mechanism type / evidence support / testability / parsimony / explanatory scope / theoretical basis)
3. Hypothesis-by-hypothesis, dimension-by-dimension population: assign a value for each hypothesis on each dimension
4. Difference highlighting: mark the dimensions with the largest differences between hypotheses
5. Overall assessment: give an overall recommendation based on the matrix
6. Output the structured comparison table

## Output Format
```json
{
  "dimensions": ["mechanism_type", "evidence_support", "testability", "parsimony", "scope", "theoretical_basis"],
  "matrix": [
    {
      "hypothesis_id": "H1",
      "label": "Primary Hypothesis",
      "statement": "...",
      "mechanism_type": "...",
      "evidence_support": "strong | moderate | weak | none",
      "testability": "high | medium | low",
      "parsimony": "high | medium | low",
      "scope": "broad | moderate | narrow",
      "theoretical_basis": "Theory name(s)"
    }
  ],
  "key_differentiators": ["Dimension where hypotheses differ most"],
  "recommendation": "Which hypothesis to prioritize and why",
  "caveats": "Important limitations of the comparison"
}
```
