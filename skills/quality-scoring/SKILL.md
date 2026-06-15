---
name: quality-scoring
description: Multi-dimensional patent quality assessment — forward citations, family
  size, claim count, geographic breadth
execution: subagent
prompt: ./prompt.md
input: patent_metadata
dependencies:
  sops:
  - spawn-agent
---

# Quality Scoring

Performs multi-dimensional quality assessment of patents using quantitative indicators: forward citation count, family size, claim count, geographic breadth, and prosecution history.
