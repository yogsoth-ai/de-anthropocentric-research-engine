---
name: design-experiment
description: "Translate a falsifiable hypothesis into a statistically defensible experiment. Factorial, ablation, comparison, scaling, and robustness designs are modes, not strategy nodes."
---

# design-experiment

## Purpose

Translate a falsifiable hypothesis into a statistically defensible experiment. Factorial, ablation, comparison, scaling, and robustness are modes.

## When to use / not applicable

Use after a hypothesis has an operational construct and discriminating prediction. Not applicable when the hypothesis or measurable outcome is absent.

## Input contract

```yaml
mode_contracts:
  factorial: &experiment_input
    required: [falsifiable_hypothesis, outcome, factors, constraints]
    optional: [baseline, candidate_models, budget, robustness_axes]
    constraints: [analysis_plan_must_be_preregistered]
  ablation: *experiment_input
  comparison: *experiment_input
  scaling: *experiment_input
  robustness: *experiment_input
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `identify-variables` to operationalize the outcome, factors, controls, and their functional roles. You MUST load skill `enumerate-dimension-values` to define admissible levels or perturbation values.
   If the resource envelope or feasibility constraints cannot support an executable design, consider `analyze-constraints-readiness` before committing to a mode.
2. Choose `factorial`, `ablation`, `comparison`, `scaling`, or `robustness` mode.
3. You MUST load skill `specify-metrics` to preregister metrics, estimands, directionality, and decision thresholds. You MUST load skill `estimate-sample-size` to derive the sample or repetition requirement. You MUST load skill `select-statistical-method` to select the inference or estimation method before observing outcomes; specify power and the stopping rule.
   If the proposed metric or validator may share artifacts, labels, or assumptions with the system under test, consider `audit-validator-independence` before freezing the analysis plan.
4. You MUST load skill `construct-design-matrix` to construct the runnable matrix for the selected mode. You MUST load skill `design-randomness-protocol` to define seeds, repetitions, and propagation rules. You MUST load skill `specify-execution-environment` to capture interpretation-relevant hardware, software, data, configuration, and versions. You MUST load skill `specify-reproducibility-protocol` to define and test the intended reproduction level. You MUST load skill `optimize-design-under-budget` to select a feasible information-efficient design under the declared resource envelope; include resource and failure checks.
   Once the design has produced observations and the task changes from planning to inference, `analyze-experiment-results` may be the better next tactic.

## Mode branches

For `comparison` or `robustness`, You MUST load skill `select-experimental-baseline` to choose a controlled baseline matched to the claim.

- `factorial`: vary multiple factors in a structured design so main effects and interactions are estimable within the declared resource envelope.
- `ablation`: remove or replace components systematically to attribute the outcome to individual parts and suspected interactions. You MUST load skill `map-ablation-components` to define ablatable units, dependencies, and legal removal or replacement operations.
- `comparison`: evaluate a target against controlled baselines with matched confounds, compute, tuning effort, and preregistered tests.
- `scaling`: instantiate geometric or otherwise justified scale points to test how the outcome changes across the declared regime.
- `robustness`: perturb relevant conditions or inputs and measure whether the claimed effect survives the defined stress space.

## Output contract

```yaml
mode_contracts:
  factorial:
    produces: [factor_level_matrix, factor_level_catalog, estimands_main_effects_interactions, metric_significance_plan, sample_power_plan]
    delta_fields: [findings, decisions, uncertainties, open_questions]
  ablation:
    produces: [ablation_matrix, baseline_anchors_full_minimal, attribution_contrasts, component_interaction_plan]
    delta_fields: [findings, decisions, uncertainties, open_questions]
  comparison:
    produces: [controlled_baseline_comparison, matched_confound_controls, seed_environment_protocol, statistical_comparison_plan, reproducibility_protocol]
    delta_fields: [findings, decisions, uncertainties, open_questions]
  scaling:
    produces: [scaling_axes, geometric_scale_points, scaling_experiment_grid, curve_fit_plan, scale_budget_plan]
    delta_fields: [findings, decisions, uncertainties, open_questions]
  robustness:
    produces: [perturbation_stress_matrix, severity_axes, baseline_comparison, degradation_metrics, survival_criteria]
    delta_fields: [findings, decisions, uncertainties, open_questions]
