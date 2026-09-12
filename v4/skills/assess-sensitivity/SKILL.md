---
name: assess-sensitivity
description: "Perturb a specified input, assumption, model choice, analysis choice, or weight and measure sensitivity of a specified output; report convergence/instability, unstable regions, and dominant drivers."
---

# assess-sensitivity

## Purpose

Perturb a specified input, assumption, model choice, analysis choice, or weight and measure the resulting output sensitivity.

## Input contract

```yaml
required: [baseline_input, perturbation_axes, output, comparison_metric]
optional: [assumptions, perturbation_design, uncertainty_model, baseline_ranking]
constraints: [each perturbation is attributable to one declared axis; the output comparison metric is fixed before evaluation; preserve the caller's scale and direction]
```

## Procedure

1. Define the baseline input, output, perturbation axes, and comparison metric.
2. Generate the caller-specified perturbation scenarios, including weight or leave-one-out variants where applicable.
3. Recompute the output for each scenario and retain the scenario-level evidence.
4. Compare scenarios, identify unstable regions and dominant drivers, and classify convergence or instability.
5. Return a sensitivity report with rankings, effect magnitudes, and rationale.

## Output contract

```yaml
produces: [sensitivity_report, scenario_results, instability_regions, dominant_drivers, stability_verdict]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Preserve source weight perturbation of ±20% per dimension, weight-vector sum 1.0 with ±0.001 tolerance, at least 4 scenarios, and stability labels `stable`/`sensitive`/`unstable` with τ bands ≥0.8, 0.5–<0.8, and <0.5.
- Rank comparison reports at least one Kendall τ or Spearman ρ and all alternatives differing by ≥2 positions.
- Conclusion sensitivity rates every assumption, identifies critical assumptions, reports interaction effects, and gives an overall robustness rating.
- Fragility index retains 0.0 as robust and 1.0 as extremely fragile; do not reinterpret it as a probability.

## Parameterization

The caller must provide the baseline object/output, perturbable axes, scenario generator or bounds, comparison metric, stability labels, and any fixed statistical bands. For ranking calls provide the normalized weight vector and scoring matrix; for conclusion calls provide assumptions and challenged variants; for meta-analysis calls provide included studies, outliers, and subgroup variables.

## Failure and counterexamples

Reject when the baseline is undefined, scenarios change more than one undeclared axis, the comparison metric is missing, or a stability verdict is given without scenario results. Do not infer causal dominance from sensitivity alone.

## Provenance map

- resolved: hypothesis-formation/weight-perturbation
- resolved: convergence/rank-comparison
- resolved: convergence/method-sensitivity-report
- resolved: deep-insight/conclusion-sensitivity-measurement
- resolved: stress-test/fragility-measurement
- resolved: convergence/conclusion-sensitivity
- resolved: knowledge-acquisition/sensitivity-analysis-design
- intermediate: Pass3/assess-rank-robustness
- intermediate: Pass3/measure-sensitivity
- intermediate: Pass3/design-meta-sensitivity
- resolved: deep-insight/convergence-assessment

## Verbatim source criteria excerpts

- `weight-perturbation` line 22: The elements of the input weight vector must sum to 1.0 (±0.001 tolerance allowed)
- `weight-perturbation` line 23: The number of rows in the scoring matrix (number of gaps) must be ≥ 2
- `weight-perturbation` line 24: At least 4 perturbation scenarios must be generated (±20% per dimension)
- `weight-perturbation` line 35: stable (all scenarios τ ≥ 0.8) / sensitive (any scenario 0.5 ≤ τ < 0.8) / unstable (any scenario τ < 0.5)
- `rank-comparison` line 27: Must report at least one rank correlation metric (Kendall tau or Spearman rho), and must list all alternatives with ranking differences >= 2 positions.
- `conclusion-sensitivity` line 24: Must consider interaction effects between assumptions.
- `fragility-measurement` line 33: fragility_index: Overall fragility (0.0 = robust, 1.0 = extremely fragile)

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| hypothesis-formation/weight-perturbation | 14 | numeric | Weight vector sums to 1.0 (±0.001); scoring matrix has ≥2 rows; at least 4 perturbation scenarios; verdict is stable/sensitive/unstable. |
| hypothesis-formation/weight-perturbation | 21 | numeric | Apply ±20% perturbations per dimension; stable means all τ ≥0.8, sensitive means any 0.5≤τ<0.8, unstable means any τ<0.5. |
| convergence/rank-comparison | 22 | numeric | Report Kendall tau or Spearman rho and all alternatives with ranking differences ≥2 positions. |
| convergence/conclusion-sensitivity | 23 | gate | Every assumption receives a sensitivity rating; identify critical assumptions, interaction effects, and overall robustness. |
| stress-test/fragility-measurement | 20 | numeric | Fragility index ranges from 0.0 robust to 1.0 extremely fragile. |
