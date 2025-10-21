from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get(
    "/system/version",
    summary="Backend Version",
    description="Returns semantic version of the backend API.",
)
def version():
    """Return a simple version string for diagnostics and client checks."""
    return {"version": "0.1.0"}
