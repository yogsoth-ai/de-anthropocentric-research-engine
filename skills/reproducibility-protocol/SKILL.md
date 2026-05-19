---
name: reproducibility-protocol
description: "Ensure experiment reproducibility through systematic environment and seed control"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: experiment-design
orchestrates:
  - seed-protocol-design
  - environment-specification
---

# Tactic: Reproducibility Protocol

## Orchestration Pattern

1. **Assess Reproducibility Requirements** → Determine level needed (exact, statistical, conceptual)
2. **seed-protocol-design** → Design random seed strategy for all stochastic components
3. **environment-specification** → Lock all software, hardware, and configuration dependencies
4. **Define Verification Plan** → How to confirm reproducibility (re-run subset, cross-machine test)
5. **Document Non-Determinism** → Identify and document unavoidable sources of variance

## Decision Criteria

| Reproducibility Level | Requirement | When to Use |
|----------------------|-------------|-------------|
| Exact (bit-for-bit) | Same hardware + deterministic ops | Debugging, verification |
| Statistical (within CI) | Same distribution of results | Standard research |
| Conceptual (same conclusion) | Same qualitative findings | Cross-platform validation |

## Quality Checks

- Are all random seeds documented and controllable?
- Is the full software environment captured (versions, dependencies)?
- Are hardware-specific non-determinisms identified (GPU atomics, cuDNN)?
- Is there a verification protocol (re-run N times, check variance)?
- Are data preprocessing steps deterministic or seeded?
- Is the order of data loading controlled?
- Are model initialization seeds separate from data shuffling seeds?
- Is there a plan for cross-machine reproducibility testing?
