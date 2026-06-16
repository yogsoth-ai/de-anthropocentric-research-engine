---
name: deep-insight-paper-search
description: AI-powered paper summary and search. Import of literature-engine/literature-search
  skill. AI summary level — cite as "AI-extracted" not "paper states".
execution: import
source: skills/literature-search/SKILL.md
dependencies:
  sops:
  - literature-search
---

# Paper Search

AI-powered paper summary and search.

## Execution

Import — strictly follow `literature-engine/literature-search` skill protocol.

## Quality Gate

AI summary level — cite findings as "AI-extracted" not "paper states". For authoritative claims about paper content, use paper-research (full text reading).

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one paper fetch + AI summary generation.

## Import Source

`literature-engine` repo → `skills/literature-search/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-search | Medium-depth literature search — read AI-summarized reports for every paper analyzed |

<!-- END available-tables (generated) -->
