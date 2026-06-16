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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
