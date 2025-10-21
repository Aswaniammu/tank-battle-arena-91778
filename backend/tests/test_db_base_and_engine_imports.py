from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.engine import Engine

from src.api.db import Base, engine


def test_db_base_and_engine_imports():
    assert isinstance(Base, DeclarativeMeta)
    assert isinstance(engine, Engine)
