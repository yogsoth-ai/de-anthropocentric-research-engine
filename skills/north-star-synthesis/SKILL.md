---
name: north-star-synthesis
description: Converge all accumulated context into a crystallized North Star statement
  and structured ResearchBrief. Performs self-review before presenting to user. Use
  as the final tactic in any start mode — this is where everything comes together.
dependencies:
  sops:
  - crystallize-north-star
  - final-validation
  - generate-research-brief
---

# North Star Synthesis

Converge all accumulated context into North Star + ResearchBrief.

## Available SOPs

| SOP | Purpose | Execution |
|-----|---------|-----------|
| crystallize-north-star | Formulate the North Star statement with user | dialogue |
| generate-research-brief | Aggregate all context into structured ResearchBrief | subagent |
| final-validation | Self-review + present to user for confirmation | dialogue |

## Methodology Guidance

- `crystallize-north-star` checks: specific? ambitious? achievable?
- `generate-research-brief` aggregates all context (ActorProfile, FieldPanorama, RankedCandidates, ObstacleReport, GoalTree, North Star, key references, key terms)
- `final-validation` performs self-review before presenting:
  1. Placeholder scan: any TBD / empty sections?
  2. Internal consistency: do sections contradict?
  3. Completeness: critical information gaps?
  4. Ambiguity: statements interpretable two ways?
- If self-review finds issues: return to specific tactic/SOP for targeted fix (not full re-run)
- If passes: present North Star + ResearchBrief to user

## Output (Tactic-Level Aggregation, Presented to User)

`North Star (one sentence) + ResearchBrief (structured context document)`
