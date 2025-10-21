from fastapi import APIRouter

router = APIRouter(prefix="/docs", tags=["docs"])


@router.get(
    "/index",
    summary="System Docs Index",
    description="Lists key diagnostics and docs endpoints exposed by the backend.",
    operation_id="system_docs_index",
)
def docs_index():
    return {
        "endpoints": [
            {"path": "/", "summary": "Health Check"},
            {"path": "/system/db-info", "summary": "Database Info"},
            {"path": "/system/diag", "summary": "System Diagnostics"},
            {"path": "/system/models", "summary": "Models List"},
            {"path": "/system/time", "summary": "Server Time"},
            {"path": "/system/seed", "summary": "Seed Minimal Demo"},
            {"path": "/docs/websocket-usage", "summary": "WebSocket Usage Notes"},
            {"path": "/docs/websocket", "summary": "WebSocket Help"},
        ]
    }
