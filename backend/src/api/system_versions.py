from fastapi import APIRouter
import sys

import fastapi
import sqlalchemy

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system/versions", summary="Dependency Versions", description="Reports key dependency and runtime versions.")
def versions():
    """Return versions of Python, FastAPI, and SQLAlchemy for diagnostics."""
    return {
        "python": sys.version.split()[0],
        "fastapi": fastapi.__version__,
        "sqlalchemy": sqlalchemy.__version__,
    }
