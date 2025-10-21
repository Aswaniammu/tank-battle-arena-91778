from fastapi import APIRouter

router = APIRouter(prefix="/docs", tags=["docs"])


@router.get(
    "/websocket-usage",
    summary="WebSocket Usage Notes",
    description="Documentation stub for future real-time gameplay WebSocket endpoints.",
    operation_id="docs_websocket_usage_notes",
)
def websocket_usage_notes():
    return {
        "connect": {
            "url": "/ws/game/{match_id}",
            "protocol": "websocket",
            "note": "Planned endpoint; not implemented in MVP.",
        },
        "messages": [
            {"type": "join", "fields": ["match_id", "user_id"]},
            {"type": "state_update", "fields": ["x", "y", "angle", "health", "score"]},
            {"type": "event", "fields": ["event_type", "payload"]},
        ],
    }
