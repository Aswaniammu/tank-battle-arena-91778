# Backend Database Notes (SQLite + SQLAlchemy)

This backend uses a lightweight SQLite database (via SQLAlchemy) by default:
- Default path: `./data/app.db` (created at runtime).
- Override with `DATABASE_URL` environment variable (see `.env.example`).

## Key Files
- `src/api/db.py` — Engine + Session management, FastAPI `get_session` dependency.
- `src/api/models.py` — ORM models: `User`, `Tank`, `Match`, `PlayerState`, `LeaderboardEntry`.
- `src/api/schemas.py` — Pydantic models for API IO.
- `src/api/seed.py` — Minimal seeding utilities.
- `src/api/main.py` — App setup, table initialization on startup, system endpoints.
- `src/api/system_*.py` — Diagnostics and docs routes.

## Quickstart
- Start backend (tables are auto-created on startup).
- Verify DB connection:
  - `GET /system/db-info`
  - `GET /system/diag`
  - `GET /system/models`
- Seed demo data:
  - `POST /system/seed`
  - or: `python -m src.api.seed_run`

## Notes
- Uses synchronous SQLAlchemy (2.x) with `check_same_thread=False` for SQLite.
- Objects retain values after commit (`expire_on_commit=False`).
- Pydantic v2 `from_attributes=True` enables ORM-to-schema conversion.
