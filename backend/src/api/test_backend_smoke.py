import os
from fastapi.testclient import TestClient

from src.api.main import app


def test_health_check():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "message" in data
    assert data["message"] == "Healthy"


def test_db_info_endpoint_creates_tables():
    # Ensure default SQLite path is used for repeatable runs in CI
    os.environ.pop("DATABASE_URL", None)
    client = TestClient(app)
    # Trigger startup events
    with client:
        resp = client.get("/system/db-info")
        assert resp.status_code == 200
        payload = resp.json()
        # users_count can be None if first run or before any insert, but should not error
        assert "users_count" in payload
