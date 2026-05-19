---
name: scenario-planning
description: "What might the future look like — construct multiple future scenarios, assess research approach robustness under different assumptions"
version: 1.0.0
category: experiment-execution
type: campaign
strategies:
  - morphological-scenario
  - narrative-scenario
  - stress-scenario
  - competitive-scenario
  - temporal-scenario
---

# Campaign: Scenario Planning

## HARD-GATE

Before launching this campaign, verify:

1. **Research direction defined** — A clear research approach or hypothesis exists to stress-test
2. **Uncertainty acknowledged** — The team recognizes key unknowns that could invalidate the approach
3. **Time horizon specified** — Short (6mo), medium (2yr), or long (5yr+) planning window declared
4. **Stakeholder buy-in** — Decision-makers agree that scenario analysis will inform strategy

If any gate fails, STOP and resolve before proceeding.

## Campaign Goal

Construct a portfolio of plausible future scenarios spanning the uncertainty space, then assess how robust our research approach is under each scenario. The output is a robustness index plus contingency triggers that tell us when to pivot.

## Strategy Selection

| Strategy | Question | When to Use |
|----------|----------|-------------|
| morphological-scenario | What are all possible combinations? | Systematic enumeration of all factor combinations needed |
| narrative-scenario | What is the story of each future? | Rich qualitative understanding of scenario dynamics needed |
| stress-scenario | What is the worst case? | Risk assessment and failure preparedness needed |
| competitive-scenario | What will competitors do? | Competitive landscape awareness needed |
| temporal-scenario | How does it evolve over time? | Technology evolution and timing decisions needed |

## Budget Gate

| Component | Token Budget | Subagent Calls |
|-----------|-------------|----------------|
| Driver identification | 8K | 1 |
| Parameter enumeration | 10K | 1 |
| Consistency filtering | 15K | 2 |
| Narrative construction | 12K per scenario | 1 per scenario |
| Impact assessment | 10K per scenario | 1 per scenario |
| Robustness scoring | 8K | 1 |
| Synthesis | 12K | 1 |
| **Total (5 scenarios)** | **~130K** | **~15** |

## Context Management

- Each SOP runs as a subagent with isolated context
- Strategy-level orchestrator maintains scenario registry
- Pass scenario IDs (not full content) between steps
- Final synthesis receives summaries, not raw outputs

## Minimum Yield

A successful campaign produces at minimum:
- 3+ internally consistent scenarios spanning the uncertainty space
- Robustness score for the research approach (0-100)
- At least 1 identified pivot trigger with threshold condition
- Contingency action for each scenario where robustness < 50
