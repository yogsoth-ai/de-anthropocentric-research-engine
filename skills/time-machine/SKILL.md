---
name: time-machine
description: Temporal projection — view a solution from future/past time horizons to generate temporally-informed insights.
execution: subagent
prompt: ./prompt.md
input: solution (string), time_scale (string)
used-by: perspective-forcing, temporal-projection, perspective-rotation
---

# Time Machine

Temporal projection: view from future/past.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Temporal projection requires sustained imaginative reasoning across multiple time horizons, benefiting from dedicated context free of present-bias.
