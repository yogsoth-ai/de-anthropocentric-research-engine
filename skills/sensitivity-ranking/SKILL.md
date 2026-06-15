---
name: sensitivity-ranking
description: Rank constraints by sensitivity — which ones most impact the outcome
  if they shift
version: 1.0.0
category: experiment-execution
type: tactic
orchestrates:
- resource-quantification
- assumption-challenging
- critical-chain-identification
dependencies:
  sops:
  - assumption-challenging
  - critical-chain-identification
  - resource-quantification
---

# Tactic: Sensitivity Ranking

## Orchestration Pattern

1. **Quantify Resources** → spawn `resource-quantification`
   - For each identified constraint, quantify its current state (demand, supply, gap)
   - Express gaps in comparable units where possible

2. **Challenge Assumptions** → spawn `assumption-challenging`
   - For each constraint, identify the assumptions that make it binding
   - Score assumption vulnerability (confidence × evidence / testability)

3. **Identify Critical Chain Impact** → spawn `critical-chain-identification`
   - Determine which constraints lie on the critical chain
   - Constraints on the critical chain have higher sensitivity

4. **Compute Sensitivity Score** → synthesize
   - Sensitivity = (Gap magnitude) × (Chain position weight) × (Assumption vulnerability)
   - Chain position weight: on critical chain = 2.0, feeding chain = 1.0, off-chain = 0.5
   - Rank all constraints by sensitivity score

## Decision Criteria

- **When to use**: After multiple constraints have been identified and need prioritization
- **When to skip**: If only 1-2 constraints exist, ranking is trivial
- **Threshold**: Constraints with sensitivity score >2× the median are "binding"
- **Output**: Ordered list with scores, used by parent strategy to focus effort

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| assumption-challenging | Challenge each assumption's validity — shared cross-repo SOP |
| critical-chain-identification | Identify the critical chain — longest path considering resource contention |
| resource-quantification | Quantify resource demand vs supply vs gap for each resource category |

<!-- END available-tables (generated) -->
