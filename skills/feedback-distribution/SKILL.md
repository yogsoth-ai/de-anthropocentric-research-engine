---
name: feedback-distribution
description: Create anonymized feedback report summarizing group judgment distribution
  for a given round.
execution: subagent
prompt: ./prompt.md
input: judgments[], round_n
dependencies:
  sops:
  - spawn-agent
---

# Feedback Distribution

Create an anonymized feedback report that summarizes the distribution of judgments from the current round. The report shows statistical summaries and representative reasoning without attributing responses to specific perspectives.

## Execution

Spawn a subagent that takes the collected judgments and round number, then produces a structured feedback report showing central tendency, spread, and anonymized reasoning excerpts.

## Why Subagent

- Report generation is a bounded transformation task
- Anonymization logic must be carefully applied
- Output format is standardized across all rounds

## HARD-GATE

Output MUST contain: statistical summary (median, IQR or % distribution), anonymized reasoning themes, and round number. Report MUST NOT contain any perspective attribution.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
