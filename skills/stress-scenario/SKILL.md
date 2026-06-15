---
name: stress-scenario
description: What is the worst case? — Extreme condition construction and failure
  mode enumeration for risk preparedness
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- scenario-driver-identification
- worst-case-construction
- scenario-impact-assessment
- robustness-scoring
- scenario-synthesis
tactics:
- strategy-robustness-testing
dependencies:
  sops:
  - robustness-scoring
  - scenario-driver-identification
  - scenario-impact-assessment
  - scenario-synthesis
  - worst-case-construction
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| strategy-robustness-testing | Orchestrates impact assessment and robustness scoring to evaluate research approach resilience across scenarios |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| robustness-scoring | Compute robustness index across scenarios with sensitivity analysis |
| scenario-driver-identification | Identify key uncertainty drivers using PESTEL framework scanning |
| scenario-impact-assessment | Assess each scenario's impact on the research approach across multiple dimensions |
| scenario-synthesis | Comprehensive scenario analysis report synthesizing all scenario work |
| worst-case-construction | Construct extreme but plausible worst-case scenarios for stress testing |

<!-- END available-tables (generated) -->
