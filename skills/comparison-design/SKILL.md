---
name: comparison-design
description: Design fair comparison experiments against baselines and competing methods
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- baseline-selection
- metric-specification
- sample-size-estimation
- seed-protocol-design
- environment-specification
tactics:
- statistical-method-selection
- reproducibility-protocol
dependencies:
  sops:
  - baseline-selection
  - environment-specification
  - metric-specification
  - sample-size-estimation
  - seed-protocol-design
  tactics:
  - reproducibility-protocol
  - statistical-method-selection
---

# Strategy: Comparison Design

**Question**: How much better is our method than the baseline?

## Methodology

- **Fair Comparison Protocol** (Bouthillier 2021): Control all confounds, same compute budget, same tuning effort.
- **Multi-Baseline Comparison**: Compare against multiple baselines (SOTA, simple, ablated).
- **Multi-Dataset Evaluation**: Test across diverse datasets to avoid dataset-specific overfitting.
- **Bayesian Comparison** (Benavoli 2017): Posterior probability of superiority, not just p-values.
- **Bootstrap/Permutation Tests**: Non-parametric significance without distributional assumptions.

## Execution Flow

1. **baseline-selection** → Select appropriate baselines (SOTA, simple, oracle)
2. **metric-specification** → Define primary metric and secondary metrics
3. **sample-size-estimation** → Power analysis for detecting meaningful differences
4. **seed-protocol-design** → Ensure fair random initialization across methods
5. **environment-specification** → Lock environment to prevent confounds
6. **reproducibility-protocol** (tactic) → Ensure all results are reproducible
7. **statistical-method-selection** (tactic) → Choose Bayesian or frequentist comparison

## Budget Gate

| Comparison Scope | Baselines | Datasets | Seeds | Min Runs |
|-----------------|-----------|----------|-------|----------|
| Minimal | 1 SOTA + 1 simple | 1 | 3 | 6 |
| Standard | 2-3 baselines | 2-3 | 5 | 30-45 |
| Comprehensive | 4+ baselines | 3-5 | 5-10 | 100+ |
| Publication-ready | All relevant | 5+ | 10+ | 200+ |

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| reproducibility-protocol | Ensure experiment reproducibility through systematic environment and seed control |
| statistical-method-selection | Select appropriate statistical methods for experiment analysis |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| baseline-selection | Select appropriate baselines for experimental comparison |
| environment-specification | SOP: define complete experiment environment specification |
| metric-specification | Define experiment metrics and significance standards |
| sample-size-estimation | SOP: power analysis and required experiment count estimation |
| seed-protocol-design | SOP: design random seed strategy for reproducibility |

<!-- END available-tables (generated) -->
