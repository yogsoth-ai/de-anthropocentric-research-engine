---
name: niche-mapping
description: Map each candidate to the niches it covers, indicating strength of coverage for each assignment.
execution: subagent
prompt: ./prompt.md
input: candidates, niches
used-by: portfolio-optimization
---

# Niche Mapping

Systematically assign candidates to the niches they cover, noting coverage strength and identifying which niches lack strong candidates.

## Execution

Spawns a subagent that evaluates each candidate against each niche definition and produces a coverage map with gap identification.

## Why Subagent

Mapping requires evaluating each candidate against each niche criterion — a systematic cross-product analysis that benefits from methodical, uninterrupted execution.

## HARD-GATE

Output must include a complete coverage map (every candidate assessed against every niche) and identification of gaps where no candidate provides strong coverage.
