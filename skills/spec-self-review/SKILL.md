---
name: spec-self-review
description: Quality gate for Research Specs. Checks for placeholders, consistency,
  scope, ambiguity, context protocol, and quantification. Mandatory before user review.
execution: sequential
---

# Spec Self-Review

You are auditing a Research Spec for quality before presenting it to the user. This review is MANDATORY and cannot be skipped.

## Checklist

Run each check. If any fails, fix the issue inline immediately.

### 1. Placeholder Scan
Search the spec for: "TBD", "TODO", "...", "fill in", "to be determined", or any vague language where specifics are needed.
- Every field must have concrete content
- "Adequate coverage" is NOT acceptable — use numbers

### 2. Internal Consistency
- Do Stage numbers match in backtrack conditions? (e.g., "→ Stage 3" actually exists)
- Do "Expected Input" references point to outputs that prior Stages actually produce?
- Are campaign/strategy names spelled consistently throughout?

### 3. Scope Check
- Is the spec executable in 3-10 sessions?
- If >10 stages, suggest splitting into sub-specs
- If <3 stages, verify this isn't too shallow for the North Star

### 4. Ambiguity Check
- Could any completion criterion be interpreted two different ways?
- Are "Focus Areas" specific enough that two different CCs would focus on the same things?
- If ambiguous, pick one interpretation and make it explicit

### 5. Context Protocol Check
- Does EVERY Stage have: context-init step + at least one context-checkpoint step + campaign-end checkpoint?
- Are topic-slugs in context-init descriptive and unique?

### 6. Quantification Check
- Are ALL completion criteria numeric or objectively verifiable?
- "≥20 papers" is good. "Sufficient papers" is not.
- "≥3 validated gaps with evidence" is good. "Identify gaps" is not.

## Output

If all checks pass: report "Spec self-review: PASS" and proceed.
If any check fails: fix inline, then report what was fixed.
