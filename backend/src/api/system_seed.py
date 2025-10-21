"""System endpoint to seed minimal demo data for quick start."""
from fastapi import APIRouter
from src.api.seed import seed_minimal_demo

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.post(
    "/seed",
    summary="Seed minimal demo data",
    description="Creates two users, tanks, a match, player states, and leaderboard entries.",
    operation_id="system_seed_minimal_demo",
)
def system_seed():
    """Trigger minimal demo data seeding. Returns basic info about created resources."""
    users_created, match_id = seed_minimal_demo()
    return {"status": "ok", "users": users_created, "match_id": match_id}
