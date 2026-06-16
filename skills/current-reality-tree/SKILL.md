---
name: current-reality-tree
description: Build TOC Current Reality Trees — connect Undesirable Effects via sufficient-cause
  logic to identify 1-3 root causes.
execution: subagent
prompt: ./prompt.md
input: undesirable_effects (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Current Reality Tree

Build formal causal logic trees from symptoms to root causes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CRT construction pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
