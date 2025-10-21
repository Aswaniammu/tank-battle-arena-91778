from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import TankRead

router = APIRouter(prefix="/tanks", tags=["tanks"])

# PUBLIC_INTERFACE
@router.get("", response_model=List[TankRead], summary="List Tanks", description="List all tanks.")
def list_tanks(db: Session = Depends(get_session)):
    """Return all tanks."""
    return list(db.execute(select(models.Tank)).scalars().all())
