from fastapi import APIRouter, Query

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/echo",
    summary="Echo",
    description="Echoes back the provided message for connectivity testing.",
    operation_id="system_echo",
)
def system_echo(msg: str = Query("ok", description="Message to echo back")):
    """Return the message payload unmodified for quick smoke tests."""
    return {"echo": msg}
