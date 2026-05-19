---
name: temporal-sensitivity-testing
description: Test whether a gap persists across different time windows (2/5/10 years). Determines if gap is narrowing, widening, or stable over time.
execution: subagent
prompt: ./prompt.md
input: gap_description (string), time_parameters (string)
used-by: gap-validation
---

# Temporal Sensitivity Testing

Assess gap stability across time windows.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one temporal sensitivity assessment for a single gap.
