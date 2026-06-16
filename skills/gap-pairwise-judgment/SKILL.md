---
name: gap-pairwise-judgment
description: 'SOP: Make a criterion-by-criterion relative priority judgment between two gaps and output the preference result'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord A + GapRecord B + list of scoring criteria (with weights)
output: PairwiseJudgment — criterion-by-criterion comparison, overall preference, and Saaty scale value
dependencies:
  skills:
  - subagent-spawning
---

# Gap Pairwise Judgment

Make a criterion-by-criterion relative priority judgment between two gaps and output the preference result.

## HARD-GATE

<HARD-GATE>
- Input must contain two GapRecords with status: "complete" and at least 1 scoring criterion
- preferred_gap must be either gap_a_id or gap_b_id ("tie" is not allowed)
- saaty_value must be within the range [1, 9] (integer or fraction 1/n)
- Each criterion must have an independent comparison result
</HARD-GATE>

## Pipeline

1. **Precondition check**: Verify the completeness of the two GapRecords; confirm the criteria list is non-empty
2. **Criterion-by-criterion comparison**: For each criterion, independently judge the relative advantage of Gap A versus Gap B; record which is better and why
3. **Overall preference determination**: Aggregate by weighting each criterion's weight to determine the overall preference direction
4. **Saaty scale assignment**: Map preference strength to the Saaty scale (1=equal / 3=slightly better / 5=clearly better / 7=strongly better / 9=extremely better); if B is better than A, take the reciprocal
5. **Output**: Return the PairwiseJudgment object

## Output Format

```json
{
  "gap_a_id": "gap_001",
  "gap_b_id": "gap_002",
  "criteria_comparisons": [
    {
      "criterion": "importance",
      "weight": 0.40,
      "preferred": "gap_001",
      "rationale": "..."
    }
  ],
  "preferred_gap": "gap_001",
  "preference_strength": "moderate",
  "saaty_value": 3,
  "overall_rationale": "Overall basis (2-3 sentences)"
}
```
