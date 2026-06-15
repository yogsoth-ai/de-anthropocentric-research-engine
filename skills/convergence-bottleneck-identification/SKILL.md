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
