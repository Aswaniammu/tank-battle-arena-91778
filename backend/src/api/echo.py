"""
System echo endpoint for quick POST diagnostics.
"""
from typing import Any, Dict
from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.post(
    "/system/echo",
    summary="Echo",
    description="Echoes the received JSON payload back to the caller.",
)
def echo(payload: Dict[str, Any]):
    """Return the same JSON payload that was sent."""
    return {"echo": payload}
