from src.api.main import app  # noqa
from src.api.db import Base, engine


def test_db_tables_create_on_startup():
    # This should be idempotent and not raise
    Base.metadata.create_all(bind=engine)
    # Reflect that at least one table exists (users)
    assert "users" in engine.dialect.get_table_names(engine.connect())
