---
name: scaling-design
description: Design scaling experiments to characterize performance-resource relationships
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- factor-identification
- level-specification
- metric-specification
- sample-size-estimation
- design-matrix-construction
tactics:
- statistical-method-selection
- budget-constrained-design
dependencies:
  sops:
  - design-matrix-construction
  - factor-identification
  - level-specification
  - metric-specification
  - sample-size-estimation
  tactics:
  - budget-constrained-design
  - statistical-method-selection
---

# Strategy: Scaling Design

**Question**: How does performance scale with resources?

## Methodology

- **Neural Scaling Laws** (Kaplan 2020, Hoffmann 2022): Power-law relationships between compute/data/parameters and loss.
- **Compute-Optimal Scaling** (Chinchilla): Find optimal allocation between model size and data.
- **Data Scaling**: Characterize learning curves as function of dataset size.
- **Model Scaling**: Performance vs. parameter count at fixed data.
- **Inference Scaling**: Throughput/latency vs. batch size, sequence length, model size.

## Execution Flow

1. **factor-identification** → Identify scaling axes (data, compute, parameters, time)
2. **level-specification** → Define scale points (geometric progression, typically 4-8 points)
3. **metric-specification** → Define metrics at each scale (loss, downstream task, efficiency)
4. **design-matrix-construction** → Build scaling experiment grid
5. **sample-size-estimation** → Determine replicates needed for reliable curve fitting
6. **budget-constrained-design** (tactic) → Optimize which scale points to run given budget

## Budget Gate

| Scaling Type | Scale Points | Replicates | Min Runs | Typical Cost |
|-------------|-------------|------------|----------|--------------|
| Data scaling | 4-6 | 3 | 12-18 | Low (same model, subset data) |
| Model scaling | 4-8 | 2-3 | 8-24 | High (different model sizes) |
| Compute-optimal | 6-10 per iso-FLOP | 1-2 | 12-20 | Very high |
| Inference scaling | 5-10 | 5 | 25-50 | Low (inference only) |

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| budget-constrained-design | Optimize experiment design under compute and time budget constraints |
| statistical-method-selection | Select appropriate statistical methods for experiment analysis |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| design-matrix-construction | Build the experiment design matrix with proper orthogonality and balance |
| factor-identification | Identify independent, dependent, and control variables for an experiment |
| level-specification | Determine appropriate levels for each experimental factor |
| metric-specification | Define experiment metrics and significance standards |
| sample-size-estimation | SOP: power analysis and required experiment count estimation |

<!-- END available-tables (generated) -->
