# Project Repository

This is the initial README file for the project.

## Backend Database (MVP)

- Uses SQLite via SQLAlchemy.
- Default database path: `./data/app.db` created at runtime.
- Optional: set `DATABASE_URL` to override (e.g., `postgresql://...` or `sqlite:///path/to/file.db`).

### Seeding

A minimal seeding utility exists:
- Import and run:
  ```python
  from src.api.seed import seed_minimal_demo
  seed_minimal_demo()
  ```
- Or call:
  - `GET /system/db-info` to verify connectivity and table initialization
  - `POST /system/seed` to populate demo data
  - `GET /system/ws-usage` to view WebSocket (planned) usage notes

Tables are created automatically on FastAPI startup.

## Backend Database (MVP)

- Uses SQLite via SQLAlchemy.
- Default database path: `./data/app.db` created at runtime.
- Optional: set `DATABASE_URL` to override (e.g., `postgresql://...` or `sqlite:///path/to/file.db`).

Tables are created automatically on FastAPI startup.

### Seeding

A minimal seeding utility exists:
- Import and run:
  ```python
  from src.api.seed import seed_minimal_demo
  seed_minimal_demo()
  ```
- Or call the debug endpoint `/system/db-info` to verify connectivity and table initialization.

### System Endpoints

- GET `/system/time` — returns current server time.
- POST `/system/seed` — populates demo data and returns created counts.
- GET `/system/db-info` — returns basic DB info and user count.
- GET `/system/help` — notes about real-time usage and API overview.

To regenerate OpenAPI spec after code changes:
```bash
cd backend
python -m src.api.generate_openapi
```
