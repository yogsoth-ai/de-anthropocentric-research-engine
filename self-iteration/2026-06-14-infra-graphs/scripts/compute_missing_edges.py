"""Machine-compute class ③ (缺失依赖 edge) as the deterministic set difference
`correct_edges − empirical_edges`, per user decisions (2026-06-15):

  1. Add ALL graph edges missing from the empirical graph — including the full
     4-layer decomposition hierarchy (strategy->sop, tactic->sop, campaign->*),
     the spawn-agent / context-* execution fan-ins (kept missing: require precise
     skill-level declaration, not empirical's coarser package-level), AND the
     research-catalog ref-structure edges. No endpoint-existence filtering.
  2. No LLM subagents — the diff is deterministic; the only fuzzy part is empirical
     name normalization, handled by norm() + a rename-map back-mapping.

Correct-graph edge endpoints are post-rename bare names (e.g.
`convergence-saturation-detection`). Empirical endpoints are original bare names
plus title-case infra nodes (`Literature Overview`). To diff, map each correct
endpoint back to its on-disk name (undo the <pkg>- rename) and kebab-normalize,
then subtract. An edge counts as PRESENT only if its exact (from,to) pair (so
normalized) is literally in the empirical edge set; everything else is missing.

Output: missing-updates.json — edge_updates (all confidence=high, since the user
elected to add every missing edge). low-confidence.json is written empty (kept for
schema stability / the Task-6 low-confidence gate)."""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
EMP = HERE.parent.parent / "2026-06-04-empirical-floor" / "data" / "forward_graph.json"
REF_PREFIX = "ref/"
SPAWN = "spawn-agent"
CTX = {"context-init", "context-checkpoint"}


def norm(s):
    """kebab-normalize: 'Literature Overview' -> 'literature-overview'."""
    return re.sub(r"[^a-z0-9]+", "-", s.strip().lower()).strip("-")


def rename_back_map():
    """post-rename bare name -> original on-disk bare name (undo <pkg>- prefix)."""
    back = {}
    for c in json.loads((HERE/"collision-links.json").read_text(encoding="utf-8"))["groups"]:
        back[f'{c["pkg"]}-{c["old"]}'] = c["old"]
    for c in json.loads((HERE/"infra-links.json").read_text(encoding="utf-8"))["collapse"]:
        back[f'{c["pkg"]}-{c["wrapper"]}'] = c["wrapper"]
    return back


def edge_update_text(f, t):
    """skill-creator-style declaration, edge-type aware so ref/spawn/context edges
    read correctly instead of as a generic skill-uses-skill dependency."""
    if t.startswith(REF_PREFIX) or f == "research-catalog":
        return (f"缺失依赖 edge: research-catalog 查阅结构 —— 在 skills/{f}/SKILL.md 正文按 "
                f"skill-creator 规范声明本 skill 经 research-catalog 编目可被查阅到 {t}。")
    if t == SPAWN:
        return (f"缺失依赖 edge: 在 skills/{f}/SKILL.md 正文按 skill-creator 规范声明本 skill "
                f"经 subagent 执行,精确用到 {t}(empirical 仅 package 级 subagent-spawning,需细化到 skill)。")
    if t in CTX:
        return (f"缺失依赖 edge: 在 skills/{f}/SKILL.md 正文按 skill-creator 规范声明本 skill "
                f"用到 {t}(empirical 仅 package 级 context-management,需细化到 skill)。")
    return (f"缺失依赖 edge: 在 skills/{f}/SKILL.md 正文按 skill-creator 规范声明本 skill "
            f"用到 {t}(正确图有此依赖,empirical 图未连通 / frontmatter 缺声明)。")


def main():
    rs = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    emp = json.loads(EMP.read_text(encoding="utf-8"))
    back = rename_back_map()
    emp_edges = {(norm(f), norm(t)) for f, t, _src in emp["edges"]}

    def disk(name):
        return norm(back.get(name, name))

    high, seen = [], set()
    for e in rs["edges"]:
        f, t = e["from"], e["to"]
        if (f, t) in seen:
            continue
        seen.add((f, t))
        if (disk(f), disk(t)) in emp_edges:
            continue                # already connected in empirical — not missing
        high.append({"from": f, "to": t, "update": edge_update_text(f, t),
                     "confidence": "high"})

    (HERE/"missing-updates.json").write_text(
        json.dumps({"note": "class ③ 缺失依赖 edge; ALL correct − empirical 集合差 (用户选全补)",
                    "edge_updates": high}, ensure_ascii=False, indent=2), encoding="utf-8")
    (HERE/"low-confidence.json").write_text(
        json.dumps({"note": "用户选择全补,无低置信缓冲区;保留空壳供 Task6 低置信门",
                    "edge_updates": []}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"missing edges: high={len(high)}, low=0 "
          f"(of {len(seen)} unique correct edges; {len(seen)-len(high)} already in empirical)")


if __name__ == "__main__":
    main()
