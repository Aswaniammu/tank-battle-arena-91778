"""
System ping endpoint for quick diagnostics.
"""
from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get(
    "/system/ping",
    summary="Ping",
    description="Returns a simple pong for liveness diagnostics.",
)
def ping():
    """Return a simple pong string for diagnostics."""
    return {"pong": True}
