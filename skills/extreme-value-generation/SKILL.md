---
name: extreme-value-generation
description: Generate boundary and extreme test values for a given parameter dimension
  to stress-test claims.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Extreme Value Generation

Subagent that produces extreme, boundary, and pathological values for a parameter dimension to probe claim validity.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
