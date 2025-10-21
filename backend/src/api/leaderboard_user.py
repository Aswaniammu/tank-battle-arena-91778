from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


# PUBLIC_INTERFACE
@router.get(
    "/user/{user_id}",
    response_model=schemas.LeaderboardEntryRead,
    summary="Get Leaderboard Entry by User",
    description="Fetch leaderboard entry for a user by user_id.",
    operation_id="get_leaderboard_by_user",
)
def get_leaderboard_by_user(user_id: int, db: Session = Depends(get_session)):
    """Return a leaderboard entry for the given user id or 404 if not found."""
    entry = db.execute(
        select(models.LeaderboardEntry).where(models.LeaderboardEntry.user_id == user_id)
    ).scalar_one_or_none()
    if not entry:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return entry
