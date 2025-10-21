# Seeding the Database

Two ways to seed minimal demo data:

1) Python (CLI)
   - In a Python shell or script:
     from src.api.seed import seed_minimal_demo
     seed_minimal_demo()

2) API (via FastAPI)
   - POST /system/seed
   - Response: { "status": "ok", "users": <int>, "match_id": <int> }

Notes:
- Seeding is idempotent for users and leaderboard entries; running multiple times is safe.
- Tables are created at app startup; DB file is at ./data/app.db unless DATABASE_URL is set.
