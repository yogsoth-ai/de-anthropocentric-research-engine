---
name: benchmark-sweep
description: Systematically scan all known solutions, identify gaps in coverage and unexplored regions of the solution space.
execution: strategy
used-by: systematic-enumeration
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
