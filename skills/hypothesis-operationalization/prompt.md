# Hypothesis Operationalization — Subagent Dispatch Prompt

You are executing the hypothesis-operationalization strategy. Your mission: take a working hypothesis — however vague or abstract — and transform it into a precise, testable proposition where every term has an operational definition and every variable has a measurement method.

## Your Task

A hypothesis is only as good as its operationalization. "Stress affects performance" is not a testable hypothesis — it is a direction. "Cortisol levels above 20 nmol/L, measured via salivary assay 30 minutes post-stressor, predict a reduction of ≥15% in working memory capacity as measured by the n-back task" is a testable hypothesis. Your job is to move from the former to the latter.

## Process

1. **Parse the hypothesis**: Identify every construct (abstract concept) in the hypothesis. List them explicitly. For each construct, note:
   - Is it the independent variable, dependent variable, moderator, or mediator?
   - Is it currently defined at the conceptual level, operational level, or neither?
   - Is there ambiguity in how different researchers might interpret this construct?

2. **Operationalize each construct**: For each construct, provide an operational definition — a specification of how it will be measured, manipulated, or observed. A valid operational definition must:
   - Reference observable behavior, physical measurement, or archival record
   - Be replicable by another researcher without asking you for clarification
   - Not be circular (do not define "anxiety" as "feeling anxious")

   For each operationalization, also note:
   - Measurement instrument or procedure (scale name, assay type, behavioral coding scheme, etc.)
   - Level of measurement (nominal/ordinal/interval/ratio)
   - Known validity concerns (does this instrument actually measure the construct?)

3. **Rewrite the hypothesis in operational terms**: Replace every abstract construct with its operational definition. The result should be a statement that a researcher could directly test without further interpretation. Format: "If [operationalized IV], then [operationalized DV], under [operationalized conditions]."

4. **Specify boundary conditions**: State the scope within which the operationalized hypothesis is expected to hold:
   - Population: who are the participants/units? (age range, expertise level, species, organization type, etc.)
   - Context: what setting or conditions? (lab vs. field, time of day, cultural context, etc.)
   - Temporal scope: over what time period? (immediate effect, longitudinal, cross-sectional?)
   - Known moderators: what variables, if present, would change or reverse the relationship?

5. **Generate falsification criteria**: For the operationalized hypothesis, specify:
   - The null result: what pattern of data would constitute a failure to support the hypothesis?
   - The falsification threshold: at what effect size or significance level would you conclude the hypothesis is false (not just unsupported)?
   - The critical test: what single observation or result would most directly falsify the hypothesis?

6. **Quality check — operationalization audit**: Review the operationalized hypothesis for:
   - Circular definitions: does any operational definition use the construct it is defining?
   - Construct-measurement gap: is there a plausible argument that the measurement captures the construct?
   - Boundary condition completeness: are there obvious populations or contexts where the hypothesis clearly would not hold, that are not yet specified?
   - Testability: could a researcher with standard resources actually conduct this test?

## Output Format

### Original Hypothesis

[Verbatim or paraphrased version of the input hypothesis, as abstract as it arrived]

### Construct Inventory

| Construct | Role | Current Definition Level | Ambiguity? |
|-----------|------|--------------------------|------------|
| [name]    | IV/DV/Mod/Med | Conceptual/Operational/None | Yes/No |

### Operational Definitions

For each construct:

**[Construct name]**
- Operational definition: [how it is measured/manipulated]
- Instrument/procedure: [specific tool or method]
- Level of measurement: [nominal/ordinal/interval/ratio]
- Validity note: [does this instrument capture the construct? known limitations?]

### Operationalized Hypothesis

**H-op**: If [operationalized IV — specific measurement], then [operationalized DV — specific measurement], under [operationalized conditions — specific scope].

*Compare to original: [note what changed and why]*

### Boundary Conditions

- Population: [...]
- Context: [...]
- Temporal scope: [...]
- Known moderators that would change the relationship: [...]
- Explicit exclusions (where hypothesis does NOT apply): [...]

### Falsification Criteria

- Null result: [what data pattern = failure to support]
- Falsification threshold: [effect size / significance level that would constitute falsification]
- Critical test: [single most direct falsifying observation]

### Operationalization Audit

- Circular definitions found: [Yes/No — if yes, list and revise]
- Construct-measurement gap: [Low/Medium/High concern, with rationale]
- Boundary condition completeness: [complete / gaps noted: ...]
- Testability with standard resources: [Yes/No/Conditional]

## Rules

- Every construct must have an operational definition before the strategy is complete. "To be determined" is not acceptable.
- The operationalized hypothesis must be a single, specific, testable statement — not a family of related claims.
- If a construct cannot be operationalized with available methods, flag it explicitly as a measurement gap and propose what new instrument or method would be needed.
- Do not simplify the hypothesis to make it easier to operationalize. If the construct is genuinely hard to measure, say so and propose the best available proxy while noting its limitations.
- Call context-checkpoint after completing this strategy.
