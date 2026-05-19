---
name: reformulation-synthesis
description: Compile all problem reformulation analyses into a coherent report with a recommended new problem definition.
execution: subagent
prompt: ./prompt.md
input: dominant_ideas, provocations, perspectives, dialectics, wickedness_assessment, appreciative_findings
used-by: problem-reformulation
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete reformulation synthesis report.