```

## Thresholds and quality gates

- `experiment-design` HARD-GATE and Budget Gate remain mandatory; no exit before declared minimum yield.
- Resource and run-scale gates are relative to the declared resource envelope and eligible factor/condition space; record numerator, denominator, batch increment, stopping reason, and source references.
- Scale, ablation, comparison, and robustness coverage must reach a justified relative floor over the declared design space; do not substitute an unreasoned fixed run count.
- Factor levels, comparison baseline, statistical test, significance threshold, sample-size rationale, and stopping rule must all be explicit.
- Significance threshold must be pre-registered, not chosen post-hoc.
- Budget-constrained design must report at least one feasible design under the stated resource envelope.
- Scaling mode retains the source criterion of a geometric progression, typically 4-8 points, while evaluating coverage relative to the declared scale domain. Relative audit: declared universe = eligible scale domain; numerator = scale points instantiated; batch increment = points added per design pass; stopping reason = predeclared coverage or saturation rule; source references = scaling-design ledger and design records; direction/threshold rationale = geometric spacing preserves regime sensitivity, with 4-8 retained as the source band.

## Failure and counterexamples

Reject post-hoc factor selection, outcome leakage, missing control, unpowered comparison, or a design whose claimed inference exceeds its measured outcome.

## Provenance map

`experiment-design`, `factor-level-design`, `ablation-design`, `comparison-design`, `scaling-design`, `robustness-design`, `statistical-method-selection`, `reproducibility-protocol`, `budget-constrained-design`; mode-specific steps retained, agent dispatch removed.

## Legacy context checkpoint / Delta notes

Record hypothesis ID, design mode, factors/levels, analysis plan, budget, preregistration status, and unresolved threats.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| experiment-design | 45 | textual | ## HARD-GATE |
| experiment-design | 47 | textual | Before entering this campaign, the following must be satisfied: |
| experiment-design | 64 | textual | 4. How to ensure reproducibility |
| experiment-design | 79 | textual | ## Budget Gate |
| experiment-design | 83 | numeric | \\| Micro \\| < 10 \\| 3 \\| 20 \\| Fractional factorial or single ablation \\| |
| experiment-design | 84 | numeric | \\| Small \\| 10-100 \\| 5 \\| 50 \\| Full factorial on key factors \\| |
| experiment-design | 85 | numeric | \\| Medium \\| 100-1000 \\| 8 \\| 200 \\| Multi-strategy composition \\| |
| experiment-design | 86 | numeric | \\| Large \\| > 1000 \\| Unlimited \\| Unlimited \\| Full design space exploration \\| |
| experiment-design | 95 | textual | ## Minimum Yield |
| experiment-design | 97 | textual | Every campaign invocation must produce at minimum: |
| ablation-design | 43 | textual | ## Budget Gate |
| ablation-design | 47 | numeric | \\| Systematic (leave-one-out) \\| 3-8 \\| N + 2 \\| Standard component analysis \\| |
| ablation-design | 48 | numeric | \\| Replacement \\| 3-8 \\| 2N + 2 \\| Need to distinguish "removal" vs "simplification" \\| |
| ablation-design | 49 | numeric | \\| Combinatorial (selected) \\| 4-6 \\| ~2N \\| Suspected interactions between components \\| |
| ablation-design | 50 | numeric | \\| Combinatorial (full) \\| 3-4 \\| 2^N \\| Small systems, need complete picture \\| |
| ablation-design | 51 | numeric | \\| Conditional \\| 3-6 \\| N * conditions \\| Context-dependent contributions \\| |
| comparison-design | 34 | textual | - **Fair Comparison Protocol** (Bouthillier 2021): Control all confounds, same compute budget, same tuning effort. |
| comparison-design | 47 | textual | 6. **reproducibility-protocol** (tactic) -> Ensure all results are reproducible |
| comparison-design | 50 | textual | ## Budget Gate |
| comparison-design | 54 | numeric-table | \\| Minimal \\| 1 SOTA + 1 simple \\| 1 \\| 3 \\| 6 \\| |
| comparison-design | 55 | numeric | \\| Standard \\| 2-3 baselines \\| 2-3 \\| 5 \\| 30-45 \\| |
| comparison-design | 56 | numeric | \\| Comprehensive \\| 4+ baselines \\| 3-5 \\| 5-10 \\| 100+ \\| |
| comparison-design | 57 | numeric-table | \\| Publication-ready \\| All relevant \\| 5+ \\| 10+ \\| 200+ \\| |
| scaling-design | 43 | numeric | 2. **level-specification** -> Define scale points (geometric progression, typically 4-8 points) |
| scaling-design | 49 | textual | ## Budget Gate |
| scaling-design | 53 | numeric | \\| Data scaling \\| 4-6 \\| 3 \\| 12-18 \\| Low (same model, subset data) \\| |
| scaling-design | 54 | numeric | \\| Model scaling \\| 4-8 \\| 2-3 \\| 8-24 \\| High (different model sizes) \\| |
| scaling-design | 55 | numeric | \\| Compute-optimal \\| 6-10 per iso-FLOP \\| 1-2 \\| 12-20 \\| Very high \\| |
| scaling-design | 56 | numeric | \\| Inference scaling \\| 5-10 \\| 5 \\| 25-50 \\| Low (inference only) \\| |
| robustness-design | 50 | textual | ## Budget Gate |
| robustness-design | 54 | numeric | \\| Single perturbation \\| 1 \\| 3-5 \\| 3-5 \\| Quick sanity check \\| |
| robustness-design | 55 | numeric | \\| Multi-perturbation \\| 3-5 \\| 3 each \\| 9-15 \\| Standard robustness eval \\| |
| robustness-design | 56 | numeric | \\| Adversarial sweep \\| 1 attack \\| 5-10 epsilon \\| 5-10 \\| Adversarial robustness curve \\| |
| robustness-design | 57 | numeric | \\| Comprehensive \\| 5+ types \\| 3-5 each \\| 50+ \\| Publication-ready robustness \\| |
| robustness-design | 58 | numeric-table | \\| Cross-domain \\| N domains \\| 1 \\| N \\| Transfer evaluation \\| |
| statistical-method-selection | 30 | numeric-table | \\| Normal data, 2 groups, paired \\| Paired t-test \\| |
| statistical-method-selection | 31 | numeric-table | \\| Normal data, 2 groups, unpaired \\| Welch's t-test \\| |
| statistical-method-selection | 32 | numeric-table | \\| Normal data, 3+ groups \\| ANOVA + post-hoc (Tukey HSD) \\| |
| statistical-method-selection | 33 | numeric-table | \\| Non-normal, 2 groups \\| Wilcoxon signed-rank / Mann-Whitney U \\| |
| statistical-method-selection | 34 | numeric-table | \\| Non-normal, 3+ groups \\| Kruskal-Wallis + Dunn's test \\| |
| statistical-method-selection | 36 | numeric-table | \\| Want probability of superiority \\| Bayesian comparison (Benavoli 2017) \\| |
| statistical-method-selection | 48 | textual | - Is the significance threshold pre-registered (not chosen post-hoc)? |
| reproducibility-protocol | 17 | textual | # Tactic: Reproducibility Protocol |
| reproducibility-protocol | 21 | textual | 1. **Assess Reproducibility Requirements** -> Determine level needed (exact, statistical, conceptual) |
| reproducibility-protocol | 22 | textual | 2. **seed-protocol-design** -> Design random seed strategy for all stochastic components |
| reproducibility-protocol | 24 | textual | 4. **Define Verification Plan** -> How to confirm reproducibility (re-run subset, cross-machine test) |
| reproducibility-protocol | 25 | textual | 5. **Document Non-Determinism** -> Identify and document unavoidable sources of variance |
| reproducibility-protocol | 29 | textual | \\| Reproducibility Level \\| Requirement \\| When to Use \\| |
| reproducibility-protocol | 37 | textual | - Are all random seeds documented and controllable? |
| reproducibility-protocol | 38 | textual | - Is the full software environment captured (versions, dependencies)? |
| reproducibility-protocol | 39 | textual | - Are hardware-specific non-determinisms identified (GPU atomics, cuDNN)? |
| reproducibility-protocol | 40 | textual | - Is there a verification protocol (re-run N times, check variance)? |
| reproducibility-protocol | 44 | textual | - Is there a plan for cross-machine reproducibility testing? |
| budget-constrained-design | 34 | numeric | \\| < 10 \\| One-factor-at-a-time or Plackett-Burman screening \\| |
| budget-constrained-design | 35 | numeric | \\| 10-30 \\| Fractional factorial (Resolution III-IV) \\| |
| budget-constrained-design | 36 | numeric | \\| 30-60 \\| Fractional factorial (Resolution V) or Taguchi \\| |
| budget-constrained-design | 37 | numeric | \\| 60-120 \\| Full factorial on top factors + screening on rest \\| |
| budget-constrained-design | 38 | numeric-table | \\| 120+ \\| Full factorial or RSM with replication \\| |
| budget-constrained-design | 53 | textual | - Are early stopping criteria pre-defined (not post-hoc)? |

## Context checkpoint / Delta notes

Record hypothesis ID, design mode, factors/levels, analysis plan, budget, preregistration status, and unresolved threats.
