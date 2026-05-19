---
name: morphological-scenario
description: "What are all possible combinations? — Zwicky Box construction with CCA consistency filtering for systematic scenario enumeration"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: scenario-planning
sops:
  - scenario-driver-identification
  - parameter-enumeration
  - consistency-pair-evaluation
  - scenario-narrative-construction
  - scenario-impact-assessment
  - robustness-scoring
  - scenario-synthesis
tactics:
  - parameter-space-construction
  - cross-consistency-filtering
  - strategy-robustness-testing
---

# Strategy: Morphological Scenario

## Methodology

General Morphological Analysis (Zwicky) combined with Cross-Consistency Assessment (Ritchey). Systematically enumerate all possible combinations of key uncertainty parameters, filter for internal consistency, and assess surviving configurations as plausible scenarios.

Key principles:
- **Completeness**: Every relevant parameter dimension is included
- **MECE values**: Each parameter has mutually exclusive, collectively exhaustive values
- **Pairwise consistency**: Filter via CCA matrix before narrative construction
- **Combinatorial discipline**: Let the morphological field drive discovery, not intuition

## Execution Flow

1. **Identify drivers** → spawn `scenario-driver-identification`
   - Input: research context, planning horizon
   - Output: 5-8 key uncertainty drivers

2. **Enumerate parameters** → spawn `parameter-enumeration`
   - Input: driver list
   - Output: Zwicky Box (parameter × value matrix)

3. **Consistency filtering** → spawn `consistency-pair-evaluation`
   - Input: Zwicky Box
   - Output: CCA matrix, surviving configurations

4. **Narrative construction** → spawn `scenario-narrative-construction` (per surviving config)
   - Input: parameter configuration
   - Output: scenario narrative

5. **Impact assessment** → spawn `scenario-impact-assessment` (per scenario)
   - Input: scenario narrative, research approach
   - Output: impact analysis

6. **Robustness scoring** → spawn `robustness-scoring`
   - Input: all impact assessments
   - Output: robustness index

7. **Synthesis** → spawn `scenario-synthesis`
   - Input: all scenarios, robustness scores
   - Output: final scenario portfolio report

## Budget Gate

| Step | Token Budget | Notes |
|------|-------------|-------|
| Driver identification | 8K | Single pass |
| Parameter enumeration | 10K | May iterate once |
| Consistency filtering | 15K | O(n²) pairwise |
| Narrative construction | 12K × N | N = surviving configs (typically 4-8) |
| Impact assessment | 10K × N | Per scenario |
| Robustness scoring | 8K | Aggregation |
| Synthesis | 12K | Final compilation |
