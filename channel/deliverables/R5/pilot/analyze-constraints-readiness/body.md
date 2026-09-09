# analyze-constraints-readiness

## Purpose

Assess feasibility and readiness by identifying constraints, resources, dependencies, bottlenecks, and maturation gates.

## Input contract

```yaml
required: [candidate_or_plan, readiness_dimensions]
optional: [resource_estimates, dependencies, assumptions, target_gates]
constraints: [evidence attached to each scored dimension]
```

## Execution protocol

1. Define candidate, dimensions, hard constraints, and target gates.
2. Select `obstacle-triage`, `readiness-assessment`, `resource-envelope`, `causal-constraint-analysis`, or `maturation-path`.
3. Score dimensions with evidence, identify binding constraints and dependencies.
4. Design removal/mitigation paths, stage gates, and a readiness conclusion.

## Output contract

```yaml
produces: [readiness_profile, constraint_register, bottlenecks, resource_envelope, stage_gates, mitigation_paths]
delta_fields: [findings, decisions, uncertainties, open_questions, recommended_jumps]
```

## Thresholds and quality gates

- Feasibility, maturity, constraint, resource, and maturation gates use declared dimension/evidence/constraint coverage ratios; record numerator, denominator, batch increment, stopping reason, and source references.
- Preserve structural requirements: at least one hard constraint, one removal path per removable constraint, explicit stage gates, and a binding-constraint rule relative to the observed score distribution.

- Feasibility dimensions >=5; blockers >=3 per candidate where source protocol applies.
- Maturity diagnosis: >=5 dimensions, >=2 evidence items per dimension, >=1 bottleneck.
- Constraint identification: >=3 constraints per candidate; >=1 hard constraint; >=1 removal path per removable constraint.
- Resource envelope: >=3 dimensions (time, cost, personnel) and >=2 analogies per estimate.
- Maturation path: >=3 stage gates and >=2 milestones per stage.
- Binding constraint threshold: sensitivity score >2× median.

## Failure and counterexamples

Do not label a candidate ready with missing evidence, unclassified hard constraints, or an unbounded resource estimate. A conflict with no manageable injection remains blocked.

## Provenance map

26 architecture `old` entries; readiness, feasibility, resource, obstacle, dependency, sensitivity, and maturation families are merged by mode. Missing aliases are listed in log.

## Context checkpoint / Delta notes

