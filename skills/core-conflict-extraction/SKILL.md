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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
