---
name: temporal-scenario
description: "How does it evolve over time? — Short/medium/long-term timeline projection with technology maturity curves"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: scenario-planning
sops:
  - scenario-driver-identification
  - timeline-projection
  - scenario-narrative-construction
  - scenario-impact-assessment
  - robustness-scoring
  - scenario-synthesis
tactics:
  - strategy-robustness-testing
---

# Strategy: Temporal Scenario

## Methodology

Temporal Scenario Planning with Technology Maturity Curves. Project how the research landscape evolves across multiple time horizons (short: 6 months, medium: 2 years, long: 5+ years). Map technology S-curves, adoption dynamics, and paradigm shift timing.

Key principles:
- **Multi-horizon**: Separate analysis for short, medium, and long term
- **S-curve awareness**: Technologies follow predictable maturity patterns
- **Paradigm sensitivity**: Identify potential paradigm shifts and their timing
- **Path dependency**: Current decisions constrain future options

## Execution Flow

1. **Identify temporal drivers** → spawn `scenario-driver-identification`
   - Input: research context, focus on time-dependent factors
   - Output: drivers with temporal dynamics (maturation rates, adoption curves)

2. **Project timelines** → spawn `timeline-projection`
   - Input: temporal drivers, current maturity levels
   - Output: multi-horizon projections with uncertainty bands

3. **Construct temporal narratives** → spawn `scenario-narrative-construction` (×3 horizons)
   - Input: timeline projections, horizon-specific drivers
   - Output: narrative per time horizon

4. **Assess impact** → spawn `scenario-impact-assessment` (per horizon)
   - Input: temporal narrative, research approach, decision timing
   - Output: time-dependent impact analysis

5. **Score robustness** → spawn `robustness-scoring`
   - Input: all temporal assessments
   - Output: temporal robustness index, optimal timing windows

6. **Synthesize** → spawn `scenario-synthesis`
   - Input: temporal scenarios, timing recommendations
   - Output: temporal strategy with decision points

## Budget Gate

| Step | Token Budget | Notes |
|------|-------------|-------|
| Driver identification | 8K | Time-dynamics focused |
| Timeline projection | 15K | Multi-horizon + S-curves |
| Narrative construction | 12K × 3 | Per horizon |
| Impact assessment | 10K × 3 | Per horizon |
| Robustness scoring | 10K | Temporal sensitivity |
| Synthesis | 12K | Timing recommendations |
