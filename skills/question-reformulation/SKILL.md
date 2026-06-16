---
name: question-reformulation
description: Reframe research questions using abstraction laddering, HMW formulation,
  and Socratic probing. Find the most productive level and framing for investigation.
dependencies:
  sops:
  - abstraction-laddering
  - hmw-formulation
  - socratic-probing
---

# Question Reformulation

Reframe research questions to find the most productive framing.

## When to Use

The current question framing may be limiting — need to explore alternative framings at different abstraction levels.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 5 | 4–6 |
| paper-overview | 20 | 18–22 |
| paper-search | 15 | 13–17 |
| paper-research | 5 | 4–6 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 5 | ? |
| paper-overview | ? | 20 | ? |
| paper-search | ? | 15 | ? |
| paper-research | ? | 5 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** abstraction-laddering, hmw-formulation, socratic-probing

## Execution Guidance

Use abstraction laddering to move between concrete and abstract framings. Generate HMW questions from tensions/insights. Apply Socratic probing to test question quality.

## Output Format

Reformulated Questions — abstraction ladder, HMW set, Socratic challenges, recommended framing with reasoning.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| abstraction-laddering | Move between concrete and abstract framings — 3 levels up (Why?) and 3 levels down (How?) to find the most productive research level. |
| hmw-formulation | Generate "How Might We" questions at different scope levels (narrow, medium, broad). Ensures each is actionable without being prescriptive. |
| socratic-probing | Apply 6 types of Socratic questions to test claims and assumptions. Exposes weaknesses and strengthens reasoning. |

<!-- END available-tables (generated) -->
