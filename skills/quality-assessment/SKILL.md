---
name: quality-assessment
description: Methodological rigor scoring for papers — evaluates bias risk, reproducibility,
  sample adequacy using established frameworks. Used by systematic-survey.
execution: subagent
prompt: ./prompt.md
input: paper_details (string)
dependencies:
  sops:
  - spawn-agent
---

# Quality Assessment

Evaluate research rigor using established quality assessment frameworks.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Quality assessment requires applying consistent criteria across multiple papers while maintaining objectivity. Dedicated context ensures the assessment framework is applied uniformly.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
