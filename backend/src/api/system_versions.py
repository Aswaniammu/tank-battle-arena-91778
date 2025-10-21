from fastapi import APIRouter
import fastapi
import sqlalchemy

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/versions",
    summary="Dependency versions",
    description="Returns versions of key backend dependencies for diagnostics.",
    operation_id="system_versions",
)
def versions():
    """Return versions of FastAPI and SQLAlchemy for quick diagnostics."""
    return {
        "fastapi": getattr(fastapi, "__version__", "unknown"),
        "sqlalchemy": getattr(sqlalchemy, "__version__", "unknown"),
    }
