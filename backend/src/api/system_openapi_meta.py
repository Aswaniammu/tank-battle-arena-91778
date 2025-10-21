"""System endpoint that returns brief OpenAPI metadata (title, version, routes count)."""
from fastapi import APIRouter
from src.api.main import app

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/openapi-meta",
    summary="OpenAPI metadata summary",
    description="Returns title, version, and total number of documented paths.",
    operation_id="system_openapi_meta",
)
def openapi_meta():
    """Return brief OpenAPI meta information for quick tooling checks."""
    spec = app.openapi()
    title = spec.get("info", {}).get("title", "")
    version = spec.get("info", {}).get("version", "")
    paths = spec.get("paths", {}) or {}
    return {"title": title, "version": version, "paths_count": len(paths)}
