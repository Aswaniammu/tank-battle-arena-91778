from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/info",
    summary="Service Info",
    description="Returns basic service metadata including name, version, and server time.",
    operation_id="system_info",
)
def system_info():
    """Return service name, version, and current UTC time."""
    return {
        "service": "Tank Battle Arena Backend",
        "version": "0.1.0",
        "time_utc": datetime.now(timezone.utc).isoformat(),
    }
