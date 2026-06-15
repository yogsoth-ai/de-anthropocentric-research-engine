---
name: failure-clustering
description: Group observed failures by mechanism (not symptom), identify common triggers
  per cluster, estimate frequency and severity.
execution: subagent
prompt: ./prompt.md
input: failure_cases (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Failure Clustering

Cluster failures by underlying mechanism.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one failure clustering pass.
