---
name: triz-contradiction-resolution
description: Resolve technical and physical contradictions via TRIZ 40 inventive principles
  and separation methods.
execution: strategy
dependencies:
  tactics:
  - contradiction-identification
  sops:
  - contradiction-matrix-lookup
  - separation-principle
  - structural-synthesis
  - triz-principle-application
---

# TRIZ Contradiction Resolution

Identify contradictions in the system and resolve them using the 40 inventive principles and separation methods.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 30 | 0 | 0% |
| web-research | 10 | 0 | 0% |
| paper-overview | 25 | 0 | 0% |
| paper-search | 15 | 0 | 0% |
| paper-research | 5 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| contradiction-identification | Identify technical and physical contradictions |
| combination-mapping | Map principle × contradiction combinations |

## Available SOPs

| SOP | Role |
|-----|------|
| function-model-construction | Build functional model to expose contradictions |
| contradiction-matrix-lookup | Query 39×39 matrix for applicable principles |
| triz-principle-application | Apply selected principles to generate solutions |
| separation-principle | Resolve physical contradictions via separation |
| structural-synthesis | Synthesize resolution outcomes |

## Execution Guidance

1. **Model**: Build function model to understand system interactions
2. **Identify**: Use contradiction-identification tactic to find contradictions
3. **Classify**: Separate into technical (parameter vs parameter) and physical (same parameter, opposing needs)
4. **Resolve technical**: Use contradiction-matrix-lookup → triz-principle-application
5. **Resolve physical**: Use separation-principle for physical contradictions
6. **Synthesize**: Produce structured output via structural-synthesis

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| contradiction-identification | Identify technical and physical contradictions in a system through functional modeling and matrix analysis. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| contradiction-matrix-lookup | Query the 39x39 TRIZ contradiction matrix to find recommended inventive principles for a given technical contradiction. |
| separation-principle | Apply time/space/condition/scale separation to resolve physical contradictions where the same parameter must satisfy opposing requirements. |
| structural-synthesis | Synthesize all structural transformation outputs into a coherent, ranked idea report with lineage tracking. |
| triz-principle-application | Select inventive principles from the contradiction matrix and generate concrete solutions for identified contradictions. |

<!-- END available-tables (generated) -->
