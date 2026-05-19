---
name: competitive-scenario
description: "What will competitors do? — Competitive method progress prediction and time window analysis"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: scenario-planning
sops:
  - scenario-driver-identification
  - competitive-move-prediction
  - timeline-projection
  - scenario-impact-assessment
  - robustness-scoring
  - scenario-synthesis
tactics:
  - strategy-robustness-testing
---

# Strategy: Competitive Scenario

## Methodology

Competitive Intelligence Scenario Planning. Predict competitor progress, publication timelines, and methodological breakthroughs that could affect our research positioning. Assess time windows of opportunity and first-mover advantages.

Key principles:
- **Actor-based thinking**: Model specific competitors and their capabilities
- **Publication signals**: Use publication patterns to predict future directions
- **Time windows**: Identify windows of opportunity that may close
- **Preemption risk**: Assess probability of being scooped or rendered redundant

## Execution Flow

1. **Identify competitive drivers** → spawn `scenario-driver-identification`
   - Input: research field, known competitors, publication landscape
   - Output: competitive uncertainty drivers

2. **Predict competitor moves** → spawn `competitive-move-prediction` (×3-5 competitors)
   - Input: competitor profile, publication history, resource level
   - Output: predicted actions and timelines per competitor

3. **Project timelines** → spawn `timeline-projection`
   - Input: competitor predictions, technology maturity
   - Output: competitive timeline with key milestones

4. **Assess impact** → spawn `scenario-impact-assessment` (per competitive scenario)
   - Input: competitive scenario, our research approach
   - Output: positioning impact, window analysis

5. **Score robustness** → spawn `robustness-scoring`
   - Input: all competitive assessments
   - Output: competitive robustness index

6. **Synthesize** → spawn `scenario-synthesis`
   - Input: competitive scenarios, timelines, robustness
   - Output: competitive strategy report

## Budget Gate

| Step | Token Budget | Notes |
|------|-------------|-------|
| Driver identification | 8K | Competitor-focused |
| Move prediction | 10K × N | N = 3-5 key competitors |
| Timeline projection | 12K | Multi-horizon |
| Impact assessment | 10K × N | Per competitive scenario |
| Robustness scoring | 8K | Competitive positioning |
| Synthesis | 12K | Strategy recommendations |
