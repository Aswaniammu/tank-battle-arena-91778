# Database Overview

This backend uses SQLite via SQLAlchemy (synchronous) for the MVP.

- Default DB path: `./data/app.db` (created at runtime)
- Optional override via `DATABASE_URL` environment variable (e.g., `sqlite:///path/to.db`, `postgresql://...`).
- Tables are created automatically at FastAPI startup.

## Models

- User
  - id (PK), username (unique), created_at
- Tank
  - id (PK), user_id (FK->User), color, speed, armor, damage
- Match
  - id (PK), started_at, ended_at (nullable), status (ongoing|completed|abandoned)
- PlayerState
  - id (PK), match_id (FK->Match), user_id (FK->User), x, y, angle, health, score
  - Unique index on (match_id, user_id)
- LeaderboardEntry
  - id (PK), user_id (FK->User, unique index), score, updated_at

## Utilities

- DB dependency: `get_session` from `src.api.db`
- Seeding: `src.api.seed.seed_minimal_demo()` creates two users (alpha/bravo), a match with two player states, tanks, and leaderboard entries.

## Endpoints

- `GET /system/db-info` — DB info and users_count
- `POST /system/seed` — populate demo data
- `GET /system/time` — server time
- `GET /system/help` — API usage notes

## OpenAPI

Regenerate schema:
```bash
cd backend
python -m src.api.generate_openapi
```
