from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/player-states", tags=["player-states"])


# PUBLIC_INTERFACE
@router.get(
    "",
    response_model=List[schemas.PlayerStateRead],
    summary="List Player States",
    description="Returns all player states across all matches.",
    operation_id="list_player_states",
)
def list_player_states(db: Session = Depends(get_session)):
    """Return all player states."""
    return db.execute(select(models.PlayerState)).scalars().all()


# PUBLIC_INTERFACE
@router.post(
    "",
    response_model=schemas.PlayerStateRead,
    summary="Create Player State",
    description="Creates a player state for a given match and user.",
    operation_id="create_player_state",
)
def create_player_state(payload: schemas.PlayerStateCreate, db: Session = Depends(get_session)):
    """Create a new player state for a user in a match."""
    match = db.execute(select(models.Match).where(models.Match.id == payload.match_id)).scalar_one_or_none()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    user = db.execute(select(models.User).where(models.User.id == payload.user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Ensure uniqueness (match_id, user_id)
    existing = db.execute(
        select(models.PlayerState).where(
            models.PlayerState.match_id == payload.match_id, models.PlayerState.user_id == payload.user_id
        )
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Player state already exists for this user in the match")

    ps = models.PlayerState(
        match_id=payload.match_id,
        user_id=payload.user_id,
        x=payload.x,
        y=payload.y,
        angle=payload.angle,
        health=payload.health,
        score=payload.score,
    )
    db.add(ps)
    db.flush()
    return ps
