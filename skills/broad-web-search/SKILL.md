---
name: broad-web-search
description: Quick web scanning for field landscape understanding. Strict import of web-browsing/web-search skill. Hard constraint: brave_web_search count=10 per call, at least 150 total search results before completing.
execution: import
source: web-browsing/skills/web-search/SKILL.md
---

# Broad Web Search

Quick web scanning for landscape understanding.

## Execution

Import — strictly follow `web-browsing/web-search` skill protocol.

## Provider Selection

- If the `tavily-search` MCP server is configured and active, use `tavily_search` (with `max_results=10`) as the search provider.
- Otherwise, fall back to `brave_web_search` (with `count=10`).

## Hard Constraints

- Set `count=10` (Brave) or `max_results=10` (Tavily) on every search call
- Execute multiple calls with varied queries
- Do not complete this SOP until at least 150 total search results have been gathered
- This ensures broad coverage, not just the first page of one query

## Import Source

`web-browsing` repo → `skills/web-search/SKILL.md`
