# Data Models Overview

This backend uses SQLAlchemy ORM with a SQLite database by default.

Entities:
- User
  - id (PK)
  - username (unique, indexed)
  - created_at (datetime)
  - relationships: tanks, player states, leaderboard entries

- Tank
  - id (PK)
  - user_id (FK -> users.id, CASCADE)
  - color (string)
  - speed (float)
  - armor (float)
  - damage (float)
  - index: user_id

- Match
  - id (PK)
  - started_at (datetime)
  - ended_at (nullable datetime)
  - status (string: ongoing|completed|abandoned)
  - relationships: players (PlayerState)

- PlayerState
  - id (PK)
  - match_id (FK -> matches.id, CASCADE)
  - user_id (FK -> users.id, CASCADE)
  - x (float), y (float), angle (float)
  - health (float), score (int)
  - indexes: (match_id, user_id) unique; user_id

- LeaderboardEntry
  - id (PK)
  - user_id (FK -> users.id, CASCADE, unique)
  - score (int)
  - updated_at (datetime)
  - indexes: user_id unique; score

Notes:
- All tables are created on startup in `src/api/main.py` through `Base.metadata.create_all(bind=engine)`.
- Default DB: `./data/app.db`; override with `DATABASE_URL`.
- CRUD schemas are in `src/api/schemas.py`.
- Session dependency `get_session` (in `src/api/db.py`) manages commit/rollback automatically.
