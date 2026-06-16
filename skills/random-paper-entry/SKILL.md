---
name: random-paper-entry
description: Select random paper facet as creative stimulus. Uses genuine randomness
  in paper selection to break domain fixation.
execution: subagent
prompt: ./prompt.md
input: none
dependencies:
  sops:
  - spawn-agent
---

# Random Paper Entry

Select random paper facet as creative stimulus.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Random paper selection requires genuine exploration without goal-directed filtering. The subagent must resist the temptation to select "relevant" papers and instead embrace true randomness, then force associations from whatever is found.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
