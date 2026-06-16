---
name: morris-screening
description: Morris method screening — compute elementary effects to quickly identify
  important vs unimportant parameters.
execution: subagent
prompt: ./prompt.md
input: parameter_space_definition, model_description
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete Morris screening analysis (trajectories designed, elementary effects computed, parameters ranked).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
