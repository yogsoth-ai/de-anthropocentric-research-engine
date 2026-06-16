---
name: stakeholder-mapping
description: Map all affected parties using CSH 12-question framework, identify jobs-to-be-done,
  classify by salience. Reveals whose perspective is systematically excluded.
dependencies:
  tactics:
  - boundary-unfolding
  sops:
  - csh-12-question
  - deep-insight-multi-stakeholder-simulation
  - jtbd-mapping
  - salience-classification
---

# Stakeholder Mapping

Map who is affected by a gap and whose perspective is missing.

## When to Use

Need to understand the human/institutional landscape around a research gap — who benefits, who suffers, who is excluded.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 40 | 36–44 |
| web-research | 15 | 13–17 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 5 | 4–6 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 40 | ? |
| web-research | ? | 15 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 5 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- boundary-unfolding

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** csh-12-question, jtbd-mapping, salience-classification
**Shared:** multi-stakeholder-simulation

## Execution Guidance

Map all affected parties using CSH 12-question framework, identify their jobs-to-be-done, classify by salience (power/legitimacy/urgency). Reveal whose perspective is systematically excluded.

## Output Format

Stakeholder Map — CSH matrix, JTBD per stakeholder, salience classification, excluded perspectives.

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| boundary-unfolding | Systematically expose hidden system boundaries — CSH 12-question is/ought comparison, identify excluded stakeholders, reveal blind spots. Combines csh-12-question, jtbd-mapping, and salience-classification SOPs. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| csh-12-question | Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions (motivation, control, expertise, legitimacy) comparing is vs ought. |
| deep-insight-multi-stakeholder-simulation | Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal. Identifies blind spots from single-perspective analysis. |
| jtbd-mapping | Map stakeholder Jobs-to-be-Done — functional, emotional, and social jobs for each affected party. Identifies unserved jobs as opportunity signals. |
| salience-classification | Classify stakeholders by Mitchell et al. framework (Power, Legitimacy, Urgency). Assigns salience category and identifies systematically excluded parties. |

<!-- END available-tables (generated) -->
