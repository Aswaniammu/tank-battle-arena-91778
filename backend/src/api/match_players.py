from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/matches", tags=["matches"])


# PUBLIC_INTERFACE
@router.get(
    "/{match_id}/players",
    response_model=List[schemas.PlayerStateRead],
    summary="List Player States for Match",
    description="Returns all player states for a given match.",
    operation_id="list_match_player_states",
)
def list_match_player_states(match_id: int, db: Session = Depends(get_session)):
    """List player states for the given match id; 404 if match not found."""
    match = db.execute(select(models.Match).where(models.Match.id == match_id)).scalar_one_or_none()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return db.execute(select(models.PlayerState).where(models.PlayerState.match_id == match_id)).scalars().all()
