from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import LeaderboardEntryCreate, LeaderboardEntryRead

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

# PUBLIC_INTERFACE
@router.post("/", response_model=LeaderboardEntryRead, summary="Upsert Leaderboard Entry", description="Create or update a leaderboard entry for a user.")
def upsert_leaderboard(payload: LeaderboardEntryCreate, db: Session = Depends(get_session)):
    """Create or update leaderboard entry for a user."""
    user = db.execute(select(models.User).where(models.User.id == payload.user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    entry = db.execute(
        select(models.LeaderboardEntry).where(models.LeaderboardEntry.user_id == payload.user_id)
    ).scalar_one_or_none()
    if entry:
        entry.score = payload.score
        return entry
    new_entry = models.LeaderboardEntry(user_id=payload.user_id, score=payload.score)
    db.add(new_entry)
    db.flush()
    return new_entry
