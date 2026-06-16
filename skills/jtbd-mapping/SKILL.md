---
name: jtbd-mapping
description: Map stakeholder Jobs-to-be-Done — functional, emotional, and social jobs
  for each affected party. Identifies unserved jobs as opportunity signals.
execution: subagent
prompt: ./prompt.md
input: research_domain (string), stakeholder_list (string)
dependencies:
  sops:
  - spawn-agent
---

# JTBD Mapping

Map stakeholder jobs-to-be-done to reveal unserved needs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one JTBD mapping pass across stakeholders.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
