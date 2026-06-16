---
name: deep-insight-assumption-extraction
description: Systematically extract all assumptions (stated, implicit, boundary, mathematical,
  practical) from a method or model.
execution: subagent
prompt: ./prompt.md
input: method_description
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete assumption extraction from a method/model description.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
