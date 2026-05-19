---
name: warm-start
description: Simplified crystallization strategy for users who have a general research direction (e.g., "I'm interested in LLM reasoning") but lack specificity. Simplifies actor profiling and landscape reconnaissance, then proceeds through direction narrowing, obstacle analysis, goal decomposition, and north-star synthesis. Use when the user's first message reveals a general area but not a specific problem.
---

# Warm Start Strategy

The user has a general direction — they know the field or area but not the specific problem.

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
actor-profiling (simplified) → landscape-reconnaissance (simplified or skipped)
→ direction-narrowing → obstacle-analysis → goal-decomposition → north-star-synthesis
```

This is a reference, not a mandate. How to simplify, how much to simplify, whether to skip entirely — these are your decisions. This strategy suggests simplification as the default posture, but you judge based on what the user's initial message reveals.

## Simplification Guidance

- **actor-profiling**: The user's stated direction already reveals partial context. Focus on resources, constraints, and intentionality rather than exhaustive background exploration.
- **landscape-reconnaissance**: The user already knows the general field. You may skip broad scanning and go directly to direction-narrowing, or do a targeted scan of the specific sub-area they mentioned.

## Iteration Points

- From obstacle-analysis: may return to landscape-reconnaissance, direction-narrowing, or obstacle-analysis itself
- From goal-decomposition: may return to landscape-reconnaissance, direction-narrowing, obstacle-analysis, or goal-decomposition itself

## How to Use This Strategy

You are the general. This strategy gives you:
1. A default flow as starting reference
2. Available tactics with their purposes
3. Simplification guidance for the warm-start context
4. Iteration points where backtracking makes sense

What you decide:
- Whether to execute a tactic fully or partially
- Whether to skip a tactic entirely
- Whether to invoke individual SOPs directly (bypassing tactic framing)
- When to iterate and where to return to
- When enough information exists to move forward

The only non-negotiable: the process ends with north-star-synthesis producing a North Star + ResearchBrief that the user confirms.
