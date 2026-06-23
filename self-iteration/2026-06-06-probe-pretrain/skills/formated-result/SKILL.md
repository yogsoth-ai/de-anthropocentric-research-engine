---
name: formated-result
description: Experiment-specific - summarize the DARE executor's research design into a clean research_result report, forced to write back into the spec file produced by formated-specs.
---

# formated-result

Summarize the research design you just produced into a **research_result** report, and
write it back into the current spec file (append a fenced ```json result block after the
graph block).

## Emit research_result
- `document`: the full body of the research design document (the design itself, not the
  result of running the research).
- This is what the 32-check probe will later read (assumption falsifiability, question
  authenticity, decision design, etc. are all properties of the *design*), so a single
  design document at probe-depth suffices; do not execute the research.

## Hard constraints
- Only summarize the design you already produced; do not add new research content.
- The result block you write back must correspond to the same design as the graph block
  in the same file.
