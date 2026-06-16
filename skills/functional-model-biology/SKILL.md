---
name: functional-model-biology
description: Build biological system functional model. Map energy, matter, and information
  flows.
execution: subagent
prompt: ./prompt.md
input: biological_system (string)
dependencies:
  sops:
  - spawn-agent
---

# Functional Model Biology

Build biological system functional model.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Functional modeling of biological systems requires understanding multi-scale interactions and mapping energy/matter/information flows. Benefits from dedicated analytical attention to produce accurate system models.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
