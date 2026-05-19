---
name: appropriateness-bounding
description: Establish acceptability standards through RAND/UCLA Appropriateness Method or Consensus Conference protocols.
used-by: structured-consensus
---

# Appropriateness Bounding

**Purpose:** Determine what is appropriate, acceptable, or indicated for a given context. Uses the RAND/UCLA Appropriateness Method (rating + discussion + re-rating) or Consensus Conference (citizen jury) format to establish boundaries of acceptability.

**When to use:**
- Medical guideline development (appropriate indications)
- Regulatory standard setting
- Establishing acceptable thresholds for action
- Any question of the form "is X appropriate when Y?"

## Budget

| Parameter | Constraint |
|-----------|-----------|
| Rounds | 2 (rate → discuss → re-rate) |
| Perspectives | ≥4 (ideally 7–15 for RAND/UCLA) |
| Rating scale | 1–9 (inappropriate to appropriate) |
| Agreement threshold | Median ≥7 without disagreement |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| indications | array | List of scenarios to rate |
| perspectives | array | Panel member perspectives |
| round_1_ratings | array | Initial ratings per indication |
| discussion_notes | string | Key points from discussion |
| round_2_ratings | array | Post-discussion ratings |
| classifications | object | Appropriate/uncertain/inappropriate per item |

## Available Tactics

- **iterative-convergence-round** — Two-round rate-discuss-rerate cycle
- **threshold-calibration** — Determine where appropriateness boundaries fall

## Available SOPs

- judgment-collection
- feedback-distribution
- consensus-measurement
- round-decision
- threshold-sweep
- consensus-classification
- consensus-synthesis

## Execution Guidance

1. Define indications/scenarios clearly (clinical scenarios, use cases)
2. Collect Round 1 ratings (1–9 scale) with brief rationale
3. Distribute feedback showing distribution of ratings
4. Facilitate structured discussion of disagreements
5. Collect Round 2 ratings
6. Classify each indication: appropriate (median 7–9), uncertain (4–6), inappropriate (1–3)
7. Flag items with disagreement (where panel lacks agreement despite median)

## Output Format

```yaml
classifications:
  appropriate: [{indication, median, agreement_level}, ...]
  uncertain: [{indication, median, agreement_level}, ...]
  inappropriate: [{indication, median, agreement_level}, ...]
disagreement_items: [{indication, reason}, ...]
panel_size: <int>
method: RAND/UCLA | Consensus Conference
```
