---
name: concept-matrix-construction
description: Build articles × concepts coverage matrix to visualize research landscape and identify empty cells as gap candidates.
execution: subagent
prompt: ./prompt.md
input: paper_collection (string), concept_list (string)
used-by: gap-identification
---

# Concept Matrix Construction

Build coverage matrices to visualize where research is dense vs absent.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one concept matrix construction from a paper collection.
