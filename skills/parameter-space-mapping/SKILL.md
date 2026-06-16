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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
