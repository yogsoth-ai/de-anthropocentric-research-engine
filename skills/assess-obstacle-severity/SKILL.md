---
name: assess-obstacle-severity
description: Rate each identified obstacle's difficulty — overcomability, time cost,
  workaround existence. May optionally use search tools to validate assessments.
execution: subagent
prompt: ./prompt.md
input: obstacles (string), actor_profile (string)
dependencies:
  sops:
  - spawn-agent
---

# Assess Obstacle Severity

Assess how severe each obstacle actually is for this specific user.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- Identified obstacles list
- ActorProfile

## Search

Optional — may use web-search, web-research, literature-overview, literature-search, literature-research to validate assessments.

## Output

Each obstacle rated on:
- Overcomability: 1-week learnable / 1-month effort / 6-month investment / fundamental blocker
- Time cost estimate
- Workaround existence (yes/no + description)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
