from fastapi import APIRouter
from src.api.seed import seed_minimal_demo

router = APIRouter(tags=["system"])

# PUBLIC_INTERFACE
@router.post("/system/seed-minimal", summary="Seed Minimal Demo", description="Seeds two users, tanks, one match, player states, and leaderboard entries.")
def seed_minimal():
    """Trigger minimal demo seed and return basic info."""
    users_created, match_id = seed_minimal_demo()
    return {"seeded": True, "users_created": users_created, "match_id": match_id}
