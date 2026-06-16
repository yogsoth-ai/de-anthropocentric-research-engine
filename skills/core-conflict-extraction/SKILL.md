---
name: core-conflict-extraction
description: Extract core conflict in Evaporating Cloud format (A-B-C-D-D')
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: causal tree root causes, identified dilemmas
output: Evaporating Cloud with assumptions on each arrow
dependencies:
  sops:
  - spawn-agent
---

# SOP: Core Conflict Extraction

Extract the core conflict from identified root causes and express it in Goldratt's Evaporating Cloud format (A-B-C-D-D') with explicit assumptions on each arrow.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
