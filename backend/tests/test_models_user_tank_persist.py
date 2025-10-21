from sqlalchemy import select

from src.api.db import SessionLocal, Base, engine
from src.api import models


def test_user_and_tank_persist_and_queryable():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    # Create a user and a tank
    with SessionLocal() as s:
        user = models.User(username="tester_user")
        s.add(user)
        s.flush()

        tank = models.Tank(user_id=user.id, color="yellow", speed=1.1, armor=1.0, damage=1.2)
        s.add(tank)
        s.commit()
        uid = user.id
        tid = tank.id

    # Query back
    with SessionLocal() as s:
        q_user = s.execute(select(models.User).where(models.User.id == uid)).scalar_one()
        assert q_user.username == "tester_user"

        q_tank = s.execute(select(models.Tank).where(models.Tank.id == tid)).scalar_one()
        assert q_tank.user_id == uid
        assert q_tank.color == "yellow"
