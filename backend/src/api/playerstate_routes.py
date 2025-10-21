from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import PlayerStateCreate, PlayerStateRead

router = APIRouter(prefix="/player-states", tags=["player-states"])

# PUBLIC_INTERFACE
@router.post("/", response_model=PlayerStateRead, summary="Create PlayerState", description="Create a player state for a user in a match.")
def create_player_state(payload: PlayerStateCreate, db: Session = Depends(get_session)):
    """Create a player state if the match and user exist."""
    match = db.execute(select(models.Match).where(models.Match.id == payload.match_id)).scalar_one_or_none()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    user = db.execute(select(models.User).where(models.User.id == payload.user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

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

# PUBLIC_INTERFACE
@router.get("/", response_model=list[PlayerStateRead], summary="List PlayerStates", description="List all player states.")
def list_player_states(db: Session = Depends(get_session)):
    """Return all player states."""
    rows = db.execute(select(models.PlayerState).order_by(models.PlayerState.id.asc())).scalars().all()
    return rows
