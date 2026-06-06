import sys
import json
from optimizer.weights import CHECK_TOKENS


def audit_revision_log(revision_log):
    """W5 保险审计：扫描全部权重修改理由，确认无任何 check/primitive 引用。"""
    violations = []
    for i, entry in enumerate(revision_log):
        reason = entry.get("reason", "").lower()
        if any(t in reason for t in CHECK_TOKENS):
            violations.append({"index": i, "reason": entry.get("reason")})
    return {"clean": not violations, "violations": violations}


if __name__ == "__main__":
    from pathlib import Path
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    log = data.get("revision_log", [])
    print(json.dumps(audit_revision_log(log), ensure_ascii=False))
