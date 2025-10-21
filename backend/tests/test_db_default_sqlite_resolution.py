import os

from importlib import reload
import src.api.db as db_module


def test_default_sqlite_database_url_resolution(monkeypatch):
    # Ensure DATABASE_URL not set
    monkeypatch.delenv("DATABASE_URL", raising=False)
    # Reload module to re-evaluate resolution
    reloaded = reload(db_module)
    assert reloaded.DATABASE_URL.startswith("sqlite:///")
    # Should end with ./data/app.db path
    assert reloaded.DATABASE_URL.endswith("/data/app.db") or reloaded.DATABASE_URL.endswith("\\data\\app.db")
