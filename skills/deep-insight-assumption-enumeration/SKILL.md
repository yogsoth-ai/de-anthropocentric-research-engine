---
name: deep-insight-assumption-enumeration
description: Systematically identify all assumptions in a method/model — structural,
  parametric, distributional, and scope assumptions.
execution: subagent
prompt: ./prompt.md
input: method_description (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Assumption Enumeration

Exhaustively list all assumptions in a method.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one assumption enumeration pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
