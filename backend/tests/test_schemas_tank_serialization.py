from src.api.schemas import TankRead
from src.api import models
from src.api.db import Base, engine, SessionLocal


def test_tank_schema_serialization_from_orm():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as s:
        user = models.User(username="schema_tester")
        s.add(user)
        s.flush()

        tank = models.Tank(user_id=user.id, color="black", speed=1.3, armor=1.1, damage=0.9)
        s.add(tank)
        s.commit()
        tid = tank.id

    with SessionLocal() as s:
        orm_tank = s.get(models.Tank, tid)
        # from_attributes should allow .model_validate to accept ORM object
        read = TankRead.model_validate(orm_tank)
        assert read.id == orm_tank.id
        assert read.user_id == orm_tank.user_id
        assert read.color == "black"
        assert isinstance(read.speed, float)
        assert isinstance(read.armor, float)
        assert isinstance(read.damage, float)
