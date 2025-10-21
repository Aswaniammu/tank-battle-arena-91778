from fastapi import APIRouter

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.get(
    "/system/models-list",
    summary="List Model Names",
    description="Returns the list of registered SQLAlchemy model names.",
)
def models_list():
    """Return a simple list of SQLAlchemy model class names registered in the app."""
    from src.api import models as m
    return {
        "models": [
            "User",
            "Tank",
            "Match",
            "PlayerState",
            "LeaderboardEntry",
        ]
    }
