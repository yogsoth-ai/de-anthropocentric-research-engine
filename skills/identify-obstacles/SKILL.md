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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
