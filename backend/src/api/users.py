"""Users API Router providing basic CRUD operations for User entities."""
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models, schemas

router = APIRouter(prefix="/users", tags=["users"])


# PUBLIC_INTERFACE
@router.get(
    "",
    summary="List users",
    description="Returns a list of users.",
    response_model=List[schemas.UserRead],
)
def list_users(db: Session = Depends(get_session)):
    """List all users."""
    result = db.execute(select(models.User).order_by(models.User.id))
    return result.scalars().all()


# PUBLIC_INTERFACE
@router.post(
    "",
    summary="Create user",
    description="Creates a new user with a unique username.",
    response_model=schemas.UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_session)):
    """Create a new user."""
    user = models.User(username=payload.username)
    db.add(user)
    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")
    db.refresh(user)
    return user


# PUBLIC_INTERFACE
@router.get(
    "/{user_id}",
    summary="Get user by ID",
    description="Returns a user by ID.",
    response_model=schemas.UserRead,
)
def get_user(user_id: int, db: Session = Depends(get_session)):
    """Get a user by ID."""
    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# PUBLIC_INTERFACE
@router.delete(
    "/{user_id}",
    summary="Delete user",
    description="Deletes a user by ID.",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(user_id: int, db: Session = Depends(get_session)):
    """Delete a user by ID."""
    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    # commit happens in dependency
    return None
