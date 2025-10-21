from fastapi import APIRouter
from src.api.main import app

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get(
    "/system/schema-catalog",
    summary="OpenAPI Schema Catalog",
    description="Returns the list of tags/groups configured in this API to assist discovery.",
)
def openapi_schema_catalog():
    """Return the OpenAPI tags configured on the FastAPI app."""
    schema = app.openapi()
    tags = schema.get("tags", [])
    return {"tags": tags}
