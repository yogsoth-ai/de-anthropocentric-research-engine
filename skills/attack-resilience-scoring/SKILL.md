---
name: attack-resilience-scoring
description: Compute overall resilience score (0.0-1.0) based on attack results, coverage,
  and vulnerability severity distribution.
execution: subagent
prompt: ./prompt.md
input: aggregated_findings (string), coverage_data (string)
dependencies:
  sops:
  - spawn-agent
---

# Attack Resilience Scoring

Computes a quantitative resilience score for the artifact based on red team results.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Scoring requires calibrated judgment independent of attack or defense bias. The scorer must weigh findings objectively against coverage.

## Input

- **aggregated_findings**: Deduplicated vulnerability report from finding-aggregation
- **coverage_data**: What percentage of threat surfaces were tested, at what depth

## Output

- **resilience_score**: 0.0-1.0 overall score
- **dimension_scores**: Per-dimension breakdown (logical, empirical, methodological, practical)
- **confidence_in_score**: How much to trust the score given coverage gaps
- **verdict**: Pass/conditional-pass/fail with justification

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
