"""System endpoint to list discoverable diagnostic and setup routes."""
from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/discovery",
    summary="System endpoint discovery",
    description="Returns a curated list of useful system endpoints for diagnostics and setup.",
    operation_id="system_endpoint_discovery",
)
def discovery():
    """Return a curated list of useful system endpoints for diagnostics and setup."""
    return {
        "health": "/",
        "db_info": "/system/db-info",
        "db_file": "/system/db-file",
        "schema_snapshot": "/system/schema-snapshot",
        "tables": "/system/tables",
        "versions": "/system/versions",
        "summary": "/system/summary",
        "openapi_meta": "/system/openapi-meta",
        "ws_usage": "/system/ws-usage",
        "seed": "/system/seed",
    }
