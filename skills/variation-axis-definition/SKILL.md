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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
