"""Seeding utilities for the MVP database.

Provides helper functions to populate a small set of demo data for local testing.
"""
from datetime import datetime
from typing import Tuple

from sqlalchemy import select

from src.api.db import session_scope
from src.api import models

"""
Seeding utilities for the Tank Battle Arena backend.

Use seed_minimal_demo() to populate a small dataset useful for local development and demos.
"""


def _get_or_create_user(username: str) -> models.User:
    with session_scope() as s:
        existing = s.execute(select(models.User).where(models.User.username == username)).scalar_one_or_none()
        if existing:
            return existing
        user = models.User(username=username, created_at=datetime.utcnow())
        s.add(user)
        s.flush()
        return user


def _get_or_create_leaderboard(user_id: int, score: int = 0) -> models.LeaderboardEntry:
    with session_scope() as s:
        existing = s.execute(
            select(models.LeaderboardEntry).where(models.LeaderboardEntry.user_id == user_id)
        ).scalar_one_or_none()
        if existing:
            return existing
        entry = models.LeaderboardEntry(user_id=user_id, score=score, updated_at=datetime.utcnow())
        s.add(entry)
        s.flush()
        return entry


# PUBLIC_INTERFACE
def seed_minimal_demo() -> Tuple[int, int]:
    """
    Seed minimal demo data: two users, a tank each, a match with two player states, and leaderboard entries.

    Returns:
        Tuple[int, int]: (users_created, match_id)
    """
    # Users
    u1 = _get_or_create_user("alpha")
    u2 = _get_or_create_user("bravo")

    # Tanks
    with session_scope() as s:
        t1 = s.execute(
            select(models.Tank).where(models.Tank.user_id == u1.id)
        ).scalar_one_or_none()
        if not t1:
            t1 = models.Tank(user_id=u1.id, color="blue", speed=1.2, armor=1.0, damage=1.1)
            s.add(t1)

        t2 = s.execute(
            select(models.Tank).where(models.Tank.user_id == u2.id)
        ).scalar_one_or_none()
        if not t2:
            t2 = models.Tank(user_id=u2.id, color="red", speed=1.0, armor=1.2, damage=1.0)
            s.add(t2)

    # Match + Player states
    with session_scope() as s:
        match = models.Match(status="ongoing")
        s.add(match)
        s.flush()

        ps1 = models.PlayerState(match_id=match.id, user_id=u1.id, x=5, y=5, angle=45, health=100, score=0)
        ps2 = models.PlayerState(match_id=match.id, user_id=u2.id, x=10, y=10, angle=135, health=100, score=0)
        s.add_all([ps1, ps2])

        match_id = match.id

    # Leaderboard
    _get_or_create_leaderboard(u1.id, score=0)
    _get_or_create_leaderboard(u2.id, score=0)

    return (2, match_id)
