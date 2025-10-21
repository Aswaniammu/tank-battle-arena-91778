import os
from pathlib import Path

def ensure_data_dir(path: str = "./data/app.db") -> None:
    """Create the parent directory for the SQLite DB if missing."""
    parent = Path(path).parent
    parent.mkdir(parents=True, exist_ok=True)
