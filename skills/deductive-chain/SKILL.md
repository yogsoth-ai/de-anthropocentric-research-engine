---
name: deductive-chain
description: Derive logical consequences step by step from a given premise, building
  a traceable derivation chain.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Deductive Chain

Subagent that takes a premise and derives logical consequences through valid inference steps, producing a traceable chain.
