---
name: abstraction-laddering
description: Move between concrete and abstract framings — 3 levels up (Why?) and 3 levels down (How?) to find the most productive research level.
execution: subagent
prompt: ./prompt.md
input: problem_statement (string), context (string)
used-by: question-reformulation
---

# Abstraction Laddering

Navigate abstraction levels to find productive framings.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one abstraction ladder construction.
