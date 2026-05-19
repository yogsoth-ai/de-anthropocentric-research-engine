---
name: synectics-synthesis
description: Synthesize all synectics outputs into a structured idea report. Combines results from all analogy types and excursion processes.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
used-by: synectics, direct-analogy, personal-analogy, symbolic-analogy, fantasy-analogy, excursion-method
---

# Synectics Synthesis

Synthesize all synectics outputs into a structured idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires holding all intermediate outputs from multiple analogy types and excursion processes simultaneously, identifying cross-cutting themes and combining complementary insights into coherent solution concepts.
