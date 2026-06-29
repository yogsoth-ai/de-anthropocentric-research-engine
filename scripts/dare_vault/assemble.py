import json
from pathlib import Path
from select import load, kept_names, kept_edges, UTIL_RE, INFRA_PKGS
ROOT = Path(__file__).resolve().parents[3]
FRAG = ROOT / "vault" / ".dare-method-frag"
CONCEPTS = ROOT / "vault" / "concepts"
EDGES = ROOT / "vault" / "_edges.jsonl"
DATE = "2026-06-29"

def _util_deps(name, edges, kept):
    # name 调用的、但被排除的 util 目标
    return sorted({e["to"] for e in edges
                   if e["from"] == name and e["to"] not in kept})

def orchestration(name, nodes, edges, kept):
    down = [e for e in edges if e["from"] == name and e["to"] in kept]
    up   = [e for e in edges if e["to"] == name and e["from"] in kept]
    L = ["## 编排关系", ""]
    L.append("**向下调用：**")
    L += [f"- [[concepts/dare-{e['to']}]] — {e.get('description','').strip()}"
          for e in down] or ["- （无）"]
    L.append("")
    L.append("**被上层编排：**")
    L += [f"- [[concepts/dare-{e['from']}]]" for e in up] or ["- （无）"]
    L.append("")
    utils = _util_deps(name, edges, kept)
    L.append("**依赖的 utils（不建页）：** " + (", ".join(utils) if utils else "无"))
    return "\n".join(L)

def page(name, nodes, frag, edges, kept):
    n = nodes[name]
    layer, pkg = n.get("layer", "?"), n.get("package", "?")
    fm = ("---\n"
          f"type: concept\n"
          f'title: "DARE 方法论：{name}"\n'
          f"created: {DATE}\n"
          f"tags: [dare-method, {layer}, {pkg}]\n"
          "---\n")
    body = (f"\n## 层级 / 包\n{layer} · {pkg}\n\n"
            f"## 方法论讲解\n{frag.strip()}\n\n"
            f"{orchestration(name, nodes, edges, kept)}\n\n"
            f"## 来源\nskills/{name}/SKILL.md\n")
    return fm + body

def main():
    nodes, edges = load()
    kept = kept_names(nodes)
    ke = kept_edges(edges, kept)
    CONCEPTS.mkdir(parents=True, exist_ok=True)
    missing = [n for n in sorted(kept) if not (FRAG / f"{n}.md").exists()]
    assert not missing, f"缺片段 {len(missing)}: {missing[:5]}"
    for name in sorted(kept):
        frag = (FRAG / f"{name}.md").read_text(encoding="utf-8")
        (CONCEPTS / f"dare-{name}.md").write_text(
            page(name, nodes, frag, edges, kept), encoding="utf-8")
    with EDGES.open("a", encoding="utf-8") as f:
        for e in ke:
            f.write(json.dumps({
                "source": f"concepts/dare-{e['from']}.md",
                "target": f"concepts/dare-{e['to']}.md",
                "edge_type": "component_of", "weight": 1, "created": DATE},
                ensure_ascii=False) + "\n")
    print(f"pages={len(kept)} edges={len(ke)}")
    assert len(kept) == 847 and len(ke) == 1851

if __name__ == "__main__":
    main()
