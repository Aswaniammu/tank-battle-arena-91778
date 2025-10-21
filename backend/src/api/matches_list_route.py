from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api import models
from src.api.schemas import MatchRead

router = APIRouter(prefix="/matches", tags=["matches"])

# PUBLIC_INTERFACE
@router.get("", response_model=List[MatchRead], summary="List Matches", description="List all matches.")
def list_matches(db: Session = Depends(get_session)):
    """Return all matches."""
    return list(db.execute(select(models.Match)).scalars().all())
