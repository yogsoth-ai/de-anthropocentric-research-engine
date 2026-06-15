---
name: sensitivity-analysis
description: Tests conclusion robustness by perturbing parameters and observing rank
  changes. Shared across scoring, portfolio, and steel-manning campaigns.
execution: subagent
prompt: ./prompt.md
input: parameter_set[], perturbation_range (float), current_ranking[]
dependencies:
  sops:
  - spawn-agent
---

# Sensitivity Analysis

Tests whether convergence conclusions are robust to parameter perturbation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Sensitivity analysis requires systematic exploration of parameter space with fresh perspective on each perturbation. Dedicated context prevents confirmation bias toward the original result.

## HARD-GATE

Must perturb ≥3 parameters. A single-parameter sensitivity check is insufficient for robustness claims.
