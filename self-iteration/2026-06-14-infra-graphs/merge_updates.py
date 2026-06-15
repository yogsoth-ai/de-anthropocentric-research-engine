"""Inject the 3 update classes into refactory_source.json (single injection entry).
--rename-only injects class ① (skill rename), computed from infra-links.json
(37 wrappers) + collision-links.json (64 collisions). The subagent-scanned classes
② (missing skill node) / ③ (missing dep edge) are injected from missing-updates.json
(produced by Task 5/6). Always edits in place: only flips `update` from "none"."""
import argparse, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RS = HERE / "refactory_source.json"

def rename_map():
    """(package, bare_new_name) -> update string."""
    out = {}
    links = json.loads((HERE/"infra-links.json").read_text(encoding="utf-8"))
    for c in links["collapse"]:
        new = f'{c["pkg"]}-{c["wrapper"]}'
        out[(c["pkg"], new)] = (
            f'skill rename: 重命名磁盘文件夹 {c["wrapper"]} → {new};'
            f'本 skill 是 import wrapper,同时修正其 source: 指针 '
            f'(指向 {c["infra"]}/{c["skill"]})。')
    col = json.loads((HERE/"collision-links.json").read_text(encoding="utf-8"))["groups"]
    for c in col:
        new = f'{c["pkg"]}-{c["old"]}'
        out[(c["pkg"], new)] = (
            f'skill rename: 重命名磁盘文件夹 {c["old"]} → {new}'
            f'(裸名 {c["old"]} 跨 package 撞车,本 package 版独立成名)。')
    return out

def inject_rename(data):
    rm = rename_map()
    hit = 0
    for n in data["nodes"]:
        key = (n["package"], n["name"])
        if key in rm:
            n["update"] = rm[key]; hit += 1
    return hit

def inject_subagent(data):
    p = HERE / "missing-updates.json"
    if not p.exists():
        return 0
    mu = json.loads(p.read_text(encoding="utf-8"))
    hit = 0
    for item in mu.get("node_updates", []):
        for n in data["nodes"]:
            if n["package"] == item["package"] and n["name"] == item["name"]:
                n["update"] = item["update"]; hit += 1
    for item in mu.get("edge_updates", []):
        for e in data["edges"]:
            if e["from"] == item["from"] and e["to"] == item["to"]:
                e["update"] = item["update"]; hit += 1
    return hit

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rename-only", action="store_true")
    a = ap.parse_args()
    data = json.loads(RS.read_text(encoding="utf-8"))
    r = inject_rename(data)
    s = 0 if a.rename_only else inject_subagent(data)
    RS.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"injected rename={r}, subagent={s}")

if __name__ == "__main__":
    main()
