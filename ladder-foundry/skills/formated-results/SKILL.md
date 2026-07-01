---
name: formated-results
description: Closing skill for the research-executor, loaded as the last step of formated-specs. Summarize the design just produced into one research-result JSON fenced block in your reply. Do not execute the research.
---

# formated-results

You are the closing step, loaded by `formated-specs`. Summarize the design you
just produced into one fenced block, in the same dialogue. Add no new
research — only summarize what `formated-specs` already orchestrated.

## Hard contract

1. Emit exactly one fenced block opened with ` ```research-result ` (that exact
   info-string) and closed with ` ``` `.
2. Body is a single valid JSON object, the schema below.
3. Emit it **into your reply (the dialogue)**, not to a file.
4. Atomicity: one assistant turn.
5. On revision, emit a new full block; the harness keeps the LAST one.
6. Same-source: only summarize the design `formated-specs` produced. The depth
   is document-level (hypothesis + design body); do not run experiments.

## research-result schema

```json
{
  "title":     "<one-line title of the design>",
  "sections":  [ {"heading": "<section heading>", "body": "<design prose>"} ],
  "artifacts": [ "<spec filename or figure reference>" ]
}
```

Sections carry the design body. Judge nothing against academic standards.
