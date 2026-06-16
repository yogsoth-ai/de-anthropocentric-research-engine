---
name: ahp-weighting
description: 'SOP: Use the AHP (Analytic Hierarchy Process) to determine scoring-dimension weights, outputting a weight vector'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: List of dimensions (string array) + optional pairwise comparison preference matrix
output: AHPWeights — weight vector, consistency ratio (CR), and judgment matrix
dependencies:
  skills:
  - subagent-spawning
---

# AHP Weighting

Use the AHP (Analytic Hierarchy Process) to determine scoring-dimension weights, outputting a weight vector.

## HARD-GATE

<HARD-GATE>
- The number of input dimensions must be in the range [2, 9] (AHP applicability range)
- The elements of the output weight vector must sum to 1.0 (±0.001 tolerance allowed)
- The consistency ratio CR must be computed and reported; if CR > 0.1 a warning must be flagged
</HARD-GATE>

## Pipeline

1. **Precondition check**: verify the dimension list is non-empty and its count is in the range [2, 9]
2. **Dimension list confirmation**: output the dimension list for the caller to confirm; if a comparison matrix is already provided, skip to step 4
3. **Pairwise comparison matrix construction**: for each pair of dimensions (i, j) assign a Saaty scale value (1-9); the matrix must satisfy a[j][i] = 1/a[i][j]
4. **Eigenvector computation**: normalize each column then take row means to obtain the priority vector (weights)
5. **Consistency ratio check**: compute the largest eigenvalue λ_max → consistency index CI = (λ_max - n)/(n-1) → CR = CI/RI (look up the Saaty RI table); CR < 0.1 is acceptable
6. **Output**: return the AHPWeights object; if CR > 0.1 attach revision suggestions

## Output Format

```json
{
  "dimensions": ["importance", "feasibility", "novelty", "impact"],
  "comparison_matrix": [[1, 3, 2, 2], [0.33, 1, 0.5, 0.5], [0.5, 2, 1, 1], [0.5, 2, 1, 1]],
  "weights": { "importance": 0.40, "feasibility": 0.15, "novelty": 0.23, "impact": 0.22 },
  "lambda_max": 4.02,
  "ci": 0.007,
  "ri": 0.90,
  "cr": 0.008,
  "cr_acceptable": true,
  "warnings": [],
  "revision_suggestions": []
}
```
</output>
