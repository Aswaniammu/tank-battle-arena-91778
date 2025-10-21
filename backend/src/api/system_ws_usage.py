"""System endpoint describing potential WebSocket usage for future real-time gameplay."""
from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/ws-usage",
    summary="WebSocket usage help",
    description=(
        "Provides notes on how a client would connect to real-time game events via WebSockets. "
        "This MVP does not implement an active WebSocket endpoint yet; this route documents "
        "the intended approach for future integration."
    ),
    operation_id="system_websocket_usage",
)
def websocket_usage():
    """Return a brief description of intended WebSocket connection patterns for the project."""
    return {
        "note": "WebSocket endpoints are planned for real-time gameplay updates.",
        "intended_examples": [
            {
                "endpoint": "ws://<host>/ws/match/{match_id}",
                "purpose": "Subscribe to match updates (positions, events, projectiles)",
                "protocol": "JSON messages with event type and payload",
            },
            {
                "endpoint": "ws://<host>/ws/lobby",
                "purpose": "Lobby matchmaking and presence updates",
                "protocol": "JSON messages (join, leave, queue status)",
            },
        ],
        "client_hint": "Use standard WebSocket client libraries; send ping/pong or rely on server heartbeat.",
    }
