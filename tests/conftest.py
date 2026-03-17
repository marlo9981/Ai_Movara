import sys
from pathlib import Path

# Allow importing tools as modules (AI Agent / on path)
sys.path.insert(0, str(Path(__file__).parent.parent))
# Allow importing src.tools.ai_client (ai-agent-team/ on path)
# From tests/conftest.py: tests/ → "AI Agent "/ → ai-agent-team/
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
