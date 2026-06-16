---
name: scenario-narrative-construction
description: Build rich narratives for surviving morphological configurations using
  Shell method
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: parameter configuration, consistency context, research approach description
output: rich scenario narrative with causal logic, signposts, and implications
dependencies:
  sops:
  - spawn-agent
---

# SOP: Scenario Narrative Construction

Build a rich, internally consistent narrative for a given parameter configuration. The narrative should tell a coherent story of how this future comes to be, what it looks like, and what it means for the research approach.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
