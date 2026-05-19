---
name: gap-keyword-extraction
description: Extract gap-indicating sentences and phrases from papers/reviews. Identifies linguistic markers of research gaps (e.g., "remains unclear", "has not been explored", "limited understanding").
execution: subagent
prompt: ./prompt.md
input: paper_text (string), extraction_scope (string)
used-by: gap-identification
---

# Gap Keyword Extraction

Extract gap-indicating sentences and phrases from academic text.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one extraction pass over a paper or review text.
