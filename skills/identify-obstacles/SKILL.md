---
name: identify-obstacles
description: Enumerate barriers to pursuing the chosen research direction — knowledge barriers, resource barriers, capability barriers, competition barriers. May optionally use search tools to discover obstacles the user hasn't mentioned.
execution: subagent
prompt: ./prompt.md
input: chosen_direction (string), actor_profile (string), ranked_candidates (string)
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
