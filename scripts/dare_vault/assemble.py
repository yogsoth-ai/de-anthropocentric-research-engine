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
    # Defect 2 fix: neutralize stray wikilink tokens in fragment prose only
    safe_frag = frag.strip().replace("[[", "［[").replace("]]", "]］")
    body = (f"\n## 层级 / 包\n{layer} · {pkg}\n\n"
            f"## 方法论讲解\n{safe_frag}\n\n"
            f"{orchestration(name, nodes, edges, kept)}\n\n"
            f"## 来源\nskills/{name}/SKILL.md\n")
    return fm + body

def main():
    nodes, edges = load()
    kept = kept_names(nodes)
    ke = kept_edges(edges, kept)
    # 数量门：写盘前先 assert，对不上即停（副作用之前）
    assert len(kept) == 847, f"kept={len(kept)}"
    assert len(nodes) - len(kept) == 83, f"excluded={len(nodes) - len(kept)}"
    assert len(ke) == 1851, f"edges={len(ke)}"
    CONCEPTS.mkdir(parents=True, exist_ok=True)
    missing = [n for n in sorted(kept) if not (FRAG / f"{n}.md").exists()]
    assert not missing, f"缺片段 {len(missing)}: {missing[:5]}"
    for name in sorted(kept):
        frag = (FRAG / f"{name}.md").read_text(encoding="utf-8")
        # Defect 1 fix: pass newline="" to disable Windows \n→\r\n translation
        (CONCEPTS / f"dare-{name}.md").write_text(
            page(name, nodes, frag, edges, kept), encoding="utf-8", newline="")
    # Defect 3 fix: idempotent edge append — skip lines already present
    existing = set()
    if EDGES.exists():
        existing = set(EDGES.read_text(encoding="utf-8").splitlines())
    new_lines = []
    for e in ke:
        line = json.dumps({
            "source": f"concepts/dare-{e['from']}.md",
            "target": f"concepts/dare-{e['to']}.md",
            "edge_type": "component_of", "weight": 1, "created": DATE},
            ensure_ascii=False)
        if line not in existing:
            new_lines.append(line)
    if new_lines:
        with EDGES.open("a", encoding="utf-8", newline="") as f:
            f.write("\n".join(new_lines) + "\n")
    print(f"pages={len(kept)} edges={len(ke)} appended={len(new_lines)}")

if __name__ == "__main__":
    main()
