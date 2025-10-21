# Running Backend Locally

## Install dependencies
pip install -r backend/requirements.txt

## Start the server
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 3001

- Tables auto-create on startup.
- SQLite DB file is created at ./data/app.db (unless DATABASE_URL is set).

## Verify endpoints
- GET http://localhost:3001/ -> {"message": "Healthy"}
- GET http://localhost:3001/system/db-info
- GET http://localhost:3001/system/diag
- GET http://localhost:3001/system/models
- GET http://localhost:3001/docs/index
- POST http://localhost:3001/system/seed

## Optional: seed via CLI
python -m src.api.seed_run
