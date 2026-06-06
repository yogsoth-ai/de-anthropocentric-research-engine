import sys
from pathlib import Path

# 让测试能 import generator.* / optimizer.* / tools.*（以本子目录为根）
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
