---
name: update-pairwise-rating
description: "Update candidate latent ratings and uncertainty from sequential pairwise outcomes using an explicitly chosen Bradley-Terry/Elo/Glicko/TrueSkill-style update model."
---

# update-pairwise-rating
## Purpose
Update latent candidate ratings and uncertainty from a pairwise outcome using an explicitly chosen rating model.
## Input contract
```yaml
required: [prior_ratings, pairwise_outcome, rating_model, update_parameters]
optional: [rating_history, draw_policy, uncertainty_floor]
constraints: [model, outcome direction, confidence, and parameter values are recorded]
```
## Procedure
1. Validate the pairwise outcome and retrieve the two prior rating states.
2. Apply the declared Bradley-Terry, Elo, Glicko, TrueSkill, or equivalent update equations.
3. Update both ratings and uncertainty, preserving the pre-update state and the reason for the magnitude.
4. Emit the updated ratings, uncertainty change, and consistency flags for downstream audit.
## Output contract
```yaml
produces: [updated_ratings, uncertainty_updates, update_trace, consistency_flags]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- The update is reproducible from prior ratings, outcome, model, and parameters.
- A weak or low-confidence outcome cannot cause a larger update than the declared model permits.
## Failure and counterexamples
Do not update ratings when the pairwise record is tied to the wrong candidate IDs or model. Do not silently reset rating history.
## Provenance map
- resolved: dynamic-tracking
