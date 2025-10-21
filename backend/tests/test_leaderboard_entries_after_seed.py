from sqlalchemy import select

from src.api.db import Base, engine, SessionLocal
from src.api.seed import seed_minimal_demo
from src.api import models


def test_leaderboard_entries_exist_after_seed():
    Base.metadata.create_all(bind=engine)
    seed_minimal_demo()

    with SessionLocal() as s:
        entries = s.execute(select(models.LeaderboardEntry)).scalars().all()
        # We expect at least two entries for users alpha and bravo after seeding
        assert len(entries) >= 2
        user_ids = {e.user_id for e in entries}
        assert len(user_ids) >= 2
