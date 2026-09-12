"""Build a dependency-light HTML view of the v4 registry graph."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "v4" / "registry" / "graph.json"
OUT = ROOT / "v4" / "docs" / "graph.html"


def main() -> None:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    rows = []
    for n in graph["nodes"]:
        rows.append(f"<tr><td>{html.escape(n['type'])}</td><td><code>{html.escape(n['id'])}</code></td><td>{html.escape(n.get('family',''))}</td><td>{html.escape(n.get('scope',''))}</td></tr>")
    counts = graph["counts"]
    body = """<!doctype html><meta charset='utf-8'><title>DARE v4 graph</title>
<style>body{{font:14px system-ui;margin:2rem;color:#222}}table{{border-collapse:collapse;width:100%%}}th,td{{border:1px solid #ddd;padding:.35rem;text-align:left}}th{{background:#eee}}input{{padding:.5rem;width:24rem}}</style>
<h1>DARE v4 graph</h1><p>267 nodes · 317 calls · 157 jumps · 474 edges · 146 contracts</p>
<input id='q' placeholder='Filter node id, family, scope'><table><thead><tr><th>type</th><th>id</th><th>family</th><th>scope</th></tr></thead><tbody id='rows'>%s</tbody></table>
<script>const q=document.querySelector('#q');q.oninput=()=>{{const v=q.value.toLowerCase();for(const r of document.querySelectorAll('#rows tr'))r.hidden=!r.textContent.toLowerCase().includes(v)}}</script>""" % "\n".join(rows)
    OUT.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    main()
