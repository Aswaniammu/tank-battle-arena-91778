# Backend Routes Overview

Core:
- GET `/` — Health Check

System:
- GET `/system/db-info` — Basic DB connectivity info
- GET `/system/diag` — Diagnostics (masked DB URL, tables, time)
- GET `/system/models` — List ORM models (tables)
- GET `/system/time` — Current server UTC time
- POST `/system/seed` — Seed minimal demo data

Docs:
- GET `/docs/index` — Index of key endpoints
- GET `/docs/websocket` — WebSocket help (docs-only)
- GET `/docs/websocket-usage` — WebSocket usage notes (docs-only)

OpenAPI:
- `/docs` (Swagger UI)
- `/openapi.json`
