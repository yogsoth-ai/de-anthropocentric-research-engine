---
name: deep-insight-web-search
description: Quick web scanning for landscape understanding. Import of web-browsing/web-search
  skill. Snippets only — no conclusions from snippets alone.
execution: import
source: skills/web-search/SKILL.md
dependencies:
  sops:
  - web-search
---

# Web Search

Quick web scanning for landscape understanding.

## Execution

Import — strictly follow `web-browsing/web-search` skill protocol.

## Quality Gate

Snippets only — do not draw conclusions from search result snippets alone. Snippets provide leads for deeper investigation (web-research or paper-search).

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one brave_web_search call (count=10 results).

## Import Source

`web-browsing` repo → `skills/web-search/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| web-search | Quick web scanning — discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

<!-- END available-tables (generated) -->
