"""System endpoint that lists registered /system routes for quick inspection."""
from fastapi import APIRouter
from src.api.main import app

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/routes",
    summary="List system routes",
    description="Returns a list of registered routes under the /system namespace.",
    operation_id="system_routes",
)
def list_system_routes():
    """Return a list of system routes (path + methods) registered in the application."""
    routes = []
    for r in app.routes:
        try:
            path = getattr(r, "path", "")
            if path.startswith("/system"):
                methods = sorted(list(getattr(r, "methods", set())))
                name = getattr(r, "name", "")
                routes.append({"path": path, "methods": methods, "name": name})
        except Exception:
            continue
    routes.sort(key=lambda x: x["path"])
    return {"count": len(routes), "routes": routes}
