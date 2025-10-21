import json
from fastapi.testclient import TestClient

from src.api.main import app


def test_health_endpoint():
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    body = r.json()
    assert "message" in body and body["message"] == "Healthy"


def test_db_info_endpoint():
    client = TestClient(app)
    r = client.get("/system/db-info")
    assert r.status_code == 200
    data = r.json()
    assert "database_url" in data
    # users_count can be None on a fresh DB if table does not exist yet; startup should create it
    assert "users_count" in data
