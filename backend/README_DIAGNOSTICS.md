# Backend Diagnostics Endpoints

Useful endpoints for runtime verification and CI logs:

- GET /system/summary
  - Returns status, masked database URL, and list of tables (if accessible).
- GET /system/tables
  - Returns just the list of DB tables.
- GET /system/schema-snapshot
  - Returns tables and per-column details (name, type, nullable, primary key).
- GET /system/db-info
  - Returns masked database URL and users table count (if exists).
- GET /system/openapi-meta
  - Returns OpenAPI title, version, and paths count.
- GET /system/versions
  - Returns Python, FastAPI, and SQLAlchemy versions.
- POST /system/seed-minimal
  - Seeds minimal demo data (idempotent).

Notes:
- DB defaults to SQLite at ./data/app.db unless DATABASE_URL is set.
- Tables are created automatically on application startup.
