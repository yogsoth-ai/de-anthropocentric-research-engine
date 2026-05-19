---
name: deep-web-search
description: Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Spawns a subagent to read pages in isolated context. Hard constraint: at least 30 web pages read in full.
execution: subagent
prompt: ./prompt.md
input: search_queries (string), field_context (string)
---

# Deep Web Search

Deep web reading for non-academic perspectives (blogs, tech reports, products, industry analysis).

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill. The subagent reads pages in its own context window, protecting the main session from context overflow.

## Hard Constraint

At least 30 web pages read in full before completing this SOP.

## Why Subagent (Not Import)

Reading 30+ full web pages consumes significant context. Running this as a subagent isolates the heavy reading from the main dialogue session. The subagent returns a structured summary, not raw page content.
