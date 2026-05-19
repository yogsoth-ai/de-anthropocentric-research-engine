---
name: dialectical-escalation
description: Double-loop learning escalation — surface governing variables, generate counter-assumptions, test if problem dissolves under alternatives, score wickedness if it persists.
execution: tactic
used-by: dialectical-reformulation
---

# Dialectical Escalation

Escalate from single-loop to double-loop learning.

## Operations

governing-variable-surfacing → counter-assumption-generation → wickedness-scoring

## Available SOPs

**Subagent:** governing-variable-surfacing, counter-assumption-generation, wickedness-scoring
**Shared:** assumption-surfacing

## Execution Guidance

Surface the governing variables (Argyris: the unstated rules everyone follows), generate the opposite assumption for each, test whether the problem still exists under the alternative. If it persists regardless, assess wickedness level.

Single-loop: "How do we solve this problem better?" Double-loop: "Should we be solving this problem at all?"

## Minimum Yield

```
<HARD-GATE>
- Governing variables surfaced: >= 3
- Counter-assumptions generated: >= 3
- Problem dissolution tests: >= 2
- Wickedness assessment: completed if problem persists
</HARD-GATE>
```
