---
name: deep-insight-validity-envelope-construction
description: Combine multi-axis perturbation data into a multi-dimensional validity
  description with boundary conditions and interaction effects.
execution: subagent
prompt: ./prompt.md
input: perturbation_data (string), axes (string)
dependencies:
  sops:
  - spawn-agent
---

# Validity Envelope Construction

Construct the multi-dimensional validity boundary.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one envelope construction from perturbation data.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
