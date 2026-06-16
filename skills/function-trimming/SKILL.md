---
name: function-trimming
description: Remove components while preserving function via TRIZ trimming methodology.
  Simplify systems by redistributing functions.
execution: strategy
dependencies:
  tactics:
  - component-decomposition
  sops:
  - function-model-construction
  - structural-synthesis
  - trimming-execution
---

# Function Trimming

Systematically remove components while preserving or redistributing their functions to remaining elements.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 25 | 0 | 0% |
| web-research | 8 | 0 | 0% |
| paper-overview | 20 | 0 | 0% |
| paper-search | 12 | 0 | 0% |
| paper-research | 5 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| component-decomposition | Identify components and trimming candidates |
| combination-mapping | Map function redistribution options |

## Available SOPs

| SOP | Role |
|-----|------|
| function-model-construction | Build functional model with useful/harmful annotations |
| trimming-execution | Progressive removal with function verification |
| recombination-generation | Reassemble trimmed system |
| structural-synthesis | Synthesize trimming outcomes |

## Execution Guidance

1. **Model**: Build complete function model via function-model-construction
2. **Identify candidates**: Use component-decomposition to find trimming targets
3. **Rank**: Prioritize components by harmful-function ratio and replaceability
4. **Trim**: Execute trimming-execution SOP progressively
5. **Redistribute**: Assign orphaned functions to remaining components
6. **Synthesize**: Produce simplified system via structural-synthesis

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| component-decomposition | Decompose system into functional components, identify dependencies, and surface trimming candidates. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| function-model-construction | Build substance-field functional model of a system, annotating useful, harmful, insufficient, and excessive interactions. |
| structural-synthesis | Synthesize all structural transformation outputs into a coherent, ranked idea report with lineage tracking. |
| trimming-execution | Progressively remove components from a system while verifying function preservation through redistribution. |

<!-- END available-tables (generated) -->
