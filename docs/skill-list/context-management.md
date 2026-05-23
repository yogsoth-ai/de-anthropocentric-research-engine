# context-management

Used for context initialization and checkpoint recording across research phases, helping preserve both process and results in long-running workflows.

[Back to skill navigation](./skill-list.md)

Skill count: 2

| Skill | Description |
|-------|-------------|
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |
