---
name: priority-sensitivity-testing
description: 'Tactic: perturb scoring weights to test the robustness of the gap ranking
  against weight choice'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: gap-prioritization
sops:
- ahp-weighting
- weight-perturbation
- priority-synthesis
dependencies:
  sops:
  - ahp-weighting
  - priority-synthesis
  - weight-perturbation
---

# Priority Sensitivity Testing

Apply weight perturbations to an existing gap scoring matrix to test whether the final ranking is sensitive to weight choice, thereby judging the credibility of the priority decision.

## Orchestration Intent

The final ranking of a scoring matrix depends on the weight settings for each dimension. If a small change in weights drastically changes the ranking, the decision is unreliable; if the ranking remains stable across a reasonable weight range, the priority conclusion is more convincing.

This tactic first establishes baseline weights (AHP or equal weights), then systematically perturbs the weights (±20%), observes the ranking changes, and finally gives a stability verdict.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| ahp-weighting | Use the AHP method to derive a weight vector from dimension-importance judgments | First step, establish baseline weights |
| weight-perturbation | Apply ±20% perturbations to each dimension weight and recompute the ranking | Second step, systematic perturbation |
| priority-synthesis | Aggregate the ranking results across all perturbation scenarios into a stability report | Third step, synthesize conclusion |

## Orchestration Pattern

**Default (standard flow)**
1. ahp-weighting: derive baseline weights from the dimension-importance judgments provided by the user/strategy; use equal weights if none provided
2. weight-perturbation: apply +20% and -20% perturbations to each dimension in turn (the remaining dimensions are adjusted proportionally to keep the sum at 1), producing a ranking for each perturbation scenario
3. priority-synthesis: tally each gap's rank distribution across all perturbation scenarios and output a stability verdict

**Simplified (S tier or fast mode)**
- Skip ahp-weighting, directly use equal weights as the baseline
- Perturb only the highest-weight dimension (±20%), producing 2 perturbation scenarios
- priority-synthesis gives a simplified stability report

**Deep (L tier or high-risk decision)**
- ahp-weighting uses a full AHP pairwise comparison (pairwise comparison between dimensions)
- weight-perturbation expands the perturbation range to ±30% and adds extreme scenarios (one dimension's weight set to 0)
- priority-synthesis additionally outputs the Spearman rank correlation coefficient (baseline ranking vs each perturbed ranking)

## Minimum Yield

- A baseline weight vector (all dimension weights sum to 1)
- Ranking results for at least 3 perturbation scenarios (each scenario annotated with its perturbation content)
- Rank-stability statistics for each gap (highest rank, lowest rank, modal rank)
- A final stability verdict: **Stable** (top N unchanged across all scenarios) / **Partially Sensitive** (1-2 changes in the top N) / **Highly Sensitive** (more than 2 changes in the top N)

## Yield Report

After execution, report to the calling strategy:
- Source of the baseline weights (AHP-derived / equal weights / user-specified)
- Number of perturbation scenarios
- The stability-verdict conclusion
- The least stable gap (largest rank fluctuation) and a suggestion (whether more evidence is needed before deciding)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| ahp-weighting | SOP: Use the AHP (Analytic Hierarchy Process) to determine scoring-dimension weights, outputting a weight vector |
| priority-synthesis | SOP: synthesize all scoring data into a final gap priority list and attack-path suggestions |
| weight-perturbation | SOP: Perturb weights to test gap-ranking stability, output a stability verdict |

<!-- END available-tables (generated) -->
