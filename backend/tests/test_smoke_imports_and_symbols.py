def test_smoke_imports():
    import src.api.main as main
    import src.api.db as db
    import src.api.models as models
    import src.api.schemas as schemas
    import src.api.system_docs as system_docs

    # App should be a FastAPI instance
    assert hasattr(main, "app")

    # DB module should expose Base and SessionLocal and engine
    assert hasattr(db, "Base")
    assert hasattr(db, "SessionLocal")
    assert hasattr(db, "engine")

    # Models should define key ORM classes
    for name in ["User", "Tank", "Match", "PlayerState", "LeaderboardEntry"]:
        assert hasattr(models, name)

    # Schemas should define corresponding Pydantic models
    for name in [
        "UserCreate",
        "UserRead",
        "TankCreate",
        "TankRead",
        "MatchCreate",
        "MatchRead",
        "PlayerStateCreate",
        "PlayerStateRead",
        "LeaderboardEntryCreate",
        "LeaderboardEntryRead",
    ]:
        assert hasattr(schemas, name)

    # System docs router should exist
    assert hasattr(system_docs, "router")
