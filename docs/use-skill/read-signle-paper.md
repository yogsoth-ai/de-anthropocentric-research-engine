# Reading a Single Paper

This document explains how to use skills in the DARE repository to read a single paper, and when to choose different reading depths.

## Quick Recommendation

If your goal is simply to read one paper, the three most useful entry points are:

| Skill | Best for | Reading depth |
|-------|----------|---------------|
| `paper-overview` | Quickly scan a paper and decide whether it is worth deeper reading | Abstract-level |
| `paper-search` | Standard paper reading with structured understanding of problem, method, experiments, and conclusions | Intermediate |
| `paper-research` | Deep technical analysis with equations, hyperparameters, and implementation details | Full depth |

For single-paper reading, especially for arXiv papers, you can usually invoke the workflow directly without extra setup for this narrow use case. Full-text reading mainly relies on `alphaxiv`.

## When To Use Each Skill

### `paper-overview`

Use this when:

- You only want to quickly judge whether the paper is relevant
- You want an early look at the research question, task, and general method direction
- You are still screening papers and are not ready to read the full paper

Limitations:

- This is only an abstract-level scan
- You should not draw method-level conclusions from the abstract alone

### `paper-search`

Use this when:

- You want to properly read a paper without necessarily going into equation-by-equation detail
- You want a structured summary
- You want to quickly understand the research problem, method, experiments, strengths, and weaknesses

Quality gate:

- Every analyzed paper must call `get_paper_content`
- You should not conclude from the title and abstract alone

### `paper-research`

Use this when:

- You want to reproduce the paper
- You need equations, symbols, hyperparameters, and training details
- You want a deep technical analysis of the method

Quality gate:

- The paper must be read at `fullText: true` depth
- The output should cover equations, hyperparameters, specific claims, and implementation details

## Recommended Process

If you are not yet sure whether the paper deserves deep reading, use this sequence:

1. Start with `paper-overview` to get the abstract-level picture
2. If it looks relevant, move to `paper-search` for standard reading
3. If you need reproduction, comparison, or a technical note, continue with `paper-research`

If you already know you need a deep reading, you can go directly to `paper-research`.

## How To Invoke It

The simplest way is to name the skill directly in the chat and provide the paper link, title, or PDF URL.

Recommended minimum input:

- A paper link, preferably an `arXiv` link
- Your reading goal
- Your preferred output structure

## Prompt Templates

### 1. Quick Scan

```text
Please use paper-overview to read this paper:
https://arxiv.org/abs/xxxx.xxxxx

Output:
1. Research question
2. Task and data
3. High-level method idea
4. Main results
5. Whether it is worth deeper reading
```

### 2. Standard Reading

```text
Please use paper-search to read this paper:
https://arxiv.org/abs/xxxx.xxxxx

Output:
1. What problem does this paper solve?
2. What is the core method?
3. What is the experimental setup and evaluation protocol?
4. What are the main results and conclusions?
5. What are the limitations?
6. What is relevant to my current research?
```

### 3. Deep Technical Analysis

```text
Please use paper-research to deeply read this paper:
https://arxiv.org/abs/xxxx.xxxxx

Focus on:
1. Equations and symbol definitions
2. Model architecture
3. Training pipeline
4. Hyperparameters and implementation details
5. Experimental design
6. Reproducibility notes
7. Potential weaknesses
```

## Recommended Output Structure

If you do not want to redesign the output format every time, you can request this structure directly:

```text
Please structure the output as follows:
1. Paper metadata
2. Research question
3. Core idea
4. Method
5. Experimental setup
6. Main results
7. Limitations
8. Reproducibility notes
9. Relevance to my topic
```

## A More Reliable Single-Paper Workflow

If you want more stable output quality, use a two-stage process.

First, judge relevance:

```text
Please use paper-overview to read this paper and tell me whether it is worth deeper reading:
https://arxiv.org/abs/xxxx.xxxxx
```

Then continue to standard reading:

```text
Based on the previous judgment, please use paper-search to continue reading the same paper.
Focus on method details, experimental design, and limitations.
```

If you need reproduction-level analysis, continue with:

```text
Please use paper-research to deeply analyze this paper, focusing on equations, hyperparameters, and implementation details.
```

## Scope Notes

- For a single arXiv paper: prefer `paper-search` or `paper-research`
- For a single paper when relevance is still uncertain: start with `paper-overview`
- If the goal is no longer a single paper but a topic-level multi-paper survey: switch to `literature-survey`
- If the goal is no longer paper reading but full research orchestration: switch to `de-anthropocentric-research-engine`

## Notes

- `paper-overview` is for screening, not for method-level conclusions
- `paper-search` is the default entry point for most single-paper reading tasks
- `paper-research` is more expensive, but better for reproduction, technical dissection, and method comparison
- If the paper is not on arXiv, try to provide an accessible PDF or a stable webpage URL
