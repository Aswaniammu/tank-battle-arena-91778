# Backend Testing

Run tests locally with pytest:
1) Create and activate virtualenv
   python -m venv .venv && . .venv/bin/activate
2) Install dependencies
   pip install -r backend/requirements.txt
3) Run tests
   pytest -q

Notes:
- Tests use FastAPI TestClient and the default SQLite DB at ./data/app.db
- Tables are auto-created on app startup
- Set DATABASE_URL to override the default DB if needed
