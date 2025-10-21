from typing import Dict, List

from sqlalchemy import inspect

from src.api.db import DATABASE_URL, engine, Base


# PUBLIC_INTERFACE
def masked_database_info() -> Dict[str, str]:
    """Returns a masked database URL suitable for logs/diagnostics."""
    masked = "sqlite:///./data/app.db" if DATABASE_URL.startswith("sqlite") else DATABASE_URL
    return {"database_url": masked}


# PUBLIC_INTERFACE
def list_existing_tables() -> List[str]:
    """Inspect and return existing table names in the connected database."""
    insp = inspect(engine)
    try:
        return sorted(insp.get_table_names())
    finally:
        insp.bind.dispose()  # clean up connections


# PUBLIC_INTERFACE
def ensure_tables_created() -> List[str]:
    """Create all tables from metadata and return the resulting table list."""
    Base.metadata.create_all(bind=engine)
    return list_existing_tables()
