---
name: white-space-identification
description: Identify unexplored viable regions in the morphological matrix where
  no existing methods operate.
execution: tactic
dependencies:
  sops:
  - combination-evaluation
  - white-space-detection
---

# White Space Identification

Identify matrix regions not covered by existing methods or solutions, then evaluate those regions for viability and novelty.

## Stages

### Stage 1: White Space Detection

Map existing solutions onto the morphological matrix and identify uncovered regions using white-space-detection SOP. Annotate each gap with reason for non-coverage (overlooked, infeasible, or unexplored).

### Stage 2: Combination Evaluation

Evaluate identified white-space combinations for feasibility and novelty using combination-evaluation SOP. Score each on technical feasibility, market novelty, and implementation difficulty.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Unexplored viable regions identified | ≥3 |
| Regions evaluated for feasibility | all identified |
| Novel viable combinations surfaced | ≥2 |

## Available SOPs

| SOP | Role |
|-----|------|
| white-space-detection | Stage 1 — detect uncovered matrix regions |
| combination-evaluation | Stage 2 — evaluate feasibility and novelty |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| combination-evaluation | Evaluate new combinations for feasibility and novelty |
| white-space-detection | Identify matrix regions not covered by existing methods |

<!-- END available-tables (generated) -->
