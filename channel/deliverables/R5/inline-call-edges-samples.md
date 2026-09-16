# Tactic call/jump edge inline samples

Status: sample only. This file does not modify any `SKILL.md`.

Authoritative relation source: `v4/registry/graph.json`, checked against
`file-transfer/2026-08-23-22-16-dare-v4-architecture.json`.

## 1. Terminal wording and placement rule

Call edges use one of these forms inside the existing execution step:

```text
You MUST load skill `<name>` to <research operation>. Do not perform this
operation inline; the loaded SOP owns its contract and thresholds.
```

```text
You MUST load skill `<name-a>` to <operation-a>, and You MUST load skill
`<name-b>` to <operation-b>. Do not perform either operation inline; each
loaded SOP owns its contract and thresholds.
```

When a call is mode-dependent, the condition narrows applicability but does
not soften the command:

```text
In `<mode>`, You MUST load skill `<name>` to <research operation>. Do not
perform this operation inline; the loaded SOP owns its contract and thresholds.
```

Jump edges use a trigger and no compulsory verb:

```text
If <trigger>, consider `<target>` as the next tactic.
If <trigger>, `<target>` may be the better next tactic.
```

Placement rules:

1. Keep every existing character of the tactic body. Add prose immediately
   below the execution step where the decision occurs.
2. Do not add a heading, table, frontmatter field, dependency list, or generic
   edge appendix to a tactic body.
3. A call is hard at its point of applicability. A jump is always conditional
   and must never use `MUST`.
4. Shared SOPs remain shared: naming the skill does not reproduce its procedure,
   contract, rubric, or thresholds in the tactic.

## 2. Source-count discrepancy

`18-inline-call-edges.md` labels `biomimetic-transfer` as “2 call”. Both the
frozen architecture and current graph contain **5 call edges and 1 jump edge**
for that node. The node has **2 modes**, so the “2 call” label appears to have
copied the mode count. This sample preserves the graph's 5+1 relations; using
two calls would violate edge conservation before injection begins.

## 3. Sample: `rank-candidates`

Graph inventory: 11 call, 5 jump. No step expansion is needed. The existing
four steps already represent four research transformations; the inserted
sentences expose the SOP boundary within each transformation rather than
turning SOP names into artificial top-level steps.

### Before

```markdown
## Execution protocol

1. Normalize candidate and criterion schemas; separate hard constraints from preferences.
2. Select `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, or `stakeholder-weighted`.
3. Elicit/validate weights, score with evidence, aggregate or apply veto/threshold rules.
4. Run sensitivity scenarios and return ordered or categorized candidates with rationale.
```

### After

```markdown
## Execution protocol

1. Normalize candidate and criterion schemas; separate hard constraints from preferences.
   For gap records, You MUST load skill `normalize-gap` to normalize them into the comparable candidate schema. You MUST load skill `define-criteria` to derive explicit criteria and directions from the objective and candidate set. Do not perform either operation inline; each loaded SOP owns its contract and thresholds.
   If the candidates cannot be made comparable because the research goal still contains unresolved branches, consider `decompose-research-goal` before ranking.
2. Select `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, or `stakeholder-weighted`.
   In `direction-selection`, You MUST load skill `assess-goal-feasibility` to test candidate directions against resources, obstacles, and timeline. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
   If candidates are better compared pairwise than scored absolutely, consider `pairwise-ranking`. If the decision requires selecting a jointly feasible subset rather than ordering independent candidates, `portfolio-optimization` may be the better next tactic. If feasibility is the binding uncertainty rather than relative merit, consider `analyze-constraints-readiness`.
3. Elicit/validate weights, score with evidence, aggregate or apply veto/threshold rules.
   You MUST load skill `normalize-comparison-scale` to put heterogeneous criterion values on a declared comparable scale. In weighted modes, You MUST load skill `elicit-weights` to produce and validate the criterion-weight vector. You MUST load skill `score-object` to score every typed candidate against the supplied rubric and evidence. In `category-sorting` or `non-compensatory-screening`, You MUST load skill `set-threshold` to justify the decision boundaries. In `non-compensatory-screening`, You MUST load skill `apply-veto-filter` to enforce hard failures. Where dominance is part of the selected decision rule, You MUST load skill `check-dominance` to expose dominated and non-dominated alternatives. You MUST load skill `aggregate-ranking` to combine the resulting criterion or comparison outputs under the declared rule. Do not perform any of these operations inline; each loaded SOP owns its contract and thresholds.
4. Run sensitivity scenarios and return ordered or categorized candidates with rationale.
   You MUST load skill `assess-sensitivity` to perturb the declared weights or decision inputs and report stability. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
   If a prioritized gap or direction is ready to become a testable proposition, consider `formulate-hypotheses` as the next tactic.
```

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `normalize-gap` | call | step 1, gap-record condition | It transforms heterogeneous gap records before comparison. |
| `define-criteria` | call | step 1 | Criteria and directions belong to schema normalization, before mode choice. |
| `assess-goal-feasibility` | call | step 2, `direction-selection` | Feasibility determines whether a direction is eligible for ranking. |
| `normalize-comparison-scale` | call | step 3, before scoring | Heterogeneous measurements must be comparable before score aggregation. |
| `elicit-weights` | call | step 3, weighted-mode condition | The selected mode determines whether a weight vector is required. |
| `score-object` | call | step 3 | This is the evidence-backed candidate scoring operation named by the step. |
| `set-threshold` | call | step 3, category/non-compensatory condition | These modes require explicit class or pass/fail boundaries. |
| `apply-veto-filter` | call | step 3, non-compensatory condition | A veto is the defining non-compensatory elimination operation. |
| `check-dominance` | call | step 3, decision-rule condition | Dominance is checked after comparable scores exist and before final aggregation. |
| `aggregate-ranking` | call | step 3 | It combines criterion-level results under the declared decision rule. |
| `assess-sensitivity` | call | step 4 | Sensitivity is the final stability transformation already named by the step. |
| `decompose-research-goal` | jump | step 1 | Trigger: the unresolved goal prevents a comparable candidate schema. |
| `pairwise-ranking` | jump | step 2 | Trigger: relative pairwise judgments are more defensible than absolute scores. |
| `portfolio-optimization` | jump | step 2 | Trigger: the output must be a jointly feasible subset, not an ordering. |
| `analyze-constraints-readiness` | jump | step 2 | Trigger: feasibility uncertainty dominates merit comparison. |
| `formulate-hypotheses` | jump | step 4 | Trigger: a selected gap or direction is ready for hypothesis construction. |

