from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/summary",
    summary="System summary",
    description="Provides a quick summary including service name, version, and current UTC time.",
    operation_id="system_summary",
)
def system_summary():
    """Return a minimal service summary useful for quick smoke checks."""
    return {
        "service": "Tank Battle Arena Backend",
        "version": "0.1.0",
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "status": "ok",
    }
