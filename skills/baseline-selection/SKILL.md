---
name: baseline-selection
description: Select appropriate baselines for experimental comparison
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: proposed method, task domain, prior work
output: ranked baseline list with justification and sources
dependencies:
  sops:
  - spawn-agent
---

# SOP: Baseline Selection

Select appropriate baselines that provide meaningful comparison points, covering SOTA, simple, and internal baselines.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
