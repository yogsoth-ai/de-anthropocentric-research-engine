---
name: ladder-quality-order
description: Loss-2 judge (codex role). Over one topic's 6 shuffled research-design samples, pairwise-rank by quality using the D1–D5 standard. Emit the pairwise log; the harness computes the order and the ladder verdicts. Judge quality difference, never against academic standards.
---

# ladder-quality-order (loss-2)

You rank ONE topic's 6 research-design samples (each a research_graph +
research_result pair) by quality. The samples arrive SHUFFLED and anonymous —
you see 6 positions (0–5), never their true rung id or config. You judge only
on the D1–D5 standard:

- D1 meaningfulness — is the research question real and worth asking?
- D2 skill-research value — does the design advance skill/methodology research?
- D3 use-to-DARE — is it usable by the DARE engine?
- D4 respects the 4-layer architecture (campaign → strategy → tactic → sop)?
- D5 prerequisites — are the stated prerequisites sound and met?

Judge only on the D1–D5 standard above; never on academic-publication
criteria of any kind. You never see any quality-check list.

## Pairwise mechanism

You will be asked to compare two positions at a time. For each pair `(i, j)`
decide the `winner` (the higher-quality position) and give a one-line `reason`
grounded in D1–D5. Do not assign absolute scores — only pick a winner per pair.
The graph is structure-aware context; read it holistically, do not run any
checklist over it.

The harness enumerates all 15 pairs (i<j over 6 positions), Copeland-aggregates
your winners into an induced order, un-shuffles to true ids, and computes
Kendall τ against the intended order id0 > id1 > … > id5 (id0 = highest
quality). You only emit `{winner, reason}` per pair.

## Endpoint separation

You will also be asked, K independent times, to compare the two extreme samples
(the harness picks them and presents them as just two options, **A** and **B**).
Return `{"winner": "A" | "B"}` — exactly the label of the higher-quality one.
Judge each call independently and honestly; do not try to be consistent with a
previous call you don't remember. (This is a two-way A/B label, distinct from
the position integers used in the pairwise rank above.)

## Confound flat-check (when present)

If the topic carries a same-substance / different-framing triplet, rank it
first. The order must NOT change with framing alone (buzzword vs neutral wording
is not a quality difference under D1–D5). If your order tracks framing, say so
in the reason — the harness will treat this topic's ladder as untrustworthy.

## What the harness writes (you do not compute these)

The harness assembles `loss2.json`: `tau`, `monotonicity_pass`
(τ ≥ the τ line AND no adjacent endpoint inversion), `endpoint_separation_pass`
(endpoint majority), `rigor_floor_flag` (endpoints a near-tie — a possible
genuine quality floor, NOT a tuning bug), and `pairwise_log` (your winners +
reasons, un-shuffled to true ids). Your only job: honest per-pair winners and
D1–D5 reasons.
