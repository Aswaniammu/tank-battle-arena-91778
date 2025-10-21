import os
import importlib
import sys


def test_default_database_url_uses_sqlite(tmp_path, monkeypatch):
    # Ensure no DATABASE_URL is set
    monkeypatch.delenv("DATABASE_URL", raising=False)

    # Reload the db module to re-evaluate URL
    if "src.api.db" in sys.modules:
        del sys.modules["src.api.db"]
    db = importlib.import_module("src.api.db")

    # The database should be sqlite and point to ./data/app.db
    assert db.DATABASE_URL.startswith("sqlite:///")
    assert db.DATABASE_URL.endswith("/data/app.db") or db.DATABASE_URL.endswith("\\data\\app.db")
