---
name: resurrection-advocacy
description: Argue for rejected candidates using Devil's Advocacy, Dialectical Inquiry, and Adversarial Collaboration to ensure elimination was justified.
used-by: steel-manning
---

# Resurrection Advocacy

**Purpose:** Construct the strongest possible case for candidates that were eliminated during convergence, ensuring rejection was based on genuine weakness rather than framing effects, anchoring bias, or insufficient consideration.

**When to use:**
- After convergence has produced a winner and eliminated alternatives
- When stakeholders express lingering doubt about rejected options
- When the elimination margin was narrow
- When rejected candidates had unique strengths not present in the winner

## Budget

| Metric | Minimum |
|--------|---------|
| Candidates resurrected | >= 2 (top rejected) |
| Advocacy depth | Full case construction per candidate |
| Debate rounds | >= 2 per resurrected candidate |

## State Ledger

```yaml
resurrected_candidates: []
advocacy_cases: {}
debate_outcomes: {}
final_dispositions: {}  # REAFFIRM_REJECTION | REVIVE | MERGE_STRENGTHS
```

## Available Tactics

| Tactic | When to Deploy |
|--------|---------------|
| adversarial-debate-protocol | Default — construct advocate, attack, judge cycle |
| multi-perspective-attack | When candidate has multi-stakeholder implications |

## Available SOPs

- advocate-construction — build strongest case for rejected candidate
- critic-attack — attack the advocacy case
- judge-verdict — render final disposition

## Execution Guidance

1. Select top 2-3 rejected candidates by elimination margin or unique strength
2. For each candidate, deploy adversarial-debate-protocol
3. If judge verdict is REVISE, escalate to campaign orchestrator
4. Record all dispositions in Challenge Ledger

## Output Format

```yaml
strategy: resurrection-advocacy
candidates_tested:
  - candidate: <name>
    advocate_strength: <1-10>
    verdict: REAFFIRM_REJECTION | REVIVE | MERGE_STRENGTHS
    key_argument: <strongest point>
    conditions: <if any>
surviving_concerns: []
recommendation: <action>
```
