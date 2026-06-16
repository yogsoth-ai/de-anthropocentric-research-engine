---
name: consistency-check
description: 'SOP: Check the transitive consistency of a pairwise judgment matrix, identify inconsistent entries, and suggest corrections'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: n×n pairwise judgment matrix (Saaty scale values) + list of dimension/gap labels
output: ConsistencyReport — CR value, list of inconsistent entries, and revision suggestions
dependencies:
  skills:
  - subagent-spawning
---

# Consistency Check

Check the transitive consistency of a pairwise judgment matrix, identify inconsistent entries, and suggest corrections.

## HARD-GATE

<HARD-GATE>
- The input matrix must be square (n×n), with n in the range [2, 9]
- The matrix must have all-ones on the diagonal and satisfy a[i][j] = 1/a[j][i] (0.001 floating-point tolerance allowed)
- CR must be computed and reported
- If CR > 0.1, the inconsistent_pairs list must not be empty
</HARD-GATE>

## Pipeline

1. **Precondition check**: verify the matrix is square; check the diagonal and reciprocal properties; if violated, report the specific location
2. **Compute judgment matrix**: confirm the input matrix is valid
3. **Compute consistency ratio**: column normalize → row means (weight vector) → weighted-sum vector → λ_max → CI → CR (look up the Saaty RI table)
4. **Identify inconsistent entries**: for each triple (i, j, k), test transitivity a[i][k] ≈ a[i][j] × a[j][k]; the pair with the largest deviation is the inconsistent entry
5. **Suggest corrections**: for each inconsistent entry, suggest adjusting a[i][j] to the value that makes transitivity hold
6. **Output**: return the ConsistencyReport object

## Output Format

```json
{
  "labels": ["gap_001", "gap_002", "gap_003"],
  "n": 3,
  "lambda_max": 3.05,
  "ci": 0.025,
  "ri": 0.58,
  "cr": 0.043,
  "cr_acceptable": true,
  "inconsistent_pairs": [],
  "revision_suggestions": [],
  "matrix_issues": []
}
```
</output>
