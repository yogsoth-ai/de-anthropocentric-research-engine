---
name: courtroom-structured
description: "Strategy: Legal adversarial structure — prosecution presents case, defense responds, evidence is cross-examined, judge delivers verdict. Emphasizes evidence quality and procedural rigor."
type: strategy
used-by: [multiagent-debate]
tactics: [evidence-tournament, dialectical-escalation]
---

# Courtroom-Structured Strategy

Legal adversarial model with formal evidence presentation and cross-examination.

## Method

1. **debate-architect** structures the case — defines charges (weaknesses to probe)
2. **debate-critic** (prosecution) presents opening arguments with evidence
3. **evidence-scout** gathers supporting/opposing evidence from external sources
4. **debate-defender** presents counter-case
5. **cross-examination** probes both sides for inconsistencies
6. **debate-judge** delivers structured verdict per charge

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [define charges]
→ [for each charge]:
    debate-critic (prosecution) → evidence-scout
    → debate-defender → evidence-scout
    → cross-examination → debate-judge
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (case structure)
- debate-critic (prosecution)
- debate-defender (defense counsel)
- evidence-scout (evidence gathering)
- cross-examination (probing)
- debate-judge (verdict per charge)
