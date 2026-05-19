---
name: resource-envelope-estimation
description: Estimate resources, budget, and timeline using parametric, analogous, and three-point (PERT) estimation methods.
used-by: feasibility-assessment
---

# Resource Envelope Estimation

**Purpose:** Produce credible resource estimates for implementing a candidate. Combines parametric estimation (model-based), analogous estimation (reference-class), and three-point PERT estimation (optimistic/likely/pessimistic) to bound the resource envelope with quantified uncertainty.

**When to use:**
- A candidate has passed initial readiness screening and needs resource scoping
- Stakeholders need budget/timeline estimates to make investment decisions
- You need to compare resource requirements across multiple candidates

## Budget

| Metric | Target |
|--------|--------|
| Estimate dimensions | >= 3 (time, cost, personnel) |
| Precision range | +/-30% initial, +/-10% refined |
| Reference analogies | >= 2 per estimate |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| candidate | object | The candidate being estimated |
| parametric_estimate | object | Model-based estimate |
| analogous_estimate | object | Reference-class estimate |
| pert_estimate | object | Three-point estimate |
| envelope | object | Synthesized resource envelope |
| confidence_level | float | Confidence in the estimate |

## Available Tactics

| Tactic | When |
|--------|------|
| multi-dimensional-readiness-scan | When resource estimation requires understanding current maturity first |
| staged-gate-evaluation | When resources need to be estimated per stage gate |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| dimension-assessment | Assess resource dimension readiness |
| gate-criteria-definition | Define resource gates |
| feasibility-synthesis | Synthesize resource estimates into overall feasibility |

## Execution Guidance

1. Decompose the candidate into estimable work packages
2. For each work package, apply parametric estimation using known cost drivers
3. Identify >= 2 analogous projects and extract their actual resource consumption
4. Construct three-point estimates (optimistic, most likely, pessimistic) for each package
5. Synthesize into a resource envelope with confidence intervals
6. Flag any estimates with confidence < 0.5 for further investigation

## Output Format

```yaml
resource_envelope:
  candidate: <name>
  time:
    optimistic: <duration>
    likely: <duration>
    pessimistic: <duration>
    expected: <PERT weighted>
  cost:
    optimistic: <amount>
    likely: <amount>
    pessimistic: <amount>
    expected: <PERT weighted>
  personnel:
    roles: [{role, count, duration}]
    total_person_months: N
  analogies_used: [{project, relevance, actual_cost, actual_time}]
  confidence: 0.X
  precision_band: "+/-N%"
  key_assumptions: [...]
```
