from fastapi import APIRouter

router = APIRouter(prefix="/docs", tags=["docs"])


# PUBLIC_INTERFACE
@router.get("/websocket", summary="WebSocket Usage Help", description="Explains how clients would connect to WebSocket endpoints when available.")
def websocket_usage():
    """
    Provide usage instructions for WebSocket clients (placeholder for MVP).
    Parameters: none
    Returns: JSON instructions for hypothetical WebSocket usage.
    """
    return {
        "note": "Real-time gameplay via WebSocket is not implemented in MVP.",
        "example_client": "wss://<host>/ws/game",
        "protocol": "JSON messages with game events and state updates",
        "status": "planned",
    }
