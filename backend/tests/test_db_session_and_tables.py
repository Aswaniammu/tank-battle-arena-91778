from sqlalchemy import inspect
from src.api.db import SessionLocal, engine
from src.api import models  # noqa: F401  # ensure models metadata is loaded


def test_session_can_connect_and_tables_exist():
    # Create a session and verify we can connect
    session = SessionLocal()
    try:
        insp = inspect(engine)
        tables = set(insp.get_table_names())
        expected = {
            "users",
            "tanks",
            "matches",
            "player_states",
            "leaderboard_entries",
        }
        assert expected.issubset(tables)
    finally:
        session.close()
