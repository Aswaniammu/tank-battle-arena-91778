from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import LeaderboardEntryRead

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

# PUBLIC_INTERFACE
@router.get("/{user_id}", response_model=LeaderboardEntryRead, summary="Get Leaderboard Entry", description="Fetch a leaderboard entry by user id.")
def get_leaderboard_entry(user_id: int, db: Session = Depends(get_session)):
    """Return the leaderboard entry for a user, or 404 if not found."""
    entry = db.execute(
        select(models.LeaderboardEntry).where(models.LeaderboardEntry.user_id == user_id)
    ).scalar_one_or_none()
    if not entry:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return entry
