---
name: failure-mode-cataloging
description: Systematically catalog all failure modes in a domain or method, producing
  a classified failure taxonomy.
execution: subagent
prompt: ./prompt.md
input: domain_or_method (string)
dependencies:
  sops:
  - spawn-agent
---

# Failure Mode Cataloging

Systematically catalog all failure modes, producing a classified taxonomy with severity and frequency.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Failure cataloging requires exhaustive enumeration across multiple sources (papers, incident reports, benchmarks). Benefits from dedicated research context to achieve comprehensive coverage.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
