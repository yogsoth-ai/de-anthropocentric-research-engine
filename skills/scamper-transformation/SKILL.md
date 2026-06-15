---
name: scamper-transformation
description: 7 operators (Substitute/Combine/Adapt/Modify/Put/Eliminate/Reverse) for
  systematic transformation of existing solutions.
execution: strategy
dependencies:
  sops:
  - recombination-generation
  - scamper-divergence
  - structural-synthesis
---

# SCAMPER Transformation

Apply the 7 SCAMPER operators systematically to transform existing solutions into novel variants.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 20 | 0 | 0% |
| web-research | 5 | 0 | 0% |
| paper-overview | 15 | 0 | 0% |
| paper-search | 10 | 0 | 0% |
| paper-research | 3 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| combination-mapping | Enumerate operator × component combinations |

## Available SOPs

| SOP | Role |
|-----|------|
| scamper-divergence | Execute all 7 operators, self-select best 2-3 |
| recombination-generation | Reassemble SCAMPER outputs into coherent proposals |
| structural-synthesis | Synthesize final transformation report |

## Execution Guidance

1. **Identify target**: Select the existing solution/system to transform
2. **Apply operators**: Run scamper-divergence SOP on the target
3. **Evaluate variants**: Score each variant for novelty and feasibility
4. **Combine**: Use combination-mapping to find multi-operator combinations
5. **Synthesize**: Produce structured output via structural-synthesis

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| recombination-generation | Reassemble decomposed system fragments into novel structural arrangements that create emergent value. |
| scamper-divergence | Execute SCAMPER 7 operators on a target solution. Subagent self-selects best 2-3 operators for deepest exploration. |
| structural-synthesis | Synthesize all structural transformation outputs into a coherent, ranked idea report with lineage tracking. |

<!-- END available-tables (generated) -->
