from src.api.db import Base, engine
from src.api import models  # noqa: F401


def test_models_metadata_tables_present():
    # Ensure DDL is created
    Base.metadata.create_all(bind=engine)
    tables = set(Base.metadata.tables.keys())
    assert {"users", "tanks", "matches", "player_states", "leaderboard_entries"}.issubset(tables)
