from fastapi import APIRouter
from src.api.main import app

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system/openapi-meta", summary="OpenAPI Meta", description="Returns title and version from the OpenAPI schema.")
def openapi_meta():
    """Return minimal OpenAPI metadata for quick checks."""
    schema = app.openapi()
    info = schema.get("info", {})
    return {
        "title": info.get("title"),
        "version": info.get("version"),
        "paths_count": len(schema.get("paths", {})),
    }
