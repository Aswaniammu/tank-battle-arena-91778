from datetime import datetime
from typing import Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.db import get_session
from src.api.seed import seed_minimal_demo

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/system/time", tags=["system"], summary="System Time", description="Returns current server time in ISO format.")
def system_time() -> Dict[str, str]:
    """Return current server time for diagnostics."""
    return {"time": datetime.utcnow().isoformat() + "Z"}


# PUBLIC_INTERFACE
@router.post(
    "/system/seed",
    tags=["system"],
    summary="Seed Demo Data",
    description="Populate the database with minimal demo data. Returns counts and identifiers.",
)
def system_seed(db: Session = Depends(get_session)) -> Dict[str, int]:
    """
    Trigger seeding of minimal demo data.
    Even though the seed uses its own session_scope, dependency injection validates DB connectivity.
    """
    users_created, match_id = seed_minimal_demo()
    return {"users": users_created, "match_id": match_id}
