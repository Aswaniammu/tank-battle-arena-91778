from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import PlayerStateRead

router = APIRouter(prefix="/player-states", tags=["player-states"])

# PUBLIC_INTERFACE
@router.get("", response_model=List[PlayerStateRead], summary="List Player States", description="List all player states.")
def list_player_states(db: Session = Depends(get_session)):
    """Return all player states."""
    return list(db.execute(select(models.PlayerState)).scalars().all())
