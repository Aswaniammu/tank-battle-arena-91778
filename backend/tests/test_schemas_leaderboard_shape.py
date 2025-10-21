from datetime import datetime
from src.api.schemas import LeaderboardEntryBase, LeaderboardEntryCreate, LeaderboardEntryRead


def test_leaderboard_base_defaults():
    base = LeaderboardEntryBase()
    assert base.score == 0


def test_leaderboard_create_requires_user_id():
    create = LeaderboardEntryCreate(user_id=42, score=100)
    assert create.user_id == 42
    assert create.score == 100


def test_leaderboard_read_fields():
    now = datetime.utcnow()
    read = LeaderboardEntryRead(id=5, user_id=1, score=10, updated_at=now)
    assert read.id == 5
    assert read.user_id == 1
    assert read.score == 10
    assert isinstance(read.updated_at, datetime)
