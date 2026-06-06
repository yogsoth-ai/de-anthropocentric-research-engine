import json
from pathlib import Path

REQUIRED_LOGS_DIR_MSG = "logs-dir is required (no default); privacy red line"


def read_conversation(sample_id: str, logs_dir):
    """Read the full session jsonl; return de-identified dialogue turns.
    Privacy red line: logs_dir is required with no default; returned content contains no log path."""
    if not logs_dir:
        raise ValueError(REQUIRED_LOGS_DIR_MSG)
    path = Path(logs_dir) / f"{sample_id}.jsonl"
    turns = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        msg = obj.get("message", {})
        role = msg.get("role") or obj.get("type", "")
        content = msg.get("content", "")
        if isinstance(content, list):
            content = " ".join(c.get("text", "") for c in content if isinstance(c, dict))
        if role in ("user", "assistant"):
            turns.append({"speaker": role, "text": content})
    return turns
