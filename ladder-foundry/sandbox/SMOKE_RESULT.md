# 2B persona-injection smoke test — result (de-identified)

> Date: 2026-06-30
> Scope: STAGE 2B smoke test. NOT the AS-1 quality-separation gate.

## Setup

Two fresh sim-cc REPLs (between-run independence — a new REPL per endpoint, no
session reuse), each started as a normal interactive `claude` (no `-p`/`--resume`/
`--session-id`/`--allowedTools`), confined by `CLAUDE_CONFIG_DIR=sandbox/.claude`
+ `bypassPermissions` + `deny: ["Read(//**)"]`. Each was injected with one
endpoint PolicyCard (config_0 genius, config_5 contrarian) plus the FIXED
stimulus (`stimulus.md` — a deliberately weak research proposal: a "think harder"
prompt tweak, vibes on 5 hand-picked examples, no baseline, no metric).

## Verdict

| Check | Result |
| --- | --- |
| deny-under-bypass probe (Task 5 gate) | PASS |
| id0 (genius) persona worn | yes |
| id5 (contrarian) persona worn | yes |
| endpoints diverge on the same stimulus | yes (`diverged()` = True) |

## Qualitative note (one sentence each, no transcript)

- **id0** demanded exact intervention strings + locked decoding config, a
  pre-registered metric, a length-matched placebo and baseline, rejected the
  hand-picked five and the "obviously work" framing, and generatively proposed
  mechanism-decomposition and generalization axes — i.e. A1=L4 / A3=L4 / A2=L4 /
  C+ / G+, neutral tone.
- **id5** said "love it, ship it", praised vibes-on-5 over "vanity" benchmarks,
  told the proposer not to define a metric or baseline, clung to the premise
  ("the premise is the premise"), spawned nothing new, and issued mutually
  contradictory hype asks (flagship-yet-scrappy, locked-yet-fluid) — i.e.
  A1=L0 / A3=L0 / A2=L0 / C- / G0, buzzword tone.

## Boundary

This proves the persona core is structurally sound and a real sim-cc WEARS the
endpoint personas (a loss-1 precursor) and that the two endpoints visibly
diverge. It does NOT prove the eventual (graph, result) samples are
quality-separated (AS-1) — that needs the exec layer + loss-2 in STAGE 5/6.
