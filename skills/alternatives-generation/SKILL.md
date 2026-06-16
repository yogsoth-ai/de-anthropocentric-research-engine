---
name: alternatives-generation
description: Generate alternatives for every known approach — ensure no approach goes
  unchallenged.
execution: subagent
prompt: ./prompt.md
input: known_approaches (string)
dependencies:
  sops:
  - spawn-agent
---

# Alternatives Generation

Generate alternatives for every known approach.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Alternatives generation requires systematically considering each known approach and producing genuinely different alternatives (not variations). Benefits from dedicated context that can maintain the "different, not better" mindset.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
