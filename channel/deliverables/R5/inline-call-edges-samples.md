# Tactic call/jump edge inline samples

Status: revised four-node sample only. This file does not modify any `SKILL.md`.

Authoritative relation source: `v4/registry/graph.json`, checked against
`file-transfer/2026-08-23-22-16-dare-v4-architecture.json`.

## 1. Terminal wording and placement rule

Write this rule once, immediately below the existing `## Execution protocol`
heading:

```text
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.
```

An unconditional call is written in the existing numbered step:

```text
You MUST load skill `<name>` to <research operation>.
```

A mode-gated call is written in the existing `## Mode branches` section, next
to the mode condition:

```text
In `<mode>`, You MUST load skill `<name>` to <research operation>.
```

Jump edges remain conditional and non-compulsory:

```text
If <trigger>, consider `<target>` as the next tactic.
If <trigger>, `<target>` may be the better next tactic.
```

Placement rules:

1. Existing wording may be edited to remove repetition, but no research
   meaning may be deleted. Thresholds, rubrics, and contract sections are
   byte-for-byte out of scope.
2. If an existing step already names its SOP, convert that step itself to the
   `MUST load skill` form. Do not append a paraphrase beneath it.
3. Put unconditional calls in `## Execution protocol` and mode-gated calls in
   the existing `## Mode branches`. Do not create a relation section.
4. A call is hard at its point of applicability. A jump is always conditional
   and must never use `MUST`.
5. Do not add frontmatter fields or reproduce a loaded SOP's procedure,
   contract, rubric, or thresholds in the tactic.

## 2. Corrected sample counts

- `biomimetic-transfer`: 5 call / 1 jump; the earlier “2 call” was its mode count.
- `design-experiment`: 12 call / 3 jump; 5 is its mode count.
- `map-research-landscape`: 2 call / 1 jump; this is the actual sparsest tactic.

## 3. Sample: `rank-candidates`

Graph inventory: 11 call, 5 jump. The four execution steps remain four research
transformations. Six conditional calls move to the existing mode section;
step 3 retains only the three calls common to every mode.

### Before

```markdown
## Execution protocol

1. Normalize candidate and criterion schemas; separate hard constraints from preferences.
2. Select `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, or `stakeholder-weighted`.
3. Elicit/validate weights, score with evidence, aggregate or apply veto/threshold rules.
4. Run sensitivity scenarios and return ordered or categorized candidates with rationale.

## Mode branches

- `gap-prioritization`: rank research gaps by evidence deficit and expected value so scarce investigation effort reaches the most consequential unknowns first.
- `direction-selection`: narrow competing research directions against explicit scope, evidence coverage, and feasibility constraints before committing to one.
- `mcda-best-choice`: combine normalized multi-criteria scores with declared weights to select the strongest feasible option while preserving criterion-level rationale.
- `full-ranking`: produce a complete ordered list using at least the required comparison methods, exposing incomparable pairs and method disagreement.
- `category-sorting`: assign candidates to threshold-defined classes when ordinal categories are more defensible than fine-grained ranks.
- `non-compensatory-screening`: apply hard thresholds and vetoes so a severe failure on one criterion cannot be hidden by strengths elsewhere.
- `rapid-triage`: use coarse importance and feasibility passes to reduce a large candidate set quickly, retaining elimination reasons for later review.
- `stakeholder-weighted`: aggregate perspective-specific scores with an explicit consensus rule, showing where stakeholder rankings converge or diverge.
```

### After

```markdown
## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. Normalize the candidate schema and separate hard constraints from preferences. You MUST load skill `define-criteria` to derive explicit criteria and criterion directions from the objective and candidate set.
   If the candidates cannot be made comparable because the research goal still contains unresolved branches, consider `decompose-research-goal` before ranking.
