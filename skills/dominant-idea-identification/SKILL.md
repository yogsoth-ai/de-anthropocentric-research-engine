---
name: dominant-idea-identification
description: Identify dominant paradigms and assumptions constraining thinking in
  a research field.
execution: subagent
prompt: ./prompt.md
input: research_domain_description
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete dominant idea analysis for a research domain.
