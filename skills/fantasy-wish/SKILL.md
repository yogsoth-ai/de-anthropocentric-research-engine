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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
