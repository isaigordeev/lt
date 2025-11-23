import sys
from pathlib import Path

# Add parent directory to path to make lt package importable
sys.path.insert(0, str(Path(__file__).parent.parent))