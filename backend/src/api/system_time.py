from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get(
    "/system/time",
    summary="Server Time",
    description="Returns the current server time in ISO8601 format (UTC).",
)
def server_time():
    """Return current server time in UTC for diagnostics."""
    now = datetime.now(timezone.utc)
    return {"utc": now.isoformat()}
