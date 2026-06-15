---
name: blend-elaboration
description: Run blend as mental simulation
execution: subagent
prompt: ./prompt.md
input: completed_blend (object)
dependencies:
  sops:
  - spawn-agent
---

# Blend Elaboration

Run blend as mental simulation — let the blend "run" according to its own logic to discover consequences, implications, and additional emergent properties.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Blend elaboration requires imaginative simulation — running the blend forward in time, exploring consequences, and discovering properties that only emerge through dynamic interaction. Benefits from sustained imaginative focus.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
