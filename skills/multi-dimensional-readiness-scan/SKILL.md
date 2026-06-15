---
name: multi-dimensional-readiness-scan
description: Assess readiness across multiple dimensions, synthesize into radar visualization,
  and identify bottleneck dimensions.
execution: tactic
dependencies:
  sops:
  - convergence-bottleneck-identification
  - dimension-assessment
  - radar-synthesis
---

# Multi-Dimensional Readiness Scan

Systematically evaluate a candidate across all relevant feasibility dimensions, produce a composite radar view, and surface the dimensions that are limiting overall readiness.

## Stages

1. **Dimension Assessment** — Score each dimension (technical, market, regulatory, resource, organizational) independently using evidence-based criteria. Deploy `dimension-assessment` SOP for each dimension (parallelizable).

2. **Radar Synthesis** — Combine all dimension scores into a unified radar chart representation. Deploy `radar-synthesis` SOP with the collected scores.

3. **Bottleneck Identification** — Analyze the radar for dimensions significantly below the mean or below required thresholds. Deploy `bottleneck-identification` SOP on the radar data.

## Available SOPs

| SOP | Stage | Purpose |
|-----|-------|---------|
| dimension-assessment | 1 | Score a single readiness dimension |
| radar-synthesis | 2 | Combine scores into radar chart data |
| bottleneck-identification | 3 | Identify limiting dimensions |

## Execution Guidance

- Stage 1 can run all dimension assessments in parallel via subagents
- Stage 2 requires all Stage 1 outputs before proceeding
- Stage 3 requires Stage 2 output
- If fewer than 5 dimensions are scoreable, flag as incomplete and note which dimensions lack evidence
- Each dimension should have at least 2 evidence items supporting the score

## Minimum Yield

- Complete radar with >= 5 dimensions scored
- Bottleneck list with severity ranking
- Overall readiness score (weighted average)
