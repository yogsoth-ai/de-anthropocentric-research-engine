---
name: budget-constrained-design
description: "Optimize experiment design under compute and time budget constraints"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: experiment-design
orchestrates:
  - factor-identification
  - level-specification
  - design-matrix-construction
---

# Tactic: Budget-Constrained Design

## Orchestration Pattern

1. **Assess Budget** → Determine available GPU-hours, wall-clock time, and cost ceiling
2. **factor-identification** → Identify all candidate factors
3. **Estimate Cost Per Run** → Calculate time/compute for a single experiment run
4. **Compute Maximum Runs** → budget / cost_per_run = max feasible runs
5. **level-specification** → Constrain levels to fit within run budget
6. **Select Design Type** → Choose most information-efficient design for the budget
7. **design-matrix-construction** → Build the constrained design matrix

## Decision Criteria

| Available Runs | Recommended Approach |
|---------------|---------------------|
| < 10 | One-factor-at-a-time or Plackett-Burman screening |
| 10-30 | Fractional factorial (Resolution III-IV) |
| 30-60 | Fractional factorial (Resolution V) or Taguchi |
| 60-120 | Full factorial on top factors + screening on rest |
| 120+ | Full factorial or RSM with replication |

## Optimization Strategies

- **Sequential Design**: Run screening first, then detailed study on important factors
- **Adaptive Allocation**: Allocate more runs to high-variance conditions
- **Early Stopping**: Define stopping criteria for clearly dominated configurations
- **Transfer from Pilot**: Use pilot study results to inform main study design
- **Shared Controls**: Reuse control/baseline runs across multiple comparisons

## Quality Checks

- Does the design have sufficient power for the primary hypothesis?
- Are the most important factors given priority in the allocation?
- Is there a contingency plan if budget is cut mid-experiment?
- Are early stopping criteria pre-defined (not post-hoc)?
- Is the design balanced despite budget constraints?
