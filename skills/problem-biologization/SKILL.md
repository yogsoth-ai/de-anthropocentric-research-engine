---
name: problem-biologization
description: "Restate technical problem as biological question. Translate engineering challenges into nature's language."
execution: subagent
prompt: ./prompt.md
input: technical_problem (string)
used-by: biologize-and-discover, functional-analogy, biological-function-mapping
---

# Problem Biologization

Restate technical problem as biological question.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Biologization requires creative reframing of technical problems into biological language, searching for functional equivalents across kingdoms of life. Benefits from dedicated attention to find non-obvious biological framings.
