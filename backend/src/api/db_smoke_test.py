"""
Lightweight DB smoke test to validate basic CRUD with the configured SQLAlchemy engine.
Can be invoked via the /system/db-smoke endpoint or run directly.
"""
from sqlalchemy import select

from src.api.db import Base, engine, session_scope
from src.api import models  # noqa: F401  # ensure table metadata is loaded


def main():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    # Simple CRUD: create a temp user, read it back, then delete it
    username = "smoke_test_user"
    with session_scope() as s:
        # Create
        u = s.execute(select(models.User).where(models.User.username == username)).scalar_one_or_none()
        if not u:
            u = models.User(username=username)
            s.add(u)
            s.flush()

        uid = u.id

    with session_scope() as s:
        # Read back
        found = s.get(models.User, uid)
        assert found is not None, "Smoke user not found"
        assert found.username == username

        # Delete
        s.delete(found)
