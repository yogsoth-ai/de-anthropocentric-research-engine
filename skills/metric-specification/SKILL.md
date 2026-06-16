---
name: metric-specification
description: Define experiment metrics and significance standards
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: hypothesis, task domain, evaluation requirements
output: metric definitions with significance thresholds
dependencies:
  sops:
  - spawn-agent
---

# SOP: Metric Specification

Define primary and secondary metrics, measurement procedures, and pre-registered significance thresholds for the experiment.

Subagent — spawned via subagent-spawning/spawn-agent skill.

**Shared**: This SOP is used across all strategies as every experiment requires well-defined metrics.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
