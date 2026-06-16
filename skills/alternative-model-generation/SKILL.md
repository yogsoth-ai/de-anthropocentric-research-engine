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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
