---
name: factor-level-design
description: Design factorial experiments to test how specific factors affect outcomes
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- factor-identification
- level-specification
- design-matrix-construction
- metric-specification
- sample-size-estimation
tactics:
- budget-constrained-design
- statistical-method-selection
dependencies:
  sops:
  - design-matrix-construction
  - experiment-config-generation
  - factor-identification
  - level-specification
  - metric-specification
  - sample-size-estimation
  tactics:
  - budget-constrained-design
  - statistical-method-selection
---

# Strategy: Factor-Level Design

**Question**: Which factors to test at what levels in combination?

## Methodology

- **Full Factorial** (Fisher): All combinations of all factor levels. Gold standard but exponential cost.
- **Fractional Factorial**: Systematic subset using defining relations. Sacrifices high-order interactions.
- **Plackett-Burman**: Screening design for many factors. Identifies main effects only.
- **Response Surface Methodology (RSM)**: Central Composite / Box-Behnken for optimization after screening.
- **Taguchi Orthogonal Arrays**: Robust design minimizing variance from noise factors.

## Execution Flow

1. **factor-identification** → Identify all independent, dependent, and control variables
2. **level-specification** → Determine discrete levels for each factor (2-5 levels typical)
3. **budget-constrained-design** (tactic) → Select design type given budget constraints
4. **design-matrix-construction** → Build the actual design matrix
5. **metric-specification** → Define primary/secondary metrics and significance thresholds
6. **sample-size-estimation** → Power analysis to determine runs per cell

## Budget Gate

| Design Type | Factors | Runs (k factors, 2 levels) | When to Use |
|-------------|---------|---------------------------|-------------|
| Full Factorial | 2-4 | 2^k | Budget allows, need all interactions |
| Fractional (Res V) | 4-6 | 2^(k-1) | Need 2-factor interactions |
| Fractional (Res III) | 5-8 | 2^(k-p) | Screening, main effects only |
| Plackett-Burman | 8-15 | k+1 (nearest multiple of 4) | Many factors, screening phase |
| Taguchi L9/L18 | 4-8 | 9 or 18 | Robust design with noise factors |
| RSM (CCD) | 2-5 | 2^k + 2k + center | Optimization after screening |

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| budget-constrained-design | Optimize experiment design under compute and time budget constraints |
| statistical-method-selection | Select appropriate statistical methods for experiment analysis |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| design-matrix-construction | Build the experiment design matrix with proper orthogonality and balance |
| experiment-config-generation | SOP: generate executable experiment configuration files |
| factor-identification | Identify independent, dependent, and control variables for an experiment |
| level-specification | Determine appropriate levels for each experimental factor |
| metric-specification | Define experiment metrics and significance standards |
| sample-size-estimation | SOP: power analysis and required experiment count estimation |

<!-- END available-tables (generated) -->
