---
name: generate-candidate-fields
description: Propose 3-8 candidate research fields based on the full ActorProfile.
  When user wants to explore beyond their current stack, use other ActorProfile signals
  (intentionality, boundary) to determine exploration space. Free exploration within
  the boundary.
execution: subagent
prompt: ./prompt.md
input: actor_profile (string)
dependencies:
  sops:
  - spawn-agent
---

# Generate Candidate Fields

Generate candidate research fields for the user to explore.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

ActorProfile (full, as formatted text).

## Output

3-8 candidate fields, each with a one-line rationale for why this user could enter it.

## Key Behavior

When user wants to explore beyond their current stack, use boundary + intentionality to determine the exploration space. Don't limit to skills-only matching.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
