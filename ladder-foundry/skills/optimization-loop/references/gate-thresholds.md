# gate-thresholds

This file is a human index of the loop's numeric lines. It is NOT the source of
truth for the gate numbers — it points back to the code that owns each one, so
no number lives in two places.

## Owned by code (DO NOT copy the digits here)

| Number | Owner | Meaning |
| --- | --- | --- |
| `FIDELITY_MIN` | `../../scripts/gate_eval.py` | per-topic batch fidelity_rate floor |
| `BATCH_RATIO_MIN` | `../../scripts/gate_eval.py` | batch pass_ratio floor + converged line |
| `TAU_MIN` | `scripts/run_codex_loss.py` | loss-2 monotonicity Kendall τ line |
| `ENDPOINT_K` | `scripts/run_codex_loss.py` | independent endpoint comparisons |
| `ENDPOINT_ALLOWANCE` | `scripts/run_codex_loss.py` | endpoint majority slack |
| `RIGOR_FLOOR_EPS` | `scripts/run_codex_loss.py` | near-tie half-window for the rigor-floor alarm |

To change any of these, edit the owning module constant — never this table.

## Owned here (no script computes with them)

These are judge-/operator-read numbers with no code owner; this doc is their
sole home:

- 丙-calibration hand-off τ line: **0.80** (τ ≥ 0.80 AND endpoints 100%
  consistent → quality good enough to hand to the next stage). Derived by the
  optimizer from the loss-2 artifact; not a persisted schema field.
- drift tolerance ε: the second-half rate may fall at most ε toward the
  cooperative pole before `drift_flag` trips. Calibrated to real dialogue at
  STAGE 5; start conservative (one band-width).

check-blind: this file names no quality-check list, only the loop's own
thresholds.
