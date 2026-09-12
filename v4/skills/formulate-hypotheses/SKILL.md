---
name: formulate-hypotheses
description: "Generate testable hypotheses from theory, empirical regularity, anomaly, or explicit explanatory competition. Deductive, inductive, abductive, and competing-hypothesis generation are modes; discriminating predictions and comparison are activated in competing mode."
---

# formulate-hypotheses

## Purpose

Generate and refine testable hypotheses from a gap, theory, induction, anomaly, or competing explanations.

## When to use / not applicable

Use when a research gap or insight can be stated. Select `deductive`, `inductive`, `abductive`, or `competing-hypotheses`; operationalization may follow any generation mode.

## Input contract

```yaml
required: [research_gap_or_observation]
optional: [theory, anomaly, candidate_explanations, variables, prior_evidence]
constraints: [at least one observable consequence]
```

## Execution protocol

1. State the gap/observation and relevant theory or anomaly.
2. Generate candidate hypotheses without premature filtering.
3. Operationalize variables and relationships; state scope and boundary conditions.
4. Check falsifiability and, for competing mode, create discriminating predictions and a comparison matrix.

## Mode branches

- `deductive`: derive predictions from an existing theoretical framework.
- `inductive`: generalize a pattern where theory is weak or absent.
- `abductive`: explain a precisely described anomaly and retain competing explanations.
- `competing-hypotheses`: require mutually discriminating predictions.

## Output contract

