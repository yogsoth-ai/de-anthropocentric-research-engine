---
name: paper-research
description: Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research
  skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted.
execution: import
source: skills/literature-research/SKILL.md
dependencies:
  sops:
  - literature-research
---

# Paper Research

Full-depth paper reading with raw text extraction.

## Execution

Import — strictly follow `literature-engine/literature-research` skill protocol.

## Quality Gate

Must read with fullText: true — extract equations, hyperparameters, specific claims, and implementation details. This is the deepest reading level.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one paper read at full depth.

## Import Source

`literature-engine` repo → `skills/literature-research/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-research | Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis |

<!-- END available-tables (generated) -->
