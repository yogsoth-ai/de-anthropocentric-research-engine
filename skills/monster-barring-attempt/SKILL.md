---
name: monster-barring-attempt
description: Attempt to exclude a counterexample as illegitimate by tightening definitions
  or preconditions (Lakatos monster-barring).
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Monster-Barring Attempt

Subagent that evaluates whether a counterexample can be legitimately excluded by refining the claim's scope or definitions.
