---
name: spawn-agent
description: 'Spawn a customized CC subagent with full MCP tool access. Used by SOPs
  that declare execution: subagent.'
type: sop
layer: sop
---

# Spawn Agent

## Purpose

When an SOP declares `execution: subagent` in its frontmatter, this skill governs how main CC creates and invokes that subagent.

## Default Strategy

| Dimension | Default |
|-----------|---------|
| Model | opus |
| Tools | all (subagent inherits main CC's full MCP access) |
| Output | markdown |

## Execution Protocol

When you encounter an SOP with `execution: subagent`:

### Step 1: Read the prompt

Read the file specified in the SOP's `prompt` frontmatter field (relative to the SOP directory).

### Step 2: Format the user message

Take the SOP's input parameters and format as:

```
[FIELD_NAME]:
[value]

[FIELD_NAME]:
[value]
```

Each field on its own line, separated by blank lines. Field names in UPPER_CASE.

### Step 3: Invoke Agent tool

```
Agent({
  description: "[SOP name] — [brief task description]",
  prompt: "[prompt.md content]\n\n---\n\n[formatted user message]",
  model: "[opus, unless SOP overrides]"
})
```

The subagent's prompt combines:
1. The prompt.md content (role definition, framework, output structure)
2. A separator (`---`)
3. The formatted input parameters

### Step 4: Return result

The Agent tool result IS the SOP output. Pass it back to the calling tactic/strategy as-is. No parsing, no transformation.

## Override Handling

If the SOP frontmatter contains override fields:

- `model: sonnet` → use `model: "sonnet"` in Agent call
- `tools: [alphaxiv, ss]` → add tool restriction note to the prompt

## Parallel Execution

When a tactic needs multiple subagents (e.g., debate with Critic + Defender), spawn them as parallel Agent tool calls in a single message. The Agent tool natively supports this.
