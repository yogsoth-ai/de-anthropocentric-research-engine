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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
