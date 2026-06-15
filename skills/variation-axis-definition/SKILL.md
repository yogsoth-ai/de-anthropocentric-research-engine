---
name: variation-axis-definition
description: Identify orthogonal axes along which a method's validity might vary.
  Ensures axes are independent, measurable, and span the relevant parameter space.
execution: subagent
prompt: ./prompt.md
input: method_description (string), domain_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Variation Axis Definition

Define the dimensions along which to test validity.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one axis definition pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
