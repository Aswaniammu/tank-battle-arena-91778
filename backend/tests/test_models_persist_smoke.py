from sqlalchemy import select
from src.api.db import SessionLocal, Base, engine
from src.api import models  # noqa: F401


def test_create_user_and_leaderboard_entry_smoke():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        # Create user
        u = models.User(username="persist_tester")
        session.add(u)
        session.flush()
        assert u.id is not None

        # Create leaderboard entry
        le = models.LeaderboardEntry(user_id=u.id, score=7)
        session.add(le)
        session.flush()
        assert le.id is not None

        # Query back
        found = session.execute(
            select(models.User).where(models.User.username == "persist_tester")
        ).scalar_one()
        assert found.id == u.id

        found_le = session.execute(
            select(models.LeaderboardEntry).where(models.LeaderboardEntry.user_id == u.id)
        ).scalar_one()
        assert found_le.score == 7

        session.rollback()  # cleanup for test isolation
    finally:
        session.close()
