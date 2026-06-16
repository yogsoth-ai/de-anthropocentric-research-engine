---
name: coverage-scoring
description: Compute coverage completeness, redundancy, and gap severity scores from
  a coverage map.
execution: subagent
prompt: ./prompt.md
input: coverage_map
dependencies:
  sops:
  - spawn-agent
---

# Coverage Scoring

Compute quantitative scores for portfolio coverage completeness, redundancy levels, and gap severity from the candidate-to-niche coverage map.

## Execution

Spawns a subagent that applies scoring algorithms to the coverage map and produces actionable metrics.

## Why Subagent

Scoring requires consistent application of metrics across the full coverage map with attention to edge cases (partial coverage, weighted importance). Focused execution ensures no niches are overlooked.

## HARD-GATE

Output must include a numeric coverage score (0-1), redundancy score (0-1), and severity-ranked gap list. All scores must be justified with methodology.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
