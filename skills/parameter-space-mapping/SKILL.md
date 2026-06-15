---
name: parameter-space-mapping
description: Identify all parameter dimensions along which a claim's validity might
  vary.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Parameter Space Mapping

Subagent that identifies the complete set of dimensions (parameters, conditions, contexts) relevant to a claim's validity.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
