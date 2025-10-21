# API Quick Reference

Health
- GET / — Health check

System
- GET /system/db-info — DB connectivity info
- POST /system/seed — Seed minimal demo data
- GET /system/info — Service metadata
- GET /system/routes — List registered routes

Users
- GET /users — List users
- POST /users — Create user {username}
- GET /users/{user_id} — Get user
- GET /users/{user_id}/tanks — List tanks for user

Tanks
- GET /tanks — List tanks
- POST /tanks — Create tank {user_id, color, speed, armor, damage}
- GET /tanks/{tank_id} — Get tank

Matches
- GET /matches — List matches
- POST /matches — Create match
- GET /matches/{match_id} — Get match
- GET /matches/{match_id}/players — List player states for match

Player States
- GET /player-states — List player states
- POST /player-states — Create player state
- GET /player-states/{player_state_id} — Get player state

Leaderboard
- GET /leaderboard — List leaderboard
- POST /leaderboard — Create/Update leaderboard entry
- GET /leaderboard/user/{user_id} — Get leaderboard entry by user

Notes
- Tables are auto-created on startup.
- SQLite file at ./data/app.db by default; override via DATABASE_URL env var.
