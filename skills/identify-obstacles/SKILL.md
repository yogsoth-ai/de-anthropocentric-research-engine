---
name: identify-obstacles
description: Enumerate barriers to pursuing the chosen research direction — knowledge
  barriers, resource barriers, capability barriers, competition barriers. May optionally
  use search tools to discover obstacles the user hasn't mentioned.
execution: subagent
prompt: ./prompt.md
input: chosen_direction (string), actor_profile (string), ranked_candidates (string)
dependencies:
  sops:
  - spawn-agent
---

# Identify Obstacles

Enumerate all barriers between the user and their chosen direction.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- Chosen research direction
- ActorProfile
- RankedCandidates context

## Search

Optional — may use web-search, web-research, literature-overview, literature-search, literature-research to discover obstacles the user hasn't mentioned.

## Output

Categorized list of obstacles (knowledge / resource / capability / competition).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
