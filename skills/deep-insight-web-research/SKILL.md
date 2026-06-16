---
name: deep-insight-web-research
description: Deep web research with full page fetching via Apify. Import of web-browsing/web-research
  skill. Must fetch full page — no conclusions from previews.
execution: import
source: skills/web-research/SKILL.md
dependencies:
  sops:
  - web-research
---

# Web Research

Deep web research with full page fetching.

## Execution

Import — strictly follow `web-browsing/web-research` skill protocol.

## Quality Gate

Must fetch full page via Apify rag-web-browser. No conclusions from search previews or snippets alone. Full page content is the minimum evidence standard.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one full page fetch + analysis.

## Import Source

`web-browsing` repo → `skills/web-research/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| web-research | Deep web research — fetches full page content for analysis. Snippets alone are PROHIBITED for conclusions. |

<!-- END available-tables (generated) -->
