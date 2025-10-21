from sqlalchemy import select

from src.api.db import SessionLocal, Base, engine
from src.api import models


def test_playerstate_score_update_persists():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    # Setup: user, match, player state
    with SessionLocal() as s:
        user = models.User(username="score_updater")
        s.add(user)
        s.flush()

        match = models.Match(status="ongoing")
        s.add(match)
        s.flush()

        ps = models.PlayerState(match_id=match.id, user_id=user.id, score=5)
        s.add(ps)
        s.commit()
        ps_id = ps.id

    # Update score
    with SessionLocal() as s:
        ps_obj = s.execute(select(models.PlayerState).where(models.PlayerState.id == ps_id)).scalar_one()
        ps_obj.score = 15
        s.add(ps_obj)
        s.commit()

    # Verify persisted
    with SessionLocal() as s:
        got = s.execute(select(models.PlayerState).where(models.PlayerState.id == ps_id)).scalar_one()
        assert got.score == 15
