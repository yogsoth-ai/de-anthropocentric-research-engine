# config/codex-skills.md

codex 仅挂载本 repo 的两个 loss 评判 skill，不安装 superpowers：

- skills/injection-fidelity/
- skills/ladder-quality-order/

挂载方式（设备上）：把这两个目录 symlink 进 codex 的 skill 搜索路径，
或在 codex 启动时用 --task 指向对应 SKILL.md。
optimizer 在算 loss 时 call 出两个 codex session 分别 load 这两个 skill。
