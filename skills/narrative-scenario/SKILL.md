---
name: narrative-scenario
description: "What is the story of each future? — Shell method narrative construction for rich qualitative scenario understanding"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: scenario-planning
sops:
  - scenario-driver-identification
  - scenario-narrative-construction
  - scenario-impact-assessment
  - robustness-scoring
  - scenario-synthesis
tactics:
  - cross-consistency-filtering
  - strategy-robustness-testing
---

# Strategy: Narrative Scenario

## Methodology

Shell Scenario Method (Wack/van der Heijden). Construct rich, internally consistent narratives that illuminate qualitatively different futures. Focus on storytelling that reveals causal mechanisms and decision points rather than exhaustive enumeration.

Key principles:
- **Narrative coherence**: Each scenario tells a believable story with cause-and-effect logic
- **Divergence**: Scenarios must be qualitatively different, not variations on a theme
- **Decision relevance**: Scenarios illuminate choices the research team faces
- **Memorable framing**: Each scenario gets a vivid name that captures its essence

## Execution Flow

1. **Identify drivers** → spawn `scenario-driver-identification`
   - Input: research context, planning horizon
   - Output: key uncertainty drivers ranked by impact × uncertainty

2. **Select axes** → identify the 2 highest-impact, highest-uncertainty drivers as scenario axes
   - Creates a 2×2 matrix of four qualitatively different futures

3. **Construct narratives** → spawn `scenario-narrative-construction` (×4)
   - Input: axis position, driver context, research approach
   - Output: rich narrative per quadrant

4. **Assess impact** → spawn `scenario-impact-assessment` (×4)
   - Input: scenario narrative, research approach
   - Output: impact analysis per scenario

5. **Score robustness** → spawn `robustness-scoring`
   - Input: all impact assessments
   - Output: robustness index

6. **Synthesize** → spawn `scenario-synthesis`
   - Input: all scenarios, robustness scores
   - Output: final report with strategic implications

## Budget Gate

| Step | Token Budget | Notes |
|------|-------------|-------|
| Driver identification | 8K | PESTEL scan |
| Axis selection | 4K | Ranking and selection |
| Narrative construction | 15K × 4 | Rich storytelling |
| Impact assessment | 10K × 4 | Per scenario |
| Robustness scoring | 8K | Aggregation |
| Synthesis | 12K | Final compilation |
