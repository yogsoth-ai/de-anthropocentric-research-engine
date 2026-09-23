---
name: research-catalog
description: "This is the v4 capability menu. It indexes exactly 51 tactics in 10 families and tells the caller when each tactic is useful."
---

# research-catalog

## Purpose

This is the v4 capability menu. It indexes exactly 51 tactics in 10 families and tells the caller when each tactic is useful. It does not list SOPs. A selected tactic owns its SOP calls through `You MUST load skill ...` instructions in the tactic body.

## Input Contract

```yaml
required: [confirmed_north_star, research_brief]
optional: [current_spec_view, state_slice, constraints]
constraints:
  - return tactic cards, not SOP cards
  - preserve the tactic id exactly as listed
```

## Execution Protocol

Read the North Star, ResearchBrief, current SpecView, and relevant state slice. Select 3-5 candidate tactics whose purpose and prerequisites match the current objective. Return their family, id, why-now condition, required inputs, expected outputs, and next call. Do not invent an order for tactics that the Spec has not ordered. Once a tactic is selected, the caller MUST load that tactic skill; its body is authoritative for SOP calls and thresholds.

## Tactic Index

### ACQUISITION

| Tactic | When to use |
| --- | --- |
| `synthesize-literature-evidence` | When the question needs a structured synthesis of literature claims and evidence. |
| `mine-patent-landscape` | When patents, assignees, classifications, or filing trends define the search space. |
| `assess-prior-art-and-claims` | When a proposed contribution must be tested against prior art and claim boundaries. |
| `map-patent-white-space` | When patent coverage and uncrowded opportunity regions must be compared. |
| `audit-benchmark-validity` | When benchmark metrics, datasets, or comparison protocols may distort conclusions. |
| `synthesize-meta-analytic-evidence` | When multiple studies provide comparable effect estimates requiring pooled interpretation. |
| `establish-empirical-baseline` | When a new method needs a reproducible baseline and a defensible comparison reference. |

### CONVERGENCE

| Tactic | When to use |
| --- | --- |
| `pairwise-ranking` | When candidates are easier to compare two at a time than on a shared absolute scale. |
| `structured-consensus` | When several judgments must be reconciled with explicit disagreement and evidence. |
| `portfolio-optimization` | When the result should be a balanced subset rather than one winner. |

### CROSS

| Tactic | When to use |
| --- | --- |
| `rank-candidates` | When typed candidates must be scored, screened, classified, or selected under stated criteria. |
| `map-validity-envelope` | When the conditions under which a claim or design remains valid are unknown. |
| `explore-dimensional-space` | When a design space needs axes, combinations, and coverage gaps. |
| `adversarial-deliberation` | When a consequential decision needs structured opposing cases before commitment. |
| `analyze-constraints-readiness` | When constraints, dependencies, conflicts, and readiness determine whether work can proceed. |

### DIRECTION

| Tactic | When to use |
| --- | --- |
| `map-research-landscape` | When fields or subfields must be compared by maturity, competition, barriers, and opportunity. |
| `decompose-research-goal` | When a broad goal must become ordered, testable objectives and dependencies. |

### EXPERIMENT

| Tactic | When to use |
| --- | --- |
| `design-experiment` | When hypotheses need factors, variables, controls, measurements, and analysis plans. |
| `analyze-future-scenarios` | When a design or strategy must be tested against plausible future conditions. |
| `analyze-experiment-results` | When observations must be interpreted against the preregistered design and gates. |

### HYPOTHESIS

| Tactic | When to use |
| --- | --- |
| `formulate-hypotheses` | When observations or gaps must become structured, named, testable hypotheses. |
| `falsifiability-audit` | When a hypothesis needs explicit disconfirmation conditions and observable consequences. |
| `formulate-research-question` | When an intent must become a precise, bounded research question. |
| `decompose-research-question` | When one question contains separable subquestions with distinct evidence needs. |

### IDEATION

| Tactic | When to use |
| --- | --- |
| `analogical-discovery` | When another domain may provide a transferable mechanism or design pattern. |
| `destructive-ideation` | When assumptions should be inverted or deliberately broken to expose alternatives. |
| `structural-transformation` | When an existing concept should be decomposed and recombined structurally. |
| `coverage-white-space-search` | When the candidate space is incomplete and missing regions need systematic search. |
| `resolve-inventive-contradiction` | When requirements conflict and a solution must preserve both sides. |
| `biomimetic-transfer` | When biological functions or mechanisms may transfer to the target problem. |
| `conceptual-blending` | When two or more concept spaces should be combined to produce emergent candidates. |
| `evolve-solution-population` | When iterative variation and selection are more useful than one-shot ideation. |

### INSIGHT

| Tactic | When to use |
| --- | --- |
| `validate-research-gap` | When an alleged gap needs evidence, novelty, and boundary verification. |
| `drill-root-causes` | When surface symptoms must be traced to mechanisms and contributing conditions. |
| `assumption-stress-test` | When hidden assumptions may determine whether a conclusion survives. |
| `robustness-analysis` | When conclusions must be checked across perturbations, alternatives, or distributions. |
| `sensitivity-analysis` | When priority depends on which inputs or assumptions drive the result. |
| `problem-reframing` | When the current problem statement may encode an unhelpful framing or boundary. |
| `map-stakeholder-system` | When actors, incentives, dependencies, and tensions shape the research problem. |

### STRESS

| Tactic | When to use |
| --- | --- |
| `structured-red-team` | When an artifact needs organized attacks from distinct critical perspectives. |
| `fmea-risk-analysis` | When failure modes should be enumerated, rated, and mitigated before execution. |
| `counterfactual-causal-analysis` | When causal necessity or sufficiency must be tested by counterfactual changes. |
| `reductio-counterexample-analysis` | When a claim can be challenged by deriving consequences or counterexamples. |
| `falsification-first-audit` | When the fastest route to confidence is to seek decisive disconfirmation. |
| `audit-structural-equivalence` | When two artifacts may be equivalent in structure despite different wording. |
| `audit-validator-independence` | When a validator may share assumptions or evidence with the artifact it checks. |
| `audit-convergence-independence` | When multiple routes to a conclusion may not be genuinely independent. |
| `audit-explanatory-compression` | When a compact explanation may be hiding unsupported jumps or omitted variables. |

### STRUCTURING

| Tactic | When to use |
| --- | --- |
| `build-domain-ontology` | When concepts and relations need a stable hierarchy and vocabulary. |
| `construct-causal-model` | When variables, mechanisms, and causal dependencies need explicit structure. |
| `construct-argument-map` | When claims, reasons, objections, and evidence need an inspectable argument graph. |

## Output Contract

```yaml
produces: [tactic_cards, selection_rationale, next_call]
tactic_card_fields: [id, family, when_to_use, requires, produces, source_ref, next_call]
```

## Completion Criteria

The response contains only valid tactic ids from the 51-item index, gives a reason for each selected card, and maps each card to its source body. No SOP is presented as a menu choice.

## Failure and Backtrack

If the North Star or scope is too vague to select a tactic, return `NEEDS_CONTEXT` and list the missing fields. If no card meets the current gate, retain the Spec stage and report the mismatch; do not substitute a generic prompt or silently choose an unrelated tactic.

## Boundary

The catalog is a product-shell index. It is not a third graph layer and does not create edges or replace the tactic body as the authority for scientific contracts and SOP calls.
