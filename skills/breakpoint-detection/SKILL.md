---
name: breakpoint-detection
description: Test a claim at extreme parameter values and detect the precise point
  where it breaks down.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Breakpoint Detection

Subagent that evaluates a claim at extreme values to find the precise breakpoint where validity fails.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
