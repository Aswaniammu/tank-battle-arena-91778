from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import UserRead

router = APIRouter(prefix="/users", tags=["users"])

# PUBLIC_INTERFACE
@router.get("", response_model=List[UserRead], summary="List Users", description="List all users.")
def list_users(db: Session = Depends(get_session)):
    """Return all users."""
    return list(db.execute(select(models.User)).scalars().all())
