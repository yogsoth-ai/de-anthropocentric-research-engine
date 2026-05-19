---
name: ishikawa-decomposition
description: Decompose problems into 6M categories (Methodology, Data, Theory, Measurement, Researchers, Environment) via fishbone diagram analysis.
execution: subagent
prompt: ./prompt.md
input: problem_statement (string), context (string)
used-by: root-cause-drilling
---

# Ishikawa Decomposition

Multi-factor causal decomposition via fishbone diagram.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one Ishikawa decomposition pass.
