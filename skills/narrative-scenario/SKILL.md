---
name: narrative-scenario
description: What is the story of each future? — Shell method narrative construction
  for rich qualitative scenario understanding
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- scenario-driver-identification
- scenario-narrative-construction
- scenario-impact-assessment
- robustness-scoring
- scenario-synthesis
tactics:
- cross-consistency-filtering
- strategy-robustness-testing
dependencies:
  sops:
  - robustness-scoring
  - scenario-driver-identification
  - scenario-impact-assessment
  - scenario-narrative-construction
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| cross-consistency-filtering | Orchestrates pairwise consistency evaluation and narrative construction to filter the morphological field |
| strategy-robustness-testing | Orchestrates impact assessment and robustness scoring to evaluate research approach resilience across scenarios |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| robustness-scoring | Compute robustness index across scenarios with sensitivity analysis |
| scenario-driver-identification | Identify key uncertainty drivers using PESTEL framework scanning |
| scenario-impact-assessment | Assess each scenario's impact on the research approach across multiple dimensions |
| scenario-narrative-construction | Build rich narratives for surviving morphological configurations using Shell method |
| scenario-synthesis | Comprehensive scenario analysis report synthesizing all scenario work |

<!-- END available-tables (generated) -->
