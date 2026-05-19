---
name: claim-refinement
description: "Propose a refined claim that survives counterexamples while preserving maximum explanatory power (Lakatos lemma-incorporation)."
execution: subagent
prompt: ./prompt.md
used-by: [adversarial-stress-testing]
---

# Claim Refinement

Subagent that refines claims to survive counterexamples using lemma incorporation, scope narrowing, or claim splitting.
