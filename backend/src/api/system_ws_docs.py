from fastapi import APIRouter

router = APIRouter(prefix="/docs", tags=["websocket"])


@router.get(
    "/websocket",
    summary="WebSocket Usage Help",
    description="Project-level usage note for future real-time WebSocket endpoints.",
    operation_id="docs_websocket_help",
)
def websocket_help():
    return {
        "message": "WebSocket endpoints planned for real-time gameplay in future iterations.",
        "note": "This MVP exposes docs only; no WS endpoints yet.",
    }
