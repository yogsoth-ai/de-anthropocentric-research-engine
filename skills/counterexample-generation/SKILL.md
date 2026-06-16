---
name: counterexample-generation
description: Systematically generate counterexamples (monsters) to a given claim using
  diverse heuristic strategies.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Counterexample Generation

Subagent that produces counterexamples to a claim using boundary cases, degenerate cases, and domain-specific heuristics.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
