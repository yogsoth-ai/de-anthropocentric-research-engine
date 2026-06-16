---
name: constraint-synthesis
description: Synthesize constraint analysis into actionable report with priorities
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: outputs from constraint-tree-building, sensitivity-ranking, constraint-breaking
output: integrated constraint report with prioritized actions and risk assessment
dependencies:
  sops:
  - context-checkpoint
  - context-init
  - spawn-agent
---

# SOP: Constraint Synthesis

Synthesize all constraint analysis outputs into a single actionable report. Integrates findings from tree-building, sensitivity ranking, and constraint-breaking into prioritized recommendations.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->
<!-- context-management rows hand-maintained (cross-package import); do not regenerate this file -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
