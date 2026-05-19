---
name: scaling-design
description: "Design scaling experiments to characterize performance-resource relationships"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: experiment-design
sops:
  - factor-identification
  - level-specification
  - metric-specification
  - sample-size-estimation
  - design-matrix-construction
tactics:
  - statistical-method-selection
  - budget-constrained-design
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
