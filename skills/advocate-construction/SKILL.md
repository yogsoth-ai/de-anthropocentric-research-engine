---
name: advocate-construction
description: Construct the strongest possible case for a rejected candidate or counter-position.
execution: subagent
prompt: ./prompt.md
input: rejected_candidate, context
used-by: [steel-manning, validation]
---

# Advocate Construction

Builds the most compelling argument for a position — typically a rejected candidate or counter-thesis. The advocate's job is to find every legitimate strength, reframe weaknesses, and construct a case that demands serious engagement.

## Execution

Spawns a subagent with the advocate role. The subagent receives the rejected candidate and convergence context, then constructs the strongest possible case for resurrection or adoption.

## Why Subagent

- Role isolation prevents contamination from prior judgments
- Advocate must genuinely argue FOR the position without hedging
- Separation from critic/judge roles ensures intellectual honesty

## HARD-GATE

Output must include:
- Explicit thesis statement
- >= 3 supporting arguments with evidence
- Reframing of at least 1 perceived weakness as a strength
- Acknowledgment of genuine weaknesses (steel-manning, not straw-manning)
