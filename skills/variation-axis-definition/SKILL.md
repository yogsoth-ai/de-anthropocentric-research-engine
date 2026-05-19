---
name: variation-axis-definition
description: Identify orthogonal axes along which a method's validity might vary. Ensures axes are independent, measurable, and span the relevant parameter space.
execution: subagent
prompt: ./prompt.md
input: method_description (string), domain_context (string)
used-by: validity-envelope-mapping
---

# Variation Axis Definition

Define the dimensions along which to test validity.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one axis definition pass.
