---
name: broad-web-search
description: Quick web scanning for field landscape understanding. Strict import of web-browsing/web-search skill. Hard constraint: ~10 results per call, at least 150 total search results before completing.
execution: import
source: web-browsing/skills/web-search/SKILL.md
---

# Broad Web Search

Quick web scanning for landscape understanding.

## Execution

Import — strictly follow `web-browsing/web-search` skill protocol.

## Provider Selection

Follow the imported skill's Provider Selection — use whichever web-search MCP
is configured. Provider-specific parameters are defined there.

## Hard Constraints

- Request ~10 results per search call (see imported skill for the provider parameter)
- Execute multiple calls with varied queries
- Do not complete this SOP until at least 150 total search results have been gathered
- This ensures broad coverage, not just the first page of one query

## Import Source

`web-browsing` repo → `skills/web-search/SKILL.md`
