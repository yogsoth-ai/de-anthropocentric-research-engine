# Q6 live execution record

Date: 2026-09-13
Path: `rank-candidates(direction-selection)`
Execution mode: one-shot standard-library run using the existing v4 node contracts and graph calls. No new runner or persistence mechanism was added.

## Preflight

- Input contract: satisfied. `candidates`, `criteria`, and `decision_rule` supplied.
- Candidate count: 2 (`gap-A`, `gap-B`).
- Criteria: `impact`, `feasibility`, `evidence_coverage`; each uses a 1-5 scale and higher-is-better direction.
- Weights: `impact=0.40`, `feasibility=0.35`, `evidence_coverage=0.25`; sum `1.00`.
- Missing-value policy: reject missing criterion values; none missing.
- Mode: `direction-selection`.

## Actual input and scores

| candidate | impact | feasibility | evidence_coverage | weighted score |
|---|---:|---:|---:|---:|
| gap-A | 4 | 5 | 3 | 4.100000 |
| gap-B | 5 | 4 | 4 | 4.400000 |

Baseline order: `gap-B > gap-A`.

## Sensitivity execution

The existing `assess-sensitivity` gate requires at least four scenarios and +/-20% per declared weight axis. Six scenarios were run, renormalizing the other weights to preserve sum 1.00.

| perturbed axis | change | gap-A | gap-B | order |
|---|---:|---:|---:|---|
| impact | -20% | 4.113333 | 4.320000 | gap-B > gap-A |
| impact | +20% | 4.086667 | 4.480000 | gap-B > gap-A |
| feasibility | -20% | 4.003077 | 4.443077 | gap-B > gap-A |
| feasibility | +20% | 4.196923 | 4.356923 | gap-B > gap-A |
| evidence_coverage | -20% | 4.173333 | 4.426667 | gap-B > gap-A |
| evidence_coverage | +20% | 4.026667 | 4.373333 | gap-B > gap-A |

All six scenarios preserve the order. Kendall tau against baseline: `1.0`. Stability verdict: `stable`.

## Checkpoint

Checkpoint: 0001-2026-09-13T12:00:00Z
Phase: direction-selection
Source: rank-candidates
Status: complete
Input slice: candidates=gap-A,gap-B; criteria=impact,feasibility,evidence_coverage; decision_rule=direction-selection; weights={impact:0.40,feasibility:0.35,evidence_coverage:0.25}
Process: normalize schemas -> select direction-selection -> validate weights -> score-object -> aggregate-ranking -> assess-sensitivity
Results: gap-B ranked first at 4.400000; six +/-20% weight scenarios retained gap-B first; Kendall tau=1.0; stability=stable
Delta: {findings: ["gap-B outranks gap-A under baseline and all six declared sensitivity scenarios"], evidence_updates: [], hypothesis_updates: [], assumption_updates: [], uncertainties: [], decisions: ["select gap-B as current direction"], open_questions: [], recommended_jumps: []}
Open questions: []

## Verification

The run produced the expected ordered recommendation, score table, weights, sensitivity results, and stability verdict required by `rank-candidates` and `assess-sensitivity`. The record uses the existing nine-field checkpoint and fixed eight-field Delta; no provider, retry, timeout, error-classification, parallel-dispatch, or monitoring mechanism was introduced.

## Scope boundary

This run verifies the scientific-graph execution layer only: scoring, weighting, sensitivity analysis, Delta construction, and checkpoint formatting. It does not execute a host implementation for SpecView reconstruction, context preflight, or catalog card retrieval. Those upstream steps remain design decisions documented in `host-design.md`; this file must not be cited as evidence that the complete host runtime has been implemented or exercised.
