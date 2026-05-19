---
name: white-space-detection
description: Identify matrix regions not covered by existing methods
execution: subagent
prompt: ./prompt.md
input: matrix (object), known_methods_mapping (object)
used-by: white-space-identification, design-space-mapping, general-morphological-analysis
---

# White Space Detection

Identify regions of the morphological matrix not covered by any existing method or solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

White space detection requires mapping known solutions onto the matrix, identifying gaps, and reasoning about why those gaps exist (overlooked vs infeasible vs unexplored).
