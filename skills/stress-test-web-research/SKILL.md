---
name: web-research
description: Deep web full-text retrieval via Apify RAG browser. Import of web-browsing/web-research
  skill. Full page content for substantive analysis.
execution: import
source: skills/web-research/SKILL.md
dependencies:
  sops:
  - web-research
---

# Web Research

Deep web full-text retrieval for substantive analysis.

## Execution

Import — strictly follow `web-browsing/web-research` skill protocol.

## Quality Gate

Must fetch full page via Apify RAG browser. No shortcuts — full text required for any substantive claim about web content.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one apify/rag-web-browser call.

## Import Source

`web-browsing` repo → `skills/web-research/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| web-research | Deep web research — fetches full page content for analysis. Snippets alone are PROHIBITED for conclusions. |

<!-- END available-tables (generated) -->
