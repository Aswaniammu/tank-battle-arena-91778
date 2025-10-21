# Contributing - Backend (FastAPI + SQLAlchemy)

Local dev quick start:
- Run the FastAPI app (e.g., `uvicorn src.api.main:app --reload` from the backend root).
- Tables are created automatically on startup.
- Default SQLite DB path: `./data/app.db`. Override with `DATABASE_URL` if needed.

Seeding:
- POST /system/seed-minimal to seed demo data (idempotent).
- Verify with:
  - GET /
  - GET /system/db-info
  - GET /system/tables
  - GET /leaderboard
  - GET /users

Architecture:
- `src/api/db.py` provides engine/session utilities and `get_session` dependency.
- `src/api/models.py` contains ORM definitions.
- `src/api/schemas.py` contains Pydantic schemas.
- `src/api/main.py` wires routes and initializes the DB.
- `src/api/*_routes.py` contain modular routers for features.

Notes:
- Keep dependencies minimal. Avoid external services for MVP.
- Use `get_session` in routes to ensure transaction and lifecycle management.
