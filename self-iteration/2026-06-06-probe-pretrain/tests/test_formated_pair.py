from tools.validate_pair import extract_blocks, validate_pair
from pathlib import Path


def test_extract_and_validate(tmp_path):
    spec = tmp_path / "spec.md"
    spec.write_text('''# spec
```json graph
{"nodes": [{"id":"n1","layer":"campaign","skill_name":"x","function":"y"}], "edges": []}
```
```json result
{"document": "a research design document body"}
```
''', encoding="utf-8")
    g, r = validate_pair(str(spec))
    assert g["nodes"][0]["layer"] == "campaign"
    assert r["document"].startswith("a research")
