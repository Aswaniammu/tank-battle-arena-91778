def test_schemas_exports_available():
    import src.api.schemas as schemas

    # Ensure key schema classes exist
    for name in [
        "UserBase",
        "UserCreate",
        "UserRead",
        "TankBase",
        "TankCreate",
        "TankRead",
        "MatchBase",
        "MatchCreate",
        "MatchRead",
        "PlayerStateBase",
        "PlayerStateCreate",
        "PlayerStateRead",
        "LeaderboardEntryBase",
        "LeaderboardEntryCreate",
        "LeaderboardEntryRead",
    ]:
        assert hasattr(schemas, name), f"schemas is missing {name}"
