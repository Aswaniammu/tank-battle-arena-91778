from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import UserRead

router = APIRouter(prefix="/users", tags=["users"])

# PUBLIC_INTERFACE
@router.get("/{user_id}", response_model=UserRead, summary="Get User", description="Fetch a single user by id.")
def get_user(user_id: int, db: Session = Depends(get_session)):
    """Return a single user by id, or 404 if not found."""
    user = db.execute(select(models.User).where(models.User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
