from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.api.db import get_session, DATABASE_URL

router = APIRouter(tags=["health"])

# PUBLIC_INTERFACE
@router.get("/system/health", summary="System Health", description="Returns service health and quick DB connectivity info.")
def system_health(db: Session = Depends(get_session)):
    """Return service health and a quick DB connectivity snapshot."""
    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    try:
        users_count = db.execute(text("SELECT COUNT(*) FROM users")).scalar()
    except Exception:
        users_count = None
    return {
        "status": "ok",
        "database_url": masked,
        "users_count": users_count,
    }
