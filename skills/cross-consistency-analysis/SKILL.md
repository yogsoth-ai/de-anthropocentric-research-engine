---
name: cross-consistency-analysis
description: 'CCA: pairwise consistency checking to reduce solution space 90-99%'
execution: strategy
dependencies:
  tactics:
  - creative-ideation-consistency-checking
  sops:
  - creative-ideation-consistency-pair-evaluation
  - morphological-synthesis
  - solution-space-reduction
---

# Cross-Consistency Analysis

Pairwise consistency checking (CCA) to reduce the total morphological solution space by 90-99%, leaving only internally consistent configurations.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 15 | 0 | 0% |
| web-research | 5 | 0 | 0% |
| paper-overview | 15 | 0 | 0% |
| paper-search | 10 | 0 | 0% |
| paper-research | 3 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| consistency-checking | Core tactic — evaluate and reduce |

## Available SOPs

| SOP | Role |
|-----|------|
| consistency-pair-evaluation | Evaluate pairwise consistency judgments |
| solution-space-reduction | Apply CCA to remove inconsistent combinations |
| morphological-synthesis | Synthesize reduced space report |

## Execution Guidance

1. **Input matrix**: Receive morphological matrix from zwicky-box-construction or GMA
2. **Pair evaluation**: Run consistency-pair-evaluation on all parameter-value pairs
3. **Classify inconsistencies**: Tag as logical, empirical, or normative
4. **Reduce space**: Apply solution-space-reduction to eliminate inconsistent configurations
5. **Report**: Document reduction ratio and remaining viable space

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| creative-ideation-consistency-checking | Pairwise consistency evaluation to reduce solution space by identifying and removing inconsistent combinations. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| creative-ideation-consistency-pair-evaluation | Evaluate pairwise value consistency (logical/empirical/normative) |
| morphological-synthesis | Synthesize all morphological exploration outputs |
| solution-space-reduction | Apply CCA to remove inconsistent combinations |

<!-- END available-tables (generated) -->
