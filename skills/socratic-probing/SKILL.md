---
name: socratic-probing
description: Apply 6 types of Socratic questions to test claims and assumptions. Exposes
  weaknesses and strengthens reasoning.
execution: subagent
prompt: ./prompt.md
input: claim_or_assumption (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Socratic Probing

Test claims via systematic Socratic questioning.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one Socratic probing pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
