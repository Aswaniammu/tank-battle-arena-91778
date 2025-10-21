from fastapi import APIRouter
from src.api.db_schema_snapshot import snapshot_schema

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.post(
    "/schema-snapshot",
    summary="Snapshot DB schema",
    description="Generates a JSON snapshot of current DB schema and returns the output path.",
    operation_id="system_schema_snapshot",
)
def schema_snapshot():
    """Trigger a DB schema snapshot and return the path of the generated file."""
    path = snapshot_schema()
    return {"status": "ok", "output": path}
