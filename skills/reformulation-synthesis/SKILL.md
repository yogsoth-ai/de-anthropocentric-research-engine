---
name: reformulation-synthesis
description: Compile all problem reformulation analyses into a coherent report with
  a recommended new problem definition.
execution: subagent
prompt: ./prompt.md
input: dominant_ideas, provocations, perspectives, dialectics, wickedness_assessment,
  appreciative_findings
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete reformulation synthesis report.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
