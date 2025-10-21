import json
import subprocess
import sys
from pathlib import Path

from src.api.db import Base, engine


def test_run_seed_cli_outputs_ok(tmp_path):
    # Ensure tables exist before running CLI seed
    Base.metadata.create_all(bind=engine)

    backend_dir = Path(__file__).resolve().parents[2]
    cmd = [sys.executable, "-m", "src.api.run_seed"]
    proc = subprocess.run(cmd, cwd=backend_dir, capture_output=True, text=True, check=True)
    stdout = proc.stdout.strip()

    # The CLI prints a dict; attempt to parse as JSON if possible, else eval-literal fallback
    try:
        data = json.loads(stdout)
    except Exception:
        # Convert single quotes to double for JSON-like parsing fallback
        data = json.loads(stdout.replace("'", '"'))

    assert isinstance(data, dict)
    assert data.get("status") == "ok"
    assert "users_created" in data
    assert "match_id" in data
