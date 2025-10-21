from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.api.db import Base, engine, get_session
from src.api import models  # noqa: F401  # ensure models are imported so metadata is aware

# OpenAPI metadata and tags
openapi_tags = [
    {"name": "health", "description": "Service health and status"},
    {"name": "system", "description": "System and initialization endpoints"},
    {"name": "seed", "description": "Utilities to populate minimal demo data for quick testing"},
]

app = FastAPI(
    title="Tank Battle Arena Backend",
    description="Backend API for Tank Battle Arena MVP with SQLite + SQLAlchemy.",
    version="0.1.0",
    openapi_tags=openapi_tags,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """
    Create database tables on application startup.
    """
    Base.metadata.create_all(bind=engine)


# PUBLIC_INTERFACE
@app.get("/", tags=["health"], summary="Health Check", description="Simple health check endpoint.")
def health_check():
    """Health check endpoint returning a simple status message."""
    return {"message": "Healthy"}


# PUBLIC_INTERFACE
@app.get(
    "/system/db-info",
    tags=["system"],
    summary="Database Info",
    description="Returns basic database connectivity info for debugging.",
)
def db_info(db: Session = Depends(get_session)):
    """Return a minimal payload to confirm DB session works."""
    from src.api.db import DATABASE_URL
    from sqlalchemy import text

    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    try:
        count_users = db.execute(text("SELECT COUNT(*) FROM users")).scalar()
    except Exception:
        count_users = None
    return {"database_url": masked, "users_count": count_users}


# Include seed router
from src.api.seed_routes import router as seed_router  # noqa: E402
from src.api.system_summary import router as system_summary_router  # noqa: E402
from src.api.system_tables import router as system_tables_router  # noqa: E402
from src.api.system_openapi import router as system_openapi_router  # noqa: E402
from src.api.system_versions import router as system_versions_router  # noqa: E402
from src.api.system_schema import router as system_schema_router  # noqa: E402
from src.api.system_health import router as system_health_router  # noqa: E402
from src.api.system_discovery import router as system_discovery_router  # noqa: E402
from src.api.db_schema_snapshot import router as db_schema_snapshot_router  # noqa: E402
from src.api.system_ws_help import router as system_ws_help_router  # noqa: E402
from src.api.leaderboard_routes import router as leaderboard_router  # noqa: E402
from src.api.users_routes import router as users_router  # noqa: E402
from src.api.tanks_routes import router as tanks_router  # noqa: E402
from src.api.matches_routes import router as matches_router  # noqa: E402
from src.api.playerstate_routes import router as playerstate_router  # noqa: E402
from src.api.leaderboard_write_routes import router as leaderboard_write_router  # noqa: E402
from src.api.users_get_route import router as users_get_router  # noqa: E402
from src.api.tanks_get_route import router as tanks_get_router  # noqa: E402
from src.api.matches_get_route import router as matches_get_router  # noqa: E402
from src.api.playerstate_get_route import router as playerstate_get_router  # noqa: E402
from src.api.leaderboard_get_route import router as leaderboard_get_router  # noqa: E402
from src.api.users_list_route import router as users_list_router  # noqa: E402
from src.api.tanks_list_route import router as tanks_list_router  # noqa: E402
from src.api.matches_list_route import router as matches_list_router  # noqa: E402
from src.api.playerstate_list_route import router as playerstate_list_router  # noqa: E402
from src.api.leaderboard_list_route import router as leaderboard_list_router  # noqa: E402

app.include_router(seed_router)
app.include_router(system_summary_router)
app.include_router(system_tables_router)
app.include_router(system_openapi_router)
app.include_router(system_versions_router)
app.include_router(system_schema_router)
app.include_router(system_health_router)
app.include_router(system_discovery_router)
app.include_router(db_schema_snapshot_router)
app.include_router(system_ws_help_router)
app.include_router(leaderboard_router)
app.include_router(users_router)
app.include_router(tanks_router)
app.include_router(matches_router)
app.include_router(playerstate_router)
app.include_router(leaderboard_write_router)
app.include_router(users_get_router)
app.include_router(tanks_get_router)
app.include_router(matches_get_router)
app.include_router(playerstate_get_router)
app.include_router(leaderboard_get_router)
app.include_router(users_list_router)
app.include_router(tanks_list_router)
app.include_router(matches_list_router)
app.include_router(playerstate_list_router)
app.include_router(leaderboard_list_router)
