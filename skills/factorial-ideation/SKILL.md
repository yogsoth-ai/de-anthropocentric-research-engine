---
name: factorial-ideation
description: 'DOE thinking: identify factors, define levels, and explore combinations
  to systematically cover the design space.'
execution: strategy
dependencies:
  sops:
  - coverage-gap-detection
  - creative-ideation-factor-level-design
  - enumeration-synthesis
  tactics:
  - gap-driven-generation
---

# Factorial Ideation

Apply Design of Experiments (DOE) thinking to ideation: identify key factors, define their levels, and systematically explore combinations.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 20 | 0 | 0% |
| web-research | 8 | 0 | 0% |
| paper-overview | 20 | 0 | 0% |
| paper-search | 12 | 0 | 0% |
| paper-research | 5 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| gap-driven-generation | Generate ideas for uncovered factor combinations |
| evaluation-filtering | Score and filter factorial-derived ideas |

## Available SOPs

| SOP | Role |
|-----|------|
| factor-level-design | Identify factors, define levels, build experiment matrix |
| coverage-gap-detection | Find unexplored regions in factorial space |
| failure-driven-generation | Generate solutions for problematic combinations |
| enumeration-synthesis | Synthesize factorial exploration into idea report |

## Execution Guidance

1. **Identify factors**: Determine key dimensions that define the solution space
2. **Define levels**: For each factor, enumerate possible values/states
3. **Design matrix**: Run factor-level-design to build the experiment matrix
4. **Detect gaps**: Run coverage-gap-detection on the factorial space
5. **Generate**: Propose solutions for high-priority unexplored combinations
6. **Filter**: Apply evaluation-filtering to rank generated ideas
7. **Synthesize**: Produce structured report via enumeration-synthesis

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| gap-driven-generation | Generate solutions targeting specific coverage gaps — detect gaps, generate failure-driven solutions, and design factor-level experiments. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| coverage-gap-detection | Detect uncovered regions in the solution space, producing a prioritized gap list. |
| creative-ideation-factor-level-design | Identify factors and their levels for a problem, then design an experiment matrix for systematic exploration. |
| enumeration-synthesis | Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations. |

<!-- END available-tables (generated) -->
