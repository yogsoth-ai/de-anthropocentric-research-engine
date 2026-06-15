---
name: web-research
description: Deep web page analysis with full content extraction. Import of web-browsing/web-research
  skill. Must fetch full page via apify — no shortcuts.
execution: import
source: skills/web-research/SKILL.md
dependencies:
  sops:
  - web-research
---

# Web Research

Deep web page analysis with full content extraction.

## Execution

Import — strictly follow `web-browsing/web-research` skill protocol.

## Quality Gate

Must fetch full page content via apify rag-web-browser. No conclusions from snippets or partial content.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one full page fetch + analysis.

## Import Source

`web-browsing` repo → `skills/web-research/SKILL.md`
