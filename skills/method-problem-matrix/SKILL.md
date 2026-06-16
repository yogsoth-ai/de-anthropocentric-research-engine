---
name: method-problem-matrix
description: Cross method×problem matrix, find unexplored intersections where known
  methods have not been applied to known problems.
execution: strategy
dependencies:
  sops:
  - creative-ideation-benchmark-inventory
  - enumeration-synthesis
  - intersection-evaluation
  - method-problem-crossing
  tactics:
  - coverage-analysis
---

# Method-Problem Matrix

Cross all known methods against all known problems to find unexplored intersections — combinations that nobody has tried yet.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 25 | 0 | 0% |
| web-research | 8 | 0 | 0% |
| paper-overview | 25 | 0 | 0% |
| paper-search | 15 | 0 | 0% |
| paper-research | 5 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| coverage-analysis | Systematic coverage evaluation pipeline |
| evaluation-filtering | Score and filter intersection-derived ideas |

## Available SOPs

| SOP | Role |
|-----|------|
| benchmark-inventory | Gather method list and problem list |
| method-problem-crossing | Build the full cross-reference matrix |
| intersection-evaluation | Annotate each cell's exploration status |
| enumeration-synthesis | Synthesize matrix analysis into actionable report |

## Execution Guidance

1. **Enumerate methods**: Catalog all known methods in the domain
2. **Enumerate problems**: Catalog all known problems/challenges
3. **Cross**: Build M×P matrix via method-problem-crossing
4. **Annotate**: Mark each cell explored/partial/unexplored
5. **Prioritize**: Rank unexplored cells by potential impact
6. **Generate**: Propose solutions for top-priority unexplored intersections

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| coverage-analysis | Systematic coverage evaluation pipeline — benchmark inventory, method-problem crossing, and intersection evaluation to map explored vs unexplored solution space. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| creative-ideation-benchmark-inventory | Catalog all known solutions/methods in a domain with performance, applicability, and limitations. |
| enumeration-synthesis | Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations. |
| intersection-evaluation | Evaluate exploration status of each cell in a method×problem matrix, annotating as explored, partial, or unexplored. |
| method-problem-crossing | Build method×problem cross-reference matrix showing which methods have been applied to which problems. |

<!-- END available-tables (generated) -->
