---
name: assumption-extraction
description: Systematically extract all assumptions (stated, implicit, boundary, mathematical,
  practical) from a method or model.
execution: subagent
prompt: ./prompt.md
input: method_description
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete assumption extraction from a method/model description.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
