from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text

from src.api.main import app
from src.api.db import DATABASE_URL


def test_tables_exist_sqlite():
    # Only run this check for sqlite driver
    if not DATABASE_URL.startswith("sqlite"):
        return

    client = TestClient(app)
    # Trigger startup (tables creation)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200

    # Now inspect sqlite_master to ensure our key tables exist
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    with engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT name FROM sqlite_master WHERE type='table' AND name IN "
                "('users','tanks','matches','player_states','leaderboard_entries')"
            )
        ).fetchall()
        table_names = {row[0] for row in res}
        assert {"users", "tanks", "matches", "player_states", "leaderboard_entries"}.issubset(table_names)
