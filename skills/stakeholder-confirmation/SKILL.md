---
name: stakeholder-confirmation
description: Simulate stakeholder perspectives to validate gap priorities. Assesses gap value from researcher, practitioner, funder, and end-user viewpoints.
execution: subagent
prompt: ./prompt.md
input: gap (string), stakeholder_roles (string)
used-by: gap-prioritization
---

# Stakeholder Confirmation

Validate gap priorities across multiple stakeholder perspectives.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one stakeholder confirmation pass for a single gap.
