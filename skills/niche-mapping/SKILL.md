---
name: niche-mapping
description: Map each candidate to the niches it covers, indicating strength of coverage
  for each assignment.
execution: subagent
prompt: ./prompt.md
input: candidates, niches
dependencies:
  sops:
  - spawn-agent
---

# Niche Mapping

Systematically assign candidates to the niches they cover, noting coverage strength and identifying which niches lack strong candidates.

## Execution

Spawns a subagent that evaluates each candidate against each niche definition and produces a coverage map with gap identification.

## Why Subagent

Mapping requires evaluating each candidate against each niche criterion — a systematic cross-product analysis that benefits from methodical, uninterrupted execution.

## HARD-GATE

Output must include a complete coverage map (every candidate assessed against every niche) and identification of gaps where no candidate provides strong coverage.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
