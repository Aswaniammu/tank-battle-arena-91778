# Environment Configuration Notes

Database URL:
- Optional: `DATABASE_URL`
  - If set, the application uses this URL for SQLAlchemy engine.
  - Example: `sqlite:///absolute/path/to/file.db` or `postgresql://user:pass@host:port/dbname`
- Default (when not set): `./data/app.db` (SQLite file on local disk)
  - The directory `./data` is created automatically if missing.

Behavior:
- Tables are created automatically on application startup.
- FastAPI dependency `get_session` manages DB sessions with commit/rollback.

No other environment variables are required for the MVP backend.
