---
name: function-model-construction
description: Build substance-field functional model of a system, annotating useful,
  harmful, insufficient, and excessive interactions.
execution: subagent
prompt: ./prompt.md
input: system_description (string)
dependencies:
  sops:
  - spawn-agent
---

# Function Model Construction

Build a substance-field functional model for system analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Functional modeling requires careful identification of all system components and their interactions, classifying each interaction type. Benefits from dedicated analytical context without distraction from downstream operations.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
