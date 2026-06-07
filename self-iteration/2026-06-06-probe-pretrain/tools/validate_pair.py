import json
import re
import sys
import jsonschema
from pathlib import Path

SCHEMA_DIR = Path(__file__).parent.parent / "schemas"


def extract_blocks(spec_text):
    """Extract the ```json graph and ```json result fenced blocks from a spec file.
    Greedy [\\s\\S] match to the closing fence, so nested objects are tolerated."""
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
