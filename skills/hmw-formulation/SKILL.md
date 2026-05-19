---
name: hmw-formulation
description: Generate "How Might We" questions at different scope levels (narrow, medium, broad). Ensures each is actionable without being prescriptive.
execution: subagent
prompt: ./prompt.md
input: insight_or_tension (string), context (string)
used-by: question-reformulation
---

# HMW Formulation

Generate generative How Might We research questions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one HMW formulation pass.
