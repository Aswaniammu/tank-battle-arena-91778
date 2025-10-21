# Backend Quickstart

Run the API locally:
```bash
cd backend
uvicorn src.api.main:app --reload --port 3001
```

Health:
```bash
curl http://localhost:3001/
```

Create tables (done automatically on startup) and seed demo data:
```bash
curl -X POST http://localhost:3001/system/seed
```

Check DB info:
```bash
curl http://localhost:3001/system/db-info
```

Time endpoint:
```bash
curl http://localhost:3001/system/time
```

OpenAPI docs:
- UI: http://localhost:3001/docs
- Schema: http://localhost:3001/openapi.json

Regenerate OpenAPI file:
```bash
cd backend
python -m src.api.generate_openapi
```

Notes:
- Default DB: SQLite at ./data/app.db
- Override using env var DATABASE_URL
