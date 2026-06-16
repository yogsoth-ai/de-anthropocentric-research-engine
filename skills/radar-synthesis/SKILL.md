---
name: radar-synthesis
description: Synthesize multiple dimension scores into radar chart data and compute
  overall readiness.
execution: subagent
prompt: ./prompt.md
input: dimension_scores[]
dependencies:
  sops:
  - spawn-agent
---

# Radar Synthesis

Combine individual dimension assessment scores into a unified radar chart representation and compute an overall readiness score. Produces visualization-ready data and a narrative summary.

## Execution

Spawns a subagent that:
1. Receives all dimension scores for a candidate
2. Normalizes scores to a common scale
3. Computes weighted overall readiness
4. Structures data for radar chart visualization
5. Produces narrative summary of the readiness profile

## Why Subagent

Synthesis requires holistic analysis of the score pattern — identifying asymmetries, computing weighted averages, and producing narrative interpretation that considers dimension interactions.

## HARD-GATE

Output MUST include: radar_chart_data with all dimensions, overall_readiness score, and narrative summary. Reject if any dimension from input is missing in output.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
