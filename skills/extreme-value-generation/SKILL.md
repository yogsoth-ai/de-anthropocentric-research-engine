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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
