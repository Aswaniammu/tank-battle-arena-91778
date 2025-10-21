# Developer Notes: OpenAPI Generation

The backend exposes multiple routers (users, tanks, matches, player-states, leaderboard, system docs/diag/seed).

To regenerate OpenAPI JSON for interfacing containers or docs:
1. Ensure the app can import and start (tables are created on startup).
2. Run:
   ```bash
   python -m src.api.generate_openapi
   ```
3. The OpenAPI document will be written to:
   - `backend/interfaces/openapi.json`

Tips:
- Use the `/docs` UI to interactively verify endpoints.
- Keep operationId, tags, and router prefixes consistent when adding new endpoints.
