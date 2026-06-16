---
name: paper-research
description: Deep paper analysis with full text reading. Import of literature-engine/literature-research
  skill. Full text access — required for quoting results, verifying claims, extracting
  detailed methodology.
execution: import
source: skills/literature-research/SKILL.md
dependencies:
  sops:
  - literature-research
---

# Paper Research

Deep paper analysis with full text reading.

## Execution

Import — strictly follow `literature-engine/literature-research` skill protocol.

## Quality Gate

Full text level — required for quoting specific results, verifying exact claims, or extracting detailed methodology steps.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one paper read at full text level.

## Import Source

`literature-engine` repo → `skills/literature-research/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-research | Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis |

<!-- END available-tables (generated) -->
