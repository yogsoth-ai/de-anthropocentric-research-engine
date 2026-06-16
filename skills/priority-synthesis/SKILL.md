---
name: priority-synthesis
description: 'SOP: synthesize all scoring data into a final gap priority list and attack-path suggestions'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: 'All scoring data (ImportanceScore[] + FeasibilityScore[] + NoveltyScore[] + ImpactScore[]) + AHP weight vector'
output: 'PriorityList — ordered gap list, weighted composite scores, attack-path suggestions for the top N'
dependencies:
  skills:
  - subagent-spawning
---

# Priority Synthesis

Synthesize all scoring data into a final gap priority list and attack-path suggestions.

## HARD-GATE

<HARD-GATE>
- Input must contain all scoring dimensions for every gap (importance / feasibility / novelty / impact)
- The weight vector must be normalized (sum to 1.0, ±0.001 tolerance allowed)
- The output priority_list is sorted by composite score in descending order, with no ties (if scores are equal, sort by the feasibility sub-score)
- The top N gaps (N = min(3, total_gaps)) must include attack-path suggestions
</HARD-GATE>

## Pipeline

1. **Precondition check**: verify completeness of the scoring data for every gap; verify the weight vector is normalized
2. **Weighted aggregation**: for each gap, use the AHP weights to compute a weighted sum of the four dimension scores into a composite score
3. **Sorting**: sort by composite score descending; on ties, sort by the feasibility sub-score
4. **Top-N attack-path suggestions**: for the top N gaps, combine their strongest dimensions with novelty's differentiation_directions to generate concrete attack-path suggestions (method choice, data sources, expected breakthrough point)
5. **Overall analysis**: output score-distribution statistics and dimension-contribution analysis
6. **Output**: return the PriorityList object

## Output Format

```json
{
  "priority_list": [
    {
      "rank": 1,
      "gap_id": "gap_003",
      "gap_title": "...",
      "composite_score": 4.2,
      "dimension_scores": {
        "importance": 4.5,
        "feasibility": 3.8,
        "novelty": 4.0,
        "impact": 4.2
      },
      "attack_path": {
        "recommended_approach": "Method suggestion (1-2 sentences)",
        "data_sources": ["Data source 1", "Data source 2"],
        "expected_breakthrough": "Expected breakthrough point (1 sentence)",
        "estimated_timeline": "Estimated timeframe"
      }
    }
  ],
  "statistics": {
    "total_gaps": 5,
    "score_range": [2.1, 4.2],
    "mean_score": 3.3,
    "top_dimension": "importance"
  },
  "synthesis_notes": "Overall analysis notes (3-5 sentences)"
}
```
