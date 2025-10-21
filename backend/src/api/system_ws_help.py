from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get(
    "/system/ws-help",
    summary="WebSocket Usage Help",
    description=(
        "Documentation placeholder for future real-time gameplay WebSocket interfaces. "
        "Notes: Clients will connect to ws(s)://<host>/ws/game for real-time updates once implemented. "
        "Authentication and room/match joining semantics will be documented here in the future."
    ),
    operation_id="system_websocket_usage_help",
)
def websocket_usage_help():
    """Provide a placeholder help document for upcoming WebSocket endpoints."""
    return {
        "message": "WebSocket endpoints are not yet implemented in the MVP.",
        "planned_endpoints": [
            {"path": "/ws/game", "description": "Real-time game updates and player actions stream (planned)"},
        ],
        "notes": "Refer to REST endpoints for current functionality. Realtime support will be added in a future iteration.",
    }
