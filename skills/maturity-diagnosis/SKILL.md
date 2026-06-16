---
name: maturity-diagnosis
description: Assess current readiness of candidates using TRL 9-level, NASSS 7-dimension,
  and Innovation Readiness Level frameworks.
dependencies:
  tactics:
  - multi-dimensional-readiness-scan
---

# Maturity Diagnosis

**Purpose:** Determine how ready a candidate is for implementation by scoring it against established maturity frameworks. Produces a multi-dimensional readiness profile that reveals which aspects are mature and which need development.

**When to use:**
- A candidate has been selected and needs readiness assessment before resource commitment
- Stakeholders need evidence-based maturity scores to inform go/no-go decisions
- You need to identify which dimensions are lagging and require focused maturation effort

## Budget

| Metric | Target |
|--------|--------|
| Dimensions scored | >= 5 |
| Evidence items per dimension | >= 2 |
| Bottlenecks identified | >= 1 |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| candidate | object | The candidate under assessment |
| dimensions[] | array | Dimensions being assessed |
| scores{} | map | Dimension -> score mapping |
| radar_data | object | Synthesized radar chart data |
| bottlenecks[] | array | Identified bottleneck dimensions |

## Available Tactics

| Tactic | When |
|--------|------|
| multi-dimensional-readiness-scan | Default — full readiness assessment across all dimensions |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| dimension-assessment | Score a single dimension |
| radar-synthesis | Combine scores into radar |
| bottleneck-identification | Find limiting dimensions |

## Execution Guidance

1. Identify relevant dimensions for the candidate (minimum: technical, market, regulatory, resource, organizational)
2. Deploy `dimension-assessment` for each dimension — can run in parallel
3. Feed all scores to `radar-synthesis` to produce the composite view
4. Run `bottleneck-identification` on the radar data to surface limiting factors
5. Record all findings in state ledger

## Output Format

```yaml
maturity_diagnosis:
  candidate: <name>
  overall_readiness: <1-9 TRL scale>
  dimension_scores:
    technical: {score: N, evidence: [...], gaps: [...]}
    market: {score: N, evidence: [...], gaps: [...]}
    regulatory: {score: N, evidence: [...], gaps: [...]}
    resource: {score: N, evidence: [...], gaps: [...]}
    organizational: {score: N, evidence: [...], gaps: [...]}
  bottlenecks: [{dimension, severity, reason}]
  radar_summary: <text>
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| multi-dimensional-readiness-scan | Assess readiness across multiple dimensions, synthesize into radar visualization, and identify bottleneck dimensions. |

<!-- END available-tables (generated) -->
