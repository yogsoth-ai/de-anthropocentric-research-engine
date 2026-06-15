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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
