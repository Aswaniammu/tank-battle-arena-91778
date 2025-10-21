from sqlalchemy import select
from src.api.db import SessionLocal, Base, engine
from src.api import models  # noqa: F401


def test_create_match_and_playerstates_smoke():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        # Create users
        u1 = models.User(username="playerstate_user_1")
        u2 = models.User(username="playerstate_user_2")
        session.add_all([u1, u2])
        session.flush()

        # Create match
        match = models.Match(status="ongoing")
        session.add(match)
        session.flush()

        # Add player states for both users
        ps1 = models.PlayerState(match_id=match.id, user_id=u1.id, x=1.0, y=2.0, angle=45.0, health=90.0, score=3)
        ps2 = models.PlayerState(match_id=match.id, user_id=u2.id, x=3.0, y=4.0, angle=90.0, health=80.0, score=6)
        session.add_all([ps1, ps2])
        session.flush()

        # Query back
        players = session.execute(
            select(models.PlayerState).where(models.PlayerState.match_id == match.id)
        ).scalars().all()
        assert len(players) == 2
        user_ids = {p.user_id for p in players}
        assert u1.id in user_ids and u2.id in user_ids

        session.rollback()  # cleanup
    finally:
        session.close()
