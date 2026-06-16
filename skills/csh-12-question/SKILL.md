---
name: csh-12-question
description: Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions
  (motivation, control, expertise, legitimacy) comparing is vs ought.
execution: subagent
prompt: ./prompt.md
input: system_description (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# CSH 12-Question

Critical Systems Heuristics boundary analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CSH 12-question analysis pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
