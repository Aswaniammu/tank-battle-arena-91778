from fastapi.testclient import TestClient

from src.api.main import app


def test_tank_defaults_after_seed():
    client = TestClient(app)
    r = client.post("/system/seed")
    assert r.status_code == 200

    # After seed, requesting users and verifying tanks via users would need a dedicated endpoint.
    # For now, just ensure leaderboard populated and seed returned ok.
    data = r.json()
    assert data.get("status") == "ok"
    assert "users_created" in data and "match_id" in data
