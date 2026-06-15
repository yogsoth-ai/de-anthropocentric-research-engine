---
name: dependency-identification
description: Identify critical dependencies from ablation results, producing a dependency
  graph and highlighting critical components.
execution: subagent
prompt: ./prompt.md
input: ablation_results (object)
dependencies:
  sops:
  - spawn-agent
---

# Dependency Identification

Extract a dependency graph from ablation results, identifying which components are critical and how they relate.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Dependency analysis requires synthesizing ablation data into graph structures and identifying non-obvious transitive dependencies. Benefits from focused analytical context.
