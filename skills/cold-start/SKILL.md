---
name: cold-start
description: Full crystallization strategy for users who have no research direction
  at all. Covers actor profiling, landscape reconnaissance, direction narrowing, obstacle
  analysis, goal decomposition, and north-star synthesis. Use when the user's first
  message reveals zero specificity about what they want to research.
dependencies:
  tactics:
  - actor-profiling
  - direction-narrowing
  - goal-decomposition
  - landscape-reconnaissance
  - north-star-synthesis
  - obstacle-analysis
---

# Cold Start Strategy

The user knows nothing — they want to publish at a top venue but have no idea what to research.

## Questioning Protocol

All SOPs in this strategy follow these rules:

- One question at a time — never overwhelm with multiple questions
- Prefer multiple choice when possible — easier to answer
- Always allow "unsure" / "TBD" as legitimate answers
- Always ask WHY — not just "what do you want" but "why do you want it"
- After user answers: confirm understanding before continuing
- If user's answer reveals new information: immediately follow up
- If user declines to answer (privacy): accept, note that downstream work becomes broader/more iterative

## Available Tactics

| Tactic | Purpose |
|--------|---------|
| actor-profiling | Understand who the user is |
| landscape-reconnaissance | Broad, shallow field exploration |
| direction-narrowing | Focus within chosen field(s) |
| obstacle-analysis | Identify and mitigate barriers |
| goal-decomposition | KAOS-style AND/OR goal structuring |
| north-star-synthesis | Converge into North Star + ResearchBrief |

## Default Flow (reference only)

```
actor-profiling → landscape-reconnaissance → direction-narrowing
→ obstacle-analysis → goal-decomposition → north-star-synthesis
```

This is a reference, not a mandate. You decide the actual execution path.

## Iteration Points

- From obstacle-analysis: may return to landscape-reconnaissance, direction-narrowing, or obstacle-analysis itself
- From goal-decomposition: may return to landscape-reconnaissance, direction-narrowing, obstacle-analysis, or goal-decomposition itself

## How to Use This Strategy

You are the general. This strategy gives you:
1. A default flow as starting reference
2. Available tactics with their purposes
3. Iteration points where backtracking makes sense

What you decide:
- Whether to execute a tactic fully or partially
- Whether to skip a tactic entirely
- Whether to invoke individual SOPs directly (bypassing tactic framing)
- When to iterate and where to return to
- When enough information exists to move forward

The only non-negotiable: the process ends with north-star-synthesis producing a North Star + ResearchBrief that the user confirms.

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| actor-profiling | Understand who the user is — background, resources, constraints, and deep motivations. Produces an ActorProfile that informs all downstream decisions. Use this tactic at the start of any crystallization process to build a model of the user's capabilities, limitations, and intent. |
| direction-narrowing | Focus within the user's chosen field(s). Identify specific sub-directions through deep paper and web research, then present ranked candidates. Use after landscape-reconnaissance has identified fields of interest. |
| goal-decomposition | Structure the user's chosen direction into a formal goal tree using KAOS-style AND/OR decomposition. Validate feasibility against ActorProfile and ObstacleReport. Use after obstacle-analysis confirms the direction is viable. |
| landscape-reconnaissance | Broad, shallow exploration of candidate research fields. Understand what's out there before narrowing. Use when the user needs to discover which fields are available to them — especially in cold-start and warm-start scenarios. |
| north-star-synthesis | Converge all accumulated context into a crystallized North Star statement and structured ResearchBrief. Performs self-review before presenting to user. Use as the final tactic in any start mode — this is where everything comes together. |
| obstacle-analysis | Identify what blocks the user from pursuing their chosen direction, assess severity, propose mitigations with search-validated evidence, and get user acceptance. Use after direction-narrowing has identified a specific direction. |

<!-- END available-tables (generated) -->
