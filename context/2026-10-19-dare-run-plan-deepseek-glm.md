# DARE Run Plan: DeepSeek / GLM (2026-10-19)

Main experiment on the two cheap backbones. Each model runs arms A, B and C on the full set of all four benchmarks. These results also decide which items the pricier models (Claude, Gemini, GPT) run later; that selection is out of scope here.

Companion plan: `2026-10-19-dare-run-plan-baselines.md`. Both plans use the same benchmarks and the same deliverable layout.

## 1. Conditions

| Condition ID | Agent | Model | Arm |
| --- | --- | --- | --- |
| `dsh.deepseek-v4-flash.A-bare` | [dsh](https://github.com/deepseek-ai/deepseek-harness) | `deepseek-v4-flash` | A. Bare |
| `dsh.deepseek-v4-flash.B-matched` | dsh | `deepseek-v4-flash` | B. Bare + matched tokens |
| `dsh.deepseek-v4-flash.C-dare` | dsh | `deepseek-v4-flash` | C. Full DARE |
| `zcode.glm-5.3.A-bare` | [ZCode CLI](https://github.com/zai-org/ZCode) | GLM-5.3 | A. Bare |
| `zcode.glm-5.3.B-matched` | ZCode CLI | GLM-5.3 | B. Bare + matched tokens |
| `zcode.glm-5.3.C-dare` | ZCode CLI | GLM-5.3 | C. Full DARE |

- **A. Bare.** The agent with no extra skills. The prompt is the benchmark input plus the output format.
- **B. Bare + matched tokens.** Same as A, but the agent is told to draft, critique and revise its answer over several rounds. If a run ends below the budget, the runner sends "continue refining your answer" turns until total tokens reach the budget. The budget per benchmark is the median per-item token use of arm C in the pilot (Section 4).
- **C. Full DARE.** DARE installed with `npx skills add yogsoth-ai/de-anthropocentric-research-engine --skill '*'` (the whole graph, not a subset). The prompt invokes `/de-anthropocentric-research-engine` with the benchmark input as the research direction. No human is in the loop, so the prompt tells the agent to approve its own Spec and run it to completion.

Rules for all six conditions:

- **Online retrieval is off.** No web search, no web fetch, no MCP servers. The only network traffic is the model API.
- **One fresh session per item.** The working directory holds only the item input (plus the installed skills in C). No benchmark repository clone sits in the workspace, since several repos hold answer keys or baseline outputs.
- **One run per item.** No re-sampling for a better answer.
- **Final answer goes to a file.** The prompt tells the agent to write its final answer to `output/answer.json` (or `output/answer.md` for PaperGym) in the benchmark's required format.
- **ZCode CLI must be built from source.** The official site ships only the desktop app. Record the build commit and command.

## 2. Benchmarks

All four run in full. FrontierScience and SciPredict are dropped.

### 2.1 Lit2Test

- **Source**: [repo](https://github.com/rrustlee/lit2test-benchmark), [paper 2608.22948](https://arxiv.org/abs/2608.22948). 200 neighborhoods, data under `data/`.
- **Input**: the context row with `url`, `decision`, `review_count`, `rating_summary` and `pool_metadata` removed. What remains is `research_context`, `open_problem`, `resource_constraint`, and `papers` (title, abstract and limitation of 4 ICLR papers).
- **Prompt**: the repo's default prompt file is missing. Copy the generation prompt verbatim from paper Appendix A.2.
- **Output**: JSON with exactly six fields: `literature_gap`, `hypothesis`, `minimal_test`, `decisive_metric`, `supporting_result`, `falsifying_result`. Tell the agent the official limit is 1,600 tokens. Record the actual length; do not truncate.
- **Judging**:
  - Judge: Gemini 3.1 Pro Preview, using `run_lit2test_v02_native_gemini_pairwise_judge.py` with the judge prompt as shipped. Do not swap the judge. It is a preview model, so run judging early.
  - Pairs, per model:
    - A vs B, A vs C, B vs C.
    - Each of A, B, C vs each of the 4 reference proposal sets in `results/proposals/` (GPT-5.2, Sonnet 4.6, GLM-5, DeepSeek-V3.2).
    - That is 15 pairs × 200 items × 2 orders = 6,000 judge calls per model.
  - Aggregation: Bradley-Terry over all pairs. Scores are relative only.
- **Platform**: the scripts use `signal.SIGALRM`, so run on Linux or WSL.

### 2.2 SoundnessBench

- **Source**: [HF hosytuyen/SoundnessBench](https://huggingface.co/datasets/hosytuyen/SoundnessBench), [code](https://github.com/hosytuyen/SoundnessBench), [paper 2605.30329](https://arxiv.org/abs/2605.30329). 1,099 items: 641 high, 458 low.
- **Input**: keep only an anonymized item ID, `short_hypothesis` and `experiments`. Remove:
  - Label fields: `rigor_bucket`, `soundness_score`, `rigor_score`, `overall_score`.
  - Fields that let the agent find the paper: `title`, `paper_id`, `pair_id`, `name`.
  - Metadata: `support_ratio`, `year`, `subfield`, `abstract`, `related_work`, `risk_factors`.
- **Prompt**: the official standard prompt (`direct_bucket` mode in `prompt.py`). Never use the aggressive variant.
- **Output**: `{"justification": "...", "rigor_bucket": "low" | "high", "confidence": 1-5}`.
- **Scoring**: deterministic match on `rigor_bucket`. Primary metric Macro-F1; also report accuracy and Cohen's κ. An unparsable answer counts as wrong.

### 2.3 SciΠvot (options-only)

- **Source**: [repo](https://github.com/AutoResearch-Factory/SciPIvot), [paper 2610.21082](https://arxiv.org/abs/2610.21082). 248 cases.
- **Input**: render with `python scripts/make_prompt.py --all --condition options-only --order ab`, then again with `--order ba`. Each case runs in both orders, 496 runs per condition. The agent sees only the two `Goal + Plan` options, never the project records or `questions.json`.
- **Output**: `{"argument": "...", "response": "A" | "B"}`.
- **Scoring**:
  - Run `python scripts/score.py predictions.json --ci`, which averages the two orders per case and then weights cases equally. Chance is 50%.
  - Also report a "pick the longer option" baseline, which reaches 60.5%.
- **Platform**: Linux or WSL. The 91 GB project records are not needed.

### 2.4 PaperGym-Design

- **Source**: [repo](https://github.com/ZJU-REAL/PaperGym), [paper 2608.31119](https://arxiv.org/abs/2608.31119). 1,200 items: cs, econ and physics, 400 each.
- **File**: the file names in the repo are swapped. Design items are in `test/PaperGym/data/innov.parquet`, not `design.parquet`. Check that every prompt ends with the "Experimental Design" guidance block.
- **Input**: only `prompt[0].content`. Never expose `reward_model.ground_truth` or `extra_info`.
- **Output**: free text, with no length cap.
- **Scoring**:
  - Judge: gpt-6-astra. Run `score_responses.py` with `--model`, `--base_url` and `--api_key`, or set `SCORE_MODEL`, `SCORE_BASE_URL` and `SCORE_API_KEY` in `run_score.sh`.
  - Method: per-rubric 0/1, averaged. The scorer is invoked as `run_score.sh innov` because it keys on the folder name.
  - Length: record each answer's length. Length regression is done at analysis time.

## 3. Deliverables

Everything goes to the public HF bucket `dare-benchmark`, under `deepseek-glm/`. The `baseline/` side uses the same layout.

```text
dare-benchmark/deepseek-glm/
├── MANIFEST.md
├── scripts/                                  # driver code, commands, configs (secrets redacted)
├── data/<benchmark>/                         # exact stripped inputs fed to agents + sha256
├── pilot/<benchmark>/<condition>/<item_id>/  # pilot runs, same per-item layout
├── runs/<benchmark>/<condition>/<item_id>/
├── judge/<benchmark>/...
├── results/
│   ├── scores.csv
│   └── summary.md
├── CHECKSUMS.sha256
└── DONE
```

`<benchmark>` is one of `lit2test`, `soundnessbench`, `scipivot`, `papergym-design`. `<item_id>` is the official item ID. For SciΠvot it is `<case_id>.<order>`, where order is `ab` or `ba`.

### 3.1 Per-item directory

| File | Content |
| --- | --- |
| `prompt.md` | The exact input sent to the agent, byte for byte |
| `transcript/` | The agent's native session log, untouched: every message, tool call, tool result, and reasoning content when the API returns it |
| `workspace/` | Snapshot of the agent's working directory after the run. For arm C this includes DARE's `context/` checkpoints |
| `raw_output.md` | The agent's final answer as written |
| `answer.json` | The answer submitted to the scorer |
| `meta.json` | Fields: `start`, `end`, `tokens_in`, `tokens_out`, `tokens_cache`, `cost_usd`, `exit_status`, `error`, `abstained`, `final_attempt`, `server_model_version` |

Do not convert transcripts to a common format. The native logs are kept, and we parse them ourselves.

### 3.2 Retries

Retry only infrastructure failures (API 5xx, timeouts, harness crashes), at most 3 times. Keep every attempt under `attempt-1/`, `attempt-2/`, and so on, failed ones included. `meta.json` marks the final valid attempt.

Wrong answers, malformed output and refusals are never retried. They are scored as they stand.

### 3.3 Judge records

Store each judge call's raw request and response, with the judge model ID and a timestamp:

- `judge/lit2test/<condA>__vs__<condB>/<item_id>.<order>.json`, where reference sets use `ref.<model>` as the condition.
- `judge/papergym-design/<condition>/<item_id>.json`.

### 3.4 `results/scores.csv`

A long table, one row per item per metric:

```text
benchmark, condition, item_id, metric, value, status, tokens_in, tokens_out, cost_usd
```

`status` is one of `ok`, `abstain`, `failed`. Every number in `summary.md` must be recomputable from `scores.csv`.

### 3.5 `MANIFEST.md`

Delivery is incomplete if any item below is missing.

- **Agents and models**: dsh version or commit SHA; ZCode commit SHA and build command; model IDs and API base URLs; the server-reported model version, recorded at the first and the last call.
- **DARE**: commit SHA.
- **Per condition**: full harness config, system prompt, temperature, max tokens.
- **Arm B**: the token budget per benchmark and how it was derived from the pilot.
- **Retrieval-off setup**: the exact settings used to disable web tools and MCP.
- **Environment**: OS, Python version, run start and end dates.
- **Data**: the stripping scripts, and the sha256 of each source data file.

### 3.6 Sync and freeze

- Sync to the bucket at least once a day while running (`hf buckets sync`).
- The bucket is public. Before every upload, redact API keys and secret environment variables from logs, configs and workspace snapshots. A leaked key blocks delivery.
- At delivery, write `CHECKSUMS.sha256` and an empty `DONE` file, then stop writing. Any later fix goes under `revision-2/` and never overwrites a delivered file.

## 4. Execution Order

```text
setup  →  pilot  →  full runs  →  judging  →  results
```

- **Setup**: install dsh and build ZCode CLI, install DARE for arm C, disable retrieval, prepare the stripped inputs, and fill in `MANIFEST.md`.
- **Pilot**: run arm C on 10 items per benchmark on each model. The median per-item tokens set arm B's budget for that model and benchmark. Pilot runs are stored under `pilot/` and are not part of the results.
- **Full runs**: all six conditions on all four benchmarks.
- **Judging**: Lit2Test pairs and PaperGym rubric scoring. SoundnessBench and SciΠvot are scored deterministically.
- **Results**: `scores.csv`, `summary.md`, checksums, `DONE`.
