# Backend API Notes

This FastAPI backend provides:
- SQLite database via SQLAlchemy at ./data/app.db by default (override with env DATABASE_URL).
- ORM models: User, Tank, Match, PlayerState, LeaderboardEntry.
- Pydantic schemas mapping for API IO.
- System endpoints for diagnostics and quick seeding.

## Database
- Default URL: sqlite:///./data/app.db (directory created on-demand)
- Override via env var: DATABASE_URL (e.g., postgresql://... or sqlite:///path)
- Tables created automatically on startup.

## System Endpoints
- GET `/` — Health check
- GET `/system/time` — Current server time (iso, epoch)
- POST `/system/seed` — Seed minimal demo data (two users alpha, bravo; tanks; one match with player states; leaderboard entries)
- GET `/system/db-info` — Masked database URL and users_count
- GET `/docs/websocket` — Placeholder for WebSocket usage notes (MVP)

## Seeding
Programmatic:
```python
from src.api.seed import seed_minimal_demo
seed_minimal_demo()
```
HTTP:
```bash
curl -X POST http://localhost:3001/system/seed
```

## OpenAPI
Generate interfaces/openapi.json:
```bash
cd backend
python -m src.api.generate_openapi
```
