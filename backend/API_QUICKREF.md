# Backend API Quick Reference

Health:
- GET `/` — Health Check

System/DB:
- GET `/system/db-info` — DB connectivity + masked URL
- GET `/system/diag` — Masked DB URL + tables + server time
- GET `/system/models` — ORM table names
- GET `/system/time` — Current server UTC time
- POST `/system/seed` — Minimal demo data seeding

Docs/Discoverability:
- GET `/docs/index` — Index of key endpoints
- GET `/docs/websocket` — WebSocket help (docs-only)
- GET `/docs/websocket-usage` — WebSocket usage notes (docs-only)

OpenAPI/Swagger:
- GET `/docs`
- GET `/openapi.json`

Database:
- SQLite via SQLAlchemy (default path: `./data/app.db`)
- Override with `DATABASE_URL` env var
