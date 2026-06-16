---
name: abstraction-to-design
description: Abstract biological principle to design principle. Bridge from biology
  to engineering.
execution: subagent
prompt: ./prompt.md
input: biological_strategy (string)
dependencies:
  sops:
  - spawn-agent
---

# Abstraction to Design

Abstract biological principle to design principle.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Abstraction requires careful removal of biological specifics while preserving the functional essence, then mapping to engineering design space. Benefits from focused analytical attention to avoid over-literal or over-abstract transfers.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
