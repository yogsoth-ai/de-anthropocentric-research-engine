---
name: contradiction-detection
description: Evaluate whether a derivation chain has reached a genuine contradiction,
  absurdity, or inconclusive state.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Contradiction Detection

Subagent that evaluates derivation chains to determine if a genuine logical contradiction has been reached.
