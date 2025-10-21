from fastapi.testclient import TestClient

from src.api.main import app


def test_seed_then_leaderboard_flow():
    client = TestClient(app)

    # Seed demo data
    r_seed = client.post("/system/seed")
    assert r_seed.status_code == 200
    assert r_seed.json().get("status") == "ok"

    # Leaderboard should be accessible and structured
    r_lb = client.get("/leaderboard")
    assert r_lb.status_code == 200
    payload = r_lb.json()
    assert "items" in payload and isinstance(payload["items"], list)
    assert "count" in payload and isinstance(payload["count"], int)