```yaml
produces: [hypothesis_set, operational_definitions, predictions, falsification_conditions, comparison_matrix]
delta_fields: [hypothesis_updates, findings, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- Candidate explanation and prediction gates report coverage relative to the declared mechanism/explanation space; record numerator, denominator, batch increment, stopping reason, and source references.
- Base hard gate: at least 1 clear research gap or insight.
- Abductive and competing modes must report relative coverage of candidate explanations and discriminating predictions over the declared mechanism space; fixed counts are not used as a proxy for exhaustiveness.
- Each mechanism must correspond to at least 1 hypothesis candidate.

## Failure and counterexamples

Reject unfalsifiable wording, variables without operational definitions, and “competing” hypotheses with no observable divergence. Deductive mode is not applicable when no usable theory exists; abductive mode is not applicable without a clear anomaly.

## Provenance map

`hypothesis-formulation`, `deductive-hypothesis-generation`, `inductive-hypothesis-generation`, `abductive-hypothesis-generation`, `hypothesis-operationalization`, `theory-mechanism-extraction`, `anomaly-driven-abduction`, `competing-hypothesis-construction`, `competing-hypothesis-matrix`; source thresholds retained.

## Context checkpoint / Delta notes

Append candidate list, selected hypotheses, operational definitions, predictions, falsification tests, and unresolved theory conflicts.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| hypothesis-formulation | 41 | textual | ## HARD-GATE |
| hypothesis-formulation | 43 | textual | <HARD-GATE> |
| hypothesis-formulation | 44 | textual | Preconditions (all must hold before starting): |
| hypothesis-formulation | 45 | numeric | 1. At least 1 clear research gap or insight has been identified |
| hypothesis-formulation | 50 | textual | </HARD-GATE> |
| hypothesis-formulation | 62 | textual | \\| abductive-hypothesis-generation \\| An anomalous phenomenon that existing theory cannot explain has been observed \\| Anomaly → best explanation \\| |
| hypothesis-formulation | 68 | textual | ## Budget Gate |
| hypothesis-formulation | 72 | numeric | \\| S \\| ≥2 structured hypotheses \\| ≥2 relevant theories \\| 1 falsification scenario per hypothesis \\| Optional \\| |
| hypothesis-formulation | 73 | numeric | \\| M \\| ≥3 structured hypotheses \\| ≥3 theories + ≥5 mechanisms \\| ≥1 scenario + boundary conditions per hypothesis \\| ≥2 competing hypotheses \\| |
| hypothesis-formulation | 74 | numeric | \\| L \\| ≥5 structured hypotheses \\| ≥5 theories + ≥8 mechanisms \\| Complete falsifiability audit \\| ≥3 competing hypotheses + discriminating predictions \\| |
| hypothesis-formulation | 78 | textual | Each hypothesis must contain: |
| hypothesis-formulation | 92 | textual | ## Minimum Yield |
| hypothesis-formulation | 94 | textual | Each campaign run must produce: |
| hypothesis-formulation | 95 | numeric | 1. ≥2 complete structured hypotheses (including all 6 components) |
| deductive-hypothesis-generation | 49 | textual | Every step must be traceable: each prediction traces back to a mechanism, each mechanism traces back to a theory. This is what distinguishes a deductive hypothesis from a guess. |
| deductive-hypothesis-generation | 52 | textual | - Theory citation that stays superficial (naming only, no specific propositions) → you must cite the theory's core propositions |
| deductive-hypothesis-generation | 53 | textual | - Skipping the mechanism and jumping straight from theory to prediction → the mechanism is the key node of the deductive chain and cannot be omitted |
| deductive-hypothesis-generation | 54 | textual | - Hypothesis scope too broad ("in all contexts") → deduction must state boundary conditions |
| deductive-hypothesis-generation | 56 | textual | ## Budget Gate |
| deductive-hypothesis-generation | 60 | numeric | \\| S \\| ≥2 named theories \\| ≥3 causal mechanisms \\| ≥2 structured hypotheses \\| 1 falsification scenario per hypothesis \\| |
| deductive-hypothesis-generation | 61 | numeric | \\| M \\| ≥3 named theories \\| ≥5 causal mechanisms \\| ≥3 structured hypotheses \\| ≥1 scenario + boundary conditions per hypothesis \\| |
| deductive-hypothesis-generation | 62 | numeric | \\| L \\| ≥5 named theories \\| ≥8 causal mechanisms \\| ≥5 structured hypotheses \\| full falsifiability audit + competing-theory comparison \\| |
| inductive-hypothesis-generation | 50 | textual | **The core risk of induction**: over-generalization (jumping from a limited sample to a universal law). Each inductive hypothesis must make explicit: |
| inductive-hypothesis-generation | 55 | textual | ## Budget Gate |
| inductive-hypothesis-generation | 59 | numeric | \\| S \\| ≥3 independent observation patterns \\| ≥2 regularities \\| ≥2 structured hypotheses \\| Each hypothesis specifies its sample source \\| |
| inductive-hypothesis-generation | 60 | numeric | \\| M \\| ≥5 independent observation patterns \\| ≥3 regularities \\| ≥3 structured hypotheses \\| Generalization boundary + falsification scenario \\| |
| inductive-hypothesis-generation | 61 | numeric | \\| L \\| ≥8 independent observation patterns \\| ≥5 regularities \\| ≥4 structured hypotheses \\| Complete generalization boundary + comparison of competing regularities \\| |
| abductive-hypothesis-generation | 24 | textual | Inference to the best explanation in the face of anomalies: when an anomalous phenomenon that existing theory cannot explain is observed, systematically generate candidate explanations and select the most plausible one as the hypothesis. |
| abductive-hypothesis-generation | 29 | textual | - Existing theory cannot adequately explain a known phenomenon |
| abductive-hypothesis-generation | 30 | textual | - One of several competing explanations must be selected as the most worth testing |
| abductive-hypothesis-generation | 47 | textual | - **Occam's razor**: when explanatory power is comparable, prefer the explanation with fewer assumptions |
| abductive-hypothesis-generation | 49 | textual | - **Testability**: the best explanation must be able to produce observable predictions (otherwise it cannot be verified) |
| abductive-hypothesis-generation | 50 | textual | - **Generation completeness**: candidate explanations must be exhausted before ranking, to avoid premature convergence |
| abductive-hypothesis-generation | 52 | textual | ## Budget Gate |
| abductive-hypothesis-generation | 56 | numeric | \\| S \\| 1 precisely described anomaly \\| ≥2 candidate explanations \\| 1 best-explanation hypothesis \\| ≥1 competing hypothesis retained \\| |
| abductive-hypothesis-generation | 57 | numeric | \\| M \\| 1–2 anomalies \\| ≥3 candidate explanations \\| ≥2 structured hypotheses \\| complete plausibility ranking \\| |
| abductive-hypothesis-generation | 58 | numeric | \\| L \\| ≥2 related anomalies \\| ≥5 candidate explanations \\| ≥3 structured hypotheses \\| complete ranking + discriminating prediction design \\| |
| hypothesis-operationalization | 50 | textual | - Circular definition (defining X in terms of X) → an operational definition must reference observable behavior or measurement |
| hypothesis-operationalization | 51 | textual | - Mismatch between measurement and construct (operationalism gap) → must argue that the measurement instrument actually captures the construct |
| hypothesis-operationalization | 52 | textual | - Overly broad boundary conditions ("in all contexts") → must be specific about sample, context, and time range |
| hypothesis-operationalization | 54 | textual | ## Budget Gate |
| hypothesis-operationalization | 58 | numeric-table | \\| S \\| All abstract terms have operational definitions \\| All variables have draft measurement methods \\| Main boundary conditions specified \\| 1 falsification scenario \\| |
| hypothesis-operationalization | 59 | numeric | \\| M \\| Above + justification of operationalization validity \\| Variable measurement includes reliability/validity considerations \\| Complete boundary conditions \\| ≥2 falsification scenarios \\| |
| theory-mechanism-extraction | 36 | textual | \\| theory-identification \\| Identify existing theories relevant to the gap/insight (including theory name, core claim, scope of applicability) \\| Required in all modes, executed first \\| |
| theory-mechanism-extraction | 37 | textual | \\| mechanism-extraction \\| Extract operationalizable causal mechanisms from each theory (mechanism = the process linking cause and effect) \\| Required in all modes, after theory-identification \\| |
| theory-mechanism-extraction | 38 | textual | \\| variable-identification \\| Identify independent, dependent, moderating, and control variables from each mechanism \\| Required in all modes, after mechanism-extraction \\| |
| theory-mechanism-extraction | 39 | textual | \\| relationship-specification \\| Specify the directional relationships between variables (positive/negative/nonlinear/moderation/mediation), generating hypothesis candidates \\| Required in all modes, executed last \\| |
| theory-mechanism-extraction | 45 | numeric | - Coverage: 1 theory, ≥1 mechanism, ≥1 hypothesis candidate |
| theory-mechanism-extraction | 48 | numeric | **Standard (M tier, 2-3 theories)** |
| theory-mechanism-extraction | 50 | numeric | - Coverage: ≥2 theories, ≥3 mechanisms, ≥1 hypothesis candidate per mechanism |
| theory-mechanism-extraction | 51 | textual | - Suitable when: the gap spans multiple theoretical frameworks and deductive paths must be compared |
| theory-mechanism-extraction | 53 | numeric | **Deep (L tier, ≥3 theories)** |
| theory-mechanism-extraction | 55 | numeric | - Coverage: ≥3 theories, ≥5 mechanisms, cross-theory variable mapping, ≥5 hypothesis candidates |
| theory-mechanism-extraction | 58 | textual | ## Minimum Yield |
| theory-mechanism-extraction | 60 | numeric | - ≥2 theories identified and described (including core claim and scope of applicability) |
| theory-mechanism-extraction | 61 | numeric | - ≥3 mechanisms extracted from the theories (each with a causal-chain description) |
| theory-mechanism-extraction | 62 | numeric | - Each mechanism corresponds to at least 1 hypothesis candidate, including: |
| anomaly-driven-abduction | 22 | textual | Inductive/abductive path — precisely describe anomalous phenomena that existing theory cannot explain, generate multiple candidate explanations, rank by plausibility, and provide a structured basis for abductive hypotheses. |
| anomaly-driven-abduction | 28 | textual | None of the three steps can be omitted: imprecise description means explanations cannot be focused; insufficient explanations make ranking meaningless; ranking without basis turns hypothesis selection into guesswork. |
| anomaly-driven-abduction | 34 | textual | \\| anomaly-characterization \\| Precisely describe the anomalous phenomenon: what was observed, deviation from expectation, conditions of occurrence, excluded trivial explanations \\| Required in all modes, execute first \\| |
| anomaly-driven-abduction | 35 | textual | \\| explanation-generation \\| Generate multiple candidate explanations (abductive hypotheses); each explanation must fully account for the anomaly \\| Required in all modes, after anomaly-characterization \\| |
| anomaly-driven-abduction | 36 | textual | \\| plausibility-ranking \\| Rank candidate explanations by plausibility criteria (prior probability, explanatory power, parsimony, testability) \\| Required in all modes, execute last \\| |
| anomaly-driven-abduction | 41 | numeric | - Sequential execution: anomaly-characterization → explanation-generation (≥3 explanations) → plausibility-ranking |
| anomaly-driven-abduction | 44 | numeric | **Standard (M tier, 1-3 related anomalies)** |
| anomaly-driven-abduction | 45 | numeric | - anomaly-characterization executes independently for each anomaly; explanation-generation generates ≥3 explanations (explanations may be shared across anomalies); plausibility-ranking ranks all explanations uniformly |
| anomaly-driven-abduction | 49 | textual | - All 3 SOPs execute; explanation-generation additional requirement: each explanation must state why existing theory cannot explain the anomaly; plausibility-ranking additional output: which explanations can be distinguished by a single experiment |
| anomaly-driven-abduction | 52 | textual | ## Minimum Yield |
| anomaly-driven-abduction | 55 | numeric | - ≥3 candidate explanations, each explanation: |
| anomaly-driven-abduction | 63 | textual | - Anomaly description completeness (whether it meets HARD-GATE requirements) |
| competing-hypothesis-construction | 41 | textual | 1. **Force diversity**: competing hypotheses must be genuinely different at the mechanism level, not variants of the same mechanism |
| competing-hypothesis-construction | 49 | textual | - **Comparability**: both hypotheses have clear testable predictions |
| competing-hypothesis-construction | 51 | textual | ## Budget Gate |
| competing-hypothesis-construction | 55 | numeric | \\| S \\| ≥2 genuinely competing hypotheses \\| ≥1 discriminating prediction \\| simplified version (2×2) \\| 1 falsification scenario per hypothesis \\| |
| competing-hypothesis-construction | 56 | numeric | \\| M \\| ≥3 competing hypotheses \\| ≥2 discriminating predictions \\| full matrix (hypotheses × predictions) \\| full falsification per hypothesis \\| |
| competing-hypothesis-construction | 57 | numeric | \\| L \\| ≥4 competing hypotheses \\| ≥3 discriminating predictions \\| full matrix + experiment design suggestions \\| full falsifiability audit \\| |
| competing-hypothesis-matrix | 28 | textual | The three steps cannot be reordered: first generate competing hypotheses (skipping not allowed), then design discriminating predictions (not allowed to only compare without testing), and finally build the comparison matrix (not allowed to only enumerate without quantifying). The final output is not "which hypothesis is correct" but "what experiment can distinguish them." |
| competing-hypothesis-matrix | 34 | numeric | \\| competing-hypothesis-generation \\| Based on the primary hypothesis, generate ≥3 alternative hypotheses competing with it (different mechanisms, same or similar phenomenon prediction range) \\| Required in all modes, execute first \\| |
| competing-hypothesis-matrix | 35 | textual | \\| discriminating-prediction-design \\| Design discriminating predictions for each pair of competing hypotheses — find an observable result for which the two hypotheses predict differently \\| Required in all modes, after competing-hypothesis-generation \\| |
| competing-hypothesis-matrix | 36 | textual | \\| hypothesis-comparison-matrix \\| Assemble all hypotheses and discriminating predictions into a structured comparison matrix, annotating each hypothesis's expected outcome for each prediction \\| Required in all modes, execute last \\| |
| competing-hypothesis-matrix | 41 | numeric | - Sequentially execute all 3 SOPs; generate ≥3 competing hypotheses; design ≥2 discriminating predictions; build comparison matrix |
| competing-hypothesis-matrix | 44 | numeric | **Standard (M tier, 2-3 primary hypotheses)** |
| competing-hypothesis-matrix | 49 | numeric | - All 3 SOPs execute; competing-hypothesis-generation additional requirement: at least 1 competing hypothesis comes from a completely different theoretical framework; discriminating-prediction-design additional requirement: each discriminating prediction annotates the required experiment scale and difficulty; hypothesis-comparison-matrix additional output: recommended experiment priority (most discriminating predictions ranked first) |
| competing-hypothesis-matrix | 52 | textual | ## Minimum Yield |
| competing-hypothesis-matrix | 54 | numeric | - ≥3 competing hypotheses (explaining the same phenomenon as the primary hypothesis but with different mechanisms) |
| competing-hypothesis-matrix | 55 | numeric | - ≥2 discriminating predictions (each prediction produces different expected outcomes for at least 2 hypotheses) |
