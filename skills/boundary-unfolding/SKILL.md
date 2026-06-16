---
name: boundary-unfolding
description: Systematically expose hidden system boundaries — CSH 12-question is/ought
  comparison, identify excluded stakeholders, reveal blind spots. Combines csh-12-question,
  jtbd-mapping, and salience-classification SOPs.
execution: tactic
dependencies:
  sops:
  - csh-12-question
  - deep-insight-multi-stakeholder-simulation
  - jtbd-mapping
  - salience-classification
---

# Boundary Unfolding

Expose hidden system boundaries and excluded perspectives.

## Operations

- csh-12-question — 4 dimensions × 3 questions, is vs ought
- jtbd-mapping — stakeholder jobs-to-be-done
- salience-classification — power/legitimacy/urgency classification

## Available SOPs

**Subagent:** csh-12-question, jtbd-mapping, salience-classification
**Shared:** multi-stakeholder-simulation

## Execution Guidance

Apply CSH 12 questions (4 dimensions × 3 questions, is vs ought). Map stakeholder jobs. Classify by salience model. Identify who is systematically excluded from the current framing.

## Minimum Yield

```
<HARD-GATE>
- CSH matrix: >= 1 completed
- stakeholders mapped: >= 4
- salience classifications: >= 4
- excluded perspectives identified: >= 1
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| csh-12-question | Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions (motivation, control, expertise, legitimacy) comparing is vs ought. |
| deep-insight-multi-stakeholder-simulation | Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal. Identifies blind spots from single-perspective analysis. |
| jtbd-mapping | Map stakeholder Jobs-to-be-Done — functional, emotional, and social jobs for each affected party. Identifies unserved jobs as opportunity signals. |
| salience-classification | Classify stakeholders by Mitchell et al. framework (Power, Legitimacy, Urgency). Assigns salience category and identifies systematically excluded parties. |

<!-- END available-tables (generated) -->
