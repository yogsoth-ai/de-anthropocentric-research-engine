---
name: paper-search
description: Mid-depth paper analysis via AI-generated summaries. Import of literature-engine/literature-search
  skill. Reads AI summary — sufficient for methodology understanding but not for quoting
  specific results.
execution: import
source: skills/literature-search/SKILL.md
dependencies:
  sops:
  - literature-search
---

# Paper Search

Mid-depth paper analysis via AI-generated summaries.

## Execution

Import — strictly follow `literature-engine/literature-search` skill protocol.

## Quality Gate

AI summary level — sufficient for understanding methodology and approach, but not for quoting specific numerical results or exact claims. Use paper-research for that.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one paper read at AI summary level.

## Import Source

`literature-engine` repo → `skills/literature-search/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| literature-search | Medium-depth literature search — read AI-summarized reports for every paper analyzed |

<!-- END available-tables (generated) -->
