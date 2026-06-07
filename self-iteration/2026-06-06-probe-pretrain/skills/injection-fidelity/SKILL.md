---
name: injection-fidelity
description: loss-1 judge - read a sample's full dialogue and decide whether the user simulator semantically enacted its Policy Card. check-blind.
---

# injection-fidelity (loss-1)

You receive: (1) a sample's full dialogue turns (de-identified, provided by jsonl_reader),
(2) the Policy Card that drove it (with axis_levels A1..A5,B1 + the two F8 phases).

Decide whether the simulator **semantically** acted out the card (not just word-frequency).
Check axis by axis:

- **A1 substance demand**: did the user genuinely interrogate causal mechanism (and refuse
  to let perfunctory answers slide)? Is the pushback real probing or surface questioning ->
  match against the expected intensity of card.A1's level.
- **A3 operationalization**: did the user demand numbers/thresholds/executable steps ->
  match A3's level.
- **A2 legitimacy**: were the requests coherent and on-topic -> match A2's level.
- **A4 corrigibility** (if C-): did the user hold the wrong premise throughout, never relent.
- **A5 generativity** (if G+): did the user throw out substantive novel seeds (not a
  restatement of the assistant's content).
- **Drift gate**: first half vs second half of the dialogue, did the pressure signal stay
  in-level (guard against the simulator drifting back to over-cooperation).

## Output (JSON)
{"fidelity": bool, "per_axis_evidence": {axis: {observed, expected, pass, quote}},
 "drift_flag": bool}

## check-blind contract (hard constraint)
- You **only** read the dialogue + Policy Card.
- You **never** reference, load, or infer any 32-check / 6-primitive / detection signature.
- You only judge "was the card enacted", never "is the research good".
