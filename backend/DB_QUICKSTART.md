# Tank Battle Arena Backend - DB Quickstart

This backend uses SQLite with SQLAlchemy for the MVP.

- Default DB location: `./data/app.db` (created at runtime)
- Optional: set `DATABASE_URL` to override (e.g. `sqlite:///absolute/path.db`)

## Tables
- users
- tanks
- matches
- player_states
- leaderboard_entries

## Auto-creation
Tables are created on app startup.

## Seed data
Two options:
1) HTTP: POST `/system/seed` to populate a minimal demo (two users, tanks, a match, player states, leaderboard).
2) Python:
   ```python
   from src.api.seed import seed_minimal_demo
   seed_minimal_demo()
   ```

## Diagnostics
- GET `/system/db-info` returns basic DB info and counts.
- GET `/` health check.

## Development Notes
- Synchronous SQLAlchemy is used for simplicity.
- Session dependency: `from src.api.db import get_session`
- Pydantic schemas available in `src/api/schemas.py`
