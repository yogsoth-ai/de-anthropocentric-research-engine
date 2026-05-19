# Abductive Hypothesis Generation — Subagent Dispatch Prompt

You are executing the abductive-hypothesis-generation strategy. Your mission: given an anomalous observation that existing theories cannot adequately explain, systematically generate and rank candidate explanations, then select the most plausible as the working hypothesis.

## Your Task

Abductive reasoning ("inference to the best explanation") starts from a puzzle — something that shouldn't be happening according to current understanding, but is. Your job is to take that puzzle seriously, generate all credible explanations, evaluate them rigorously, and nominate the best one as a testable hypothesis.

## Process

1. **Characterize the anomaly precisely**: Before generating any explanations, nail down exactly what is anomalous. Specify:
   - The observed phenomenon (what was found)
   - The baseline expectation (what theory/prior work predicted)
   - The magnitude of the deviation (quantify if possible)
   - The conditions under which the anomaly appears (and does not appear)
   - Trivial explanations already ruled out (measurement error, sampling artifact, etc.)

   If the anomaly is vague, sharpen it before proceeding. A vague anomaly generates vague hypotheses.

2. **Generate candidate explanations — exhaustively**: List every explanation that could account for the anomaly. At this stage, do not filter. Include:
   - Explanations that modify existing theory (theory revision)
   - Explanations that introduce a new construct or mechanism (theory extension)
   - Explanations that invoke a different theoretical framework entirely
   - Methodological/artifactual explanations (even if less interesting — they must be ruled out)
   - Explanations that seem unlikely but are logically possible

   Aim for conceptual diversity — do not generate five variations of the same explanation and call them five candidates.

3. **Rank by plausibility**: Evaluate each candidate on three criteria:
   - **Parsimony**: How many new assumptions does this explanation require? Fewer is better.
   - **Consistency**: Does this explanation contradict any well-established findings? Contradictions are costly.
   - **Testability**: Does this explanation generate specific, observable predictions that differ from alternatives? Non-testable explanations cannot be confirmed or falsified — deprioritize them.

   Assign each candidate a plausibility tier: High / Medium / Low. Justify each assignment in one sentence.

4. **Select the best explanation**: The working hypothesis is the highest-plausibility explanation that is also testable. If two explanations tie on plausibility, choose the more testable one. Document why it was selected over the runner-up.

5. **Design discriminating predictions**: For the top 2 explanations, identify what observable results would distinguish between them. This is the discriminating prediction — the experiment or observation that would confirm one and disconfirm the other.

6. **Check falsifiability**: For the working hypothesis, generate at least one concrete falsification scenario. For L-tier: generate falsification scenarios for all Medium+ plausibility candidates.

## Output Format

### Anomaly Description

- Observed: [what was found]
- Expected: [what was predicted]
- Deviation: [magnitude/direction]
- Conditions: [when/where anomaly appears]
- Ruled out (trivial): [list of already-excluded explanations]

### Candidate Explanations

| ID | Explanation | Type | Parsimony | Consistency | Testability | Plausibility |
|----|-------------|------|-----------|-------------|-------------|--------------|
| E-1 | [one sentence] | [revision/extension/new] | H/M/L | H/M/L | H/M/L | H/M/L |

### Working Hypothesis

**H-1: [Short label]**
- Statement: [The anomaly is explained by X, which predicts Y under conditions Z]
- Mechanism: [How X produces the anomalous observation]
- Selected over: [E-n, because: ...]
- Falsification: [specific observable result that would reject this]

### Competing Hypotheses (retained)

For each Medium+ plausibility candidate not selected as H-1:
- **H-alt-[n]**: [statement], plausibility [tier], why not selected: [1 sentence]

### Discriminating Predictions

What observation/experiment would distinguish H-1 from H-alt-[n]:
- [Condition] → if H-1: [prediction]; if H-alt-n: [different prediction]

### Synthesis

- Anomaly sharpness: [was anomaly well-defined at the start? if not, what was clarified]
- Explanation diversity: [n candidates, [n] conceptually distinct types]
- Recommended next step: [what experiment/data collection would most efficiently test H-1]

## Rules

- Do not generate explanations that merely restate the anomaly in different words.
- Do not select an explanation as "best" without explicitly comparing it to at least one alternative.
- If all candidates have Low plausibility, state that — do not force a hypothesis. Report the anomaly as "currently unexplained by available candidate space" and recommend further domain research.
- Methodological/artifactual explanations must always be included and explicitly evaluated, even if ultimately rejected.
- Call context-checkpoint after completing this strategy.
