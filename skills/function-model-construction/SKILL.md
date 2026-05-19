---
name: function-model-construction
description: Build substance-field functional model of a system, annotating useful, harmful, insufficient, and excessive interactions.
execution: subagent
prompt: ./prompt.md
input: system_description (string)
used-by: structural-deconstruction, contradiction-identification, component-decomposition, function-trimming
---

# Function Model Construction

Build a substance-field functional model for system analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Functional modeling requires careful identification of all system components and their interactions, classifying each interaction type. Benefits from dedicated analytical context without distraction from downstream operations.
