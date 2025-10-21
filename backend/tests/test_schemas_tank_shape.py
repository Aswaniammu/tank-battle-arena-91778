from src.api.schemas import TankBase, TankCreate, TankRead


def test_tank_base_defaults():
    base = TankBase()
    assert base.color == "green"
    assert base.speed == 1.0
    assert base.armor == 1.0
    assert base.damage == 1.0


def test_tank_create_requires_user_id():
    create = TankCreate(user_id=1)
    assert create.user_id == 1
    # defaults still apply
    assert create.color == "green"
    assert create.speed == 1.0


def test_tank_read_fields():
    read = TankRead(id=5, user_id=2, color="blue", speed=1.2, armor=1.1, damage=1.3)
    assert read.id == 5
    assert read.user_id == 2
    assert read.color == "blue"
