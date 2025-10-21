from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.api.db import Base, engine, get_session
from src.api import models  # noqa: F401  # ensure models are imported so metadata is aware

# Routers
from src.api.system_docs import router as system_docs_router
from src.api.system_diag import router as system_diag_router
from src.api.system_ws_docs import router as system_ws_docs_router
from src.api.system_docs_index import router as system_docs_index_router
from src.api.system_realtime_docs import router as system_realtime_docs_router
from src.api.system_info import router as system_info_router
from src.api.system_routes import router as system_routes_router
from src.api.system_echo import router as system_echo_router
from src.api.system_ws_usage import router as system_ws_usage_router
from src.api.system_ping import router as system_ping_router
from src.api.system_openapi_meta import router as system_openapi_meta_router
from src.api.system_routes import router as system_routes_router
from src.api.system_seed import router as system_seed_router
from src.api.system_counts import router as system_counts_router
from src.api.system_ws_usage import router as system_ws_usage_router
from src.api.users import router as users_router
from src.api.tanks import router as tanks_router
from src.api.system_openapi import router as system_openapi_router
from src.api.system_dbfile import router as system_dbfile_router
from src.api.system_schema import router as system_schema_router
from src.api.system_summary import router as system_summary_router
from src.api.system_tables import router as system_tables_router
from src.api.system_versions import router as system_versions_router
from src.api.system_discovery import router as system_discovery_router
from src.api.system_seed import router as system_seed_router
from src.api.system_seed import router as system_seed_router
from src.api.users import router as users_router
from src.api.users_detail import router as users_detail_router
from src.api.user_tanks import router as user_tanks_router
from src.api.tanks import router as tanks_router
from src.api.tanks_detail import router as tanks_detail_router
from src.api.matches import router as matches_router
from src.api.match_players import router as match_players_router
from src.api.matches_detail import router as matches_detail_router
from src.api.player_states import router as player_states_router
from src.api.player_states_detail import router as player_states_detail_router
from src.api.leaderboard import router as leaderboard_router
from src.api.leaderboard_user import router as leaderboard_user_router

# Configure OpenAPI metadata and tags
openapi_tags = [
    {"name": "health", "description": "Service health and status"},
    {"name": "system", "description": "System and initialization endpoints"},
    {"name": "docs", "description": "Documentation helper endpoints"},
    {"name": "websocket", "description": "WebSocket documentation"},
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
@app.get(
    "/",
    tags=["health"],
    summary="Health Check",
    description="Simple health check endpoint.",
    operation_id="health_check",
)
def health_check():
    """Health check endpoint returning a simple status message."""
    return {"message": "Healthy"}


# PUBLIC_INTERFACE
@app.get(
    "/system/db-info",
    tags=["system"],
    summary="Database Info",
    description="Returns basic database connectivity info for debugging.",
    operation_id="system_db_info",
)
def db_info(db: Session = Depends(get_session)):
    """Return a minimal payload to confirm DB session works."""
    # Since it's SQLite MVP, return the database URL masked
    from src.api.db import DATABASE_URL

    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    # Basic query to ensure session is usable: count users
    from sqlalchemy import text

    try:
        count_users = db.execute(text("SELECT COUNT(*) FROM users")).scalar()  # may be 0 if unseeded
    except Exception:
        count_users = None
    return {"database_url": masked, "users_count": count_users}


# Include routers
app.include_router(system_docs_router)
app.include_router(system_diag_router)
app.include_router(system_ws_docs_router)
app.include_router(system_docs_index_router)
app.include_router(system_realtime_docs_router)
app.include_router(system_seed_router)
app.include_router(system_counts_router)
app.include_router(system_ws_usage_router)
app.include_router(system_ping_router)
app.include_router(system_openapi_meta_router)
app.include_router(system_routes_router)
app.include_router(users_router)
app.include_router(tanks_router)
app.include_router(system_openapi_router)
app.include_router(system_dbfile_router)
app.include_router(system_schema_router)
app.include_router(system_summary_router)
app.include_router(system_tables_router)
app.include_router(system_versions_router)
app.include_router(system_discovery_router)
app.include_router(system_seed_router)
app.include_router(system_info_router)
app.include_router(system_routes_router)
app.include_router(system_echo_router)
app.include_router(system_ws_usage_router)
app.include_router(system_seed_router)
app.include_router(users_router)
app.include_router(users_detail_router)
app.include_router(user_tanks_router)
app.include_router(tanks_router)
app.include_router(tanks_detail_router)
app.include_router(matches_router)
app.include_router(match_players_router)
app.include_router(matches_detail_router)
app.include_router(player_states_router)
app.include_router(player_states_detail_router)
app.include_router(leaderboard_router)
app.include_router(leaderboard_user_router)
