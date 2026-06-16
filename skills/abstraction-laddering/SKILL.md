---
name: abstraction-laddering
description: Move between concrete and abstract framings — 3 levels up (Why?) and
  3 levels down (How?) to find the most productive research level.
execution: subagent
prompt: ./prompt.md
input: problem_statement (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Abstraction Laddering

Navigate abstraction levels to find productive framings.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one abstraction ladder construction.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
