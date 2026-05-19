---
name: maturation-pathway-design
description: Design path to readiness using Stage-Gate, Technology Roadmapping, and milestone planning methods.
used-by: feasibility-assessment
---

# Maturation Pathway Design

**Purpose:** Given a candidate that is not yet ready, design a concrete pathway to bring it to implementation readiness. Uses Stage-Gate processes to define decision points, Technology Roadmapping to sequence development activities, and milestone planning to create actionable checkpoints.

**When to use:**
- A candidate has potential but is not yet mature enough for implementation
- Stakeholders need a roadmap showing how and when readiness can be achieved
- You need to define clear gates and milestones for a maturation effort

## Budget

| Metric | Target |
|--------|--------|
| Stage gates defined | >= 3 |
| Milestones per stage | >= 2 |
| Resource estimates per stage | 1 per stage |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| candidate | object | The candidate needing maturation |
| current_readiness | object | Starting maturity profile |
| target_readiness | object | Required maturity for implementation |
| stages[] | array | Defined maturation stages |
| gates[] | array | Decision gates between stages |
| milestones[] | array | Checkpoints within stages |
| roadmap | object | Complete maturation roadmap |

## Available Tactics

| Tactic | When |
|--------|------|
| staged-gate-evaluation | To define and evaluate gates along the maturation path |
| multi-dimensional-readiness-scan | To assess readiness at each stage |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| gate-criteria-definition | Define criteria for each gate |
| gate-judgment | Evaluate readiness at each gate |
| dimension-assessment | Assess dimension readiness at checkpoints |
| feasibility-synthesis | Synthesize pathway into overall feasibility view |

## Execution Guidance

1. Establish current readiness profile (from maturity-diagnosis output)
2. Define target readiness required for implementation
3. Identify the gap between current and target across all dimensions
4. Design stages that progressively close the gap
5. Define gate criteria for transitions between stages
6. Place milestones within each stage as progress indicators
7. Estimate resources and timeline for each stage
8. Identify critical path and dependencies between stages

## Output Format

```yaml
maturation_pathway:
  candidate: <name>
  current_readiness: <overall score>
  target_readiness: <required score>
  gap_dimensions: [{dimension, current, target, gap}]
  stages:
    - stage: 1
      name: <stage name>
      objective: <what this stage achieves>
      milestones: [{name, criteria, target_date}]
      resources: {time, cost, personnel}
      gate:
        criteria: [...]
        pass_threshold: <condition>
  total_timeline: <duration>
  total_cost: <estimate>
  critical_path: [<stage dependencies>]
  risk_factors: [{risk, mitigation, stage_affected}]
```
