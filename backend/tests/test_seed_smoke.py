def test_seed_smoke_invocation():
    from src.api.seed import seed_minimal_demo

    users, match_id = seed_minimal_demo()
    # Basic sanity checks
    assert isinstance(users, int)
    assert isinstance(match_id, int)
