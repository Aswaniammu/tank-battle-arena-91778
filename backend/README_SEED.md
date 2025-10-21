# Seeding Demo Data

Endpoint:
- POST /system/seed-minimal
  - Tags: seed
  - Summary: Seed minimal demo data
  - Description: Creates two users (alpha, bravo), a tank for each, one match, two player states, and leaderboard entries.
  - Response: {"status":"ok","users":2,"match_id":<int>}

Notes:
- Safe to call multiple times; it is idempotent.
- Database path defaults to ./data/app.db unless DATABASE_URL is set.
