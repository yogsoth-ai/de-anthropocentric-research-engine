---
name: ablation-execution
description: Remove components one by one from a system, record the response/impact
  of each removal.
execution: subagent
prompt: ./prompt.md
input: system (string)
dependencies:
  sops:
  - spawn-agent
---

# Ablation Execution

Systematically remove components from a system one by one and record the resulting changes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Ablation requires careful, systematic removal of each component while tracking cascading effects. Benefits from dedicated context to maintain the full system model during iterative removal.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
