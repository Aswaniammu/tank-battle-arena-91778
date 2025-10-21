# Diagnostics Reference

Available helpful endpoints for debugging:

- GET /                       -> Health check
- GET /system/db-info         -> Database info and basic connectivity
- GET /system/orm-tables      -> ORM tables registered in metadata
- GET /system/db-url          -> Resolved DB driver (masked)
- GET /system/openapi-tags    -> OpenAPI tags configured
- GET /system/catalog         -> Quick catalog of common endpoints
- GET /system/time            -> Server time in UTC
- GET /system/version         -> Backend version
- GET /system/ping            -> Simple ping endpoint
- POST /system/echo           -> Echo back payload for POST checks
- GET /system/websocket-usage -> WebSocket usage notes (MVP: none)
- POST /system/seed           -> Seed minimal demo data
