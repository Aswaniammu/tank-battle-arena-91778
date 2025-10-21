from fastapi import APIRouter
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from src.api.db import get_session

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system/tables", summary="List DB Tables", description="Returns the list of current database tables.")
def list_tables(db: Session = get_session().__next__()):
    """Return the list of database tables for diagnostics."""
    try:
        inspector = inspect(db.bind)
        tables = sorted(inspector.get_table_names())
    except Exception:
        tables = []
    return {"tables": tables}
