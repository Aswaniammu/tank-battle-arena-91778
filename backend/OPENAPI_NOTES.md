# OpenAPI Generation

This backend includes a helper to export the current OpenAPI schema to `backend/interfaces/openapi.json`.

Usage:
- Ensure dependencies are installed: `pip install -r backend/requirements.txt`
- Run from the backend root:
  python -m src.api.generate_openapi

This will:
- Import the FastAPI app from `src.api.main`
- Generate OpenAPI JSON
- Save it to `backend/interfaces/openapi.json`

Notes:
- Routers and endpoints defined in `src/api/main.py` and `src/api/system_*.py` are included.
- Keep the backend running cleanly so the OpenAPI export reflects current reality.
