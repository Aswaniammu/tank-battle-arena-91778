import os
from fastapi.testclient import TestClient

from src.api.main import app
from src.api.db_utils import ensure_tables_created, list_existing_tables

client = TestClient(app)


def test_tables_create_on_startup():
    tables = ensure_tables_created()
    # Core tables expected
    for t in ["users", "tanks", "matches", "player_states", "leaderboard_entries"]:
        assert t in tables


def test_health_and_system_endpoints():
    r = client.get("/")
    assert r.status_code == 200
    body = r.json()
    assert "message" in body and body["message"] == "Healthy"

    r = client.get("/system/time")
    assert r.status_code == 200
    assert "now_utc" in r.json()

    r = client.get("/system/models")
    assert r.status_code == 200
    models = r.json()
    assert isinstance(models, list)
    assert "users" in models

    # Seed
    r = client.post("/system/seed")
    assert r.status_code == 200
    data = r.json()
    assert data.get("ok") is True
    assert isinstance(data.get("match_id"), int)
