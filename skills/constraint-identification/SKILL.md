---
name: constraint-identification
description: Find blockers and showstoppers using TOC, TRIZ contradiction analysis,
  and Pre-mortem techniques.
dependencies:
  tactics:
  - constraint-drilling
---

# Constraint Identification

**Purpose:** Systematically discover what could prevent a candidate from being implemented. Uses Theory of Constraints to find bottlenecks, TRIZ to surface contradictions, and Pre-mortem to anticipate failures before they occur.

**When to use:**
- A candidate looks promising but you need to stress-test its viability
- Stakeholders want to know what could go wrong before committing
- You need a structured inventory of blockers with severity and removability assessments

## Budget

| Metric | Target |
|--------|--------|
| Constraints identified | >= 3 per candidate |
| Hard constraints classified | >= 1 |
| Removal paths designed | >= 1 per removable constraint |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| candidate | object | The candidate under assessment |
| constraints[] | array | All identified constraints |
| hard_constraints[] | array | Non-negotiable blockers |
| soft_constraints[] | array | Constraints that can be worked around |
| assumptions[] | array | Unvalidated beliefs that may become constraints |
| removal_paths{} | map | Constraint -> removal path mapping |

## Available Tactics

| Tactic | When |
|--------|------|
| constraint-drilling | Default — full constraint discovery, classification, and removal path design |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| constraint-identification-sop | Discover constraints |
| constraint-classification | Sort into hard/soft/assumptions |
| removability-assessment | Score how removable each constraint is |
| removal-path | Design steps to remove a constraint |

## Execution Guidance

1. Deploy `constraint-identification-sop` to discover all constraints using TOC, TRIZ, and Pre-mortem
2. Feed discovered constraints to `constraint-classification` to sort them
3. For each non-trivial constraint, run `removability-assessment`
4. For constraints with removability score > 0.3, design `removal-path`
5. Aggregate findings into state ledger

## Output Format

```yaml
constraint_analysis:
  candidate: <name>
  total_constraints: N
  hard_constraints:
    - {constraint, severity, rationale}
  soft_constraints:
    - {constraint, severity, workaround_sketch}
  assumptions:
    - {assumption, risk_if_false, validation_method}
  removal_paths:
    - {constraint, removability: 0.X, steps: [...], timeline, resources}
  showstopper_verdict: <yes/no>
  showstopper_reason: <if yes>
```
