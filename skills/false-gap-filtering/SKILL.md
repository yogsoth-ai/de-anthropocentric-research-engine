---
name: false-gap-filtering
description: Detect false gaps — search failures, already-solved gaps, and inherently
  unanswerable questions masquerading as research gaps.
execution: subagent
prompt: ./prompt.md
input: gap_candidate (string), search_results (string)
dependencies:
  sops:
  - spawn-agent
---

# False Gap Filtering

Distinguish genuine research gaps from artifacts of search failure.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one false-gap assessment for a single gap candidate.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
