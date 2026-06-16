---
name: divergence-detection
description: Identifies agreement and disagreement patterns across multiple perspective
  evaluations. Maps consensus clusters and persistent divergence points.
execution: subagent
prompt: ./prompt.md
input: perspective_outputs (string), round_number (string)
dependencies:
  sops:
  - spawn-agent
---

# Divergence Detection

Identifies agreement/disagreement across perspectives.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Divergence analysis requires comparing all perspective outputs simultaneously in dedicated context without being anchored to any single perspective.

## Input

- **perspective_outputs**: All perspective-critic outputs from current round
- **round_number**: Current deliberation round (for tracking convergence trend)

## Output

- **consensus_points**: Issues where >70% of perspectives agree
- **divergence_points**: Issues where >50% of perspectives disagree
- **convergence_trend**: Whether disagreements are shrinking, stable, or growing
- **irreconcilable**: Points unlikely to resolve through further deliberation

## Budget

One unit = one divergence analysis per round.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
