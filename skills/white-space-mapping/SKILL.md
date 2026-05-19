---
name: white-space-mapping
description: Feature cross-matrix construction and blank area identification for patent opportunity mapping
execution: subagent
prompt: ./prompt.md
input: feature_dimensions, existing_patents
used-by: patent-mining
---

# White Space Mapping

Constructs multi-dimensional feature cross-matrices from patent data and identifies blank areas representing unprotected technology combinations.
