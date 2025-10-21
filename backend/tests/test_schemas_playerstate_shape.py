from src.api.schemas import PlayerStateBase, PlayerStateCreate, PlayerStateRead


def test_playerstate_base_defaults():
    base = PlayerStateBase()
    assert base.x == 0.0
    assert base.y == 0.0
    assert base.angle == 0.0
    assert base.health == 100.0
    assert base.score == 0


def test_playerstate_create_requires_ids():
    create = PlayerStateCreate(match_id=1, user_id=2)
    assert create.match_id == 1
    assert create.user_id == 2
    # defaults still apply
    assert create.health == 100.0


def test_playerstate_read_contains_ids():
    # Simulate ORM read conversion by providing all required fields
    read = PlayerStateRead(id=10, match_id=1, user_id=2, x=1.0, y=2.0, angle=90.0, health=50.0, score=5)
    assert read.id == 10
    assert read.match_id == 1
    assert read.user_id == 2
