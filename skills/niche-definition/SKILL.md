---
name: niche-definition
description: Define niches and capability areas that a portfolio should cover based
  on domain structure and objectives.
execution: subagent
prompt: ./prompt.md
input: domain, objectives
dependencies:
  sops:
  - spawn-agent
---

# Niche Definition

Identify and define the distinct niches, capability areas, or coverage zones that a well-constructed portfolio should span.

## Execution

Spawns a subagent that analyzes the domain and objectives to produce a taxonomy of niches with descriptions and importance ratings.

## Why Subagent

Niche definition requires domain analysis and taxonomic thinking to carve the solution space into meaningful, non-overlapping regions. This conceptual work benefits from dedicated focus.

## HARD-GATE

Output must contain 4-10 niches that are mutually distinct and collectively cover the relevant solution space. Each niche must have a clear description and importance rating.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