## 4. Sample: `biomimetic-transfer`

Graph inventory: 5 call, 1 jump. Its sparse body needs no wrapper prose: each
existing workflow step receives exactly one hard SOP boundary, and the jump is
attached to the point where single-mechanism transfer may fail.

### Before

```markdown
## Execution protocol
1. Biologize the problem (`biologize-problem`).
2. Discover biological analogs (`discover-biological-analog`).
3. Extract the causal strategy (`extract-biological-strategy`).
4. Instantiate the target transfer (`instantiate-transfer`).
5. Check compatibility (`evaluate-compatibility`).
Deviation: BioTRIZ mode may branch during strategy extraction, but all five checks remain required.
```

### After

```markdown
## Execution protocol
1. Biologize the problem (`biologize-problem`).
   You MUST load skill `biologize-problem` to express the target need as an implementation-independent biological function. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
2. Discover biological analogs (`discover-biological-analog`).
   You MUST load skill `discover-biological-analog` to identify living systems that solve the stated function. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
3. Extract the causal strategy (`extract-biological-strategy`).
   You MUST load skill `extract-biological-strategy` to recover the mechanism, conditions, and causal strategy from the selected analogs. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
4. Instantiate the target transfer (`instantiate-transfer`).
   You MUST load skill `instantiate-transfer` to map the extracted mechanism into a concrete target-domain design. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
5. Check compatibility (`evaluate-compatibility`).
   You MUST load skill `evaluate-compatibility` to test the transfer against target constraints and failure conditions. Do not perform this operation inline; the loaded SOP owns its contract and thresholds.
   If a viable transfer requires composing mechanisms from multiple biological analogs rather than applying one causal strategy, consider `conceptual-blending` as the next tactic.
Deviation: BioTRIZ mode may branch during strategy extraction, but all five checks remain required.
```

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `biologize-problem` | call | step 1 | It performs the function reframing named by the step. |
| `discover-biological-analog` | call | step 2 | It performs analog discovery after function definition. |
| `extract-biological-strategy` | call | step 3 | It separates causal mechanism from surface resemblance. |
| `instantiate-transfer` | call | step 4 | It converts the biological strategy into a target-domain candidate. |
| `evaluate-compatibility` | call | step 5 | It tests the instantiated candidate against target constraints. |
| `conceptual-blending` | jump | step 5 | Trigger: one-to-one mechanism transfer is insufficient and mechanisms must be composed. |

## 5. Sample: `design-experiment`

Graph inventory: 12 call, 3 jump, 5 modes. Modes parameterize the common SOP
pipeline; they are not substitutes for it. Only `map-ablation-components` and
`select-experimental-baseline` need mode-gated hard calls. The other SOPs serve
the common design transformation with mode-specific inputs and outputs.

### Before

```markdown
## Execution protocol

1. Operationalize outcome and factors; identify levels, controls, and comparison baseline.
2. Choose `factorial`, `ablation`, `comparison`, `scaling`, or `robustness` mode.
3. Select statistical method before observing outcomes; specify sample, power, and stopping rule.
4. Write reproducibility, resource, and failure checks; return a runnable design matrix.
```

### After

