---
name: strategy-robustness-testing
description: "Orchestrates impact assessment and robustness scoring to evaluate research approach resilience across scenarios"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: scenario-planning
orchestrates:
  - scenario-impact-assessment
  - robustness-scoring
---

# Tactic: Strategy Robustness Testing

## Orchestration Pattern

1. **Spawn impact assessment** → `scenario-impact-assessment` (per scenario)
   - Pass: scenario narrative, research approach description, evaluation dimensions
   - Receive: multi-dimensional impact analysis per scenario

2. **Validate impact assessments**
   - Check: All evaluation dimensions covered?
   - Check: Impact ratings justified with reasoning?
   - Check: Assessments distinguish between scenarios (not all identical)?
   - If validation fails: re-spawn with clarified criteria

3. **Compile assessment matrix**
   - Rows: scenarios
   - Columns: evaluation dimensions (feasibility, relevance, competitive position, resource needs, timeline)
   - Cells: impact ratings (1-5 scale)

4. **Spawn robustness scoring** → `robustness-scoring`
   - Pass: compiled assessment matrix, scenario probabilities, weighting preferences
   - Receive: robustness index, sensitivity analysis, pivot triggers

5. **Validate robustness results**
   - Check: Index is well-calibrated (not always 50 or always 90)
   - Check: Pivot triggers are specific and measurable
   - Check: Sensitivity analysis identifies which scenarios matter most
   - If validation fails: re-spawn with recalibrated inputs

6. **Identify contingencies**
   - For each scenario where robustness < 50: define contingency action
   - For each pivot trigger: define monitoring mechanism
   - Compile into actionable contingency plan

## Quality Checks

- [ ] Every scenario has a complete impact assessment
- [ ] Robustness index reflects genuine variation across scenarios
- [ ] Pivot triggers are observable and measurable
- [ ] Contingency actions are specific and feasible
- [ ] Results distinguish between "adapt" and "abandon" thresholds
