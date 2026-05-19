---
name: gap-synthesis
description: Compile all gap analysis intermediate products into a coherent final report with executive summary, detailed findings, and research agenda.
execution: subagent
prompt: ./prompt.md
input: intermediate_products (string), report_scope (string)
used-by: gap-synthesis-strategy
---

# Gap Synthesis

Compile gap analysis products into a final coherent report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one synthesis report generation.
