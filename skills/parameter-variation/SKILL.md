---
name: parameter-variation
description: Systematic one-factor-at-a-time parameter sweep
execution: strategy
used-by: morphological-exploration
---

# Parameter Variation

Systematic one-factor-at-a-time (OFAT) parameter sweep to explore how individual dimension changes affect the solution space.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 20 | 0 | 0% |
| web-research | 5 | 0 | 0% |
| paper-overview | 20 | 0 | 0% |
| paper-search | 12 | 0 | 0% |
| paper-research | 5 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| combination-mapping | Map parameter-value combinations |

## Available SOPs

| SOP | Role |
|-----|------|
| value-enumeration | Enumerate values for sweep |
| combination-evaluation | Evaluate each variation |
| path-generation | Generate sweep paths |
| morphological-synthesis | Synthesize variation report |

## Execution Guidance

1. **Baseline selection**: Identify a reference configuration as baseline
2. **Parameter ordering**: Rank parameters by expected impact
3. **Sweep execution**: Vary one parameter at a time, holding others at baseline
4. **Evaluation**: Assess each variation for novelty and feasibility
5. **Sensitivity mapping**: Identify which parameters have highest creative leverage
6. **Synthesis**: Report parameter sensitivity and promising variation directions
