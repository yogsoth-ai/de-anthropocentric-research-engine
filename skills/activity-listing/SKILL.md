---
name: activity-listing
description: Enumerate all implementation activities from an experiment design
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: experiment design document
output: complete list of implementation activities with descriptions
dependencies:
  sops:
  - spawn-agent
---

# SOP: Activity Listing

Enumerate all discrete implementation activities required to execute an experiment design.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
