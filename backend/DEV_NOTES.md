# Developer Notes

## Override Database URL

Default DB is `sqlite:///./data/app.db`. To override for local testing:
- Temporarily export `DATABASE_URL` in your shell before starting the server:
  ```bash
  export DATABASE_URL="sqlite:///./data/dev.db"
  uvicorn src.api.main:app --reload --port 3001
  ```
- Or set it for a single command:
  ```bash
  DATABASE_URL="sqlite:///./data/tmp.db" python -m src.api.run_seed
  ```

## Common Tasks

- Create tables and start server:
  ```bash
  uvicorn src.api.main:app --reload --port 3001
  ```
- Seed demo data:
  ```bash
  python -m src.api.run_seed
  ```
  Or via HTTP:
  ```bash
  curl -X POST http://localhost:3001/system/seed
  ```

## Notes

- Tables are auto-created on startup.
- The seed operation is idempotent and safe to re-run.
- Use the `/system/db-info` endpoint to verify the DB connection and users count.

