"""System endpoint exposing OpenAPI metadata for quick inspection."""
from fastapi import APIRouter
from src.api.main import app

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/openapi-meta",
    summary="OpenAPI metadata",
    description="Returns a summary of OpenAPI title, version, and tags.",
    operation_id="system_openapi_meta",
)
def openapi_meta():
    """Return OpenAPI title, version, and tags to aid quick inspection."""
    schema = app.openapi()
    tags = [t.get("name") for t in schema.get("tags", [])]
    return {
        "title": schema.get("info", {}).get("title"),
        "version": schema.get("info", {}).get("version"),
        "tags": tags,
        "paths_count": len(schema.get("paths", {})),
    }
