# Phase 1 — Empirical Floor

DARE's empirical self-analysis. Six one-shot scripts measure the 771-skill body.
See `../../docs/superpowers/specs/2026-06-04-phase1-empirical-floor-design.md`.

## Privacy

`usage_telemetry.py` reads Claude Code logs via a required `--logs-dir` argument.
No log path is hardcoded. Committed outputs in `data/` contain only aggregate
statistics — no paths, session IDs, timestamps, or message content.

## Run

```
python scripts/parse_skills.py   --skills-dir <path-to/.claude/skills> --out data/skills_model.json
python scripts/build_graph.py    --model data/skills_model.json --out data/forward_graph.json
python scripts/blast_radius.py   --graph data/forward_graph.json --out data/blast_radius.json
python scripts/usage_telemetry.py --logs-dir <cc-logs> --graph data/forward_graph.json --out data/telemetry.json
python scripts/completeness_map.py --model data/skills_model.json --graph data/forward_graph.json --telemetry data/telemetry.json --out data/completeness_map.json
python scripts/conformance_audit.py --model data/skills_model.json --out data/conformance_contract.md
```