Append dimension scores/evidence, constraint IDs, bottleneck rationale, resources, gates, and unresolved conflicts.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| feasibility-assessment | 42 | numeric-table | \\| maturity-diagnosis \\| Assess current readiness using TRL 9-level, NASSS 7-dimension, and Innovation Readiness Level frameworks \\| |
| feasibility-assessment | 75 | numeric | \\| Dimensions assessed \\| >= 5 (technical, market, regulatory, resource, organizational) \\| |
| feasibility-assessment | 76 | numeric | \\| Blockers identified \\| >= 3 per candidate \\| |
| feasibility-assessment | 77 | numeric | \\| Estimate precision \\| from +/-30% to +/-10% through iteration \\| |
| feasibility-assessment | 78 | numeric | \\| Gates evaluated \\| >= 3 stage gates \\| |
| maturity-diagnosis | 23 | numeric | \\| Dimensions scored \\| >= 5 \\| |
| maturity-diagnosis | 24 | numeric | \\| Evidence items per dimension \\| >= 2 \\| |
| maturity-diagnosis | 25 | numeric | \\| Bottlenecks identified \\| >= 1 \\| |
| maturity-diagnosis | 53 | textual | 1. Identify relevant dimensions for the candidate (minimum: technical, market, regulatory, resource, organizational) |
| maturity-diagnosis | 64 | numeric | overall_readiness: <1-9 TRL scale> |
| constraint-identification | 23 | numeric | \\| Constraints identified \\| >= 3 per candidate \\| |
| constraint-identification | 24 | numeric | \\| Hard constraints classified \\| >= 1 \\| |
| constraint-identification | 25 | numeric | \\| Removal paths designed \\| >= 1 per removable constraint \\| |
| constraint-identification | 58 | numeric | 4. For constraints with removability score > 0.3, design `removal-path` |
| resource-envelope-estimation | 24 | numeric | \\| Estimate dimensions \\| >= 3 (time, cost, personnel) \\| |
| resource-envelope-estimation | 25 | numeric | \\| Precision range \\| +/-30% initial, +/-10% refined \\| |
| resource-envelope-estimation | 26 | numeric | \\| Reference analogies \\| >= 2 per estimate \\| |
| resource-envelope-estimation | 58 | numeric | 3. Identify >= 2 analogous projects and extract their actual resource consumption |
| resource-envelope-estimation | 61 | numeric | 6. Flag any estimates with confidence < 0.5 for further investigation |
| comparative-feasibility-ranking | 16 | textual | **Purpose:** Produce a defensible ranking of candidates by feasibility. Uses multi-dimensional radar charts to visualize relative strengths and a weighted feasibility index to collapse multiple dimensions into a single comparable score. |
| comparative-feasibility-ranking | 27 | numeric | \\| Candidates compared \\| >= 2 \\| |
| comparative-feasibility-ranking | 28 | numeric | \\| Dimensions in radar \\| >= 5 \\| |
| comparative-feasibility-ranking | 29 | numeric-table | \\| Weight justifications \\| 1 per dimension \\| |
| comparative-feasibility-ranking | 58 | numeric | 2. Normalize scores to a common scale (1-9 recommended) |
| maturation-pathway-design | 27 | numeric | \\| Stage gates defined \\| >= 3 \\| |
| maturation-pathway-design | 28 | numeric | \\| Milestones per stage \\| >= 2 \\| |
| maturation-pathway-design | 29 | numeric-table | \\| Resource estimates per stage \\| 1 per stage \\| |
| maturation-pathway-design | 37 | textual | \\| target_readiness \\| object \\| Required maturity for implementation \\| |
| maturation-pathway-design | 62 | textual | 2. Define target readiness required for implementation |
| maturation-pathway-design | 76 | textual | target_readiness: <required score> |
| multi-dimensional-readiness-scan | 23 | textual | 3. **Bottleneck Identification** — Analyze the radar for dimensions significantly below the mean or below required thresholds. Deploy `bottleneck-identification` SOP on the radar data. |
| multi-dimensional-readiness-scan | 29 | numeric-table | \\| dimension-assessment \\| 1 \\| Score a single readiness dimension \\| |
| multi-dimensional-readiness-scan | 30 | numeric-table | \\| radar-synthesis \\| 2 \\| Combine scores into radar chart data \\| |
| multi-dimensional-readiness-scan | 31 | numeric-table | \\| bottleneck-identification \\| 3 \\| Identify limiting dimensions \\| |
| multi-dimensional-readiness-scan | 39 | numeric | - Each dimension should have at least 2 evidence items supporting the score |
| multi-dimensional-readiness-scan | 41 | textual | ## Minimum Yield |
| multi-dimensional-readiness-scan | 43 | numeric | - Complete radar with >= 5 dimensions scored |
| constraint-drilling | 26 | numeric | 4. **Removal Path Design** — For constraints with removability > 0.3, design concrete steps to remove or mitigate them. Deploy `removal-path` SOP for each removable constraint. |
| constraint-drilling | 32 | numeric-table | \\| constraint-identification-sop \\| 1 \\| Discover constraints using structured methods \\| |
| constraint-drilling | 33 | numeric-table | \\| constraint-classification \\| 2 \\| Categorize constraints by type \\| |
| constraint-drilling | 34 | numeric-table | \\| removability-assessment \\| 3 \\| Score removability of each constraint \\| |
| constraint-drilling | 35 | numeric-table | \\| removal-path \\| 4 \\| Design removal steps and timeline \\| |
| constraint-drilling | 42 | numeric | - Stage 4 only runs for constraints with removability score > 0.3 |
| constraint-drilling | 45 | textual | ## Minimum Yield |
| constraint-drilling | 47 | numeric | - Classified constraint list with >= 3 constraints identified |
| constraint-drilling | 49 | numeric | - Removal paths for all constraints scoring removability > 0.3 |
| staged-gate-evaluation | 19 | textual | 1. **Gate Criteria Definition** — Define what must be true for a candidate to pass each gate. Deploy `gate-criteria-definition` SOP for each stage gate. |
| staged-gate-evaluation | 29 | numeric-table | \\| gate-criteria-definition \\| 1 \\| Define criteria and pass thresholds \\| |
| staged-gate-evaluation | 30 | numeric-table | \\| gate-judgment \\| 2 \\| Evaluate and render verdict \\| |
| staged-gate-evaluation | 31 | numeric-table | \\| feasibility-synthesis \\| 3 \\| Synthesize into final recommendation \\| |
| staged-gate-evaluation | 35 | numeric | - Stage 1 should define >= 3 gates (e.g., concept feasibility, technical feasibility, implementation readiness) |
| staged-gate-evaluation | 42 | textual | ## Minimum Yield |
| obstacle-analysis | 24 | textual | \\| propose-mitigations \\| Propose evidence-backed mitigations \\| subagent (search **required**) \\| |
| propose-mitigations | 29 | textual | **Required** — must use imported skills to validate feasibility: |
| constraint-analysis | 44 | textual | ## HARD-GATE |
| constraint-analysis | 46 | textual | Before entering this campaign, the following must be true: |
| constraint-analysis | 78 | textual | ## Budget Gate |
| constraint-analysis | 82 | numeric | \\| Subagent calls \\| ≤15 per strategy \\| Pause and report partial \\| |
| constraint-analysis | 83 | numeric | \\| Wall-clock time \\| ≤30 min per strategy \\| Checkpoint and continue \\| |
| constraint-analysis | 84 | numeric | \\| Context tokens \\| ≤80k per strategy \\| Summarize and spawn fresh \\| |
| constraint-analysis | 85 | numeric | \\| Total campaign \\| ≤5 strategies \\| Skip if constraint already resolved \\| |
| constraint-analysis | 94 | textual | ## Minimum Yield |
| constraint-analysis | 97 | numeric | - At least 1 binding constraint identified and characterized |
| constraint-analysis | 100 | numeric | - No unresolved conflicts between top-3 constraints |
| resource-constraint | 63 | textual | ## Budget Gate |
| resource-constraint | 67 | numeric | \\| Subagent calls \\| ≤6 \\| 3 SOPs + synthesis \\| |
| resource-constraint | 68 | numeric | \\| Iterations \\| ≤2 \\| Re-quantify if estimates change \\| |
| resource-constraint | 69 | numeric | \\| Output size \\| ≤3000 tokens \\| Gap table + recommendation \\| |
| assumption-constraint | 55 | numeric | - Top-5 fragile assumptions with validation paths |
| assumption-constraint | 58 | textual | ## Budget Gate |
| assumption-constraint | 62 | numeric | \\| Subagent calls \\| ≤5 \\| 2 SOPs + synthesis \\| |
| assumption-constraint | 63 | numeric | \\| Iterations \\| ≤2 \\| Re-rank if new assumptions surface \\| |
| assumption-constraint | 64 | numeric | \\| Output size \\| ≤3000 tokens \\| Ranked table + validation plan \\| |
| dependency-constraint | 60 | textual | ## Budget Gate |
| dependency-constraint | 64 | numeric | \\| Subagent calls \\| ≤5 \\| 2 SOPs + synthesis \\| |
| dependency-constraint | 65 | numeric | \\| Iterations \\| ≤2 \\| Re-build if tasks change \\| |
| dependency-constraint | 66 | numeric | \\| Output size \\| ≤3000 tokens \\| Graph summary + critical chain \\| |
| conflict-resolution | 66 | textual | ## Budget Gate |
| conflict-resolution | 70 | numeric | \\| Subagent calls \\| ≤8 \\| 3 SOPs + injection generation + validation \\| |
| conflict-resolution | 71 | numeric | \\| Iterations \\| ≤3 \\| May need multiple injection attempts \\| |
| conflict-resolution | 72 | numeric | \\| Output size \\| ≤3000 tokens \\| EC + injection + FRT summary \\| |
| constraint-tree-building | 25 | textual | - Minimum 5 UDEs for a meaningful tree |
| constraint-tree-building | 42 | numeric | - **When to escalate**: If >10 UDEs found, prioritize top-5 by severity before tracing |
| constraint-tree-building | 43 | textual | - **Quality gate**: Every causal link must have a BECAUSE clause (the underlying assumption) |
| sensitivity-ranking | 25 | textual | - Express gaps in comparable units where possible |
| sensitivity-ranking | 43 | numeric | - **When to skip**: If only 1-2 constraints exist, ranking is trivial |
| sensitivity-ranking | 44 | numeric | - **Threshold**: Constraints with sensitivity score >2× the median are "binding" |
| constraint-breaking | 26 | textual | - If constraint is not a dilemma, reframe: "We need X" vs "We cannot have X because Y" |
| constraint-breaking | 29 | numeric | - Input: all assumptions from the EC (typically 8-15 assumptions across 4 arrows) |
| constraint-breaking | 35 | textual | - Injection must be: specific, actionable, within our control, and testable |
| constraint-breaking | 36 | numeric | - Generate 2-3 candidate injections |
| constraint-breaking | 43 | textual | - What conditions (prerequisites) must hold? |
| constraint-breaking | 54 | numeric | - **Success criterion**: At least one injection that resolves the conflict with ≤2 manageable side effects |
