---
name: bottleneck-identification
description: Identify bottleneck dimensions from radar data with severity ranking.
execution: subagent
prompt: ./prompt.md
input: radar_data
dependencies:
  sops:
  - spawn-agent
---

# Bottleneck Identification

Analyze radar chart data to identify which dimensions are bottlenecks — the limiting factors that constrain overall feasibility. Produces a severity-ranked list of bottlenecks with analysis of why each is limiting.

## Execution

Spawns a subagent that:
1. Receives radar synthesis data
2. Identifies dimensions scoring significantly below the mean or below required thresholds
3. Analyzes why each bottleneck is limiting (gap analysis)
4. Ranks bottlenecks by severity and impact on overall feasibility
5. Suggests which bottleneck to address first

## Why Subagent

Bottleneck identification requires comparative analysis across dimensions and judgment about which low scores are truly limiting vs. acceptable given the context.

## HARD-GATE

Output MUST include: at least 1 bottleneck identified, severity ranking, and prioritized recommendation. Reject if no bottlenecks are identified (even high-readiness candidates have relative bottlenecks).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
