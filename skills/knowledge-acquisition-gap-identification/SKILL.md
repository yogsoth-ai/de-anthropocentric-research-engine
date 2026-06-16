---
name: gap-identification
description: Identify what the literature has NOT addressed — missing methods, untested
  combinations, unexplored applications, contradictions without resolution. Used by
  all strategies.
execution: subagent
prompt: ./prompt.md
input: corpus_summary (string), taxonomy (string)
dependencies:
  sops:
  - spawn-agent
---

# Gap Identification

Find what the literature hasn't addressed.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Gap identification requires reasoning about absence — what SHOULD exist but doesn't. This requires holding the full picture of what DOES exist and reasoning about the negative space. Dedicated context for this analytical work.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
