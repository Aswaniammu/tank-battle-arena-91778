from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import LeaderboardEntryRead

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

# PUBLIC_INTERFACE
@router.get("", response_model=List[LeaderboardEntryRead], summary="List Leaderboard", description="List all leaderboard entries.")
def list_leaderboard(db: Session = Depends(get_session)):
    """Return all leaderboard entries ordered by score desc then id."""
    stmt = select(models.LeaderboardEntry).order_by(models.LeaderboardEntry.score.desc(), models.LeaderboardEntry.id.asc())
    return list(db.execute(stmt).scalars().all())
