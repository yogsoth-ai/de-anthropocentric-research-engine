---
name: cross-database-verification
description: Verify gap existence across multiple databases (Semantic Scholar, Google
  Scholar, arXiv, domain-specific). Distinguishes database-specific gaps from universal
  gaps.
execution: subagent
prompt: ./prompt.md
input: gap_description (string), databases_to_check (string)
dependencies:
  sops:
  - spawn-agent
---

# Cross-Database Verification

Verify gap authenticity by searching across multiple databases.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one cross-database verification pass for a single gap.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
