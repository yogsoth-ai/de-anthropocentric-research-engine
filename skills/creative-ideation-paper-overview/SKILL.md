---
name: paper-overview
description: Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview
  skill. Abstract-level only — no methodology conclusions from abstracts.
execution: import
source: skills/literature-overview/SKILL.md
dependencies:
  sops:
  - literature-overview
---

# Paper Overview

Abstract-level paper scanning for broad coverage.

## Execution

Import — strictly follow `literature-engine/literature-overview` skill protocol.

## Quality Gate

Abstract-level only — do not draw methodology conclusions from abstracts alone. Abstracts provide leads for deeper investigation (paper-search or paper-research).

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one paper scanned at abstract level.

## Import Source

`literature-engine` repo → `skills/literature-overview/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| literature-overview | Quick landscape scan — discover papers on a topic without full-text reading |

<!-- END available-tables (generated) -->
