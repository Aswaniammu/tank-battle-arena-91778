from src.api.seed import seed_minimal_demo
from src.api.db import Base, engine


def test_seed_utility_return_shape():
    # Ensure tables exist before seeding
    Base.metadata.create_all(bind=engine)
    result = seed_minimal_demo()
    assert isinstance(result, tuple)
    assert len(result) == 2
    users_created, match_id = result
    assert isinstance(users_created, int)
    assert isinstance(match_id, int)
