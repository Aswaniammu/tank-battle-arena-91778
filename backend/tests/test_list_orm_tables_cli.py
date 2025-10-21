import subprocess
import sys
from pathlib import Path

from src.api.db import Base, engine
from src.api import models  # noqa: F401


def test_list_orm_tables_cli_outputs_tables(tmp_path):
    # Ensure tables exist prior to invoking the CLI
    Base.metadata.create_all(bind=engine)

    # Run the CLI script as a module
    backend_dir = Path(__file__).resolve().parents[2]
    cmd = [sys.executable, "-m", "src.api.list_orm_tables"]
    proc = subprocess.run(cmd, cwd=backend_dir, capture_output=True, text=True, check=True)

    output = proc.stdout.strip().splitlines()
    # Expect the core tables to be present
    expected_tables = {
        "users",
        "tanks",
        "matches",
        "player_states",
        "leaderboard_entries",
    }
    assert expected_tables.issubset(set(output))
