---
name: gap-typology-classification
description: Classify gaps using Miles 7-type taxonomy (theoretical, methodological,
  empirical, population, practical, knowledge void, evidence gap).
execution: subagent
prompt: ./prompt.md
input: gap_description (string), evidence (string)
dependencies:
  sops:
  - spawn-agent
---

# Gap Typology Classification

Classify research gaps by type using established taxonomies.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one gap classification pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
