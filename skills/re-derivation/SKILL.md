---
name: re-derivation
description: Re-derive conclusions under a negated assumption, tracking where the
  derivation diverges from the original.
execution: subagent
prompt: ./prompt.md
input: original_method, alternative_assumption
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete re-derivation under one alternative assumption.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
