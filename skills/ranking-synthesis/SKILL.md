---
name: ranking-synthesis
description: Produce the final ranking artifact from converged ratings and consistency
  report.
execution: subagent
prompt: ./prompt.md
input: ratings(object), consistency_report(object)
dependencies:
  sops:
  - spawn-agent
---

# Ranking Synthesis

Produces the final, presentation-ready ranking from converged ratings and consistency verification. Combines quantitative scores with confidence intervals, method metadata, and quality indicators into the deliverable artifact.

## Execution

Runs as a subagent. Receives final ratings and consistency report, returns the formatted ranking artifact.

## Why Subagent

Synthesis requires formatting decisions, confidence interval computation, and quality narrative generation that benefit from focused attention without orchestration overhead.

## HARD-GATE

Output MUST rank ALL candidates. Output MUST include confidence intervals. Output MUST reference the consistency status. No candidate may be omitted from the final ranking.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
