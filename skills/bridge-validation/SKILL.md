---
name: bridge-validation
description: Validate analogy depth and transfer viability. Ensures only deep structural analogies (not surface-level similarities) proceed to transfer.
execution: tactic
used-by: cross-domain-discovery, facet-bisociation, analogical-transfer, random-stimulus-entry, forced-bridge-construction, design-by-analogy
---

# Bridge Validation

Validate analogy depth and transfer viability before committing resources to transfer.

## Stages

### Stage 1: Analogy Quality Assessment

Apply analogy-quality-assessment SOP to each candidate analogy. Classify depth:
- **Surface**: Shared object attributes only (e.g., "both are round") — REJECT
- **Structural**: Shared relational structure (e.g., "both use negative feedback to maintain homeostasis") — ACCEPT
- **Systemic**: Shared higher-order constraints and causal structure — STRONG ACCEPT

### Stage 2: Transfer Adaptation

For accepted analogies, test transfer viability using transfer-adaptation SOP:
- Can the principle be stated independently of source domain?
- Does the target domain have the necessary substrate for the principle?
- What adaptations are needed to fit target constraints?

### Stage 3: Structural Consistency Check

Verify the adapted transfer maintains structural consistency:
- Mapped relations preserve directionality
- Higher-order constraints are respected
- No critical source elements are unmapped without justification
- The transfer does not violate known target domain physics/logic

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Analogies assessed | all candidates |
| Validated deep analogies | ≥2 |
| Transfer viability confirmed | ≥2 |
| Structural consistency verified | ≥2 |

## Available SOPs

| SOP | Role |
|-----|------|
| analogy-quality-assessment | Stage 1 — classify analogy depth |
| transfer-adaptation | Stage 2 — test and adapt transfer |
| structural-mapping | Stage 3 — verify structural consistency |
| abstraction-extraction | Support — re-abstract if mapping fails |
