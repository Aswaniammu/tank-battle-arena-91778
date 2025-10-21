from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


# PUBLIC_INTERFACE
@router.get(
    "",
    response_model=List[schemas.LeaderboardEntryRead],
    summary="List Leaderboard",
    description="Returns all leaderboard entries.",
    operation_id="list_leaderboard",
)
def list_leaderboard(db: Session = Depends(get_session)):
    """Return all leaderboard entries."""
    return db.execute(select(models.LeaderboardEntry)).scalars().all()


# PUBLIC_INTERFACE
@router.post(
    "",
    response_model=schemas.LeaderboardEntryRead,
    summary="Upsert Leaderboard Entry",
    description="Create a leaderboard entry for a user if it does not exist, otherwise update score.",
    operation_id="upsert_leaderboard",
)
def upsert_leaderboard(payload: schemas.LeaderboardEntryCreate, db: Session = Depends(get_session)):
    """Create or update a leaderboard entry for a user."""
    user = db.execute(select(models.User).where(models.User.id == payload.user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    entry = db.execute(
        select(models.LeaderboardEntry).where(models.LeaderboardEntry.user_id == payload.user_id)
    ).scalar_one_or_none()

    if entry:
        entry.score = payload.score
    else:
        entry = models.LeaderboardEntry(user_id=payload.user_id, score=payload.score)
        db.add(entry)

    db.flush()
    return entry
