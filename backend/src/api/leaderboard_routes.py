from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.api.db import get_session

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

# PUBLIC_INTERFACE
@router.get("/", summary="Get Leaderboard", description="Returns a simple leaderboard list ordered by score desc.")
def get_leaderboard(db: Session = Depends(get_session)):
    """Return a list of leaderboard entries with username and score."""
    try:
        rows = db.execute(
            text(
                """
                SELECT u.username, l.score, l.updated_at
                FROM leaderboard_entries l
                JOIN users u ON u.id = l.user_id
                ORDER BY l.score DESC, u.username ASC
                """
            )
        ).mappings().all()
        return {"items": [dict(r) for r in rows]}
    except Exception:
        # If table does not exist yet or any error occurs, return empty
        return {"items": []}
