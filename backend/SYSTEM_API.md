# System API Overview

FastAPI backend provides core system endpoints for diagnostics, initialization, and documentation.

Base URL: /

## Health

GET `/`  
- Summary: Health Check  
- Response: `{ "message": "Healthy" }`

## System Group

All endpoints prefixed with `/system`.

- GET `/system/time`
  - Summary: Current Server Time
  - Response:
    ```
    {
      "iso": "2025-01-01T00:00:00.000000+00:00",
      "epoch": 1735689600
    }
    ```

- POST `/system/seed`
  - Summary: Seed Minimal Demo Data
  - Response:
    ```
    {
      "users_created": 2,
      "match_id": 1
    }
    ```

- GET `/system/db-info`
  - Summary: Database Info
  - Response:
    ```
    {
      "database_url": "sqlite:///./data/app.db",
      "users_count": 0
    }
    ```

- GET `/system/help`
  - Summary: API Help and Usage Notes
  - Response:
    ```
    {
      "title": "Tank Battle Arena - System Help",
      "description": "...",
      "websocket_notes": "...",
      "endpoints": {
        "GET /": "Health check",
        "GET /system/time": "Current server time",
        "POST /system/seed": "Populate minimal demo data",
        "GET /system/db-info": "Show basic DB info and connectivity",
        "GET /docs": "OpenAPI docs",
        "GET /openapi.json": "Raw OpenAPI schema"
      }
    }
    ```

## OpenAPI

- Docs UI: GET `/docs`
- Schema: GET `/openapi.json`

To regenerate the OpenAPI schema file into `backend/interfaces/openapi.json`:
```bash
cd backend
python -m src.api.generate_openapi
```
