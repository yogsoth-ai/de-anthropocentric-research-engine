---
name: importance-scoring
description: 'SOP: assess the academic and practical importance of a research gap, output a 1-5 score with rationale'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — a single standardized gap record
output: ImportanceScore — dimension scores, composite score (1-5), and textual rationale
dependencies:
  skills:
  - subagent-spawning
---

# Importance Scoring

Assess the academic and practical importance of a research gap, output a 1-5 score with rationale.

## HARD-GATE

<HARD-GATE>
- Input must be a GapRecord with status: "complete" (id, title, description, domain all non-empty)
- The output composite score must lie in the [1, 5] range (may be a decimal, one decimal place)
- Each sub-dimension must carry at least 1 sentence of textual rationale
</HARD-GATE>

## Pipeline

1. **Precondition check**: verify input GapRecord completeness; confirm the domain field is valid
2. **Domain impact assessment**: judge how much this gap affects the core problems of its field (1-5); reference: whether it blocks the field's progress, whether it is repeatedly mentioned across multiple papers
3. **Theoretical contribution assessment**: judge the contribution that filling this gap makes to the theoretical system (1-5); reference: whether it challenges the existing paradigm, whether it can unify fragmented theories
4. **Practical value assessment**: judge the real-world application value of filling this gap (1-5); reference: size of the benefiting population, implementability, industry/policy impact
5. **Composite score**: weighted average of the three dimensions (domain impact 40%, theoretical contribution 30%, practical value 30%), to one decimal place
6. **Output**: return the ImportanceScore object

## Output Format

```json
{
  "gap_id": "gap_001",
  "dimension_scores": {
    "domain_impact": { "score": 4, "rationale": "..." },
    "theoretical_contribution": { "score": 3, "rationale": "..." },
    "practical_value": { "score": 4, "rationale": "..." }
  },
  "composite_score": 3.7,
  "overall_rationale": "Overall rationale (2-4 sentences)"
}
```
