---
name: false-gap-filtering
description: Detect false gaps — search failures, already-solved gaps, and inherently unanswerable questions masquerading as research gaps.
execution: subagent
prompt: ./prompt.md
input: gap_candidate (string), search_results (string)
used-by: gap-validation
---

# False Gap Filtering

Distinguish genuine research gaps from artifacts of search failure.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one false-gap assessment for a single gap candidate.
