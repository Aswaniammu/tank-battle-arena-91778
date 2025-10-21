from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import MatchCreate, MatchRead

router = APIRouter(prefix="/matches", tags=["matches"])

# PUBLIC_INTERFACE
@router.post("/", response_model=MatchRead, summary="Create Match", description="Create a new match with default status.")
def create_match(payload: MatchCreate, db: Session = Depends(get_session)):
    """Create a match; status defaults to payload.status or 'ongoing'."""
    match = models.Match(status=payload.status)
    db.add(match)
    db.flush()
    return match

# PUBLIC_INTERFACE
@router.get("/", response_model=list[MatchRead], summary="List Matches", description="List all matches.")
def list_matches(db: Session = Depends(get_session)):
    """Return all matches."""
    rows = db.execute(select(models.Match).order_by(models.Match.id.asc())).scalars().all()
    return rows
