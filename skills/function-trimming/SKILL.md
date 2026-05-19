---
name: function-trimming
description: Remove components while preserving function via TRIZ trimming methodology. Simplify systems by redistributing functions.
execution: strategy
used-by: structural-deconstruction
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
