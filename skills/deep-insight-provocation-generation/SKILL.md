---
name: provocation-generation
description: Generate de Bono lateral thinking provocations to challenge dominant
  ideas using escape, reversal, exaggeration, and distortion.
execution: subagent
prompt: ./prompt.md
input: dominant_idea
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete provocation set (4+ provocations) for one dominant idea.
