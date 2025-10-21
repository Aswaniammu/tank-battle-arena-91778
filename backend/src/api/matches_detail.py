from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/matches", tags=["matches"])


# PUBLIC_INTERFACE
@router.get(
    "/{match_id}",
    response_model=schemas.MatchRead,
    summary="Get Match",
    description="Fetch a single match by id.",
    operation_id="get_match",
)
def get_match(match_id: int, db: Session = Depends(get_session)):
    """Return a single match by id or 404 if not found."""
    match = db.execute(select(models.Match).where(models.Match.id == match_id)).scalar_one_or_none()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match
