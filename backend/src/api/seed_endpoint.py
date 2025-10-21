from fastapi import APIRouter
from src.api.seed import seed_minimal_demo

router = APIRouter(prefix="/system", tags=["system"])

# PUBLIC_INTERFACE
@router.post("/seed", summary="Seed minimal demo data", description="Seeds two users, their tanks, one match and leaderboard entries.")
def seed_minimal():
    """Trigger minimal demo data seeding. Safe to call multiple times (idempotent for key entities)."""
    users_created, match_id = seed_minimal_demo()
    return {"status": "ok", "users": users_created, "match_id": match_id}
