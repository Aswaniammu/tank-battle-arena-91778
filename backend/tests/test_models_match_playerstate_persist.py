from sqlalchemy import select
import pytest

from src.api.db import SessionLocal, Base, engine
from src.api import models


def test_match_and_playerstate_persist_and_unique_constraint():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as s:
        # Create user
        user = models.User(username="match_player_tester")
        s.add(user)
        s.flush()

        # Create match
        match = models.Match(status="ongoing")
        s.add(match)
        s.flush()

        # Create player state for user in match
        ps = models.PlayerState(match_id=match.id, user_id=user.id, x=1.0, y=2.0, angle=90.0, health=100.0, score=10)
        s.add(ps)
        s.commit()
        pid = ps.id

    with SessionLocal() as s:
        # Query back
        got = s.execute(select(models.PlayerState).where(models.PlayerState.id == pid)).scalar_one()
        assert got.match_id == match.id
        assert got.user_id == user.id
        assert got.score == 10

        # Try to add a duplicate player state for same (match_id, user_id) which should violate unique index
        dup = models.PlayerState(match_id=match.id, user_id=user.id, x=0, y=0, angle=0, health=100, score=0)
        s.add(dup)
        with pytest.raises(Exception):
            s.commit()
            # rollback to cleanup for other tests
        s.rollback()
