---
name: appreciative-discovery
description: Search for positive deviants and extract transferable principles using
  Appreciative Inquiry.
execution: subagent
prompt: ./prompt.md
input: problem_domain
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete appreciative discovery (positive deviants + enabling conditions + principles).
