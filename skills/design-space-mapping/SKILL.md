---
name: design-space-mapping
description: Visualize explored/unexplored regions of solution space
execution: strategy
dependencies:
  sops:
  - combination-evaluation
  - design-space-visualization
  - morphological-synthesis
  - white-space-detection
  tactics:
  - white-space-identification
---

# Design Space Mapping

Visualize and map explored vs unexplored regions of the morphological solution space, identifying coverage gaps and opportunity zones.

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
| white-space-identification | Identify unexplored viable regions |
| combination-mapping | Map existing coverage |

## Available SOPs

| SOP | Role |
|-----|------|
| white-space-detection | Detect uncovered matrix regions |
| combination-evaluation | Evaluate white-space combinations |
| design-space-visualization | Generate space map description |
| morphological-synthesis | Synthesize mapping report |

## Execution Guidance

1. **Coverage audit**: Map existing solutions/methods onto the morphological matrix
2. **White-space detection**: Run white-space-identification tactic to find gaps
3. **Evaluation**: Assess white-space combinations for feasibility and novelty
4. **Visualization**: Generate structured design space description
5. **Synthesis**: Produce coverage report with opportunity recommendations

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| white-space-identification | Identify unexplored viable regions in the morphological matrix where no existing methods operate. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| combination-evaluation | Evaluate new combinations for feasibility and novelty |
| design-space-visualization | Generate structured description of design space |
| morphological-synthesis | Synthesize all morphological exploration outputs |
| white-space-detection | Identify matrix regions not covered by existing methods |

<!-- END available-tables (generated) -->
