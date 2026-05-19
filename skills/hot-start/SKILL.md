---
name: hot-start
description: Minimal crystallization strategy for users who already have a specific research topic or problem (e.g., "I want to improve CoT faithfulness in LLMs") and need structuring into a formal North Star. Heavily simplifies or skips exploration tactics, focusing on obstacle analysis, goal decomposition, and synthesis. Use when the user's first message reveals a specific, actionable research direction.
---

# Hot Start Strategy

The user already knows their direction. Your job is to structure it, not explore alternatives.

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
actor-profiling (heavily simplified) → landscape-reconnaissance (skipped or minimal)
→ direction-narrowing (heavily simplified) → obstacle-analysis (simplified)
→ goal-decomposition → north-star-synthesis
```

This is a reference, not a mandate. The user already knows their direction. landscape-reconnaissance and direction-narrowing may only need a few searches for context — or may be skipped entirely if the user's topic is already well-defined.

## Simplification Guidance

- **actor-profiling**: Focus only on resources and constraints relevant to the stated topic. Skip broad background exploration.
- **landscape-reconnaissance**: Usually skippable. Only invoke if you need context about the field to properly structure the user's goal.
- **direction-narrowing**: Usually skippable. The user has already narrowed. Only invoke if their stated topic is still too broad for a single North Star.
- **obstacle-analysis**: Focus on the specific obstacles to their stated direction, not hypothetical alternatives.

## Iteration Points

- From obstacle-analysis: may return to landscape-reconnaissance, direction-narrowing, or obstacle-analysis itself
- From goal-decomposition: may return to landscape-reconnaissance, direction-narrowing, obstacle-analysis, or goal-decomposition itself

## How to Use This Strategy

You are the general. This strategy gives you:
1. A default flow as starting reference
2. Available tactics with their purposes
3. Simplification guidance for the hot-start context
4. Iteration points where backtracking makes sense

What you decide:
- Whether to execute a tactic fully or partially
- Whether to skip a tactic entirely
- Whether to invoke individual SOPs directly (bypassing tactic framing)
- When to iterate and where to return to
- When enough information exists to move forward

The only non-negotiable: the process ends with north-star-synthesis producing a North Star + ResearchBrief that the user confirms.
