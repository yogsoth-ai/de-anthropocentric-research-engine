---
name: ahrq-picme-assessment
description: 'SOP: Use the AHRQ PiCMe framework to systematically assess a research gap across 6 dimensions'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — a single standardized gap record
output: PiCMeAssessment — independent scores across 6 dimensions, overall verdict, and research question draft
dependencies:
  skills:
  - subagent-spawning
---

# AHRQ PiCMe Assessment

Use the AHRQ PiCMe framework to systematically assess a research gap across 6 dimensions.

## HARD-GATE

<HARD-GATE>
- Input must be a GapRecord with status: "complete"
- All 6 dimensions (P/I/C/M/E + overall verdict) must be completed; none may be skipped
- Each dimension must have an independent score (1-5) and a textual rationale
- overall_verdict must be one of "strong" | "moderate" | "weak"
</HARD-GATE>

## Pipeline

1. **Precondition check**: verify completeness of the input GapRecord; confirm the domain field is valid
2. **Population (P)**: identify the target population/system/dataset the gap concerns; assess clarity of definition (1-5)
3. **Intervention (I)**: identify the proposed intervention/method/solution; assess operationalizability (1-5)
4. **Comparator (C)**: identify the comparison baseline (existing SOTA, no intervention, alternative approach); assess baseline reasonableness (1-5)
5. **Metrics (M)**: identify the evaluation metrics; assess their measurability and relevance (1-5)
6. **Evidence (E)**: assess the strength of existing evidence supporting the existence of the gap (1-5)
7. **Overall verdict**: judge overall quality from the mean of the 5 dimensions (strong ≥ 3.5 / moderate 2.5-3.4 / weak < 2.5); generate a research question draft
8. **Output**: return the PiCMeAssessment object

## Output Format

```json
{
  "gap_id": "gap_001",
  "dimensions": {
    "population": { "score": 4, "description": "Target population description", "rationale": "..." },
    "intervention": { "score": 3, "description": "Intervention/method description", "rationale": "..." },
    "comparator": { "score": 3, "description": "Comparison baseline description", "rationale": "..." },
    "metrics": { "score": 4, "description": "Evaluation metric description", "rationale": "..." },
    "evidence": { "score": 4, "description": "Evidence strength description", "rationale": "..." }
  },
  "mean_score": 3.6,
  "overall_verdict": "strong",
  "research_question_draft": "Research question draft (1 sentence)",
  "improvement_suggestions": ["Suggestion 1", "Suggestion 2"]
}
```
</output>
