"""Utility to create all tables and print verification details for local debugging."""
from sqlalchemy import inspect
from src.api.db import Base, engine
from src.api import models  # noqa: F401 - ensure models are imported


# PUBLIC_INTERFACE
def main():
    """Create all tables (idempotent) and print a simple verification summary."""
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    tables = sorted(inspector.get_table_names())
    print("DB initialized. Tables:", tables)


if __name__ == "__main__":
    main()
