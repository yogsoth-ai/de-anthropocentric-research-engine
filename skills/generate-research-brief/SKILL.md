---
name: generate-research-brief
description: Aggregate all accumulated context from the crystallization process into
  a structured ResearchBrief document. This is the final output artifact alongside
  the North Star — a comprehensive requirement context document for downstream research
  strategies.
execution: subagent
prompt: ./prompt.md
input: actor_profile (string), field_panorama (string), ranked_candidates (string),
  obstacle_report (string), goal_tree (string), north_star (string), key_references
  (string)
dependencies:
  sops:
  - spawn-agent
---

# Generate Research Brief

Aggregate all context into a structured ResearchBrief.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

All accumulated artifacts from the crystallization process.

## Output

ResearchBrief — structured context document (not a research plan).

## Key Behavior

Does not output directly to user — feeds into final-validation first.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
