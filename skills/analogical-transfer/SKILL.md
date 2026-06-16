---
name: analogical-transfer
description: Systematic structure-mapping from source to target domain (Gentner).
  Identify relational correspondences and transfer higher-order constraints.
execution: strategy
dependencies:
  sops:
  - abstraction-extraction
  - analogy-quality-assessment
  - cross-domain-synthesis
  - structural-mapping
  - transfer-adaptation
  tactics:
  - bridge-validation
  - domain-divergence
---

# Analogical Transfer

Systematic structure-mapping from source to target domain following Gentner's structure-mapping theory. Prioritize relational similarity over surface similarity.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 25 | 0 | 0% |
| web-research | 10 | 0 | 0% |
| paper-overview | 30 | 0 | 0% |
| paper-search | 20 | 0 | 0% |
| paper-research | 8 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| analogy-extraction | Core tactic — extract and validate structural analogies |
| domain-divergence | Find distant source domains with high structural similarity |
| bridge-validation | Validate mapping depth before transfer |

## Available SOPs

| SOP | Role |
|-----|------|
| domain-scanning | Find candidate source domains |
| abstraction-extraction | Extract abstract relational structure |
| structural-mapping | Map source→target correspondences |
| analogy-quality-assessment | Rate analogy depth (surface/structural/systemic) |
| transfer-adaptation | Adapt transferred principle to target constraints |
| cross-domain-synthesis | Synthesize transfer outputs |

## Execution Guidance

1. **Functionalize target**: Restate target problem in relational terms (not object terms)
2. **Source search**: Use domain-scanning to find domains with similar relational structure
3. **Abstract source**: Extract relational structure from source using abstraction-extraction
4. **Map structure**: Use structural-mapping to align source→target correspondences
5. **Assess depth**: Apply analogy-quality-assessment — only proceed with STRUCTURAL or SYSTEMIC matches
6. **Transfer**: Carry over higher-order relational constraints from source to target
7. **Adapt**: Use transfer-adaptation to fit transferred principles to target constraints
8. **Validate**: Confirm transferred solution respects target domain physics/logic

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| bridge-validation | Validate analogy depth and transfer viability. Ensures only deep structural analogies (not surface-level similarities) proceed to transfer. |
| domain-divergence | Scan and select maximally diverse source domains. Ensures creative search covers genuinely unrelated fields with high transfer potential. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| abstraction-extraction | Extract abstract principles from concrete domain cases. Strips domain-specific details to reveal transferable mechanisms. |
| analogy-quality-assessment | Assess analogy depth (surface/structural/systemic). Determines whether an analogy warrants transfer investment. |
| cross-domain-synthesis | Synthesize all cross-domain findings into a structured idea report. Integrates outputs from all strategies and SOPs. |
| structural-mapping | Map source→target structural correspondences. Identifies corresponding, missing, and extra elements between domains. |
| transfer-adaptation | Adapt transferred principle to target problem constraints. Produces concrete adapted solutions from abstract principles. |

<!-- END available-tables (generated) -->
