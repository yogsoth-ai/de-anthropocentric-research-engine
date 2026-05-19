---
name: coverage-gap-detection
description: Detect uncovered regions in the solution space, producing a prioritized gap list.
execution: subagent
prompt: ./prompt.md
input: coverage_analysis (object)
used-by: gap-driven-generation, failure-taxonomy, factorial-ideation
---

# Coverage Gap Detection

Detect uncovered regions in the solution space and prioritize them for targeted generation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Gap detection requires comparing actual coverage against theoretical completeness. Benefits from focused context to systematically scan all dimensions without missing regions.
