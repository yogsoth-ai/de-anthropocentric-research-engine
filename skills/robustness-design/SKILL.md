---
name: robustness-design
description: Design experiments to identify failure boundaries and robustness limits
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- factor-identification
- level-specification
- baseline-selection
- metric-specification
- sample-size-estimation
- design-matrix-construction
tactics:
- statistical-method-selection
dependencies:
  sops:
  - baseline-selection
  - design-matrix-construction
  - factor-identification
  - level-specification
  - metric-specification
  - sample-size-estimation
  tactics:
  - statistical-method-selection
---

# Strategy: Robustness Design

**Question**: Under what conditions does the method fail?

## Methodology

- **Distribution Shift Testing**: Evaluate under covariate shift, label shift, domain shift.
- **Adversarial Robustness**: Perturbation-based attacks (PGD, AutoAttack) at varying epsilon.
- **Cross-Domain Transfer**: Test on domains not seen during training.
- **Noise Injection**: Gaussian noise, label noise, missing data at varying severity.
- **Stress Testing**: Push inputs to boundary conditions (extreme lengths, rare categories, edge cases).

## Execution Flow

1. **factor-identification** → Identify robustness dimensions (noise type, shift type, severity)
2. **level-specification** → Define severity levels for each perturbation
3. **baseline-selection** → Select robust baselines for comparison
4. **metric-specification** → Define degradation metrics (absolute and relative to clean)
5. **design-matrix-construction** → Build perturbation grid
6. **sample-size-estimation** → Determine samples needed per condition
7. **statistical-method-selection** (tactic) → Choose tests for degradation significance

## Budget Gate

| Robustness Type | Conditions | Severities | Min Runs | Notes |
|----------------|-----------|-----------|----------|-------|
| Single perturbation | 1 | 3-5 | 3-5 | Quick sanity check |
| Multi-perturbation | 3-5 | 3 each | 9-15 | Standard robustness eval |
| Adversarial sweep | 1 attack | 5-10 epsilon | 5-10 | Adversarial robustness curve |
| Comprehensive | 5+ types | 3-5 each | 50+ | Publication-ready robustness |
| Cross-domain | N domains | 1 | N | Transfer evaluation |

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| statistical-method-selection | Select appropriate statistical methods for experiment analysis |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| baseline-selection | Select appropriate baselines for experimental comparison |
| design-matrix-construction | Build the experiment design matrix with proper orthogonality and balance |
| factor-identification | Identify independent, dependent, and control variables for an experiment |
| level-specification | Determine appropriate levels for each experimental factor |
| metric-specification | Define experiment metrics and significance standards |
| sample-size-estimation | SOP: power analysis and required experiment count estimation |

<!-- END available-tables (generated) -->
