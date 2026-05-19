---
name: egm-construction
description: Build structured Evidence Gap Maps — define axes (intervention × outcome or method × domain), place gaps in cells, annotate with evidence density and quality.
execution: subagent
prompt: ./prompt.md
input: classified_gaps (string), axis_definitions (string)
used-by: gap-identification, gap-synthesis-strategy
---

# EGM Construction

Build structured Evidence Gap Maps for visual gap representation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one EGM construction from classified gaps.