2. Select `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, or `stakeholder-weighted`.
   If candidates are better compared pairwise than scored absolutely, consider `pairwise-ranking`. If the decision requires selecting a jointly feasible subset rather than ordering independent candidates, `portfolio-optimization` may be the better next tactic. If feasibility is the binding uncertainty rather than relative merit, consider `analyze-constraints-readiness`.
3. You MUST load skill `normalize-comparison-scale` to put heterogeneous criterion values on a declared comparable scale. You MUST load skill `score-object` to score every typed candidate against the supplied rubric and evidence. You MUST load skill `aggregate-ranking` to combine the criterion or comparison outputs under the declared rule.
4. You MUST load skill `assess-sensitivity` to perturb the declared weights or decision inputs, report stability, and return ordered or categorized candidates with rationale.
   If a prioritized gap or direction is ready to become a testable proposition, consider `formulate-hypotheses` as the next tactic.

## Mode branches

For `mcda-best-choice`, `full-ranking`, `category-sorting`, or `stakeholder-weighted`, You MUST load skill `elicit-weights` to produce and validate the criterion-weight vector. For `category-sorting` or `non-compensatory-screening`, You MUST load skill `set-threshold` to justify the decision boundaries.

- `gap-prioritization`: You MUST load skill `normalize-gap` to normalize heterogeneous gap records before ranking them by evidence deficit and expected value, so scarce investigation effort reaches the most consequential unknowns first.
- `direction-selection`: You MUST load skill `assess-goal-feasibility` to test candidate directions against resources, obstacles, and timeline before committing to one under explicit scope and evidence-coverage constraints.
- `mcda-best-choice`: combine normalized multi-criteria scores with declared weights to select the strongest feasible option while preserving criterion-level rationale.
- `full-ranking`: produce a complete ordered list using at least the required comparison methods, exposing incomparable pairs and method disagreement.
- `category-sorting`: assign candidates to threshold-defined classes when ordinal categories are more defensible than fine-grained ranks.
- `non-compensatory-screening`: You MUST load skill `apply-veto-filter` to enforce hard failures, and You MUST load skill `check-dominance` to expose dominated and non-dominated alternatives, so a severe failure on one criterion cannot be hidden by strengths elsewhere.
- `rapid-triage`: use coarse importance and feasibility passes to reduce a large candidate set quickly, retaining elimination reasons for later review.
- `stakeholder-weighted`: aggregate perspective-specific scores with an explicit consensus rule, showing where stakeholder rankings converge or diverge.
```

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `define-criteria` | call | execution step 1 | Criteria and directions must be explicit before mode choice. |
| `normalize-comparison-scale` | call | execution step 3 | All modes require comparable criterion values before scoring. |
| `score-object` | call | execution step 3 | Every mode evaluates typed candidates against supplied evidence and rubric. |
| `aggregate-ranking` | call | execution step 3 | Every mode combines its criterion or comparison results under a declared rule. |
| `assess-sensitivity` | call | execution step 4 | Stability is the final shared research transformation. |
| `elicit-weights` | call | Mode branches, four named weighted modes | Only modes whose result contract carries weights require weight elicitation. |
| `set-threshold` | call | Mode branches, category/non-compensatory modes | Those modes require explicit class or pass/fail boundaries. |
| `normalize-gap` | call | `gap-prioritization` branch | Only gap records need the gap-specific normalization schema. |
| `assess-goal-feasibility` | call | `direction-selection` branch | Direction eligibility depends on resources, obstacles, and timeline. |
| `apply-veto-filter` | call | `non-compensatory-screening` branch | Veto enforcement defines non-compensatory elimination. |
| `check-dominance` | call | `non-compensatory-screening` branch | The source mode requires a dominance report beside pass/fail filtering. |
| `decompose-research-goal` | jump | execution step 1 | Trigger: unresolved goal branches prevent a comparable candidate schema. |
| `pairwise-ranking` | jump | execution step 2 | Trigger: pairwise judgments are more defensible than absolute scores. |
| `portfolio-optimization` | jump | execution step 2 | Trigger: the output must be a jointly feasible subset, not an ordering. |
| `analyze-constraints-readiness` | jump | execution step 2 | Trigger: feasibility uncertainty dominates merit comparison. |
| `formulate-hypotheses` | jump | execution step 4 | Trigger: a selected gap or direction is ready for hypothesis construction. |

## 4. Sample: `biomimetic-transfer`

