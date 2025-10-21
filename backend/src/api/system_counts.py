"""System endpoint that returns counts of core tables for a quick sanity check."""
from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/counts",
    summary="Counts of core tables",
    description="Returns row counts for users, tanks, matches, player states, and leaderboard entries.",
    operation_id="system_counts",
)
def counts(db: Session = Depends(get_session)):
    """Return row counts for key tables to quickly verify DB state."""
    def count(query):
        return db.execute(select(func.count()).select_from(query.subquery())).scalar_one()

    return {
        "users": db.execute(select(func.count(models.User.id))).scalar_one(),
        "tanks": db.execute(select(func.count(models.Tank.id))).scalar_one(),
        "matches": db.execute(select(func.count(models.Match.id))).scalar_one(),
        "player_states": db.execute(select(func.count(models.PlayerState.id))).scalar_one(),
        "leaderboard_entries": db.execute(select(func.count(models.LeaderboardEntry.id))).scalar_one(),
    }