```markdown
## Execution protocol

1. Operationalize outcome and factors; identify levels, controls, and comparison baseline.
   You MUST load skill `identify-variables` to identify factors and their functional roles, and You MUST load skill `enumerate-dimension-values` to define admissible levels or perturbation values. Do not perform either operation inline; each loaded SOP owns its contract and thresholds.
   If the resource envelope or feasibility constraints cannot yet support an executable design, consider `analyze-constraints-readiness` before committing to a mode.
2. Choose `factorial`, `ablation`, `comparison`, `scaling`, or `robustness` mode.
   In `ablation`, You MUST load skill `map-ablation-components` to define ablatable units, dependencies, and legal removal or replacement operations. In `comparison` or `robustness`, You MUST load skill `select-experimental-baseline` to choose controlled baselines matched to the claim. Do not perform either operation inline; each loaded SOP owns its contract and thresholds.
3. Select statistical method before observing outcomes; specify sample, power, and stopping rule.
   You MUST load skill `specify-metrics` to preregister metrics, estimands, directionality, and decision thresholds. You MUST load skill `estimate-sample-size` to derive the sample or repetition requirement, and You MUST load skill `select-statistical-method` to select the inference or estimation method. Do not perform any of these operations inline; each loaded SOP owns its contract and thresholds.
   If the proposed metric or validator may share artifacts, labels, or assumptions with the system under test, consider `audit-validator-independence` before freezing the analysis plan.
4. Write reproducibility, resource, and failure checks; return a runnable design matrix.
   You MUST load skill `construct-design-matrix` to build the runnable matrix for the selected mode. You MUST load skill `design-randomness-protocol` to define seeds, repetitions, and propagation rules. You MUST load skill `specify-execution-environment` to capture interpretation-relevant hardware, software, data, configuration, and versions. You MUST load skill `specify-reproducibility-protocol` to define and test the intended reproduction level. You MUST load skill `optimize-design-under-budget` to select a feasible information-efficient design under the declared resource envelope. Do not perform any of these operations inline; each loaded SOP owns its contract and thresholds.
   Once the design has produced observations and the task changes from planning to inference, `analyze-experiment-results` may be the better next tactic.
```

### Mode-to-call relationship

| mode | common calls receive | additional hard call |
|---|---|---|
| `factorial` | factors, levels, estimands, interaction structure | none |
| `ablation` | component states, attribution contrasts, interaction plan | `map-ablation-components` |
| `comparison` | treatments, matched controls, comparison estimand | `select-experimental-baseline` |
| `scaling` | scale axis, geometric levels, curve estimand | none |
| `robustness` | perturbation axis, severity levels, survival metric | `select-experimental-baseline` |

The table explains parameter flow only; it is not proposed body content and
does not create a relation section in `SKILL.md`.

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `identify-variables` | call | step 1 | Outcomes, factors, controls, and roles must be operationalized first. |
| `enumerate-dimension-values` | call | step 1 | Factor levels or perturbation values are part of operationalization. |
| `map-ablation-components` | call | step 2, `ablation` | Ablation mode needs a legal component/removal model before matrix construction. |
| `select-experimental-baseline` | call | step 2, `comparison`/`robustness` | These modes interpret effects relative to a controlled baseline. |
| `specify-metrics` | call | step 3 | Metrics and estimands must be frozen before outcomes are observed. |
| `estimate-sample-size` | call | step 3 | Power or precision determines the sample/repetition plan. |
| `select-statistical-method` | call | step 3 | The analysis method is preregistered with the sample and stopping rule. |
| `construct-design-matrix` | call | step 4 | It turns the selected mode and declared levels into the runnable matrix. |
| `design-randomness-protocol` | call | step 4 | Randomness controls are part of reproducibility and execution. |
| `specify-execution-environment` | call | step 4 | Environment variables constrain interpretation and reproduction. |
| `specify-reproducibility-protocol` | call | step 4 | It defines the reproduction target and its verification controls. |
| `optimize-design-under-budget` | call | step 4 | It reconciles matrix validity with the declared resource envelope. |
| `analyze-constraints-readiness` | jump | step 1 | Trigger: feasibility is unresolved before design-mode commitment. |
| `audit-validator-independence` | jump | step 3 | Trigger: the metric or validator may not be independent of the tested system. |
| `analyze-experiment-results` | jump | step 4 | Trigger: observations exist and the task has changed from design to inference. |

## 6. Sample self-check

| node | graph call | sample call | graph jump | sample jump | original lines changed | new body section/frontmatter |
|---|---:|---:|---:|---:|---:|---:|
| `rank-candidates` | 11 | 11 | 5 | 5 | 0 | 0 |
| `biomimetic-transfer` | 5 | 5 | 1 | 1 | 0 | 0 |
| `design-experiment` | 12 | 12 | 3 | 3 | 0 | 0 |

The sample introduces no harness terms, runtime budgets, context-management
instructions, or scheduling policy.
