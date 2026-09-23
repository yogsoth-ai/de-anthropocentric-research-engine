---
name: apply-perturbation
description: "Apply a controlled change to an assumption, factor, component, parameter, or condition and record response."
---

# apply-perturbation

## Purpose

Apply a controlled change to an assumption, factor, component, parameter, or condition and record the response.

## Input contract

```yaml
required: [baseline_artifact, perturbation_target, perturbation_axis, response_metric]
optional: [variation_range, removal_mode, factor_list, uncertainty_model]
constraints: [change one declared target or axis at a time unless the caller explicitly supplies an interaction design; preserve baseline comparability]
```

## Procedure

1. Record the baseline artifact, target, axis, response metric, and comparison direction.
2. Generate the caller-specified variation, removal, negation, or ablation conditions.
3. Re-evaluate the response at each condition and attach evidence and uncertainty.
4. Identify degradation, flip points, or threshold regions and summarize the effect.

## Output contract

```yaml
produces: [perturbation_series, response_comparison, degradation_or_flip_points, interpretation]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Controlled perturbation records performance at each point along one defined axis and identifies degradation thresholds where applicable.
- Single-factor removal retains a degradation score from 0.0 (no effect) to 1.0 (collapse) and states conclusion before/after.
- Ablation removes components one by one; do not combine removals while labeling the result single-factor.

## Parameterization

The caller must provide the baseline artifact or system, perturbation target and axis, range or removal mode, response metric, factor list when needed, and degradation/flip classification rule.

## Failure and counterexamples

Reject when the baseline is missing, the perturbation is not attributable, response measurements are incomparable, or a degradation score is reported without before/after reasoning.

## Provenance map

- resolved: deep-insight/controlled-perturbation
- concept: creative-ideation/assumption-perturbation
- resolved: creative-ideation/ablation-execution
- resolved: stress-test/single-factor-removal

## Verbatim source criteria excerpts

- `single-factor-removal` line 35: degradation_score: 0.0 (no effect) to 1.0 (collapse)

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| stress-test/single-factor-removal | 24 | numeric | Degradation score ranges from 0.0 (no effect) to 1.0 (collapse), with before/after conclusion and reasoning. |
