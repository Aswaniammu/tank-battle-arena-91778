from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import TankRead

router = APIRouter(prefix="/tanks", tags=["tanks"])

# PUBLIC_INTERFACE
@router.get("/{tank_id}", response_model=TankRead, summary="Get Tank", description="Fetch a single tank by id.")
def get_tank(tank_id: int, db: Session = Depends(get_session)):
    """Return a single tank by id, or 404 if not found."""
    tank = db.execute(select(models.Tank).where(models.Tank.id == tank_id)).scalar_one_or_none()
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not found")
    return tank
