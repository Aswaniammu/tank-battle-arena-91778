import pytest
from sqlalchemy import select

from src.api.db import SessionLocal, Base, engine
from src.api import models


def test_leaderboard_persist_and_unique_user():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as s:
        # Create user
        user = models.User(username="leader_user")
        s.add(user)
        s.flush()

        # Create leaderboard entry for the user
        lb = models.LeaderboardEntry(user_id=user.id, score=42)
        s.add(lb)
        s.commit()
        lid = lb.id

    with SessionLocal() as s:
        # Query back
        got = s.execute(select(models.LeaderboardEntry).where(models.LeaderboardEntry.id == lid)).scalar_one()
        assert got.user_id == user.id
        assert got.score == 42

        # Attempt to create another leaderboard entry for the same user should fail due to unique index
        dup = models.LeaderboardEntry(user_id=user.id, score=100)
        s.add(dup)
        with pytest.raises(Exception):
            s.commit()
        s.rollback()
