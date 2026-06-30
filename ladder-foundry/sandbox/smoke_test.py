"""2B persona-injection smoke test helpers. The real sim-cc spawn is a manual
Bash-tool procedure (see SMOKE_RESULT.md); these helpers build the injection
message and check endpoint divergence. NOT the AS-1 quality gate."""
import json
from pathlib import Path


def build_injection(config_path, stimulus_path):
    cfg = json.loads(Path(config_path).read_text(encoding="utf-8"))
    stimulus = Path(stimulus_path).read_text(encoding="utf-8")
    cfg_text = json.dumps(cfg, indent=2, ensure_ascii=False)
    return (
        "You are role-playing a research-supervisor USER persona defined by the "
        "PolicyCard below. Stay fully in character for the whole conversation.\n\n"
        f"=== PolicyCard ===\n{cfg_text}\n=== end PolicyCard ===\n\n"
        "React to the following fixed stimulus AS this persona would. When you "
        "have given your full in-character reaction, end your message with the "
        "single line: DONE\n\n"
        f"=== Stimulus ===\n{stimulus}\n=== end Stimulus ==="
    )


def diverged(turns0, turns5):
    def assistant_text(turns):
        return " ".join(t["text"] for t in turns if t["role"] == "assistant").lower()
    a, b = assistant_text(turns0), assistant_text(turns5)
    if not a or not b:
        return False
    return a != b


if __name__ == "__main__":   # ponytail: prints the id0 injection for a dry run
    import sys
    print(build_injection(sys.argv[1], sys.argv[2]))
