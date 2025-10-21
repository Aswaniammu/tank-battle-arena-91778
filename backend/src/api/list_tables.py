"""
List SQLAlchemy ORM tables registered via metadata.

Usage:
    python -m src.api.list_tables
"""
from src.api.db import Base  # ensures metadata access
from src.api import models as _  # noqa: F401 - import to register models with metadata


def main():
    # PUBLIC_INTERFACE
    def list_tables():
        """Return a sorted list of ORM table names registered on Base.metadata."""
        return sorted(Base.metadata.tables.keys())

    for name in list_tables():
        print(name)


if __name__ == "__main__":
    main()
