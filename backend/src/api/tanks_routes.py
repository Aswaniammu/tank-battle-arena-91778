from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import TankCreate, TankRead

router = APIRouter(prefix="/tanks", tags=["tanks"])

# PUBLIC_INTERFACE
@router.post("/", response_model=TankRead, summary="Create Tank", description="Create a tank for a given user.")
def create_tank(payload: TankCreate, db: Session = Depends(get_session)):
    """Create a tank if the user exists."""
    user = db.execute(select(models.User).where(models.User.id == payload.user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    tank = models.Tank(
        user_id=payload.user_id,
        color=payload.color,
        speed=payload.speed,
        armor=payload.armor,
        damage=payload.damage,
    )
    db.add(tank)
    db.flush()
    return tank

# PUBLIC_INTERFACE
@router.get("/", response_model=list[TankRead], summary="List Tanks", description="List all tanks.")
def list_tanks(db: Session = Depends(get_session)):
    """Return all tanks."""
    rows = db.execute(select(models.Tank).order_by(models.Tank.id.asc())).scalars().all()
    return rows
