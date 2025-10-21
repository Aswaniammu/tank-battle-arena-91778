"""Database utilities and SQLAlchemy engine/session setup for the FastAPI backend.

- Default SQLite DB at ./data/app.db (directory auto-created)
- Optional override via DATABASE_URL environment variable
- Synchronous SQLAlchemy engine configured for FastAPI usage
- Exposes Base (declarative base), SessionLocal, get_session (PUBLIC_INTERFACE), and session_scope

This module is safe to import during app startup and scripts.
"""
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# Default database path: ./data/app.db (relative to backend working directory)
DEFAULT_SQLITE_PATH = os.path.join(".", "data", "app.db")
Base = declarative_base()


def _resolve_database_url() -> str:
    """
    Determine the database URL to use:
    - If DATABASE_URL env var is set, use it as-is.
    - Otherwise, use SQLite file at ./data/app.db
    Ensures directory exists for SQLite file path.
    """
    env_url: Optional[str] = os.getenv("DATABASE_URL")
    if env_url:
        return env_url

    # Ensure data directory exists
    db_path = DEFAULT_SQLITE_PATH
    data_dir = Path(db_path).parent
    data_dir.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{db_path}"


# Create SQLAlchemy engine and SessionLocal (synchronous)
DATABASE_URL = _resolve_database_url()

# SQLite specific: check_same_thread False for usage with FastAPI threads
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, future=True, connect_args=connect_args)

# Expire on commit False so objects retain attribute values after commit
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)


# PUBLIC_INTERFACE
def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a database Session and ensures proper close/rollback on errors."""
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    """
    Context manager for non-FastAPI contexts (e.g., scripts/seeders).
    Handles commit/rollback and closing automatically.
    """
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
