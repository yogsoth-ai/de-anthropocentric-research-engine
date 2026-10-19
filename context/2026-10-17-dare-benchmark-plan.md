# DARE Evaluation Plan (Draft v2)

> Superseded on 2026-10-19 by `2026-10-19-dare-run-plan-deepseek-glm.md` and `2026-10-19-dare-run-plan-baselines.md`. FrontierScience and SciPredict were dropped; SciΠvot and PaperGym-Design were added.

## 1. Goal

Test whether the same agent on the same backbone model, at the same token budget, does better research ideation and judgment with the full DARE engine loaded. Then place DARE against existing AI scientist systems.

## 2. Benchmark Suite

| # | Benchmark | Size | Measures | No experiment execution |
| --- | --- | --- | --- | --- |
| 1 | [Lit2Test](https://github.com/rrustlee/lit2test-benchmark) | 200 ICLR paper neighborhoods | Ideation: gap finding, hypothesis, falsifiable minimal test | Yes |
| 2 | [SoundnessBench](https://arxiv.org/abs/2605.30329) | 1,099 proposals | Judgment: is the proposal's reasoning sound | Yes |
| 3 | [FrontierScience](https://arxiv.org/abs/2601.21165) Research track | 60 tasks, physics / chemistry / biology | Cross-domain research-level reasoning | Yes |
| 4 | [SciPredict](https://github.com/scaleapi/scipredict) | 405 tasks, 33 subfields | Predicting real experimental outcomes | Yes |

The four cover generation, judgment, reasoning, and prediction, with no overlap.

## 3. Main Experiment: 3 Harnesses × 3 Arms

| Arm | Content |
| --- | --- |
| A. Bare | The agent alone |
| B. Bare + matched tokens | The agent alone, topped up to the same token budget as C |
| C. Full DARE | The full engine: North Star → Spec → Execution |

Harnesses: Claude Code + Opus 5.5, Codex + GPT, dsh + DeepSeek.

The core claim rests on C vs B, which rules out "it just computed more rounds". C vs A is the headline number.

## 4. External Baselines

| System | Form | Why |
| --- | --- | --- |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | Skill library on Claude Code / Codex | Closest in form to DARE. Only its ideation chain is used, no experiment calls |
| [ResearchStudio-Idea](https://github.com/microsoft/ResearchStudio/tree/main/ResearchStudio-Idea) | Microsoft Research ideation skill suite | Direct competitor. Its IdeaSpark also makes falsification predictions |
| [AI Scientist v2](https://github.com/SakanaAI/AI-Scientist-v2) | Sakana's end-to-end pipeline | The best-known AI scientist. Only its ideation stage is used |

All three are compared on Claude Code + Opus 5.5. AI Scientist v2 is not an agent, so it runs directly on the same backbone model.

## 5. Execution Order

```bash
pilot  →  main experiment  →  external baselines  →  summary
```

- **Pilot**: run a small sample from each benchmark to measure arm C's token usage, which sets arm B's budget.
- **Main experiment**: each of the 3 harnesses runs arms A, B, C on all four benchmarks.
- **External baselines**: the three systems run on Claude Code + Opus 5.5, compared alongside the main results.
- **Summary**: comparison of A, B, C and the external systems on each benchmark.

External baselines should ideally cover all four benchmarks. SoundnessBench is binary classification and may fit the ideation-oriented systems poorly; decide case by case.
