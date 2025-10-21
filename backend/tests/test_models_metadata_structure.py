from src.api import models


def test_user_table_and_columns():
    assert models.User.__tablename__ == "users"
    cols = set(models.User.__table__.columns.keys())
    assert {"id", "username", "created_at"}.issubset(cols)


def test_tank_table_and_columns():
    assert models.Tank.__tablename__ == "tanks"
    cols = set(models.Tank.__table__.columns.keys())
    assert {"id", "user_id", "color", "speed", "armor", "damage"}.issubset(cols)


def test_match_table_and_columns():
    assert models.Match.__tablename__ == "matches"
    cols = set(models.Match.__table__.columns.keys())
    assert {"id", "started_at", "ended_at", "status"}.issubset(cols)


def test_playerstate_table_and_columns():
    assert models.PlayerState.__tablename__ == "player_states"
    cols = set(models.PlayerState.__table__.columns.keys())
    assert {"id", "match_id", "user_id", "x", "y", "angle", "health", "score"}.issubset(cols)


def test_leaderboard_table_and_columns():
    assert models.LeaderboardEntry.__tablename__ == "leaderboard_entries"
    cols = set(models.LeaderboardEntry.__table__.columns.keys())
    assert {"id", "user_id", "score", "updated_at"}.issubset(cols)
