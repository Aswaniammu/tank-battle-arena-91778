from fastapi import APIRouter
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from src.api.db import get_session

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system/schema-snapshot", summary="Schema Snapshot", description="Returns tables with columns and types.")
def schema_snapshot(db: Session = get_session().__next__()):
    """Return a lightweight snapshot of the database schema (tables, columns, types)."""
    out = {}
    try:
        inspector = inspect(db.bind)
        for table in inspector.get_table_names():
            cols = inspector.get_columns(table)
            out[table] = [
                {
                    "name": c.get("name"),
                    "type": str(c.get("type")),
                    "nullable": c.get("nullable"),
                    "default": str(c.get("default")),
                    "primary_key": c.get("primary_key"),
                }
                for c in cols
            ]
    except Exception:
        out = {}
    return {"schema": out}
