from pathlib import Path
from select import load, kept_names

FRAG_DIR = Path(__file__).resolve().parents[3] / "vault" / ".dare-method-frag"

def pending():
    nodes, _ = load()
    done = {p.stem for p in FRAG_DIR.glob("*.md")} if FRAG_DIR.exists() else set()
    return sorted(n for n in kept_names(nodes) if n not in done)

if __name__ == "__main__":
    FRAG_DIR.mkdir(exist_ok=True)
    for n in pending():
        print(n)
