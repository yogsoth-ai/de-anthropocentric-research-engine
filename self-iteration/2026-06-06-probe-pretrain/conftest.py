import sys
from pathlib import Path

# Let tests import generator.* / optimizer.* / tools.* (with this subdir as root)
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
