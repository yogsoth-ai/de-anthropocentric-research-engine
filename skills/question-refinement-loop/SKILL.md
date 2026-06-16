---
name: question-refinement-loop
description: 'Tactic: iteratively refine a research question until it passes all 5
  FINER criteria'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: research-question
sops:
- finer-criteria-check
- scope-assessment
- success-criteria-definition
dependencies:
  sops:
  - finer-criteria-check
  - scope-assessment
  - success-criteria-definition
---

# Question Refinement Loop

Iteratively refine a research question — polish it repeatedly until it passes all 5 FINER criteria.

## Orchestration Intent

Structure "refining the question" as a loop: check → identify problems → revise → re-check. Each round focuses on the criteria that did not pass.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| finer-criteria-check | Check each of the 5 FINER criteria item by item | The check step of each loop |
| scope-assessment | Assess whether the question's scope is appropriate | When F (Feasible) fails |
| success-criteria-definition | Define measurable success criteria | After the loop ends, to confirm the RQ is measurable |

## Orchestration Pattern

**Standard loop**:
1. finer-criteria-check → obtain the 5 verdicts
2. If all pass → call success-criteria-definition → end
3. If any fail → targeted revision:
   - F fails → scope-assessment → narrow the scope
   - I fails → strengthen the theoretical motivation
   - N fails → check the literature to confirm novelty
   - E fails → adjust the research design
   - R fails → reinforce practical significance
4. After revision, return to step 1

**Max iterations**: 3 rounds. If it still fails after 3 rounds → report which criterion persistently fails + suggest a fundamental change of direction.

## Minimum Yield

- RQ passes FINER 5/5
- Success criteria defined (measurable)
- If 3 rounds fail: clearly report the failing criteria + suggestions

## Yield Report

After execution, report:
- Number of iterations
- The FINER results of each round
- The final RQ statement
- Success criteria

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| finer-criteria-check | SOP: check research-question quality against each of the 5 FINER criteria |
| scope-assessment | SOP: Assess whether a research question has appropriate scope (too broad / appropriate / too narrow) |
| success-criteria-definition | SOP: Define measurable success criteria for a research question |

<!-- END available-tables (generated) -->
