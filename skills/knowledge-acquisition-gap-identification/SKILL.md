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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
