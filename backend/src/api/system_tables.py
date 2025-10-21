from fastapi import APIRouter
from sqlalchemy import inspect
from src.api.db import engine

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/tables",
    summary="List DB tables",
    description="Returns the list of current database table names.",
    operation_id="system_tables",
)
def list_tables():
    """Return a sorted list of current database table names."""
    insp = inspect(engine)
    return {"tables": sorted(insp.get_table_names())}
