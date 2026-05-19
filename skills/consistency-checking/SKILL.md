---
name: consistency-checking
description: Pairwise consistency evaluation to reduce solution space by identifying and removing inconsistent combinations.
execution: tactic
used-by: morphological-exploration, cross-consistency-analysis, general-morphological-analysis
---

# Consistency Checking

Evaluate pairwise value consistency and reduce the solution space by removing logically, empirically, or normatively inconsistent combinations.

## Stages

### Stage 1: Consistency Pair Evaluation

Evaluate all pairwise combinations of parameter values using consistency-pair-evaluation SOP. Classify each pair as consistent, inconsistent (logical), inconsistent (empirical), or inconsistent (normative).

### Stage 2: Solution Space Reduction

Apply CCA reduction rules via solution-space-reduction SOP. Remove all configurations containing at least one inconsistent pair. Report reduction ratio.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Inconsistent combinations identified and removed | ≥50% |
| Consistency types classified | all 3 (logical/empirical/normative) |
| Reduction ratio documented | yes |

## Available SOPs

| SOP | Role |
|-----|------|
| consistency-pair-evaluation | Stage 1 — evaluate pairwise consistency |
| solution-space-reduction | Stage 2 — apply CCA reduction |
