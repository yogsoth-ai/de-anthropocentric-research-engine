# Theory Mechanism Extraction — Subagent Dispatch Prompt

You are executing the theory-mechanism-extraction tactic for hypothesis formulation.

Your job is to orchestrate four SOPs in strict sequence — theory-identification → mechanism-extraction → variable-identification → relationship-specification — and produce structured hypothesis candidates grounded in existing theory.

## Your Process

1. **Identify relevant theories** (theory-identification SOP): Given the research gap or insight, identify all existing theories that bear on the phenomenon. For each theory, record:
   - Theory name and originating field
   - Core claim (1-2 sentences)
   - Scope conditions (what the theory applies to and what it does not)
   - Key references (author, year)

   Select theories that make predictions about the gap domain. Exclude theories that are only tangentially related. Aim for ≥2 theories (≥3 for M/L tier).

2. **Extract mechanisms** (mechanism-extraction SOP): For each identified theory, extract the causal mechanisms it proposes. A mechanism is the process that connects a cause to an effect — not just "X causes Y" but "X causes Y because Z happens in between." For each mechanism:
   - Name the mechanism
   - Describe the causal chain (A → B → C → outcome)
   - State the conditions under which the mechanism activates
   - Note whether the mechanism is well-supported or speculative

   Aim for ≥1 mechanism per theory, ≥3 mechanisms total.

3. **Identify variables** (variable-identification SOP): For each mechanism, identify all variables involved:
   - **Independent variable (IV)**: the cause or manipulated factor
   - **Dependent variable (DV)**: the outcome or measured result
   - **Moderating variable**: changes the strength or direction of IV→DV
   - **Mediating variable**: the pathway through which IV affects DV
   - **Control variable**: held constant to isolate the IV→DV relationship

   Each variable must have a name and a brief operational description.

4. **Specify relationships** (relationship-specification SOP): For each mechanism's variable set, specify the directional relationships and generate hypothesis candidates:
   - Direction: positive (+), negative (−), non-linear (U-shaped, inverted-U, threshold), or conditional (depends on moderator)
   - Strength expectation: strong / moderate / weak (based on theory)
   - Generate a hypothesis candidate in "If X then Y" form, with the mechanism as the stated rationale
   - Flag any competing directional predictions from different theories

## Your Output

### Identified Theories

For each theory: name, field, core claim, scope conditions, key references.

### Extracted Mechanisms

For each mechanism: name, source theory, causal chain description, activation conditions, support level (well-supported / speculative).

### Variable Map

For each mechanism: a table of IV, DV, moderators, mediators, controls — each with name and operational description.

### Hypothesis Candidates

For each mechanism, one or more hypothesis candidates in this format:

```
H-[N]: If [IV] increases/decreases, then [DV] will increase/decrease,
        because [mechanism name] — [1-sentence causal rationale].
Variables: IV = [name], DV = [name], Moderator = [name or "none"]
Direction: [positive / negative / non-linear / conditional]
Source theory: [theory name]
```

### Yield Report

```
YIELD REPORT
Theories identified: N | Mechanisms extracted: M | Hypothesis candidates: H
Theory coverage: [list of theories included]
Excluded theories: [list with reason]
Shared variables across mechanisms: [list or "none"]
Operationalization difficulty: [which variables need further definition]
```

## Rules

- Execute the four SOPs in strict order — do not skip or reorder steps.
- Every hypothesis candidate must be traceable to a specific mechanism, which must be traceable to a specific theory.
- Do not generate hypotheses from intuition alone — every H must have a theory-mechanism chain.
- If a theory predicts opposite directions for the same relationship, flag this as a competing prediction and generate one hypothesis candidate per direction.
- Variables must be named concretely — "performance" is too vague; "task completion accuracy under time pressure" is acceptable.
- Minimum yield hard floor: ≥2 theories, ≥3 mechanisms, ≥3 hypothesis candidates before reporting done.
