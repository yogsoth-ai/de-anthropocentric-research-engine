---
name: matrix-construction
description: Build n-dimensional morphological matrix
execution: subagent
prompt: ./prompt.md
input: parameters (array), values (object)
dependencies:
  sops:
  - spawn-agent
---

# Matrix Construction

Build an n-dimensional morphological matrix from parameters and their enumerated values.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Matrix construction requires careful organization of multi-dimensional data, computing combination counts, and presenting the matrix in a format suitable for downstream CCA and path generation.
