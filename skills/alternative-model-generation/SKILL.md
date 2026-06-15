---
name: alternative-model-generation
description: Generate alternative model formulations by relaxing, replacing, or generalizing
  specific assumptions.
execution: subagent
prompt: ./prompt.md
input: original_model (string), assumption_to_relax (string)
dependencies:
  sops:
  - spawn-agent
---

# Alternative Model Generation

Generate model variants by relaxing assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one alternative model generation pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
