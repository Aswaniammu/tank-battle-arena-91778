# Contributing - Backend (FastAPI + SQLite/SQLAlchemy)

Run locally:
1) Create venv and install deps:
   python -m venv .venv && . .venv/bin/activate
   pip install -r backend/requirements.txt

2) Start API:
   uvicorn src.api.main:app --reload --host 0.0.0.0 --port 3001

Database:
- Default SQLite DB at ./data/app.db (auto-created).
- Override with env var: DATABASE_URL

Tables:
- Auto-created on startup.

Seed:
- HTTP: POST http://localhost:3001/system/seed
- Python: from src.api.seed import seed_minimal_demo; seed_minimal_demo()

Quick checks:
- GET /                      -> {"message":"Healthy"}
- GET /system/db-info        -> masked DB URL and user count
- GET /users                 -> []
- POST /users {"username":"alpha"} -> creates user
- POST /tanks {"user_id":1}  -> creates tank for user 1
- POST /matches              -> creates match
- POST /player-states {...}  -> creates a player state

Docs:
- /docs (Swagger UI)
- To regenerate OpenAPI file: python -m src.api.generate_openapi (writes backend/interfaces/openapi.json)
