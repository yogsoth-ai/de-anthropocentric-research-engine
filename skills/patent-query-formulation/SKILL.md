---
name: patent-query-formulation
description: Construct keyword + IPC/CPC + assignee combination search strategies for patent databases
execution: subagent
prompt: ./prompt.md
input: research_question, target_technology, known_assignees
used-by: patent-mining
---

# Patent Query Formulation

Generates multi-faceted patent search strategies combining keywords, classification codes, and assignee names to maximize recall across patent databases.
