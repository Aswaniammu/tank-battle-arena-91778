from src.api.db import get_session, Base, engine
from src.api import models


def test_get_session_dependency_smoke():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    # Use the dependency generator manually
    gen = get_session()
    db = next(gen)
    try:
        # Create a user to ensure commit path works
        u = models.User(username="dep_smoke_user")
        db.add(u)
        # Yield end should commit
    finally:
        try:
            next(gen)
        except StopIteration:
            pass

    # Verify user persisted
    gen2 = get_session()
    db2 = next(gen2)
    try:
        found = db2.query(models.User).filter_by(username="dep_smoke_user").first()
        assert found is not None
    finally:
        try:
            next(gen2)
        except StopIteration:
            pass
