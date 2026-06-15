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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
