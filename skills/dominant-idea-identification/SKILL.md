---
name: dominant-idea-identification
description: Identify dominant paradigms and assumptions constraining thinking in
  a research field.
execution: subagent
prompt: ./prompt.md
input: research_domain_description
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete dominant idea analysis for a research domain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
