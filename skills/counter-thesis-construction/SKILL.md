---
name: counter-thesis-construction
description: Construct the strongest possible counter-argument to the convergence
  decision using Dialectical Inquiry and Thesis-Antithesis-Synthesis methods.
dependencies:
  tactics:
  - adversarial-debate-protocol
  - assumption-excavation
  sops:
  - steel-manning-synthesis
---

# Counter-Thesis Construction

**Purpose:** Build the most compelling counter-thesis to the convergence winner — not to overturn the decision, but to ensure it can withstand the strongest possible intellectual challenge and to surface any synthesis opportunities.

**When to use:**
- When the decision needs maximum intellectual rigor
- When the problem domain is complex with legitimate competing views
- When synthesis between thesis and antithesis might produce a superior option
- When the decision will face external scrutiny

## Budget

| Metric | Minimum |
|--------|---------|
| Counter-thesis depth | Full argument with evidence |
| Debate rounds | >= 2 (thesis vs antithesis) |
| Synthesis attempts | >= 1 |

## State Ledger

```yaml
thesis: <the convergence decision>
antithesis: <constructed counter-argument>
debate_rounds: []
synthesis_attempted: false
synthesis_result: null
final_verdict: null  # THESIS_STANDS | ANTITHESIS_WINS | SYNTHESIS_FOUND
```

## Available Tactics

| Tactic | When to Deploy |
|--------|---------------|
| adversarial-debate-protocol | Default — formal advocate/critic/judge cycle |
| assumption-excavation | When counter-thesis rests on different assumptions |

## Available SOPs

- advocate-construction — build the counter-thesis case
- critic-attack — attack from both thesis and antithesis sides
- judge-verdict — render verdict on thesis vs antithesis
- steel-manning-synthesis — attempt synthesis of thesis and antithesis

## Execution Guidance

1. Articulate the thesis (convergence decision) clearly
2. Construct the strongest antithesis using advocate-construction
3. Deploy adversarial-debate-protocol: thesis advocates vs antithesis advocates
4. After debate, attempt synthesis — is there a superior option combining both?
5. Judge renders final verdict with explicit reasoning

## Output Format

```yaml
strategy: counter-thesis-construction
thesis: <decision>
antithesis: <counter-argument>
antithesis_strength: <1-10>
debate_rounds: <count>
synthesis_found: true | false
synthesis: <if found>
verdict: THESIS_STANDS | ANTITHESIS_WINS | SYNTHESIS_FOUND
reasoning: <key evidence>
conditions: []
```
