---
name: landscape-synthesis
description: Evaluate each candidate research field on maturity, competition, entry
  barrier, and publication opportunity. Synthesizes broad-web-search results into
  a structured FieldPanorama. Must consider both niche approaches AND direct frontal
  competition in hot fields.
execution: subagent
prompt: ./prompt.md
input: candidate_fields (string), web_search_results (string), actor_profile (string)
dependencies:
  sops:
  - spawn-agent
---

# Landscape Synthesis

Evaluate candidate fields and produce FieldPanorama.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- Candidate fields list
- Accumulated web search results
- ActorProfile

## Output

FieldPanorama[] — structured evaluation of each field.

## Hard Constraint

Don't only propose niche/novel combinations or "stitched-together" approaches. Must also consider direct frontal competition in hot fields. The ambition to tackle hard problems head-on must be present.
