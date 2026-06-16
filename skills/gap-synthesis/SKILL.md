---
name: gap-synthesis
description: Compile all gap analysis intermediate products into a coherent final
  report with executive summary, detailed findings, and research agenda.
execution: subagent
prompt: ./prompt.md
input: intermediate_products (string), report_scope (string)
dependencies:
  sops:
  - spawn-agent
---

# Gap Synthesis

Compile gap analysis products into a final coherent report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one synthesis report generation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
