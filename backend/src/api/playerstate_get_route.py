from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import PlayerStateRead

router = APIRouter(prefix="/player-states", tags=["player-states"])

# PUBLIC_INTERFACE
@router.get("/{player_state_id}", response_model=PlayerStateRead, summary="Get PlayerState", description="Fetch a single player state by id.")
def get_player_state(player_state_id: int, db: Session = Depends(get_session)):
    """Return a single player state by id, or 404 if not found."""
    ps = db.execute(select(models.PlayerState).where(models.PlayerState.id == player_state_id)).scalar_one_or_none()
    if not ps:
        raise HTTPException(status_code=404, detail="PlayerState not found")
    return ps
