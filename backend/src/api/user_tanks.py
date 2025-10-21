from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/users", tags=["users"])


# PUBLIC_INTERFACE
@router.get(
    "/{user_id}/tanks",
    response_model=List[schemas.TankRead],
    summary="List Tanks For User",
    description="Returns all tanks belonging to a specific user.",
    operation_id="list_user_tanks",
)
def list_user_tanks(user_id: int, db: Session = Depends(get_session)):
    """List tanks for a given user id; 404 if user not found."""
    user = db.execute(select(models.User).where(models.User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return db.execute(select(models.Tank).where(models.Tank.user_id == user_id)).scalars().all()
