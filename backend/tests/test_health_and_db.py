import os
from fastapi.testclient import TestClient

# Force a temp SQLite DB under project data dir for tests
os.environ.pop("DATABASE_URL", None)

from src.api.main import app  # noqa: E402

client = TestClient(app)


def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("message") == "Healthy"


def test_db_info_and_seed():
    # Tables should exist after startup
    r = client.get("/system/db-info")
    assert r.status_code == 200
    assert "database_url" in r.json()

    # Seed minimal
    r2 = client.post("/system/seed-minimal")
    assert r2.status_code == 200
    body = r2.json()
    assert body.get("seeded") is True
    assert "match_id" in body

    # Verify tables endpoint
    r3 = client.get("/system/tables")
    assert r3.status_code == 200
    tables = r3.json().get("tables", [])
    assert isinstance(tables, list)
    assert "users" in tables
