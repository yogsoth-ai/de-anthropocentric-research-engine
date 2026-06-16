---
name: disagreement-cartography
description: Map the structure of disagreement across perspectives using Policy Delphi,
  Argument Delphi, or SAST methods.
dependencies:
  tactics:
  - disagreement-mapping
---

# Disagreement Cartography

**Purpose:** Rather than forcing convergence, map the topology of disagreement — identify clusters of opinion, the arguments supporting each cluster, and the fault lines between them. Useful for wicked problems where premature consensus would be harmful.

**When to use:**
- Wicked problems with legitimate value conflicts
- Policy questions where understanding disagreement matters more than resolving it
- Situations where forced consensus would mask important minority views
- Interdisciplinary disputes with incommensurable frameworks

## Budget

| Parameter | Constraint |
|-----------|-----------|
| Rounds | 1–2 (mapping, not converging) |
| Perspectives | ≥4 independent |
| Cluster minimum | ≥2 distinct clusters to be useful |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| question | string | The focal question or issue |
| perspectives | array | List of perspective descriptions |
| judgments | array | Raw collected judgments |
| clusters | array | Identified opinion clusters |
| arguments | array | Extracted arguments per cluster |
| disagreement_map | object | Final visualization structure |

## Available Tactics

- **disagreement-mapping** — Core flow: collect → cluster → extract arguments → visualize

## Available SOPs

- judgment-collection
- cluster-analysis
- argument-extraction
- disagreement-visualization

## Execution Guidance

1. Frame the question to elicit diverse positions (not just ratings)
2. Run disagreement-mapping tactic
3. Ensure each cluster has its strongest arguments represented
4. Produce disagreement map showing fault lines and bridging possibilities

## Output Format

```yaml
clusters:
  - id: <cluster_id>
    position: <summary>
    size: <number of perspectives>
    core_arguments: [...]
fault_lines:
  - between: [cluster_a, cluster_b]
    nature: <empirical/value/definitional>
bridging_possibilities: [...]
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| disagreement-mapping | Map disagreement structure by collecting judgments, clustering opinions, extracting arguments per cluster, and visualizing fault lines. |

<!-- END available-tables (generated) -->
