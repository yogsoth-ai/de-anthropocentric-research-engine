---
name: biotriz-principle-selection
description: "Select applicable BioTRIZ principles for a given contradiction. Map to biological cases."
execution: subagent
prompt: ./prompt.md
input: contradiction_description (string)
used-by: biotriz-resolution
---

# BioTRIZ Principle Selection

Select applicable BioTRIZ principles for a given contradiction.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

BioTRIZ principle selection requires knowledge of the biological 40 principles, the bio contradiction matrix, and the ability to find relevant biological cases. Benefits from focused specialist attention.
