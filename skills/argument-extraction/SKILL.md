---
name: argument-extraction
description: Extract and steel-man the core arguments supporting a given opinion cluster.
execution: subagent
prompt: ./prompt.md
input: cluster, judgments[]
dependencies:
  sops:
  - spawn-agent
---

# Argument Extraction

Extract the core arguments supporting a given opinion cluster and present them in their strongest possible form (steel-manned). Synthesizes reasoning from multiple perspectives within the cluster into coherent, well-structured arguments.

## Execution

Spawn a subagent that takes a cluster characterization and the relevant judgments, then produces a set of steel-manned arguments representing the cluster's position.

## Why Subagent

- Argument extraction requires careful synthesis across multiple inputs
- Steel-manning requires dedicated analytical attention
- Output feeds directly into disagreement-visualization

## HARD-GATE

Output MUST contain: at least 1 argument per cluster, each with `claim`, `evidence`, `reasoning`, and `strength` fields. Arguments must be steel-manned (strongest possible version).
