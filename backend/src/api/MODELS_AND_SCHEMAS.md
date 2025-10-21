# Models and Schemas Overview

This document summarizes the SQLAlchemy ORM models and the Pydantic schemas used by the FastAPI backend.

## ORM Models

- User
  - Fields: id (PK), username (unique), created_at
  - Relationships: tanks (1:N), matches (via PlayerState), leaderboard_entries (1:1)
- Tank
  - Fields: id (PK), user_id (FK users.id), color, speed, armor, damage
  - Indexes: user_id
- Match
  - Fields: id (PK), started_at, ended_at (nullable), status
  - Relationships: players (1:N PlayerState)
- PlayerState
  - Fields: id (PK), match_id (FK matches.id), user_id (FK users.id), x, y, angle, health, score
  - Indexes: (match_id, user_id) unique, user_id
- LeaderboardEntry
  - Fields: id (PK), user_id (unique FK users.id), score, updated_at
  - Indexes: user_id unique, score

## Pydantic Schemas

- UserBase, UserCreate, UserRead
- TankBase, TankCreate, TankRead
- MatchBase, MatchCreate, MatchRead
- PlayerStateBase, PlayerStateCreate, PlayerStateRead
- LeaderboardEntryBase, LeaderboardEntryCreate, LeaderboardEntryRead

Schemas use `Config.from_attributes = True` for ORM mode compatibility.

## DB Session

- Dependency: `get_session()` (yields SQLAlchemy Session with commit/rollback handling)
- Utility: `session_scope()` context manager for script/CLI usage

## Initialization

- Tables are created on FastAPI startup using `Base.metadata.create_all(bind=engine)`.
- Default DB URL: `sqlite:///./data/app.db` (created automatically).
- Optional override via `DATABASE_URL` environment variable.

## Seeding

- HTTP: `POST /system/seed`
- Python: `from src.api.seed import seed_minimal_demo`
- CLI: `python -m src.api.run_seed` (from backend directory)

## Notes

- This MVP uses synchronous SQLAlchemy engine and sessions.
- For future migrations, consider integrating Alembic.
- Add CRUD routers using `Depends(get_session)` and the provided schemas.
