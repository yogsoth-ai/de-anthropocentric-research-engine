---
name: method-problem-matrix
description: Cross method×problem matrix, find unexplored intersections where known methods have not been applied to known problems.
execution: strategy
used-by: systematic-enumeration
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
