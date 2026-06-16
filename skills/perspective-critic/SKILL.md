---
name: perspective-critic
description: Evaluates artifact from a specific assigned perspective. Produces assessment
  grounded in that viewpoint's values, priorities, and expertise.
execution: subagent
prompt: ./prompt.md
input: artifact (string), perspective (string), other_perspectives_output (string)
dependencies:
  sops:
  - spawn-agent
---

# Perspective Critic

Evaluates artifact from a specific assigned perspective.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Each perspective requires dedicated context to maintain viewpoint consistency. Mixing perspectives in one context leads to averaging rather than genuine diversity.

## Input

- **artifact**: The artifact being evaluated
- **perspective**: Assigned viewpoint (e.g., "methodological skeptic", "domain expert", "practitioner")
- **other_perspectives_output**: Previous outputs from other perspectives (empty in round 1)

## Output

- **assessment**: Structured evaluation from this perspective
- **concerns**: Issues visible from this viewpoint
- **strengths**: Positives visible from this viewpoint
- **confidence**: How viable the artifact appears from this perspective (0.0–1.0)

## Budget

One unit = one perspective evaluation per round.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