Graph inventory: 5 call, 1 jump. Every existing step already names its SOP, so
each step is converted directly into a command. No duplicate explanatory line
is added.

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

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `biologize-problem` to biologize the problem.
2. You MUST load skill `discover-biological-analog` to discover biological analogs.
3. You MUST load skill `extract-biological-strategy` to extract the causal strategy.
4. You MUST load skill `instantiate-transfer` to instantiate the target transfer.
5. You MUST load skill `evaluate-compatibility` to check compatibility.
   If a viable transfer requires composing mechanisms from multiple biological analogs rather than applying one causal strategy, consider `conceptual-blending` as the next tactic.
Deviation: BioTRIZ mode may branch during strategy extraction, but all five checks remain required.
```

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `biologize-problem` | call | execution step 1 | It performs the existing function-reframing step. |
| `discover-biological-analog` | call | execution step 2 | It performs the existing analog-discovery step. |
| `extract-biological-strategy` | call | execution step 3 | It separates causal mechanism from surface resemblance. |
| `instantiate-transfer` | call | execution step 4 | It converts the biological strategy into a target-domain candidate. |
| `evaluate-compatibility` | call | execution step 5 | It tests the instantiated candidate against target constraints. |
| `conceptual-blending` | jump | execution step 5 | Trigger: one-to-one transfer is insufficient and mechanisms must be composed. |

## 5. Sample: `design-experiment`

Graph inventory: 12 call, 3 jump, 5 modes. Ten calls are shared by all modes.
The ablation-specific and baseline-specific calls live in the existing mode
section rather than the mode-selection execution step.

### Before

```markdown
## Execution protocol

1. Operationalize outcome and factors; identify levels, controls, and comparison baseline.
2. Choose `factorial`, `ablation`, `comparison`, `scaling`, or `robustness` mode.
3. Select statistical method before observing outcomes; specify sample, power, and stopping rule.
4. Write reproducibility, resource, and failure checks; return a runnable design matrix.

## Mode branches

- `factorial`: vary multiple factors in a structured design so main effects and interactions are estimable within the declared resource envelope.
- `ablation`: remove or replace components systematically to attribute the outcome to individual parts and suspected interactions.
- `comparison`: evaluate a target against controlled baselines with matched confounds, compute, tuning effort, and preregistered tests.
- `scaling`: instantiate geometric or otherwise justified scale points to test how the outcome changes across the declared regime.
- `robustness`: perturb relevant conditions or inputs and measure whether the claimed effect survives the defined stress space.
```

### After

```markdown
## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `identify-variables` to operationalize the outcome, factors, controls, and their functional roles. You MUST load skill `enumerate-dimension-values` to define admissible levels or perturbation values.
   If the resource envelope or feasibility constraints cannot support an executable design, consider `analyze-constraints-readiness` before committing to a mode.
2. Choose `factorial`, `ablation`, `comparison`, `scaling`, or `robustness` mode.
3. You MUST load skill `specify-metrics` to preregister metrics, estimands, directionality, and decision thresholds. You MUST load skill `estimate-sample-size` to derive the sample or repetition requirement. You MUST load skill `select-statistical-method` to select the inference or estimation method before observing outcomes; specify power and the stopping rule.
   If the proposed metric or validator may share artifacts, labels, or assumptions with the system under test, consider `audit-validator-independence` before freezing the analysis plan.
4. You MUST load skill `construct-design-matrix` to construct the runnable matrix for the selected mode. You MUST load skill `design-randomness-protocol` to define seeds, repetitions, and propagation rules. You MUST load skill `specify-execution-environment` to capture interpretation-relevant hardware, software, data, configuration, and versions. You MUST load skill `specify-reproducibility-protocol` to define and test the intended reproduction level. You MUST load skill `optimize-design-under-budget` to select a feasible information-efficient design under the declared resource envelope; include resource and failure checks.
   Once the design has produced observations and the task changes from planning to inference, `analyze-experiment-results` may be the better next tactic.

## Mode branches

For `comparison` or `robustness`, You MUST load skill `select-experimental-baseline` to choose a controlled baseline matched to the claim.

