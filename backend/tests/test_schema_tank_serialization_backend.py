from src.api.schemas import TankRead
from src.api import models
from src.api.db_utils import ensure_tables_created

def test_tank_schema_serialization_from_orm():
    ensure_tables_created()
    orm = models.Tank(id=1, user_id=99, color="green", speed=1.0, armor=1.0, damage=1.0)
    dto = TankRead.model_validate(orm)
    assert dto.id == 1
    assert dto.user_id == 99
    assert dto.color == "green"
    assert dto.speed == 1.0
    assert dto.armor == 1.0
    assert dto.damage == 1.0
