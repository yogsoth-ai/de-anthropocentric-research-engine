---
name: gap-identification
description: Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies.
execution: subagent
prompt: ./prompt.md
input: corpus_summary (string), taxonomy (string)
used-by: literature-survey, benchmark-archaeology, baseline-establishment
---

# Gap Identification

Find what the literature hasn't addressed.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Gap identification requires reasoning about absence — what SHOULD exist but doesn't. This requires holding the full picture of what DOES exist and reasoning about the negative space. Dedicated context for this analytical work.
