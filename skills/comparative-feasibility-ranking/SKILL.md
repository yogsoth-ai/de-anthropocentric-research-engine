---
name: comparative-feasibility-ranking
description: Compare feasibility across multiple candidates using multi-dimensional
  radar and weighted feasibility index.
dependencies:
  tactics:
  - multi-dimensional-readiness-scan
  - staged-gate-evaluation
  sops:
  - feasibility-synthesis
  - radar-synthesis
---

# Comparative Feasibility Ranking

**Purpose:** Produce a defensible ranking of candidates by feasibility. Uses multi-dimensional radar charts to visualize relative strengths and a weighted feasibility index to collapse multiple dimensions into a single comparable score.

**When to use:**
- Multiple candidates have been assessed and need to be compared
- Stakeholders need a clear ranking to prioritize resource allocation
- You need to identify which candidates are most implementable given current constraints

## Budget

| Metric | Target |
|--------|--------|
| Candidates compared | >= 2 |
| Dimensions in radar | >= 5 |
| Weight justifications | 1 per dimension |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| candidates[] | array | All candidates being compared |
| dimension_weights{} | map | Dimension -> weight mapping |
| radar_data[] | array | Per-candidate radar scores |
| feasibility_index[] | array | Weighted composite scores |
| ranking[] | array | Final ranked list |

## Available Tactics

| Tactic | When |
|--------|------|
| multi-dimensional-readiness-scan | To generate per-candidate radar data for comparison |
| staged-gate-evaluation | To compare gate-passage likelihood across candidates |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| radar-synthesis | Produce radar data for each candidate |
| feasibility-synthesis | Produce final comparative matrix |

## Execution Guidance

1. Ensure all candidates have been assessed on the same dimensions
2. Normalize scores to a common scale (1-9 recommended)
3. Assign dimension weights based on context (stakeholder priorities, strategic fit)
4. Calculate weighted feasibility index for each candidate
5. Produce comparative radar visualization data
6. Rank candidates and identify clear tiers (strong/moderate/weak feasibility)

## Output Format

```yaml
comparative_ranking:
  dimensions: [technical, market, regulatory, resource, organizational]
  weights: {technical: 0.3, market: 0.25, regulatory: 0.2, resource: 0.15, organizational: 0.1}
  candidates:
    - {name, scores: {...}, weighted_index: 0.X, rank: N, tier: strong|moderate|weak}
  radar_data: [{candidate, dimension_scores: [...]}]
  recommendation: <top candidate(s) with rationale>
  caveats: [...]
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| multi-dimensional-readiness-scan | Assess readiness across multiple dimensions, synthesize into radar visualization, and identify bottleneck dimensions. |
| staged-gate-evaluation | Define gate criteria for each stage, evaluate candidates at each gate, and render go/kill/recycle decisions with evidence. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| feasibility-synthesis | Synthesize all assessments into a feasibility matrix, recommendation, and risk summary. |
| radar-synthesis | Synthesize multiple dimension scores into radar chart data and compute overall readiness. |

<!-- END available-tables (generated) -->