- `factorial`: vary multiple factors in a structured design so main effects and interactions are estimable within the declared resource envelope.
- `ablation`: You MUST load skill `map-ablation-components` to define ablatable units, dependencies, and legal removal or replacement operations before attributing the outcome to individual parts and suspected interactions.
- `comparison`: evaluate a target against controlled baselines with matched confounds, compute, tuning effort, and preregistered tests.
- `scaling`: instantiate geometric or otherwise justified scale points to test how the outcome changes across the declared regime.
- `robustness`: perturb relevant conditions or inputs and measure whether the claimed effect survives the defined stress space relative to the selected baseline.
```

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `identify-variables` | call | execution step 1 | Outcomes, factors, controls, and roles must be operationalized first. |
| `enumerate-dimension-values` | call | execution step 1 | Factor levels or perturbation values are part of operationalization. |
| `specify-metrics` | call | execution step 3 | Metrics and estimands must be frozen before outcomes are observed. |
| `estimate-sample-size` | call | execution step 3 | Power or precision determines the sample/repetition plan. |
| `select-statistical-method` | call | execution step 3 | The analysis method is preregistered with power and stopping rules. |
| `construct-design-matrix` | call | execution step 4 | It turns the selected mode and declared levels into the runnable matrix. |
| `design-randomness-protocol` | call | execution step 4 | Randomness controls are part of reproducibility and execution. |
| `specify-execution-environment` | call | execution step 4 | Environment variables constrain interpretation and reproduction. |
| `specify-reproducibility-protocol` | call | execution step 4 | It defines the reproduction target and its verification controls. |
| `optimize-design-under-budget` | call | execution step 4 | It reconciles matrix validity with the declared resource envelope. |
| `select-experimental-baseline` | call | Mode branches, comparison/robustness | These modes interpret effects relative to a controlled baseline. |
| `map-ablation-components` | call | `ablation` branch | Ablation needs a legal component/removal model before matrix construction. |
| `analyze-constraints-readiness` | jump | execution step 1 | Trigger: feasibility is unresolved before design-mode commitment. |
| `audit-validator-independence` | jump | execution step 3 | Trigger: the metric or validator may not be independent of the tested system. |
| `analyze-experiment-results` | jump | execution step 4 | Trigger: observations exist and the task has changed from design to inference. |

## 6. Sample: `map-research-landscape`

Graph inventory: 2 call, 1 jump. Both existing steps already name their SOPs,
so the sparse node stays compact after direct command conversion.

### Before

```markdown
## Execution protocol

1. Generate diverse candidate fields and deliberate boundary crossings (`generate-candidate-directions`).
2. Synthesize maturity, competition, entry-barrier, tractability, and opportunity evidence (`synthesize-field-panorama`).

Deviation: Evidence acquisition is host-selected; do not invoke removed tool wrappers. Re-run candidate generation only when intent or scope changes materially.
```

### After

```markdown
## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `generate-candidate-directions` to generate diverse candidate fields and deliberate boundary crossings.
2. You MUST load skill `synthesize-field-panorama` to synthesize maturity, competition, entry-barrier, tractability, and opportunity evidence.
   If the resulting fields must be ordered, screened, or selected under explicit criteria, consider `rank-candidates` as the next tactic.

Deviation: Evidence acquisition is host-selected; do not invoke removed tool wrappers. Re-run candidate generation only when intent or scope changes materially.
```

### Edge placement ledger

| edge | type | landing | reason |
|---|---|---|---|
| `generate-candidate-directions` | call | execution step 1 | It performs the existing candidate-field generation transformation. |
| `synthesize-field-panorama` | call | execution step 2 | It performs the existing multi-dimensional landscape synthesis. |
| `rank-candidates` | jump | execution step 2 | Trigger: the mapped fields require comparative ordering or selection. |

## 7. Sample self-check

| node | graph call | sample call | graph jump | sample jump | inline rule count | new body section/frontmatter |
|---|---:|---:|---:|---:|---:|---:|
| `rank-candidates` | 11 | 11 | 5 | 5 | 1 | 0 |
| `biomimetic-transfer` | 5 | 5 | 1 | 1 | 1 | 0 |
| `design-experiment` | 12 | 12 | 3 | 3 | 1 | 0 |
| `map-research-landscape` | 2 | 2 | 1 | 1 | 1 | 0 |

Totals: 30/30 call and 10/10 jump. The revised text does not touch frontmatter,
contracts, thresholds, rubrics, provenance, or criteria ledgers. It introduces
no harness terms, runtime budgets, context-management instructions, or
scheduling policy.
