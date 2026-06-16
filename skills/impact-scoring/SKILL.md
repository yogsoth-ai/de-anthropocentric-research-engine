---
name: impact-scoring
description: 'SOP: assess the potential impact of a research gap, identify beneficiaries and output an impact score'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — a single standardized gap record
output: ImpactScore — dimension scores, composite score (1-5), beneficiary analysis, and rationale
dependencies:
  skills:
  - subagent-spawning
---

# Impact Scoring

Assess the potential impact of a research gap, identify beneficiaries and output an impact score.

## HARD-GATE

<HARD-GATE>
- Input must be a GapRecord with status: "complete"
- The output composite score must lie in the [1, 5] range
- The beneficiaries list must not be empty (at least 1 beneficiary)
- Each sub-dimension must carry at least 1 sentence of textual rationale
</HARD-GATE>

## Pipeline

1. **Precondition check**: verify input GapRecord completeness
2. **Beneficiary identification**: enumerate the direct and indirect beneficiaries once this gap is filled (researchers, practitioners, patients, policymakers, society, etc.)
3. **Impact breadth assessment**: the breadth of beneficiaries — the size of the affected population/institutions (1-5)
4. **Impact depth assessment**: the degree of change for beneficiaries — marginal improvement or fundamental transformation (1-5)
5. **Composite score**: equal-weighted average of the two dimensions, to one decimal place
6. **Output**: return the ImpactScore object

## Output Format

```json
{
  "gap_id": "gap_001",
  "beneficiaries": [
    { "group": "beneficiary name", "type": "direct | indirect", "description": "how they benefit" }
  ],
  "dimension_scores": {
    "breadth": { "score": 4, "rationale": "..." },
    "depth": { "score": 3, "rationale": "..." }
  },
  "composite_score": 3.5,
  "overall_rationale": "Overall rationale (2-4 sentences)"
}
```
