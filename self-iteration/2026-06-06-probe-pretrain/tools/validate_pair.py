import json
import re
import sys
import jsonschema
from pathlib import Path

SCHEMA_DIR = Path(__file__).parent.parent / "schemas"


def extract_blocks(spec_text):
    """从 spec 文件抽出 ```json graph 与 ```json result 两个 fenced 块。
    用 [\\s\\S] 贪婪匹配到 fence 收尾，能容纳嵌套对象。"""
    graph = re.search(r"```json graph\s*([\s\S]*?)\s*```", spec_text)
    result = re.search(r"```json result\s*([\s\S]*?)\s*```", spec_text)
    if not graph or not result:
        raise ValueError("spec missing graph or result block")
    return json.loads(graph.group(1)), json.loads(result.group(1))


def validate_pair(spec_path):
    text = Path(spec_path).read_text(encoding="utf-8")
    g, r = extract_blocks(text)
    jsonschema.validate(g, json.loads((SCHEMA_DIR / "graph.schema.json").read_text(encoding="utf-8")))
    jsonschema.validate(r, json.loads((SCHEMA_DIR / "result.schema.json").read_text(encoding="utf-8")))
    return g, r


if __name__ == "__main__":
    validate_pair(sys.argv[1])
    print("pair ok")
