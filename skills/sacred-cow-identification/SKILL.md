---
name: sacred-cow-identification
description: Find domain's unquestioned beliefs. Systematic identification of dogma that constrains innovation.
execution: subagent
prompt: ./prompt.md
input: domain_description (string), known_practices (string)
used-by: assumption-enumeration, anti-benchmark, sacred-cow-hunting
---

# Sacred Cow Identification

Find domain's unquestioned beliefs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Sacred cow identification requires deep domain analysis and the ability to distinguish between well-justified constraints and mere tradition. Benefits from dedicated critical thinking without solution-generation pressure.
