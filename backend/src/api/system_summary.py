from fastapi import APIRouter
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from src.api.db import get_session, DATABASE_URL

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system/summary", summary="System Summary", description="Returns basic runtime information.")
def system_summary(db: Session = get_session().__next__()):
    """Return a minimal system summary for diagnostics."""
    try:
        inspector = inspect(db.bind)
        tables = sorted(inspector.get_table_names())
    except Exception:
        tables = None
    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    return {
        "status": "ok",
        "database_url": masked,
        "tables": tables,
    }
