from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.api.db import get_session, engine, DATABASE_URL
from src.api.seed import seed_minimal_demo

router = APIRouter(prefix="/system", tags=["system"])


@router.get(
    "/db-info",
    summary="Database Info",
    description="Returns basic database connectivity info for debugging.",
    operation_id="system_db_info",
)
def db_info(db: Session = Depends(get_session)):
    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    try:
        # basic connectivity check
        db.execute(text("SELECT 1"))
        ok = True
    except Exception:
        ok = False

    return {"database_url": masked, "ok": ok}


@router.post(
    "/seed",
    summary="Seed Minimal Demo Data",
    description="Seeds two users, tanks, a match, player states, and leaderboard entries. Returns match id.",
    operation_id="system_seed_minimal",
)
def system_seed(db: Session = Depends(get_session)):
    users_created, match_id = seed_minimal_demo()
    return {"ok": True, "users_created": users_created, "match_id": match_id}
