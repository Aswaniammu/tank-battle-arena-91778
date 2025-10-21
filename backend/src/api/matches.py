from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/matches", tags=["matches"])


# PUBLIC_INTERFACE
@router.get(
    "",
    response_model=List[schemas.MatchRead],
    summary="List Matches",
    description="Returns all matches.",
    operation_id="list_matches",
)
def list_matches(db: Session = Depends(get_session)):
    """Return all matches."""
    return db.execute(select(models.Match)).scalars().all()


# PUBLIC_INTERFACE
@router.post(
    "",
    response_model=schemas.MatchRead,
    summary="Create Match",
    description="Creates a new match with status ongoing.",
    operation_id="create_match",
)
def create_match(db: Session = Depends(get_session)):
    """Create a new match."""
    match = models.Match(status="ongoing")
    db.add(match)
    db.flush()
    return match
