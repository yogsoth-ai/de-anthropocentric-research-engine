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
