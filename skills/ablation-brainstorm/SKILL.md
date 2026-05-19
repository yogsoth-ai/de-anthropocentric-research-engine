---
name: ablation-brainstorm
description: Remove components one by one, observe system changes to reveal hidden dependencies and generate ideas from structural gaps.
execution: strategy
used-by: systematic-enumeration
---

# Ablation Brainstorm

Systematically remove components from a system one by one, observe what changes, and use the resulting insights to generate novel ideas.

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
| coverage-analysis | Ensure all components are ablated |
| evaluation-filtering | Score and filter ablation-derived ideas |

## Available SOPs

| SOP | Role |
|-----|------|
| ablation-execution | Remove components one by one, record responses |
| dependency-identification | Extract dependency graph from ablation results |
| enumeration-synthesis | Synthesize ablation insights into idea report |

## Execution Guidance

1. **Decompose**: List all components of the target system
2. **Ablate**: Run ablation-execution — remove each component, record effects
3. **Analyze**: Run dependency-identification to find critical dependencies
4. **Ideate**: For each critical dependency, ask "what if this were replaced/eliminated/redesigned?"
5. **Filter**: Apply evaluation-filtering to rank generated ideas
6. **Synthesize**: Produce structured report via enumeration-synthesis
