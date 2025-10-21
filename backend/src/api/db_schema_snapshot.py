from fastapi import APIRouter
from src.api.db import Base

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system/models", summary="Models Introspection", description="Lists ORM model tables based on SQLAlchemy metadata.")
def models_introspection():
    """Return list of table names known to SQLAlchemy ORM metadata."""
    try:
        tables = sorted(Base.metadata.tables.keys())
    except Exception:
        tables = []
    return {"orm_tables": tables}
