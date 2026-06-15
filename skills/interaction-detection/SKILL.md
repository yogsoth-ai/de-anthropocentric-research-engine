---
name: interaction-detection
description: Detect and characterize significant parameter interactions from Sobol
  decomposition results.
execution: subagent
prompt: ./prompt.md
input: sobol_results
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete interaction analysis (detection, characterization, implications).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
