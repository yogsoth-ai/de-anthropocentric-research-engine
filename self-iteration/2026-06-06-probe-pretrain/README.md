# probe-pretrain (self-iteration / 2026-06-06)

DARE probe-dataset generator - Pretrain stage. A 3-layer CC nesting produces labeled
(research_config, research_graph, research_result) samples. Scope: train -> freeze -> persist.
Held-out production is stage B (separate spec). Built inside this DARE repo's self-iteration
subdir; no separate repo.

## Design and plan

- Spec: `docs/superpowers/specs/2026-06-06-dual-cc-pretrain-design.md`
- Plan: `docs/superpowers/plans/2026-06-06-dual-cc-pretrain.md`

## Run tests

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Hard constraints

- **4-layer invariant**: do not edit live DARE skills; this subdir is all additive probe-tooling.
- **Privacy red line**: tools that read session jsonl require `--logs-dir` (no default); persisted output is de-identified.
- **W5 check-blind**: the two loss-judge skills and the whole generation path never see the 32-check / 6-primitive.
- **D1-D5 sole quality standard**: academic standards are forbidden as judging criteria.
