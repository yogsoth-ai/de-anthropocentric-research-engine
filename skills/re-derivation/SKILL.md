---
name: re-derivation
description: Re-derive conclusions under a negated assumption, tracking where the
  derivation diverges from the original.
execution: subagent
prompt: ./prompt.md
input: original_method, alternative_assumption
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete re-derivation under one alternative assumption.
