---
name: stress-scenario
description: "What is the worst case? — Extreme condition construction and failure mode enumeration for risk preparedness"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: scenario-planning
sops:
  - scenario-driver-identification
  - worst-case-construction
  - scenario-impact-assessment
  - robustness-scoring
  - scenario-synthesis
tactics:
  - strategy-robustness-testing
---

# Strategy: Stress Scenario

## Methodology

Stress Testing combined with Failure Mode Analysis. Deliberately construct extreme but plausible scenarios that maximally challenge the research approach. Identify breaking points, failure modes, and minimum conditions for viability.

Key principles:
- **Extreme but plausible**: Push parameters to edges without crossing into fantasy
- **Failure-seeking**: Actively look for conditions that break the approach
- **Compound stress**: Combine multiple adverse conditions (correlated failures)
- **Recovery assessment**: For each failure, assess whether recovery is possible

## Execution Flow

1. **Identify drivers** → spawn `scenario-driver-identification`
   - Input: research context, focus on threat vectors
   - Output: vulnerability drivers and failure dimensions

2. **Construct worst cases** → spawn `worst-case-construction` (×3-5)
   - Input: driver extremes, compound combinations
   - Output: extreme scenario descriptions

3. **Assess impact** → spawn `scenario-impact-assessment` (per worst case)
   - Input: stress scenario, research approach
   - Output: failure mode analysis, breaking points

4. **Score robustness** → spawn `robustness-scoring`
   - Input: all stress test results
   - Output: stress robustness index, failure threshold map

5. **Synthesize** → spawn `scenario-synthesis`
   - Input: stress scenarios, failure modes, robustness scores
   - Output: risk report with mitigation recommendations

## Budget Gate

| Step | Token Budget | Notes |
|------|-------------|-------|
| Driver identification | 8K | Threat-focused |
| Worst-case construction | 12K × N | N = 3-5 stress scenarios |
| Impact assessment | 12K × N | Deeper analysis for stress |
| Robustness scoring | 10K | Failure threshold mapping |
| Synthesis | 12K | Risk mitigation report |
