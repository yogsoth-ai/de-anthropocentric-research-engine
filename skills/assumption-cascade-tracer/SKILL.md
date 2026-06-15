---
name: assumption-cascade-tracer
description: Build assumption dependency graphs and trace cascade failures when root
  assumptions are invalidated.
execution: subagent
prompt: ./prompt.md
input: assumptions (string), attack_results (string)
dependencies:
  sops:
  - spawn-agent
---

# Assumption Cascade Tracer

Maps assumption dependencies and traces how failures propagate through the dependency graph.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Cascade tracing requires systematic graph analysis without bias toward minimizing impact. The tracer must follow every dependency path honestly.

## Input

- **assumptions**: List of assumptions with their dependency relationships
- **attack_results**: Results from probing root assumptions (which ones failed)

## Output

- **dependency_graph**: Directed graph of assumption dependencies
- **cascade_paths**: For each failed root, the full list of downstream conclusions that collapse
- **impact_scope**: Percentage of artifact conclusions affected by each cascade
