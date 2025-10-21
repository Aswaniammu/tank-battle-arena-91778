from datetime import datetime
from typing import List

from fastapi import APIRouter
from sqlalchemy import inspect

from src.api.db import engine, DATABASE_URL

router = APIRouter(prefix="/system", tags=["system"])


@router.get(
    "/diag",
    summary="System Diagnostics",
    description="Returns masked DB URL and existing tables.",
    operation_id="system_diagnostics",
)
def system_diag():
    inspector = inspect(engine)
    tables: List[str] = sorted(inspector.get_table_names())

    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    return {
        "db": {"database_url": masked},
        "tables": tables,
        "time": datetime.utcnow().isoformat() + "Z",
    }


@router.get(
    "/models",
    summary="List ORM Models",
    description="Lists table names known by SQLAlchemy metadata for quick diagnostics.",
    operation_id="system_list_models",
)
def list_models() -> List[str]:
    inspector = inspect(engine)
    return sorted(inspector.get_table_names())


@router.get(
    "/time",
    summary="Current Server Time",
    description="Returns the current UTC server time for diagnostics.",
    operation_id="system_time",
)
def system_time():
    return {"utc": datetime.utcnow().isoformat() + "Z"}
