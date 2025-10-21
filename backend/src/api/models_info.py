from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get("/models", summary="List ORM Models", description="Returns a list of available ORM model names for diagnostics.")
def list_models():
    """
    Return the names of ORM models included in the backend.
    Parameters: none
    Returns: JSON with a list of names.
    """
    return {
        "models": [
            "User",
            "Tank",
            "Match",
            "PlayerState",
            "LeaderboardEntry",
        ]
    }
