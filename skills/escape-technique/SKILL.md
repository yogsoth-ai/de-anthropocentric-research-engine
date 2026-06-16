---
name: escape-technique
description: Identify dominant thinking pattern and escape it via deliberate pattern-breaking.
execution: subagent
prompt: ./prompt.md
input: current_thinking (string)
dependencies:
  sops:
  - spawn-agent
---

# Escape Technique

Identify dominant thinking pattern and escape it.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Escape requires first identifying the dominant pattern (which is invisible to those inside it) and then deliberately breaking free. Benefits from dedicated context that can analyze the thinking pattern from outside.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
