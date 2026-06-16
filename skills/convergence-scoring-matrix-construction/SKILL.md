---
name: convergence-scoring-matrix-construction
description: Build a complete scoring matrix through criterion definition, weighting,
  scoring, normalization, and sensitivity testing.
execution: tactic
dependencies:
  sops:
  - alternative-scoring
  - criterion-definition
  - normalization
  - scoring-synthesis
  - weight-elicitation-sop
---

# Scoring Matrix Construction

Standard MCDA workflow of define criteria → assign weights → score → aggregate → sensitivity check, producing a complete scoring matrix and ranking results.

## Stages

1. **Criterion Definition** — Extract evaluation criteria from research goals and candidates
2. **Weight Elicitation** — Compute criteria weights using specified method
3. **Alternative Scoring** — Score candidates against each criterion
4. **Normalization** — Normalize scores to make different scales comparable
5. **Sensitivity Testing** — Perturb weights to verify result robustness

## Available SOPs

- criterion-definition — Extract evaluation criteria
- weight-elicitation-sop — Compute criteria weights
- alternative-scoring — Score alternatives
- normalization — Normalize scores
- scoring-synthesis — Aggregation and sensitivity (including perturbation analysis)

## Execution Guidance

- Stages execute sequentially; each stage's output serves as input for the next
- Stage 2 method options: AHP, Swing, BWM, MACBETH, Simos
- Stage 4 normalization method must match the subsequent aggregation method (linear normalization for WSM, vector normalization for TOPSIS)
- Sensitivity testing must perturb at least 3 weight parameters by ±10%
- If any stage's output fails quality requirements, roll back and redo that stage

## Minimum Yield

Complete scoring matrix + weight vector + ranking results

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| alternative-scoring | Score each candidate alternative against all criteria to produce a score matrix. |
| criterion-definition | Extract evaluation criteria from research goals and candidate alternatives. |
| normalization | Normalize a score matrix using a specified method to make scores comparable across criteria. |
| scoring-synthesis | Synthesize score matrix, rankings, and sensitivity analysis into a final recommendation. |
| weight-elicitation-sop | Compute criteria weights using a specified elicitation method (AHP, Swing, BWM, MACBETH, or Simos). |

<!-- END available-tables (generated) -->
