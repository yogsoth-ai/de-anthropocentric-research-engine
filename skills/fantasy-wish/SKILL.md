---
name: fantasy-wish
description: Unconstrained wish-fulfillment ideation. Ignore all physical laws to
  imagine the ideal solution, then identify realization directions.
execution: subagent
prompt: ./prompt.md
input: problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Fantasy Wish

Unconstrained wish-fulfillment ideation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Fantasy ideation requires complete suspension of critical judgment and physical constraints. Benefits from dedicated imaginative space without analytical interference pulling ideas back to feasibility prematurely.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
