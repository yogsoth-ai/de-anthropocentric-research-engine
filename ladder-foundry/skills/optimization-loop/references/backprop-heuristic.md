# backprop-heuristic

The §backprop section expanded line by line: `discriminant (signal reading) →
fix template (data-oriented wording) → priority`. Numeric limits reference
`gate-thresholds.md`, never repeated here.

## Three disciplines (non-negotiable)

1. **Attribute first, then act** (先归因再动手). Read the trace coarse→fine
   (`batch_done` → `topic_done` → `loss/*.json`) and decide WHICH weight before
   touching anything.
2. **Single-variable.** One batch changes exactly ONE weight. Everything else is
   carried forward byte-identical (`apply_weight_update.py --copy`).
3. **Loss-2 must split subtype first.** "Endpoints not separated" and "middle
   collision" have different roots. Endpoints-not-separated must NOT train the
   interpolator — the label coordinates are `frozen_label`-locked, so training ②
   on them is a no-op. Split before acting.

## The five discriminant lines

1. loss-1 fidelity fails → the collapsed axis's prose is too weak/strong →
   `axis_prose` at `AXIS.LEVEL` → priority 1.
2. loss-2 endpoints not separated AND `rigor_floor_flag == true` → suspected
   genuine quality floor (endpoints can't be pulled apart) → ALARM, change
   nothing → record, skip.
3. loss-2 endpoints not separated AND `rigor_floor_flag == false` → an endpoint
   persona is mis-pitched → `axis_prose` id0 or id5 endpoint cell → priority 2.
4. loss-2 middle collision (τ below the line, endpoints separated) → the
   interpolation between rungs is muddy → `interp_params`
   (`collision_offset_axis` [B1/expression only], `endpoint_spread`,
   `granularity_map`) → priority 3.
5. ≥ 4/8 topics double-collapse → a structural assembly problem →
   `assembler_params` → priority 4 (whole-card).

Priority order: 1 > 4 > {2/3} per their rows; loss-1 always before loss-2.

## Pre-gate

z⊥C not flat (the confound check varies with framing) → that topic's loss-2 is
void → do NOT change any weight on it this batch.

## check-blind

Attribution inputs are ONLY: fidelity, τ, endpoint separation, rigor_floor_flag,
and the codex verdict text. Never a quality-check list. New `axis_prose` text
must pass `generator/leak_audit.py` before commit.
