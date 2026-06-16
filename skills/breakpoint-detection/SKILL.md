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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
