---
name: patent-categorization
description: Classify patents by tech subdomain, application scenario, and value chain position
execution: subagent
prompt: ./prompt.md
input: patent_list
used-by: patent-mining
---

# Patent Categorization

Classifies a list of patents into technology sub-domains, application scenarios, and value chain positions using their titles, abstracts, and IPC codes.
