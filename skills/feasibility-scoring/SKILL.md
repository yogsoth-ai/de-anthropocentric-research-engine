---
name: feasibility-scoring
description: 'SOP: assess the attackability of a research gap, identify bottlenecks, and output a feasibility score'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: 'GapRecord — a single normalized gap record'
output: 'FeasibilityScore — dimension scores, composite score (1-5), bottleneck list and rationale'
dependencies:
  skills:
  - subagent-spawning
---

# Feasibility Scoring

Assess the attackability of a research gap, identify bottlenecks, and output a feasibility score.

## HARD-GATE

<HARD-GATE>
- The input must be a GapRecord with status: "complete"
- The output composite score must be within the [1, 5] range
- The bottleneck list (bottlenecks) must exist; if there are no bottlenecks it is an empty array []
- Each sub-dimension must carry at least 1 sentence of textual rationale
</HARD-GATE>

## Pipeline

1. **Pre-check**: verify the completeness of the input GapRecord
2. **Method-availability assessment**: is the existing methodological toolbox sufficient to attack this gap (1-5); reference: are there mature algorithms/frameworks to reuse
3. **Data-accessibility assessment**: are the required datasets/corpora publicly available (1-5); reference: existence of public datasets, data-scale requirements
4. **Resource-requirement assessment**: are compute/experiment resource needs within a reasonable range (1-5); reference: GPU needs, lab equipment, funding
5. **Time-horizon assessment**: can it be completed within a typical PhD/project cycle (1-5); reference: expected workload, dependency-chain length
6. **Composite scoring**: equal-weighted average of the four dimensions, kept to one decimal place; extract the main bottlenecks (dimensions with score ≤ 2)
7. **Output**: return the FeasibilityScore object

## Output Format

```json
{
  "gap_id": "gap_001",
  "dimension_scores": {
    "method_availability": { "score": 4, "rationale": "..." },
    "data_accessibility": { "score": 2, "rationale": "..." },
    "resource_requirements": { "score": 3, "rationale": "..." },
    "time_horizon": { "score": 3, "rationale": "..." }
  },
  "composite_score": 3.0,
  "bottlenecks": ["data_accessibility"],
  "overall_rationale": "Composite rationale (2-4 sentences)"
}
```
