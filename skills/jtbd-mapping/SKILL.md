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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
