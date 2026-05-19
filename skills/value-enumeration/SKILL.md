---
name: value-enumeration
description: Enumerate 3-5 values per parameter including extremes
execution: subagent
prompt: ./prompt.md
input: parameter_list (array)
used-by: zwicky-box-construction, general-morphological-analysis, parameter-variation, combination-mapping
---

# Value Enumeration

Enumerate 3-5 meaningful values per parameter, ensuring coverage of boundary and extreme values.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Value enumeration requires creative thinking about each parameter's range, including non-obvious extremes and boundary values that expand the solution space beyond conventional options.
