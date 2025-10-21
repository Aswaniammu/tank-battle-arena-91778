# Contributing Guide (Backend)

This project uses FastAPI with SQLAlchemy (SQLite by default).

## Getting Started

- Python version: 3.11+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run the server:
  ```bash
  uvicorn src.api.main:app --reload --port 3001
  ```
  Open http://localhost:3001/docs for API docs.

## Database

- Default DB: `./data/app.db` (auto-created).
- Override with `DATABASE_URL` env var (e.g., `sqlite:///path/to.db`, `postgresql://...`).

Tables are created on app startup.

## Seeding

- HTTP:
  - POST: `/system/seed`
- Python:
  ```python
  from src.api.seed import seed_minimal_demo
  seed_minimal_demo()
  ```
- CLI:
  ```bash
  python -m src.api.run_seed
  ```

## Diagnostics

Useful endpoints:
- GET `/` (health)
- GET `/system/db-info`
- GET `/system/orm-tables`
- GET `/system/db-url`
- GET `/system/openapi-tags`
- GET `/system/catalog`
- GET `/system/time`
- GET `/system/version`
- GET `/system/ping`
- POST `/system/echo`
- GET `/system/websocket-usage`

## Tests

- Run backend tests:
  ```bash
  pytest -q
  ```
- Minimal tests exist to validate diagnostics endpoints.

## OpenAPI

Regenerate OpenAPI file:
```bash
python -m src.api.generate_openapi
```
Outputs to `interfaces/openapi.json`.

## Coding Style

- Use PEP8 conventions (flake8 configured).
- Add docstrings to public routes and functions.
- Avoid hardcoding configuration; use environment variables.
