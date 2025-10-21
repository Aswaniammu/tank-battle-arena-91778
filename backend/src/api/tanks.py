"""Tanks API Router providing basic CRUD operations for Tank entities."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/tanks", tags=["tanks"])


# PUBLIC_INTERFACE
@router.get(
    "",
    summary="List tanks",
    description="Returns a list of tanks.",
    response_model=List[schemas.TankRead],
)
def list_tanks(db: Session = Depends(get_session)):
    """List all tanks."""
    res = db.execute(select(models.Tank).order_by(models.Tank.id))
    return res.scalars().all()


# PUBLIC_INTERFACE
@router.post(
    "",
    summary="Create tank",
    description="Creates a new tank for a given user.",
    response_model=schemas.TankRead,
    status_code=status.HTTP_201_CREATED,
)
def create_tank(payload: schemas.TankCreate, db: Session = Depends(get_session)):
    """Create a tank for a user ID."""
    # Ensure user exists
    user = db.get(models.User, payload.user_id)
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
    db.refresh(tank)
    return tank


# PUBLIC_INTERFACE
@router.get(
    "/{tank_id}",
    summary="Get tank by ID",
    description="Returns a tank by ID.",
    response_model=schemas.TankRead,
)
def get_tank(tank_id: int, db: Session = Depends(get_session)):
    """Get a tank by ID."""
    tank = db.get(models.Tank, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not found")
    return tank


# PUBLIC_INTERFACE
@router.delete(
    "/{tank_id}",
    summary="Delete tank",
    description="Deletes a tank by ID.",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_tank(tank_id: int, db: Session = Depends(get_session)):
    """Delete a tank by ID."""
    tank = db.get(models.Tank, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not found")
    db.delete(tank)
    return None
