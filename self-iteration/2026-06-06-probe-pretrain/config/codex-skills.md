# config/codex-skills.md

codex mounts only the two loss-judge skills in this repo; it does not install superpowers:

- skills/injection-fidelity/
- skills/ladder-quality-order/

Mounting (on-device): symlink these two directories into codex's skill search path,
or point codex at the corresponding SKILL.md via --task at startup.
When computing loss, the optimizer spawns two codex sessions that load these two skills.
