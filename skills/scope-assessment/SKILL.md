---
name: scope-assessment
description: 'SOP: Assess whether a research question has appropriate scope (too broad / appropriate / too narrow)'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Research question (RQ)
output: Scope verdict + adjustment suggestions
dependencies:
  skills:
  - subagent-spawning
---

# Scope Assessment

Assess the scope of a research question — judge whether it is too broad, appropriate, or too narrow, and give adjustment suggestions.

## HARD-GATE

<HARD-GATE>
Input must contain: at least 1 fully stated research question.
</HARD-GATE>

## Pipeline

1. **Precheck**: Is the RQ a complete sentence
2. **Dimension analysis**: Identify the qualifying dimensions in the RQ (time / place / population / method / phenomenon)
3. **Answerability judgment**: How large a study is needed to answer this question?
4. **Scope verdict**: too broad / appropriate / too narrow
5. **Adjustment suggestion**: If not appropriate, suggest a concrete adjustment direction
6. **Output**: Verdict + rationale + adjustment suggestion

## Judgment Criteria

- **Too broad**: Requires a book / multiple papers / cannot be answered by a single experiment design
- **Appropriate**: Answerable by one paper / a clear study design can be specified
- **Too narrow**: Answer is self-evident / lacks theoretical contribution / trivial

## Output Format

```
Scope: TOO_BROAD / APPROPRIATE / TOO_NARROW
Rationale: [one-sentence rationale]
Dimensions: [list of current qualifying dimensions]
Suggestion: [adjustment direction] (only if not APPROPRIATE)
```
