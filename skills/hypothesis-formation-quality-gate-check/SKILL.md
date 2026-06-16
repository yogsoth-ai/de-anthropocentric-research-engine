---
name: hypothesis-formation-quality-gate-check
description: 'Shared SOP: General quality-gate check (format completeness, logical consistency)'
version: 1.0.0
category: hypothesis-formation
type: sop
shared: true
campaigns:
- gap-prioritization
- hypothesis-formulation
- research-question
input: Any deliverable (gap list / hypothesis / RQ)
output: Pass/fail + issue list
dependencies:
  skills:
  - subagent-spawning
---

# Quality Gate Check

General quality-gate check — verify the format completeness and logical consistency of a deliverable.

## HARD-GATE

<HARD-GATE>
Input must contain: at least 1 deliverable to check.
</HARD-GATE>

## Pipeline

1. **Precondition check**: Is the deliverable non-empty
2. **Format completeness**: Does it contain all required fields
3. **Logical consistency**: Are the parts contradictory
4. **Citation completeness**: Do the cited sources exist
5. **Actionability**: Is the deliverable specific and executable enough
6. **Overall determination**: PASS / FAIL
7. **Output**: Determination + issue list (if any)

## Check Dimensions

| Dimension | What is checked | FAIL condition |
|------|---------|----------|
| Format completeness | Are all required fields present | Missing required fields |
| Logical consistency | Are the parts contradictory | Internal contradiction exists |
| Citation completeness | Are cited sources traceable | Citation cannot be verified |
| Actionability | Is it specific enough | Too abstract to execute |
| Unambiguity | Are there multiple interpretations | Key terms are ambiguous |

## Output Format

```
Judgment: PASS / FAIL
Issues found: [count]
Issue list:
  1. [dimension]: [specific issue] — [correction suggestion]
  2. ...
Severity: CRITICAL / MINOR (per issue)
```
