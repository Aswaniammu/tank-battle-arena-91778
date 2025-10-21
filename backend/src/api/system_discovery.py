from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get("/system", summary="System Endpoints Index", description="Lists available system/diagnostics endpoints.")
def system_index():
    """Return a simple index of available system/diagnostic endpoints."""
    return {
        "endpoints": [
            {"method": "GET", "path": "/", "description": "Health check"},
            {"method": "GET", "path": "/system/health", "description": "Combined system health and DB snapshot"},
            {"method": "GET", "path": "/system/db-info", "description": "DB info and users count"},
            {"method": "GET", "path": "/system/tables", "description": "List database tables"},
            {"method": "GET", "path": "/system/schema-snapshot", "description": "Schema snapshot with columns"},
            {"method": "GET", "path": "/system/openapi-meta", "description": "OpenAPI meta information"},
            {"method": "GET", "path": "/system/versions", "description": "Dependency/runtime versions"},
            {"method": "POST", "path": "/system/seed-minimal", "description": "Seed minimal demo data"},
            {"method": "GET", "path": "/system/summary", "description": "System summary (status, DB, tables)"},
        ]
    }
