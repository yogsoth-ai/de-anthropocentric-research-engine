---
name: benchmark-sweep
description: Systematically scan all known solutions, identify gaps in coverage and
  unexplored regions of the solution space.
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

# Benchmark Sweep

Systematically scan all known solutions in a domain, catalog their properties, and identify gaps where no solution exists.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 30 | 0 | 0% |
| web-research | 10 | 0 | 0% |
| paper-overview | 30 | 0 | 0% |
| paper-search | 20 | 0 | 0% |
| paper-research | 8 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| coverage-analysis | Inventory → crossing → intersection evaluation pipeline |
| evaluation-filtering | Score and filter generated gap-filling ideas |

## Available SOPs

| SOP | Role |
|-----|------|
| benchmark-inventory | Catalog all known solutions with performance/applicability/limitations |
| method-problem-crossing | Build cross-reference matrix from inventory |
| intersection-evaluation | Annotate matrix cells as explored/partial/unexplored |
| enumeration-synthesis | Synthesize sweep findings into structured report |

## Execution Guidance

1. **Inventory**: Run benchmark-inventory to catalog all known methods
2. **Structure**: Use method-problem-crossing to organize into matrix form
3. **Evaluate**: Run intersection-evaluation to find gaps
4. **Generate**: For each gap, brainstorm potential solutions
5. **Filter**: Apply evaluation-filtering to rank gap-filling ideas
6. **Synthesize**: Produce final report via enumeration-synthesis

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| coverage-analysis | Systematic coverage evaluation pipeline — benchmark inventory, method-problem crossing, and intersection evaluation to map explored vs unexplored solution space. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| creative-ideation-benchmark-inventory | Catalog all known solutions/methods in a domain with performance, applicability, and limitations. |
| enumeration-synthesis | Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations. |
| intersection-evaluation | Evaluate exploration status of each cell in a method×problem matrix, annotating as explored, partial, or unexplored. |
| method-problem-crossing | Build method×problem cross-reference matrix showing which methods have been applied to which problems. |

<!-- END available-tables (generated) -->
