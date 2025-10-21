from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

# PUBLIC_INTERFACE
@router.post("/", response_model=UserRead, summary="Create User", description="Create a new user with a unique username.")
def create_user(payload: UserCreate, db: Session = Depends(get_session)):
    """Create a user if the username is not taken."""
    existing = db.execute(select(models.User).where(models.User.username == payload.username)).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = models.User(username=payload.username)
    db.add(user)
    db.flush()
    return user

# PUBLIC_INTERFACE
@router.get("/", response_model=list[UserRead], summary="List Users", description="List all users.")
def list_users(db: Session = Depends(get_session)):
    """Return all users."""
    rows = db.execute(select(models.User).order_by(models.User.id.asc())).scalars().all()
    return rows
