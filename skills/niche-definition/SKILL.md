---
name: niche-definition
description: Define niches and capability areas that a portfolio should cover based on domain structure and objectives.
execution: subagent
prompt: ./prompt.md
input: domain, objectives
used-by: portfolio-optimization
---

# Niche Definition

Identify and define the distinct niches, capability areas, or coverage zones that a well-constructed portfolio should span.

## Execution

Spawns a subagent that analyzes the domain and objectives to produce a taxonomy of niches with descriptions and importance ratings.

## Why Subagent

Niche definition requires domain analysis and taxonomic thinking to carve the solution space into meaningful, non-overlapping regions. This conceptual work benefits from dedicated focus.

## HARD-GATE

Output must contain 4-10 niches that are mutually distinct and collectively cover the relevant solution space. Each niche must have a clear description and importance rating.
