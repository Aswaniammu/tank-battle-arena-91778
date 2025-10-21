"""System endpoint providing a lightweight ping for diagnostics."""
from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/ping",
    summary="System ping",
    description="Returns a simple pong with server timestamp for diagnostics.",
    operation_id="system_ping",
)
def ping():
    """Return a minimal pong payload with server time."""
    return {"pong": True, "server_time": datetime.now(timezone.utc).isoformat()}
