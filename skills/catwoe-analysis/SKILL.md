---
name: catwoe-analysis
description: Apply Checkland's CATWOE analysis from a specific stakeholder perspective to reveal how the problem looks from that viewpoint.
execution: subagent
prompt: ./prompt.md
input: system_description, stakeholder_perspective
used-by: multi-perspective-reframing
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CATWOE analysis from one stakeholder perspective.
