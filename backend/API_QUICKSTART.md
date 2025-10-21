# API Quickstart

Run the server:
- uvicorn src.api.main:app --reload --host 0.0.0.0 --port 3001

Explore docs:
- http://localhost:3001/docs
- http://localhost:3001/openapi.json

Core endpoints (MVP):
- Health: GET /
- System:
  - GET /system/db-info
  - POST /system/seed
  - GET /system/ws-usage
- Matches: list/create at /matches (if router added in future iterations)
- Player States: list/create at /player-states (if router added in future iterations)
- Leaderboard: list/upsert at /leaderboard (if router added in future iterations)

Database:
- SQLite file created at ./data/app.db by default; override with env var DATABASE_URL.

Notes:
- Tables are created automatically on startup.
- Seeding creates basic demo data to test flows quickly.
