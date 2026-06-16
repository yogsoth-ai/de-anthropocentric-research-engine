---
name: failure-chain-construction
description: Build cause-mode-effect chains tracing upstream root causes and downstream
  cascading effects for each failure mode.
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), function_tree (string), depth (number)
dependencies:
  sops:
  - spawn-agent
---

# Failure Chain Construction

Builds multi-level cause → mode → effect chains for systemic failure understanding.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Chain construction requires disciplined causal reasoning without skipping levels. Isolated context prevents shortcutting.

## Input

- **failure_modes**: Structured failure mode catalog
- **function_tree**: Function decomposition for context
- **depth**: Max chain depth (2/4/6 per budget)

## Output

- **chains**: List of cause-mode-effect chains with level annotations
- **shared_causes**: Root causes appearing in multiple chains
- **cascade_risks**: Modes that trigger other modes

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
